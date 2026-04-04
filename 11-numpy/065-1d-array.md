


# 1D Arrays: 

## Step-by-Step Visualization

We start with two 1D arrays in **NumPy**:

`x  =  np.array([1, 2])`
`y  =  np.array([3, 4])`

----------

### Step 1: How NumPy “sees” 1D arrays

A 1D array has **shape `(2,)`**, meaning:
For x
```python
     x → [1   2]  
          ↑   ↑  
    index 0,  1  
```
For y
```python
     y → [3   4]
          ↑   ↑  
    index 0,  1 
```
👉 Important:

-   There is **no row/column distinction yet**
-   It is just a **flat vector**

----------

### Step 2: `np.hstack((x, y))`

#### Operation: “Join along existing axis”

Since 1D arrays only have **axis = 0**, `hstack` behaves like:

```python
[1   2]  +  [3   4]  
 ↓           ↓  
Concatenate along axis 0
```

#### Result:

[1   2   3   4]

#### Shape:

(4,)

----------

### Step 3: `np.concatenate((x, y), axis=0)`

This is exactly the same operation:

```python
[1   2]  +  [3   4]  
 ↓           ↓  
axis = 0
```

#### Result:

[1   2   3   4]

####  Key Insight:

> For 1D arrays, **`hstack()` = `concatenate(axis=0)`**

----------

###  Step 4: `np.vstack((x, y))`

Now things change 

#### Step 4A: Implicit reshaping

`vstack()` first converts 1D arrays into **row vectors (2D)**:

x → [[1   2]]   shape (1,2)  ie 1 row and 2 columns
y → [[3   4]]   shape (1,2) ie 1 row and 2 columns

##### This step is **hidden but crucial**

----------

#### Step 4B: Stack along axis 0

Now we stack rows:

```
[[1   2]]  
[[3   4]]
```
#### Final Result:
```
[[1   2]  
 [3   4]]
```

#### Shape:
(2, 2)

### Side-by-Side Comparison

  

| Operation | Internal Step | Result | Shape |
| --- | --- | --- | --- |
| hstack | No reshape | [1 2 3 4] | (4,) |
| concatenate(axis=0) | No reshape | [1 2 3 4] | (4,) |
| vstack | Reshape → (1,2) | [[1 2],[3 4]] | (2,2) |


