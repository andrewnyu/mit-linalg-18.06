# MIT 18.06 Linear Algebra Study Repository

This repository is for working through MIT 18.06 Linear Algebra with Python/Jupyter.

## Course Sources

- Main 18.06 course page and lecture-video index: https://web.mit.edu/18.06/www/
- Problem set archive used here: https://web.mit.edu/18.06/www/Fall2022/
- OCW syllabus followed for course structure: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/

## Contents

- `ps/`: Fall 2022 problem sets converted from MIT's HTML notebook exports to Python 3 Jupyter notebooks.
- `ps/raw-html/`: original MIT HTML notebook exports used as conversion sources.
- `ps/raw-ipynb/`: clean, generated Python/NumPy notebook conversions from the raw HTML.
- `convert_psets.py`: local converter used to generate `ps/raw-ipynb/` from the downloaded HTML files.
- `LECTURE_SYLLABUS.md`: optional lecture, pset, and exam coverage map.

## Python Setup

The converted notebooks use NumPy, SciPy, and Matplotlib:

```bash
python3 -m pip install -r ps/requirements.txt
```

The original MIT starter code was written in Julia. Simple starter cells were translated to Python/NumPy where practical; cells that were too Julia-specific were preserved as commented reference code with a Python TODO. The notebooks in `ps/raw-ipynb/` are clean regenerated copies for reference, while the notebooks directly in `ps/` are the main working copies.

For study pacing, see `LECTURE_SYLLABUS.md`. The main repo workflow is to work through and answer the notebooks in `ps/`.
