



# Research Project

## Project Title: Row Vectors vs Column Vectors in NumPy and Linear Algebra: Concepts, Comparisons, and Transformations



## Research/ Project Question

Study the concept of **row vectors and column vectors** in NumPy and linear algebra.  
Explain their structure, differences, and practical use cases in data science, machine learning, and mathematical transformations.

Your study should include:

1.  Definition and structure of row vectors and column vectors.
2.  Comparison between:
    -   Python lists
    -   NumPy 1D arrays
    -   Row vectors
    -   Column vectors
3.  Explanation of why many mathematical transformations use **column vectors**.
4.  Demonstration of matrix multiplication involving:
    -   Matrix × Column vector
5.  Implementation of geometric transformations such as:
    -   Rotation of a point in a 2D system
    -   Scaling transformation
6.  Use NumPy scripts to demonstrate the concepts.
7.  Include tables, diagrams, and explanations.

Finally, conclude when it is preferable to use row vectors and when column vectors are more appropriate.

----------

# Answer 


## 1. Introduction

Vectors are fundamental objects in mathematics, data science, and machine learning. In NumPy, vectors can be represented in different forms depending on how the data is structured.

The two main forms are:

-   Row vector
-   Column vector

Although both store the same values, their **orientation affects mathematical operations**, especially matrix multiplication and transformations.

----------

## 2. Row Vector

A row vector is a horizontal arrangement of values.

Example:

`[ 3  5  7 ]`

Shape in NumPy:

`(1, 3)`

Example code:

```python

# This code demonstrates how to create a row vector using NumPy and reshape it to have a specific shape.
# A row vector is a 1D array that has only one row and multiple columns.
# NumPy library is used for creating and manipulating arrays in Python. 
# The reshape method is used to change the shape of the array without changing its data. 
# In this case, we are reshaping a 1D array into a 2D array with 1 row and 3 columns.

import numpy as np  

# Create a row vector (1D array) with values 3, 5, and 7, and reshape it to have 1 row and 3 columns.
# The reshape(1, 3) method is used to change the shape of the array to a 2D array with 1 row and 3 columns.
row_vector = np.array([3,5,7]).reshape(1,3)  

print(row_vector)  # Output: [[3 5 7]]
print("Shape:", row_vector.shape)  # Output: (1, 3) - This indicates that the array has 1 row and 3 columns.


```


## 3. Column Vector

A column vector is a vertical arrangement of values.

Example:

```python
[3  
 5  
 7]
```
Shape:

`(3,1)`

Example:


```python

# This code demonstrates how to create a column vector using NumPy and check its shape.
# A column vector is a 2D array that has multiple rows and only one column.
# NumPy library is used for creating and manipulating arrays in Python. 
# The reshape method is used to change the shape of the array without changing its data.

import numpy as np

# Create a column vector (2D array) with values 3, 5, and 7, and 
# reshape it to have 3 rows and 1 column.
column_vector = np.array([3,5,7]).reshape(3,1)

print(column_vector) # Output: [[3]
#                    #          [5]
#                    #          [7]]
                    
print("Shape:", column_vector.shape)  
# Output: (3, 1) - This indicates that the array has 3 rows and 1 column.

```

**Interpretation: Three values stacked vertically.**


## Comparison Table (Row Vector | Column Vector) 

  

| Feature | Row Vector | Column Vector |
| --- | --- | --- |
| Shape | (1,n) | (n,1) |
| Orientation | Horizontal | Vertical |
| Common use | Represent one data record | Used in matrix transformations |
| Machine learning | Prediction input | Model computations |
| Linear algebra | Less common | Standard representation |



## 5. Comparison with Python Lists


  

| Feature | Python List | NumPy Row Vector | NumPy Column Vector |
| --- | --- | --- | --- |
| Structure | Flexible | Structured | Structured |
| Shape | Not defined | Defined | Defined |
| Matrix math | Not supported | Supported | Supported |
| Performance | Slower | Fast | Fast |



## 6. Why Column Vectors Are Used in Transformations

In linear algebra, transformations such as:

rotation
scaling
projection
translation

are defined using:

`Matrix × Column Vector`

Mathematically:

`y = Mx`

Where

`M = transformation matrix`
`x = column vector`


## 7. Example: Rotation by 90 Degrees

Suppose we have a point: `(2,1)`

We represent it as a column vector.

Rotation matrix for 90°:

```python

[ 0  -1 ]
[ 1   0 ]
```










