# MIT 18.06 Linear Algebra Study Repository

This repository is for working through MIT 18.06 Linear Algebra with Python/Jupyter.

## Course Sources

- Main 18.06 course page and lecture-video index: https://web.mit.edu/18.06/www/
- Problem set archive used here: https://web.mit.edu/18.06/www/Fall2022/
- OCW syllabus followed for course structure: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/

## Contents

- `ps/`: Fall 2022 problem sets converted from MIT's HTML notebook exports to Python 3 Jupyter notebooks.
- `ps/raw-html/`: original MIT HTML notebook exports used as conversion sources.
- `convert_psets.py`: local converter used to generate the Python notebooks from the downloaded HTML files.

## Syllabus Notes

Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/

### Course Info

- Course: 18.06 Linear Algebra
- Instructor: Prof. Gilbert Strang
- As taught: Spring 2010
- Level: Undergraduate
- Prerequisite: Multivariable Calculus, 18.02

### Meeting Times

- Lectures: 3 sessions per week, 1 hour per session
- Recitations: 1 session per week, 1 hour per session

### Text

- Gilbert Strang, *Introduction to Linear Algebra*, 4th edition, Wellesley-Cambridge Press, 2009.
- The OCW page also gives reading assignments for the 5th edition, 2016.

### Goals

The course goals are to use matrices and understand them. The syllabus highlights these major computations and ideas:

1. Solving square systems `Ax = b` by elimination, pivots, multipliers, back substitution, invertibility, and `A = LU`.
2. Complete solution to `Ax = b`, including column space, rank, nullspace, and special solutions to `Ax = 0`.
3. Basis and dimension, including bases for the four fundamental subspaces.
4. Least squares and projections.
5. Gram-Schmidt orthogonalization and `A = QR`.
6. Determinants, cofactor formulas, inverse applications, and volume.
7. Eigenvalues, eigenvectors, diagonalization, powers of `A`, and matrix exponentials.
8. Symmetric and positive definite matrices.
9. Linear transformations, change of basis, and the Singular Value Decomposition.
10. Engineering applications, including graphs, networks, Markov matrices, Fourier matrices, FFT, and linear programming.

### Homework, Exams, And Grading

- Homework is described as essential for learning linear algebra.
- The syllabus allows discussion with other students after trying difficult problems, but solutions must be written individually.
- Exams: three one-hour exams and a final exam.
- Calculators and notes are not permitted during exams.

Study breakpoints for the local Fall 2022 problem sets in `ps/`:

| Study block | Stop after | Pset coverage | Main exam focus |
| --- | --- | --- | --- |
| Exam 1 | Problem Set 4 | Psets 1-4 | Matrix operations, solving `Ax = b`, elimination, triangular systems, `LU` and `PA = LU`, inverses, singular matrices, rank, subspaces, nullspaces, column spaces, bases, dimensions, complete solutions, transposes, dot products, orthogonality, and the four fundamental subspaces. |
| Exam 2 | Problem Set 8 | Psets 5-8, plus Exam 1 material | Orthogonality-heavy block: orthogonal subspaces and complements, projections, least squares, orthonormal bases, Gram-Schmidt, `QR`, orthogonal functions, the SVD, matrix-calculus topics, and determinant properties. Eigenvalue problems start after this cutoff. |
| Exam 3 | Problem Set 13 | Psets 9-13, plus earlier material | Eigenproblem block: determinants, trace, eigenvalues and eigenvectors, diagonalization, similar matrices, matrix powers, recurrences, Markov matrices, linear ODEs, matrix exponentials, complex matrices and adjoints, symmetric/Hermitian matrices, positive definiteness, SVD connections, and defective matrices. |
| Final exam | Problem Set 13 | All psets | Cumulative review of all three blocks. |

For a practical self-study rhythm: finish the listed psets for a block, take that exam, then move on to the next block.

Grading:

| Activity | Percentage |
| --- | ---: |
| Problem sets | 15% |
| Three one-hour exams | 45% |
| Final exam | 40% |

The OCW syllabus mentions MATLAB for some homework problems. This repository is instead set up for Python/Jupyter practice.

## Python Setup

The converted notebooks use NumPy, SciPy, and Matplotlib:

```bash
python3 -m pip install -r ps/requirements.txt
```

The original MIT starter code was written in Julia. Simple starter cells were translated to Python/NumPy where practical; cells that were too Julia-specific were preserved as commented reference code with a Python TODO.
