


# PROJECT: Golden Rules of Vectorization in NumPy

## Objective: The goal of this project is to:

-   Understand the concept of **vectorization in NumPy**
-   Compare **loop-based vs vectorized approaches**
-   Learn and apply the **Golden Rules of Vectorization**
-   Analyze **performance, readability, and memory efficiency**
-   Write clean, efficient NumPy code

----------

## PART A — THEORY TASK (Research-Based)

### Task Instructions

Write a detailed note covering:

### 1. What is Vectorization?

-   Definition
-   Why it is important in NumPy
-   Difference from traditional Python loops

----------

### 2. The Golden Rules of Vectorization

Explain each of the following in detail:

1.  Avoid loops for numerical operations
2.  Avoid `np.append()` in loops
3.  Use Boolean masking instead of `if/else`
4.  Use NumPy ufuncs instead of Python `math` functions

For each rule, include:

-   Explanation
-   Example
-   Why the wrong approach is inefficient

----------

### 3. Performance Analysis

-   Why vectorization is faster
-   Role of C-level execution
-   Memory efficiency (no repeated copying)

----------

### 4. Comparison Table

Create a table comparing:

-   Loop-based approach
-   Vectorized approach

----------

### 5. Real-World Applications

Explain where vectorization is used:

-   Machine Learning
-   Data Analysis
-   Image Processing

----------

## PART B — SCRIPT TASK (Implementation)

## Task Instructions

Write a Python script that:

1.  Demonstrates each golden rule
2.  Shows:
    -   Wrong approach
    -   Correct approach
3.  Measures execution time
4.  Displays results clearly
5.  Includes **detailed comments**

----------

# ANSWER — THEORY

### 1. What is Vectorization?

Vectorization is the process of performing operations on entire arrays at once instead of using loops.
### Example:

```python

# Loop approach
result = []
for i in range(len(arr)):
    result.append(arr[i] * 2)

# Vectorized approach
result = arr * 2

```

## 2. Golden Rules Explained

### Rule 1: Avoid Loops

```python
# Dont do Loop:
for i in range(len(a)):
    c[i] = a[i] + b[i]

# Vectorized:
c = a + b

# Reason: Python loops are slow
```

### Rule 2: Avoid np.append()

```python

# Wrong:

arr = np.array([])
for i in range(1000):
    arr = np.append(arr, i)

#Problem: Creates new array every time → O(n²)

# Correct:

temp = []
for i in range(1000):
    temp.append(i)

arr = np.array(temp)

```

Rule 3: Boolean Masking

```python

# Wrong:

result = []
for x in arr:
    if x > 10:
        result.append(x)

# Correct:

result = arr[arr > 10]
```

### Rule 4: Use Ufuncs

```python

# Wrong:

import math
[math.sqrt(x) for x in arr]

# Correct:

np.sqrt(arr)

```

## 3. Why Vectorization is Faster

  

| Reason | Explanation |
| --- | --- |
| C-level execution | NumPy runs in optimized C code |
| No Python loops | Avoid interpreter overhead |
| Memory efficiency | No repeated allocations |
| SIMD optimization | CPU-level parallelism |


## 4. Comparison Table


| Aspect | Loop Approach | Vectorized Approach |
| --- | --- | --- |
| Speed | Slow | Fast |
| Readability | Low | High |
| Memory | Inefficient | Efficient |
| Code Length | Long | Short |












