# MIT 18.06 Lecture Syllabus

This is a compact study map for the local Fall 2022 problem sets in `ps/`. The repo itself is mainly for working through and answering the notebooks; this file keeps lecture and exam pacing out of the main README.

Sources:

- MIT 18.06 course page and lecture-video topic list: https://web.mit.edu/18.06/www/
- MIT OCW 18.06 Spring 2010 syllabus: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/

## Course Info

- Course: 18.06 Linear Algebra
- Instructor: Prof. Gilbert Strang
- As taught on OCW: Spring 2010
- Level: Undergraduate
- Prerequisite: Multivariable Calculus, 18.02
- Lectures: 3 sessions per week, 1 hour per session
- Recitations: 1 session per week, 1 hour per session

## Text

- Gilbert Strang, *Introduction to Linear Algebra*, 4th edition, Wellesley-Cambridge Press, 2009.
- The OCW page also gives reading assignments for the 5th edition, 2016.

## Course Goals

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

## Exam Breakpoints

| Study block | Stop after | Pset coverage | Main exam focus |
| --- | --- | --- | --- |
| Exam 1 | Problem Set 4 | Psets 1-4 | Matrix operations, solving `Ax = b`, elimination, triangular systems, `LU` and `PA = LU`, inverses, singular matrices, rank, subspaces, nullspaces, column spaces, bases, dimensions, complete solutions, transposes, dot products, orthogonality, and the four fundamental subspaces. |
| Exam 2 | Problem Set 8 | Psets 5-8, plus Exam 1 material | Orthogonality-heavy block: orthogonal subspaces and complements, projections, least squares, orthonormal bases, Gram-Schmidt, `QR`, orthogonal functions, the SVD, matrix-calculus topics, and determinant properties. Eigenvalue problems start after this cutoff. |
| Exam 3 | Problem Set 13 | Psets 9-13, plus earlier material | Eigenproblem block: determinants, trace, eigenvalues and eigenvectors, diagonalization, similar matrices, matrix powers, recurrences, Markov matrices, linear ODEs, matrix exponentials, complex matrices and adjoints, symmetric/Hermitian matrices, positive definiteness, SVD connections, and defective matrices. |
| Final exam | Problem Set 13 | All psets | Cumulative review of all three blocks. |

For a practical self-study rhythm: finish the listed psets for a block, take that exam, then move on to the next block.

## Lecture-To-Pset Map

This table is a practical alignment between the Fall 2022 psets and the public MIT 18.06 lecture-video topic list.

| Pset | Lecture coverage | Lecture topics | Exam coverage |
| --- | --- | --- | --- |
| Pset 1 | L1-L3 | Geometry of linear equations; elimination with matrices; matrix multiplication and inverses. | Exam 1 |
| Pset 2 | L4-L5 | `A = LU`; transposes; permutations; vector spaces in `R^n`. | Exam 1 |
| Pset 3 | L6-L8 | Column space and nullspace; solving `Ax = 0`; pivot/free variables; row-reduced form for `Ax = b`. | Exam 1 |
| Pset 4 | L9-L10 | Independence, basis, dimension, and the four fundamental subspaces. | Exam 1 |
| Pset 5 | L11-L14 | Matrix spaces; rank-one matrices; graph/network incidence matrices; orthogonal vectors and subspaces. | Exam 2 |
| Pset 6 | L15-L16 | Projections onto subspaces; projection matrices; least squares. | Exam 2 |
| Pset 7 | L17 | Orthogonal matrices and Gram-Schmidt, including `QR` and best-fit bases. | Exam 2 |
| Pset 8 | L18-L20 | Determinant properties, formulas, cofactors, Cramer's rule, inverse formulas, and volume. | Exam 2 |
| Pset 9 | L21-L22 | Eigenvalues, eigenvectors, diagonalization, and powers of `A`. | Exam 3 |
| Pset 10 | L23-L24 | Differential equations, `exp(At)`, Markov matrices, and Fourier-series connections. | Exam 3 |
| Pset 11 | L25-L27 | Symmetric matrices, positive definiteness, complex matrices, FFT, and quadratic minima. | Exam 3 |
| Pset 12 | L28-L31 | Similar matrices, Jordan form, SVD, linear transformations, change of basis, and image compression. | Exam 3 |
| Pset 13 | L32-L34 | Quiz 3 review, left/right inverses, pseudoinverse, and final review topics. | Exam 3 and final review |

## Grading Reference

| Activity | Percentage |
| --- | ---: |
| Problem sets | 15% |
| Three one-hour exams | 45% |
| Final exam | 40% |

The OCW syllabus mentions MATLAB for some homework problems. This repository is instead set up for Python/Jupyter practice.
