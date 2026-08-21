#!/usr/bin/env python3
from html.parser import HTMLParser
from html import unescape
from pathlib import Path
import json
import re


ROOT = Path("ps")
HTML_ROOT = ROOT / "raw-html"
NOTEBOOK_ROOT = ROOT / "raw-ipynb"


class CellParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.cells = []
        self._cell_type = None
        self._depth = 0
        self._capture_md = False
        self._md_depth = 0
        self._md_chunks = []
        self._capture_pre = False
        self._pre_chunks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        cls = attrs.get("class", "")
        if self._cell_type is None and tag == "div" and "jp-Cell" in cls:
            if "jp-MarkdownCell" in cls:
                self._cell_type = "markdown"
                self._depth = 1
            elif "jp-CodeCell" in cls:
                self._cell_type = "code"
                self._depth = 1
            return

        if self._cell_type is not None:
            if tag == "div":
                self._depth += 1
                if self._cell_type == "markdown" and "jp-RenderedMarkdown" in cls:
                    self._capture_md = True
                    self._md_depth = 1
                    return
            if self._capture_md:
                if tag == "a" and attrs.get("class") == "anchor-link":
                    return
                self._md_depth += 1
                self._md_chunks.append(self.get_starttag_text())
            elif self._cell_type == "code" and tag == "pre":
                self._capture_pre = True

    def handle_endtag(self, tag):
        if self._capture_pre and tag == "pre":
            self._capture_pre = False
            return

        if self._capture_md:
            if tag == "a":
                return
            self._md_depth -= 1
            if self._md_depth == 0:
                self._capture_md = False
            else:
                self._md_chunks.append(f"</{tag}>")

        if self._cell_type is not None and tag == "div":
            self._depth -= 1
            if self._depth == 0:
                if self._cell_type == "markdown":
                    text = "".join(self._md_chunks).strip()
                    if text:
                        self.cells.append(("markdown", normalize_markdown_html(text)))
                    self._md_chunks = []
                elif self._cell_type == "code":
                    code = unescape("".join(self._pre_chunks)).strip("\n")
                    if code:
                        self.cells.append(("code", julia_to_python(code)))
                    self._pre_chunks = []
                self._cell_type = None

    def handle_data(self, data):
        if self._capture_pre:
            self._pre_chunks.append(data)
        elif self._capture_md:
            self._md_chunks.append(data)

    def handle_entityref(self, name):
        text = f"&{name};"
        if self._capture_pre:
            self._pre_chunks.append(unescape(text))
        elif self._capture_md:
            self._md_chunks.append("&" if name == "amp" else text)

    def handle_charref(self, name):
        text = f"&#{name};"
        if self._capture_pre:
            self._pre_chunks.append(unescape(text))
        elif self._capture_md:
            self._md_chunks.append(text)


def normalize_markdown_html(text):
    text = re.sub(r'<a class="anchor-link"[^>]*>.*?</a>', "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def convert_matrix_literal(expr):
    body = expr.strip()[1:-1].strip()
    if "\n" not in body and ";" not in body:
        return expr
    rows = [r.strip() for r in re.split(r";|\n", body) if r.strip()]
    converted = []
    for row in rows:
        if "???" in row or "????" in row:
            return "..."
        row = re.sub(r"\s+", " ", row)
        converted.append("[" + ", ".join(row.split(" ")) + "]")
    return "np.array([" + ", ".join(converted) + "])"


def convert_julia_matrix_lines(lines):
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if "=" in line and "[" in line and "]" not in line:
            block = [line]
            while i + 1 < len(lines) and "]" not in lines[i]:
                i += 1
                block.append(lines[i])
            joined = "\n".join(block)
            name, rhs = joined.split("=", 1)
            out.append(f"{name.strip()} = {convert_matrix_literal(rhs.strip())}")
        else:
            out.append(line)
        i += 1
    return out


def julia_to_python(code):
    original = code
    code = code.replace("????", "...").replace("???", "...")
    code = code.replace("using LinearAlgebra", "import numpy as np\nimport scipy.linalg as la")
    code = code.replace("using PyPlot", "import matplotlib.pyplot as plt")
    code = re.sub(r"\brandn\(([^)]*)\)", r"np.random.randn(\1)", code)
    code = re.sub(r"\bsin\.\(([^)]*)\)", r"np.sin(\1)", code)
    code = re.sub(r"\bcos\.\(([^)]*)\)", r"np.cos(\1)", code)
    code = re.sub(r"range\(([^,]+),\s*([^,]+),\s*length\s*=\s*([^)]+)\)", r"np.linspace(\1, \2, \3)", code)
    code = code.replace(" .+ ", " + ").replace(" .- ", " - ").replace(" .* ", " * ").replace(" ./ ", " / ")
    code = code.replace("Δx", "dx")
    code = re.sub(r"\b([A-Za-z]\w*)\s*=\s*([^#\n]+)\s*≈\s*([^#\n]+)", r"\1 = np.allclose(\2, \3)", code)
    code = re.sub(r"^(\s*)([A-Za-z]\w*)\s*=\s*([A-Za-z]\w*)\s*\\\s*([A-Za-z]\w*)", r"\1\2 = np.linalg.solve(\3, \4)", code, flags=re.M)
    code = re.sub(r"^(\s*)([A-Za-z]\w*)\s*=\s*([A-Za-z]\w*)\s*/\s*\(([^)\n]+)\)", r"\1\2 = \3 @ np.linalg.inv(\4)", code, flags=re.M)
    code = re.sub(r"^(\s*)([A-Za-z]\w*)\s*\^-1\s*$", r"\1np.linalg.inv(\2)", code, flags=re.M)
    code = re.sub(r"^(\s*)plot\(", r"\1plt.plot(", code, flags=re.M)
    code = re.sub(r"^(\s*)title\(", r"\1plt.title(", code, flags=re.M)
    code = re.sub(r"^(\s*)xlabel\(", r"\1plt.xlabel(", code, flags=re.M)
    code = re.sub(r"^(\s*)ylabel\(", r"\1plt.ylabel(", code, flags=re.M)
    code = re.sub(r"^(\s*)legend\(", r"\1plt.legend(", code, flags=re.M)
    code = code.replace("x[1:end-1]", "x[:-1]")
    code = code.replace("D*f", "D @ f")
    code = re.sub(r"L\"([^\"]*)\"", r"r\"\1\"", code)
    code = "\n".join(convert_julia_matrix_lines(code.splitlines()))
    if code.strip() != original.strip():
        code = "# Converted from the original Julia starter code.\n" + code
    code = code.strip() + "\n"
    try:
        compile(code, "<converted-cell>", "exec")
    except SyntaxError:
        return commented_julia_todo(original)
    return code


def commented_julia_todo(code):
    commented = "\n".join("# " + line if line else "#" for line in code.splitlines())
    return (
        "# Original Julia starter code kept for reference; translate/implement in Python.\n"
        f"{commented}\n\n"
        "# TODO: write the Python version for this cell.\n"
        "...\n"
    )


def nb(cells, title, source_url):
    setup = (
        "# Python setup for this problem set\n"
        "import numpy as np\n"
        "import scipy.linalg as la\n"
        "import matplotlib.pyplot as plt\n\n"
        "np.set_printoptions(precision=4, suppress=True)\n"
    )
    notebook_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"<!-- Source: {source_url} -->\n",
                "\n",
                "This notebook was converted from the MIT 18.06 Fall 2022 problem set HTML. Original Julia starter cells were translated to Python/NumPy where practical.\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": setup.splitlines(True),
        },
    ]
    for typ, source in cells:
        notebook_cells.append(
            {
                "cell_type": typ,
                "metadata": {},
                "source": source.splitlines(True),
                **({"execution_count": None, "outputs": []} if typ == "code" else {}),
            }
        )
    return {
        "cells": notebook_cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
            "source_url": source_url,
            "title": title,
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main():
    NOTEBOOK_ROOT.mkdir(exist_ok=True)
    for i in range(1, 14):
        html_path = HTML_ROOT / f"pset{i}.html"
        parser = CellParser()
        parser.feed(html_path.read_text(encoding="utf-8"))
        notebook = nb(parser.cells, f"18.06 Pset {i}", f"https://web.mit.edu/18.06/www/Fall2022/pset{i}.html")
        out = NOTEBOOK_ROOT / f"pset{i}.ipynb"
        out.write_text(json.dumps(notebook, ensure_ascii=False, indent=1), encoding="utf-8")
        code_count = sum(1 for typ, _ in parser.cells if typ == "code")
        md_count = sum(1 for typ, _ in parser.cells if typ == "markdown")
        print(f"{out}: {md_count} markdown cells, {code_count} code cells")


if __name__ == "__main__":
    main()
