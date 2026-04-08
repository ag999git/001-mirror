

## 1. Vectors and Matrices

In standard algebra, a vector is typically represented as a column matrix. While a 1-D array in Python is simply a list of numbers, mathematically we view it as a column vector v of dimension n×1

$$
\mathbf{v} = \begin{bmatrix} x_1 
\\ x_2 \\ \vdots \\ x_n \end{bmatrix}
$$

An alternate, convenient notation often used in textbooks is the transpose of a row vector. This saves vertical space on the page:
$$ \mathbf{v} = \begin{bmatrix} x_1 & x_2 & \dots & x_n \end{bmatrix}^T $$

Here, the superscript T denotes the **transpose**, effectively converting a row into a column.
## 2. Matrix-Vector Multiplication as Transformation

When an n×n square matrix A multiplies a vector x of dimension n×1 , the result is a new vector y. This operation is called a **linear transformation**.

y=Ax

The components of the new vector y are linear combinations of the components of x. For a 2×2 system:

$$ \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} a_{11}x_1 + a_{12}x_2 \\ a_{21}x_1 + a_{22}x_2 \end{bmatrix} $$

## 3. Scaling Transformations

Scaling changes the length of a vector. It is achieved using a **diagonal matrix**, where all off-diagonal elements are zero.

### Uniform Scaling
Consider a vector x

$$ \mathbf{x} = \begin{bmatrix} 1 \\ 2 \\ \end{bmatrix} $$

and a scalar matrix M
$$ \mathbf{M} = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}$$ 
$$\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} a_{11}x_1 + a_{12}x_2 \\ a_{21}x_1 + a_{22}x_2 \end{bmatrix} $$

$$
\mathbf{y}=\left[\begin{array}{ll}
3 & 0 \\
0 & 3
\end{array}\right]\left[\begin{array}{l}
1 \\
2
\end{array}\right]=\left[\begin{array}{l}
3(1)+0(2) \\
0(1)+3(2)
\end{array}\right]=\left[\begin{array}{l}
3 \\
6
\end{array}\right]
$$

**Here, the vector was "stretched" by a factor of 3 in all directions. The magnitude increased, but the direction remained unchanged.**

### 4. Non-Uniform Scaling

If the diagonal elements differ, the scaling is different along each axis.




$$ M = \begin{bmatrix} 3 & 0 \\ 0 & 5 \end{bmatrix} \implies \mathbf{y} = \begin{bmatrix} 3(1) \\ 5(2) \end{bmatrix} = \begin{bmatrix} 3 \\ 10 \end{bmatrix} $$


The x-component stretched by 3, while the y-component stretched by 5. This changes the shape of the vector space (e.g., turning a square into a rectangle).

### 5. General Form

For a general scaling matrix in n dimensions:


$$
\mathrm{M}=\left(\begin{array}{ccccc}
\lambda_1 & 0 & 0 & . . & . . \\
0 & \lambda_2 & 0 & . . & . . \\
0 & 0 & \lambda_3 & . . & . . \\
. . & . . & . . & . . & . . \\
. . & . . & . . & . . & \lambda_n
\end{array}\right) \text { and } \mathrm{x}=\left(\begin{array}{c}
x_1 \\
x_2 \\
. . \\
. . \\
x_n
\end{array}\right) \text { then } \mathrm{y}=\left(\begin{array}{ccccc}
\lambda_1 & 0 & 0 & . . & . . \\
0 & \lambda_2 & 0 & . . & . . \\
0 & 0 & \lambda_3 & . . & . . \\
. . & . . & . . & . . & . . \\
. . & . . & . . & . . & \lambda_n
\end{array}\right)\left(\begin{array}{c}
x_1 \\
x_2 \\
. . \\
. . \\
x_n
\end{array}\right)=\left(\begin{array}{c}
\lambda_1 \cdot x_1 \\
\lambda_2 \cdot x_2 \\
. . \\
. \\
\lambda_n \cdot x_n
\end{array}\right)
$$



## 6. Reflection Transformations

Reflection flips the orientation of a vector across a specific axis or line. In 2D geometry, if we have a point (x,y), its reflection depends on the mirror line. The following list summarizes standard reflection matrices:

**1. Reflection in the X-axis** Changes (x,y) to (x,−y)

$$ M = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$ 

**2. Reflection in the Y-axis** Changes (x,y) to (−x,y)

$$ M = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$$ 


**3. Reflection in the Origin** Changes (x,y) to (−x,−y)

$$ M = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$$ 

**4. Reflection in the line** y=x Swaps coordinates to (y,x)

$$ M = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$ 


## 7. Rotation Transformations

To rotate a vector counter-clockwise by an angle θ, we use the standard rotation matrix. This matrix preserves the length of the vector but changes its direction.

$$ R(θ) = \begin{bmatrix} cosθ & -sinθ \\ sinθ & cosθ \end{bmatrix}$$ 

**Example:** Suppose we want to rotate the following pointRotating 
$$x=\begin{bmatrix} 1\\2\end{bmatrix}$$

by 90∘ (π/2 Radians)​

Since cos(90∘)=0 and sin(90∘)=1


$$
\mathbf{x}^{\prime}=\left[\begin{array}{cc}
0 & -1 \\
1 & 0
\end{array}\right]\left[\begin{array}{l}
1 \\
0
\end{array}\right]=\left[\begin{array}{l}
0 \\
1
\end{array}\right]
$$





