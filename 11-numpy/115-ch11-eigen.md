

# Draft 1


# Eigen Decomposition: A Detailed Guide

_(Note: The topic of eigen decomposition may appear a bit mathematical. However, it is essential to understand this before moving on to Singular Value Decomposition (SVD). Those not interested in SVD may skip this topic.)_

To effectively use eigenvalues and eigenvectors, one must understand the concept of Eigen Decomposition.

### 1. The Core Concept

Previously, we established that if A is a square matrix, v is a non-zero vector, and λ is a scalar, the following relationship holds:

$Av=λ\vec{v}$  In this equation, the matrix $A$ acts on the vector $\vec{v}$ . The result is simply a scaled version of $\vec{v}$. 
This implies that matrix A does not change the direction of $\vec{v}$ , it only changes its magnitude by a factor of $\lambda.$
Note $\lambda$ is a scalar

-   If λ=1, the matrix leaves the vector unchanged.
-   If λ>1, the matrix "stretches" the vector.
-   If 0<λ<1, the matrix "compresses" the vector.
-   If λ<0, the direction is reversed.

### 2. The Logic Behind Decomposition

Why do we break a matrix apart? The logic is similar to understanding how a machine works by taking it apart into its components.

Suppose a square matrix $A$ (size $n \times n$) has $n eigenvalues $λ_1$​,$λ_2$​,$…,λ_n$​ and corresponding eigenvectors $\vec{v_1}$. $\vec{v_2}$, $...... \vec{v_n}$


We can arrange the eigenvectors as columns into a matrix $Q$

$Q =[\vec{v_1}$. $\vec{v_2}$, $...... \vec{v_n}]$

We can arrange the eigenvalues into a diagonal matrix  $\Lambda$) (Capital Lambda):


$$
\Lambda =
\begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$


Using the definition $Av=λ\vec{v}$, we can write a combined matrix equation for all eigenvectors simultaneously:

$AQ = Q\Lambda$ If the matrix $Q$ is invertible (which is true if the eigenvectors are linearly independent), we can multiply both sides by 
$Q^{-1}$ from the right:
We get:
$AQQ^{-1} = Q\Lambda Q^{-1}$
Since $QQ^{-1} =1$, then we have 
We have $A = Q\Lambda Q^{-1}$
 This is the Eigen Decomposition. It reveals that the matrix A is actually (Considering $Q\Lambda Q^{-1}$ from right to left) a rotation ($Q^{-1}$), followed by a scaling ($\Lambda$), followed by a rotation back ($Q$).





# Draft 2



# Eigen Decomposition: A Detailed Guide

> *Note:* The topic of eigen decomposition may appear mathematical. However, it is essential for understanding advanced topics like Singular Value Decomposition (SVD). If you are not interested in SVD, you may skip this section.

---

# 1. The Core Concept

Previously, we established that if:

- \( A \) is a square matrix  
- \( v \) is a non-zero vector  
- \( $\lambda\$) is a scalar  

then:

$A\vec{v}$ = $\lambda$ $\vec{v}$



### Interpretation

- The matrix $\( A \)$ acts on vector $\vec{v}$
- The result is a **scaled version of the same vector**

This means:
- The **direction remains unchanged**
- Only the **magnitude changes** by a factor of $\lambda$.

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

The logic is similar to how a machine works by taking it apart into its components.
It is just like breaking a machine into parts to understand it.

---

## Step 1: Eigenvalues and Eigenvectors




We can arrange the eigenvectors as columns into a matrix Q:

For a $matrix \( A \)$ of dimensions  $\( n \times n \)$:

- Suppose the Eigenvalues are:  
  \[
  $\lambda_1, \lambda_2, \dots, \lambda_n$
  \]

- And the corresponding Eigenvectors are :  
  \[
  $\vec{v_1}$, $\vec{v_2}$ , $\dots$, $\vec{v_n}$
  \]

---

## Step 2: Construct Matrix \( Q \)
Then we can arrange the eigenvectors as columns into a matrix Q:

$$
Q = [v_1 \; v_2 \; \dots \; v_n]
$$


**Columns are eigenvectors**

---

## Step 3: Construct Diagonal Matrix ( $\Lambda\$ )
Next we can arrange the eigenvalues into a diagnolal matrix ( $\Lambda\$ ) as follows:


$$
\Lambda =
\begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$

---

## Step 4: Key Equation
Using the definition $A\vec{v}$ = $\lambda$ $\vec{v}$ , we can write a combined matrix equation for all the eigenvalues simultaneously as follows:

$$
AQ = Q\Lambda
$$

If \( Q \) is invertible:


$$
A = Q \Lambda Q^{-1}
$$

---

## Interpretation

Eigen Decomposition represents:

```text
A = Rotation → Scaling → Rotation back
```










