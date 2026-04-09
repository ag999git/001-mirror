


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

$AQ = Q\Lambda$ If the matrix $Q$ is invertible (which is true if the eigenvectors are linearly independent), we can multiply both sides by $Q^{-1}$ from the right:


We get: $AQQ^{-1} = Q\Lambda Q^{-1}$


Since $QQ^{-1} =1$, then we have 


We have $A = Q\Lambda Q^{-1}$
 This is the Eigen Decomposition. It reveals that the matrix A is actually (Considering $Q\Lambda Q^{-1}$ from right to left) a rotation ($Q^{-1}$), followed by a scaling ($\Lambda$), followed by a rotation back ($Q$).




## Interpretation

Eigen Decomposition represents:

```text
A = Rotation → Scaling → Rotation back
```




### 3. Step-by-Step Mathematical Example

Let us take a real example to understand the math. Let:

$$
A=\left[\begin{array}{ccc}
3 & 1 & -1 \\
1 & 3 & -1 \\
-1 & -1 & 5
\end{array}\right]
$$


**Step 1: Find the Eigenvalues**

We must solve the characteristic equation $det(A−λI)=0$.
Where

$$
I=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]
$$


**So we get**


$$
I=\left[\begin{array}{ccc}
3- \lambda & 1 & -1 \\
1 & 3-\lambda & -1 \\
-1 & -1 & 5-\lambda
\end{array}\right] =0
$$


Solving this cubic equation yields the eigenvalues:

$λ1​=6, λ2​=2, λ3​=3$

 **Step 2: Find the Eigenvectors**




For each eigenvalue, we solve $(A−λI)\vec{v}_1=0$.

### For $\lambda_1 ​= 6:$

$$
(A-6 I) \vec{v}=\left[\begin{array}{ccc}
-3 & 1 & -1 \\
1 & -3 & -1 \\
-1 & -1 & -1
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\
0
\end{array}\right]
$$


Solving this system gives the eigenvector 

$$
\text { eigenvector } \vec{v}_1=\left[\begin{array}{c}
-1 \\
-1 \\
2
\end{array}\right] .\left(\text { Normalized: } \frac{1}{\sqrt{6}}[-1,-1,2]^T\right) .
$$


### For λ2​=2:

$$
(A-2 I) \vec{v}=\left[\begin{array}{ccc}
1 & 1 & -1 \\
1 & 1 & -1 \\
-1 & -1 & 3
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\
0
\end{array}\right]
$$

Solving this system gives the eigenvector 

$$
\text { eigenvector } \vec{v}_2=\left[\begin{array}{c}
-1 \\
1 \\
0
\end{array}\right] .\left(\text { Normalized: } \frac{1}{\sqrt{2}}[-1,1,0]^T\right) .
$$



### For λ3​=3:

$$
(A-3 I) \vec{v}=\left[\begin{array}{ccc}
0 & 1 & -1 \\
1 & 0 & -1 \\
-1 & -1 & 2
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\
0
\end{array}\right]
$$

Solving this system gives the eigenvector 

$$
\text { eigenvector } \vec{v}_3=\left[\begin{array}{c}
1 \\
1 \\
1
\end{array}\right] .\left(\text { Normalized: } \frac{1}{\sqrt{3}}[1,1,1]^T\right) .
$$





**Step 3: Construct Matrices $Q$ and $\Lambda$**

We form matrix Q with normalized eigenvectors as columns and Λ with eigenvalues on the diagonal.

$$
Q=\left[\begin{array}{ccc}
-\frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \\
-\frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \\
\frac{2}{\sqrt{6}} & 0 & \frac{1}{\sqrt{3}}
\end{array}\right], \quad \Lambda=\left[\begin{array}{lll}
6 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 3
\end{array}\right]
$$


**Step 4: Verify Decomposition**

We verify that $A=QΛQ^{−1}$. Since A is symmetric, $Q$ is orthogonal, meaning $Q^{−1}=Q^T$ (the transpose).

$A=QΛQ^T$ 

If you perform the matrix multiplication $QΛQ^T$, you will recover the original matrix $A$.

### 4. Elaborate Discussion

Why is this important?

-   **Dimensionality Reduction:** In Principal Component Analysis (PCA), eigenvalues tell us which directions (eigenvectors) contain the most information (variance). We keep the vectors with large λ and discard those with small λ.
-   **Matrix Powers:** Calculating $A^100$ is hard. But using decomposition: $A^{100}=(QΛQ^{−1})^{100}=QΛ^{100}Q^{−1}$. Since Λ is diagonal, $Λ^{100}$ is just raising the diagonal elements to the power of 100. This makes computation trivial.
-   **Symmetric Matrices:** For symmetric matrices ($A=A^T$), the eigenvectors are always orthogonal (vi​⋅vj​=0). This makes decomposition stable and is the foundation for spectral clustering and graph partitioning.





















