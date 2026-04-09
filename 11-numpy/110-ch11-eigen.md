

# Eigen Decomposition: A Detailed Guide

> ⚠️ *Note:* The topic of eigen decomposition may appear mathematical. However, it is essential for understanding advanced topics like Singular Value Decomposition (SVD). If you are not interested in SVD, you may skip this section.

---

# 1. The Core Concept

Previously, we established that if:

- \( A \) is a square matrix  
- \( v \) is a non-zero vector  
- \( $\lambda\$) is a scalar  

then:


\[
$A\vec{v}$ = $\lambda$ $\vec{v}$
\]


### Interpretation

- The matrix $\( A \)$ acts on vector $\vec{v}$
- The result is a **scaled version of the same vector**

👉 This means:
- The **direction remains unchanged**
- Only the **magnitude changes**

---

### Cases of Eigenvalues

| Condition | Meaning |
|----------|--------|
| \( $\lambda$ = 1 \) | Vector remains unchanged |
| \( $\lambda$ > 1 \) | Vector is stretched |
| \( 0 < $\lambda$ < 1 \) | Vector is compressed |
| \( $\lambda$ < 0 \) | Direction is reversed |

---

# 2. The Logic Behind Decomposition

Why do we decompose a matrix?

👉 Just like breaking a machine into parts to understand it.

---

## Step 1: Eigenvalues and Eigenvectors

For an $\( n \times n \)$ $matrix \( A \)$ :

- Eigenvalues:  
  \[
  $\lambda_1, \lambda_2, \dots, \lambda_n$
  \]

- Eigenvectors:  
  \[
  $\vec{v_1}$, $\vec{v_2}$ , $\dots$, $\vec{v_n}$
  \]

---

## Step 2: Construct Matrix \( Q \)

\[
Q = [v_1 \; v_2 \; \dots \; v_n]
\]

👉 Columns are eigenvectors

---

## Step 3: Construct Diagonal Matrix \( \Lambda \)

\[
\Lambda =
\begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}
\]

---

## Step 4: Key Equation

\[
AQ = Q\Lambda
\]

If \( Q \) is invertible:

\[
A = Q \Lambda Q^{-1}
\]

---

## Interpretation

Eigen Decomposition represents:

```text
A = Rotation → Scaling → Rotation back
```









## XXX
Common Vector Equations
Dot Product: $\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i$



Euclidean Norm: $\|\mathbf{v}\| = \sqrt{\sum_{i=1}^n v_i^2}$


Vector Addition: $\mathbf{c} = \mathbf{a} + \mathbf{b}$


Cauchy-Schwarz Inequality: $(\sum a_k b_k)^2 \leq (\sum a_k^2)(\sum b_k^2)$ 
GitHub Docs 
GitHub Docs
 +4
Common Matrix Equations
Matrix Multiplication: $\mathbf{C} = \mathbf{A}\mathbf{B}$ where $\mathbf{C}_{ij} = \sum_{k} A_{ik} B_{kj}$


Transpose Identity: $(\mathbf{AB})^\top = \mathbf{B}^\top \mathbf{A}^\top$


Inverse Identity: $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$


Eigendecomposition: $\mathbf{A} = \mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^{-1}$


Singular Value Decomposition (SVD): $\mathbf{M} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^*$ 
GitHub
GitHub
 +1
Matrix Formatting Cheat Sheet 
To render a full matrix, use the pmatrix or bmatrix environments within a GitHub math block. 
Feature 	LaTeX Code Example	Resulting Style
Basic Matrix	\begin{pmatrix} a & b \\ c & d \end{pmatrix}	Parentheses ()
Bracketed Matrix	\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}	Square Brackets []
Vector (Column)	\begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}	Vertical stack
Ellipses	a_{11} & \dots & a_{1n}	Horizontal dots
Vertical Dots	\vdots	Vertical dots












