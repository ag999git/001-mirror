



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











