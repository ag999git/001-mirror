




# Understanding Coordinate Data and Grid/Matrix Data in Matplotlib




## Problem Statement

Matplotlib provides different plotting methods for different kinds of data.

Some plots use **coordinate data (X–Y data)** where values are given as pairs of coordinates.

Examples:

-   marks of students
-   temperature across months
-   rainfall across years

Other plots use **grid or matrix data**, where values are arranged in rows and columns.

Examples:

-   temperature across cities and months
-   passenger counts across months and years
-   image data stored as pixels

Different plotting methods are suitable for different situations.

For example:

-   `plot()` and `scatter()` work well for coordinate data
-   `imshow()` and `contour()` work well for grid or matrix data

In this project, students will study these plotting methods and compare their usefulness.

----------

## Task Requirements

### Part A — Theory Questions

Answer the following questions.

### Q1. Explain the difference between:

**(a) Coordinate Data (X–Y Data)**  
**(b) Grid or Matrix Data**

Give one real-life example of each.

----------

### Q2. Explain the purpose of the following Matplotlib methods:

1.  `plot()`
2.  `scatter()`
3.  `imshow()`
4.  `contour()`

State:

-   what kind of data each method accepts
-   where the method is useful

----------

### Q3. Explain the role of matrix slicing in NumPy.

Use examples to explain the syntax:

```python
matrix[row_start:row_end, col_start:col_end]
```

----------

## Part B — Programming Tasks

Use the **flights dataset** available in Seaborn.

This dataset stores the number of airline passengers for different:

-   months
-   years

### Task 1: Load the Dataset

Write a Python script to:

1.  import the required libraries
2.  load the flights dataset
3.  display first few rows
4.  explain what each column means

----------

### Task 2: Convert Data into Matrix Form

Convert the dataset into a table where:

-   rows represent **years**
-   columns represent **months**
-   cell values represent **passenger counts**

Display the matrix.

----------

### Task 3: Matrix Slicing

Use slicing to extract only a selected group of years.

For example:

-   1952–1958

Explain the slicing used.

----------

### Task 4: Plot Coordinate Data

Choose one year from the dataset.

Create:

#### (a) Line Plot using `plot()`

Show:

-   month on x-axis
-   passenger count on y-axis

#### (b) Scatter Plot using `scatter()`

Plot the same data.

Compare the two graphs.

----------

### Task 5: Plot Grid or Matrix Data

Using the sliced matrix:

#### (a) Create a graph using `imshow()`

#### (b) Create another graph using `contourf()`

Add:

-   title
-   axis labels
-   color bar

Compare the two graphs.

----------

### Task 6: Comparative Discussion

Write a short discussion on:

1.  Which methods were easier to understand?
2.  When should `plot()` be preferred?
3.  When should `imshow()` or `contour()` be preferred?
4.  Which graph looked most informative and why?

----------

## Expected Learning Outcomes

After completing this project, students should be able to:

1.  distinguish between coordinate data and grid/matrix data
2.  use `plot()` and `scatter()`
3.  use `imshow()` and `contour()`
4.  perform matrix slicing using NumPy
5.  choose an appropriate visualization method

----------



# Solution

## 1. Explaining the Difference Between: (a) Coordinate Data (X–Y Data) and (b) Grid or Matrix Data

### 1. Coordinate Data (X–Y Data)

### Meaning

Coordinate data consists of **pairs of values**.

Each observation contains:

-   one **x-value**
-   one **y-value**

These values together form a **coordinate point**.

A graph is created by plotting many such points.

### General Form

```python
(x, y)
```

Example:

```python
(1, 18)(2, 21)(3, 25)
```

These points may represent:
| Month | Temperature |
| --- | --- |
| 1 | 18 |
| 2 | 21 |
| 3 | 25 |

Here:

-   x-axis → Month
-   y-axis → Temperature

Common Plot Types for Coordinate Data

| Plot Type | Function |
| --- | --- |
| Line graph | plot() |
| Scatter plot | scatter() |


### Real-Life Examples of Coordinate Data

-   student marks across subjects
-   monthly rainfall
-   yearly population growth
-   temperature across months
-   company sales across years

----------

## 2. Grid or Matrix Data

### Meaning

Grid or matrix data consists of values arranged in:

-   **rows**
-   **columns**

Each position in the grid contains a value.

This type of data looks like a table.

### Example

Suppose temperature is recorded for several cities:

| City / Month | Jan | Feb | Mar |
| --- | --- | --- | --- |
| Delhi | 18 | 21 | 25 |
| Ranchi | 15 | 19 | 22 |
| Mumbai | 26 | 28 | 30 |

This can be represented as:

```python
[ 
[18, 21, 25], 
[15, 19, 22], 
[26, 28, 30]
]
```

This is called a **matrix or grid**.

## Script

```python
# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Create matrix data. This is a 3x3 matrix where each row represents a 
# different set of temperature readings.
data = np.array([
    [18, 21, 25],
    [15, 19, 22],
    [26, 28, 30]
])

# Display matrix using colors. 
# Each cell's color intensity corresponds to its value, creating a heatmap effect.
plt.imshow(data)

# Add title
plt.title("Temperature Grid")

# Display graph
plt.show()


```
#### Output
![Temperature Grid](/resources/ch15-temperature-grid.png)


### Common Plot Types for Grid/Matrix Data

| Plot Type | Function |
| --- | --- |
| Heat map style plot | imshow() |
| Contour plot | contour() |
| Filled contour plot | contourf() |


### Comparison Between Coordinate Data and Grid Data


| Feature | Coordinate Data | Grid / Matrix Data |
| --- | --- | --- |
| Structure | X–Y pairs | Rows and columns |
| Example | Month vs temperature | City × Month temperature |
| Shape | Separate lists/arrays | Matrix/table |
| Common Methods | plot(), scatter() | imshow(), contour() |


### Flowchart: Types of Plot Data

XXX


## Important Note

> **Important:**  
> Having two variables does **not automatically mean grid data**.
> For example:
> Month and temperature contain **two variables**, but they are usually plotted as **coordinate data**.
> Grid data occurs when values are arranged in **rows and columns**.

## Answer2. Solution to: Explain the Purpose of the Following Matplotlib Methods

### 1. `plot()`

### Purpose

`plot()` is used to create a **line graph**.

It joins data points using lines.

### Best Use

It is useful for showing:

-   trends
-   growth
-   increase or decrease over time

### Simplified Syntax

```
plt.plot(x_values, y_values)
```

### Example

```python
# import matplotlib
import matplotlib.pyplot as plt
# Create data
x = [1, 2, 3, 4]
y = [10, 20, 15, 30]
# Plot line 
graphplt.plot(x, y)
# Display graph
plt.show()
```

### Typical Uses

-   sales trend
-   rainfall trend
-   stock prices
-   student performance

----------

## 2. `scatter()`

### Purpose

`scatter()` is used to create a **scatter plot**.

It displays individual points without joining them.

### Best Use

It is useful for studying:

-   relationships
-   clustering
-   spread of data

### Simplified Syntax

```
plt.scatter(x_values, y_values)
```

### Example

```python
# Import matplotlib
import matplotlib.pyplot as plt
# Create data
height = [150, 155, 160, 165]
weight = [45, 50, 52, 60]
# Create scatter plot
plt.scatter(height, weight)
# Display graph
plt.show()
```

### Typical Uses

-   height vs weight
-   study time vs marks
-   advertising cost vs sales

----------

## 3. `imshow()`

### Purpose

`imshow()` displays matrix values using **colors**.

Larger values and smaller values are represented using different colors.

### Best Use

It is useful for:

-   images
-   heat maps
-   matrix data

### Simplified Syntax

```python
plt.imshow(matrix)
```

### Example

```python
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
# Create matrix
data = np.arange(25)
# Convert into matrix
data = data.reshape(5, 5)
# Display matrix
plt.imshow(data)
# Display graph
plt.show()
```

----------

## 4. `contour()`

### Purpose

`contour()` draws lines joining places having the **same value**.

These lines are called **contour lines**.

### Best Use

It is useful for:

-   weather maps
-   height maps
-   pressure maps

### Simplified Syntax

```python
plt.contour(X, Y, Z)
```

### Example

```
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
# Create x values
x = np.linspace(-3, 3, 50)
# Create y values
y = np.linspace(-3, 3, 50)
# Create coordinate grid
X, Y = np.meshgrid(x, y)
# Create height values
Z = np.sin(X) * np.cos(Y)
# Draw contour 
plotplt.contour(X, Y, Z)
# Display graph
plt.show()
```

### Comparison of Plotting Methods

| Method | Type of Data | Best Use |
| --- | --- | --- |
| plot() | Coordinate data | Trends |
| scatter() | Coordinate data | Relationships |
| imshow() | Matrix data | Heat maps |
| contour() | Matrix data | Equal-value regions |


### Common Beginner Error

```python
# WRONG EXAMPLE
# A 1-D list is passed to imshow()
# data = [1, 2, 3, 4]
# plt.imshow(data)
# This may cause an error because
# imshow() expects matrix-style data
```

## Answer3. Solution to: Explain the Role of Matrix Slicing in NumPy

----------

### Meaning of Matrix Slicing

Matrix slicing means **extracting a selected portion of a matrix**.

Sometimes the entire matrix is not required.

A programmer may need:

-   only selected rows
-   only selected columns
-   a smaller section of data

Instead of manually copying values, NumPy allows easy extraction using **slicing**.

----------

## Why Matrix Slicing is Important

Matrix slicing is useful because:

-   it helps focus on selected data
-   reduces unnecessary processing
-   allows comparison of specific regions
-   makes visualization easier

For example:

Suppose passenger data is available from:

**1949 to 1960**

But analysis is required only for:

**1952 to 1958**

Instead of using the complete dataset, only the required rows may be extracted.

----------

## Example Matrix

Suppose the following matrix is given:

```python
import numpy as np
# Create matrix
A = np.arange(25)
# Convert into 5 × 5 matrix
A = A.reshape(5, 5)
# Display matrix
print(A)
```

### Output

```python
[[ 0  1  2  3  4] 
[ 5  6  7  8  9] 
[10 11 12 13 14] 
[15 16 17 18 19] 
[20 21 22 23 24]]
```

----------

## General Syntax of Matrix Slicing

```python
matrix[row_start:row_end,
       column_start:column_end]
```

### Meaning of Terms

| Part | Meaning |
| --- | --- |
| row_start | Starting row index |
| row_end | Ending row index (excluded) |
| column_start | Starting column index |
| column_end | Ending column index (excluded) |


## Example 1: Extract Selected Rows

```
# Extract rows 1 to 3
B = A[1:4, :]
# Display result
print(B)
```

### Explanation
`1:4` means:

-   start at row index **1**
-   stop before row index **4**

`:` means:

> select all columns

### Output

```python
[[ 5  6  7  8  9] 
[10 11 12 13 14] 
[15 16 17 18 19]]
```

----------

## Example 2: Extract Selected Columns

```python
# Extract columns 1 to 3
B = A[:, 1:4]
# Display result
print(B)
```

### Explanation

`:`

means: all rows

`1:4` means: columns 1 to 3

### Output

```python
[[ 1  2  3] 
[ 6  7  8] 
[11 12 13] 
[16 17 18] 
[21 22 23]]
```

----------

## Example 3: Extract a Smaller Matrix

```python
# Extract middle section
B = A[1:4, 1:4]
# Display result
print(B)
```

### Output

```
[[ 6  7  8] 
[11 12 13] 
[16 17 18]]
```

----------

## Mermaid Flowchart — Matrix Slicing

XXX


## Small Concept Script

```
# import NumPy
import numpy as np
# Create matrix
matrix = np.arange(36)
# Convert to 6 × 6 matrix
matrix = matrix.reshape(6, 6)
# Display full matrix
print("Original Matrix")
print(matrix)
# Slice smaller section
small_matrix = matrix[2:5, 1:4]
# Display sliced matrix
print("Sliced Matrix")
print(small_matrix)
```

----------

## Common Beginner Error

```
# WRONG EXAMPLE
# Trying to access invalid index
# matrix = np.arange(25).reshape(5, 5)
# print(matrix[10])
# IndexError may occur because
# row 10 does not exist
```

----------

## Important Note

> **Remember:**  
> In slicing, the ending index is **not included**.

Example: `A[1:4]` means: `1, 2, 3`, not: `1, 2, 3, 4`

----------

### Compare the Following Methods in Tabular Form


| Method | Type of Data | Main Purpose | Typical Use |
| --- | --- | --- | --- |
| plot() | Coordinate Data | Draws line graph | Trends over time |
| scatter() | Coordinate Data | Shows separate points | Relationship analysis |
| imshow() | Grid / Matrix Data | Displays values using colors | Heat maps, images |
| contour() | Grid / Matrix Data | Draws equal-value lines | Weather and height maps |


### Additional Comparison

| Feature | plot() | scatter() | imshow() | contour() |
| --- | --- | --- | --- | --- |
| Joins points | Yes | No | No | No |
| Uses colors | Limited | Limited | Yes | Yes |
| Matrix data | No | No | Yes | Yes |
| Best for | Trends | Relationships | Heat maps | Regions/levels |


## Part B — Programming Model Solution

### Task 1 — Load the Dataset

### Objective

To load the **flights dataset** from Seaborn and understand its columns.

```python
# Import required libraries
import seaborn as sns

# Load flights dataset. This dataset contains monthly passenger counts for 
# an airline over several years, making it ideal for time series analysis and visualization.
df = sns.load_dataset("flights")

# Display first five rows. This gives us a quick look at the structure of the dataset, 
# including the columns and sample data.
print(df.head())

# Display column names. This helps us understand 
# the different attributes available in the dataset.
print(df.columns)

```

#### Output

```python
   year month  passengers
0  1949   Jan         112
1  1949   Feb         118
2  1949   Mar         132
3  1949   Apr         129
4  1949   May         121
Index(['year', 'month', 'passengers'], dtype='str')

```









