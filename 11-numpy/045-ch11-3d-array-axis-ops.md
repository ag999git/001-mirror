


# Project: Understanding 3D Arrays and Axis Operations in NumPy

----------

## Objective

To understand:

-   Structure of 3D arrays
-   Meaning of axes (0, 1, 2)
-   How `sum(axis=...)` works
-   How multi-dimensional data is reduced

----------

## PART A — CONCEPTUAL STUDY

## Study Questions

1.  What is the shape of a 3D array?
2.  What do the three indices represent?
3.  What does each axis correspond to?
4.  What does it mean to “collapse an axis”?

----------

# Visualizing a 3D Array

Given a 3D array:
```
arr  =  np.array([  
 [[1,2],[3,4]],  
 [[5,6],[7,8]]  
])
```
### Its Shape = (2, 2, 2)

----------

## There are various ways in which it can be represented/ visualized
 ### Representation 1: Visualizing it as 2 layers
```
Layer 0:  
[[1 2]  
 [3 4]]  
  
Layer 1:  
[[5 6]  
 [7 8]]
```
----------

### Representation 2: Indexed View
**Here we view each item by its index of form `arr[i, j, k]`**
```
arr[0,0,0] = 1   arr[0,0,1] = 2  
arr[0,1,0] = 3   arr[0,1,1] = 4  
  
arr[1,0,0] = 5   arr[1,0,1] = 6  
arr[1,1,0] = 7   arr[1,1,1] = 8
```
----------

### Representation 3: Coordinates

***Here we view each item in the array as `(i, j, k) → value`** 
  ```
(0,0,0) → 1  
(1,1,1) → 8
```
----------

## Part B: Task

Write a script that:

1.  Creates the 3D array
2.  Displays it in multiple forms
3.  Computes:
    -   `sum(axis=0)`
    -   `sum(axis=1)`
    -   `sum(axis=2)`
4.  Explains each result

----------

### HINTS

-   Use loops to print layers
-   Print shapes after each operation
-   Compare results carefully

----------

## Script

















