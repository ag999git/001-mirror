


# Project: Matrix–Vector Multiplication as Transformations


## Objective

To explore how matrix–vector multiplication:

-   transforms vectors
-   performs scaling, reflection, rotation
-   is used in data science and ML

----------

## PART A — RESEARCH QUESTIONS

### Conceptual

1.  What is a vector in NumPy?
2.  What happens when a matrix multiplies a vector?
3.  Why is matrix multiplication called a “transformation”?
4.  What is a diagonal matrix and how does it affect a vector?
5.  How do matrices represent:
    -   scaling
    -   reflection
    -   rotation

## Part B — Task

Write a script that:

1.  Defines a vector
2.  Applies:
    -   scaling
    -   non-uniform scaling
    -   reflection
    -   rotation
3.  Prints results clearly
4.  Explains transformation

----------

### HINTS

-   Use `@` operator
-   Use small vectors (2D)
-   Compare input vs output

----------

## Solution (Explanation)


## What is happening when we multiply?
Suppose we have 2D Matrix **M** of dimensions say **m x n**.
and we have vector **x** of dimension **n x 1**.
Note; 
-    Multiplication between **M** and **x** is only possible if the number of columns in **M** is equal to number of rows in **x**. 
-   Also note that when we do $$y=Mx$$ , then y will have dimensions m x 1.
- So multiplying a matrix of dimensions **m x n** to a vector of dimensions **n x 1** will result in a new vector y of dimensions **m x 1**.
- Note that matrix to vector multiplication will not only change the individual contents in each position but also change the dimensions of a vector.
- So, each matrix: (1) changes the vector (2) produces a new vector
- This change of a vector by a matrix is called **Transformation**.

----------

## Types of Transformations

Having understood what a transformation is , we can consider the **various types of transformations** which can be done to a vector by a matrix

  

| Type | Matrix Form | Effect |
| --- | --- | --- |
| Scaling | Diagonal | Stretch/shrink |
| Reflection | Special matrices | Flip direction |
| Rotation | Trigonometric | Rotate vector |

Consider the common transformations which can be done by a 2 x 2 matrix.
They are shown in the table below:-

  

| Operation | Matrix | Effect |
| --- | --- | --- |
| Uniform scaling | `[[k,0],[0,k]]` | Stretch equally |
| Non-uniform | `[[a,0],[0,b]]` | Stretch differently |
| Reflection X | `[[1,0],[0,-1]]` | Flip vertically |
| Reflection Y | `[[-1,0],[0,1]]` | Flip horizontally |
| Rotation | `[[cosθ,-sinθ],[sinθ,cosθ]]` | Rotate |










