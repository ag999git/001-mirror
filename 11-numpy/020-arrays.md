





# BEGINNER LEVEL FUNCTIONS





## 1. `np.array()`

**Signature**

`np.array(object, dtype=None, copy=True, ndmin=0)`

**Parameters**

-   `object` → list, tuple, nested list
-   `dtype` → data type (optional)
-   `copy` → whether to copy data
-   `ndmin` → minimum number of dimensions

**Output**

NumPy ndarray

Example output:

`array([1, 2, 3])`

**Common Usage**

-   Convert Python lists to arrays
-   Creating matrices

**Possible Errors**

`ValueError`: setting an array element with a sequence

Occurs when nested lists have inconsistent lengths.

**Important Notes**

-   Automatically infers datatype
-   Most commonly used NumPy function

----------

## 2. `np.zeros()`

**Signature**

`np.zeros(shape, dtype=float)`

**Parameters**

-   `shape` → tuple specifying dimensions
-   `dtype` → data type

**Output**

Array filled with zeros.

**Common Usage**

-   Initialization of matrices
-   Placeholder arrays

**Possible Errors**

`TypeError`: '`int`' object is not iterable

Occurs when incorrect shape provided.

----------

## 3. `np.ones()`

**Signature**

`np.ones(shape, dtype=float)`

**Output**

Array filled with ones.

**Common Usage**

-   Machine learning weight initialization
-   Matrix operations

----------

## 4. `np.full()`

**Signature**

`np.full(shape, fill_value, dtype=None)`

**Parameters**

-   `shape`
-   `fill_value`

**Output**

Array filled with a constant value.

----------

## 5. `np.arange()`

**Signature**

`np.arange(start, stop, step, dtype=None)`

**Output**

1D array.

Example:

`array([0,2,4,6,8])`

**Common Usage**

Generating numeric sequences.

**Common Error**

Floating step sometimes produces unexpected results due to precision.

----------

## 6. `np.linspace()`

**Signature**

`np.linspace(start, stop, num=50)`

**Output**

Evenly spaced array.

**Important Note**

Includes the stop value.

----------

## 7. `np.eye()`

**Signature**

`np.eye(N, M=None, k=0)`

**Parameters**

-   N rows
-   M columns
-   k diagonal offset

**Output**

Identity matrix.

----------

## 8. `np.random.rand()`

**Signature**

`np.random.rand(d0, d1, ..., dn)`

**Output**

Random array with values between 0 and 1.

----------
## Table (Beginner Level)

| S.No | Method | Purpose | Example | Input | Output | Key Concept | When to Use | Important Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | np.array() | Convert Python data to NumPy array | np.array([1,2,3]) | List / tuple | n-D array | Basic conversion | Almost always first step | Creates a new array |
| 2 | np.zeros() | Create array of zeros | np.zeros((2,3)) | Shape | Numeric array | Initialization | Default values | dtype defaults to float |
| 3 | np.ones() | Create array of ones | np.ones((3,3)) | Shape | Numeric array | Matrix creation | ML / matrices | Efficient initialization |
| 4 | np.full() | Create constant array | np.full((2,2),7) | Shape + value | Numeric array | Constant arrays | Defaults | Flexible dtype |
| 5 | np.arange() | Create sequence with step | np.arange(0,10,2) | Start/stop/step | 1D array | Range generation | Loops / sequences | Stop excluded |
| 6 | np.linspace() | Evenly spaced values | np.linspace(0,1,5) | Start/stop/count | 1D array | Fixed number of values | Plotting | Includes endpoint |
| 7 | np.eye() | Identity matrix | np.eye(3) | Size | Square matrix | Linear algebra basics | Matrix math | Supports diagonal offset |
| 8 | np.random.rand() | Random floats | np.random.rand(2,2) | Dimensions | Numeric array | Random generation | Simulations | Uniform distribution |




# INTERMEDIATE LEVEL FUNCTIONS

----------

## 9. `np.empty()`

**Signature**

`np.empty(shape, dtype=float)`

**Output**

Uninitialized array.

**Important**

Contains random memory values.

**Common Error**

Dont assume it contains zeros because it does not.

----------

## 10. `np.zeros_like()`

**Signature**

`np.zeros_like(a)`

Creates zero array matching structure.

----------

## 11. `np.ones_like()`

Same as above but fills with ones.

----------

## 12. `np.full_like()`

Copies structure with constant value.

----------

## 13. `np.identity()`

Simpler identity matrix function.

----------

## 14. `np.diag()`

Creates or extracts diagonal.

Common confusion:  
Behavior depends on input dimension.

----------

## 15. `np.logspace()`

Logarithmic scale array.

Used in scientific computing.

----------

## 16. `np.meshgrid()`

Used for coordinate grids.

Important in plotting surfaces.

----------

## 17. `np.indices()`

Creates index matrices.

Used in image processing and matrix math.

----------

## Table (Intermediate level)

  

| S. No | Method | Purpose | Example | Input | Output | Shape Rule | Key Feature | Typical Use | Important Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | np.empty() | Allocate array without initialization | np.empty((3,3)) | Shape | Numeric array | User-defined | Very fast allocation | Performance computing | Contains garbage values |
| 10 | np.zeros_like() | Copy shape but fill with zeros | np.zeros_like(A) | Array | Same shape array | Matches input | Template arrays | Algorithms | Keeps structure |
| 11 | np.ones_like() | Copy structure filled with ones | np.ones_like(A) | Array | Same shape | Same as source | Efficient replication | ML models | Keeps dtype |
| 12 | np.full_like() | Copy shape with constant value | np.full_like(A,9) | Array | Same shape | Based on input | Structured duplication | Matrix templates | Consistent structure |
| 13 | np.identity() | Identity matrix | np.identity(4) | Size | Square matrix | n × n | Simpler syntax | Linear algebra | Same as eye |
| 14 | np.diag() | Create or extract diagonal | np.diag([1,2,3]) | Array | Matrix/vector | Depends on input | Dual behavior | Matrix operations | Input type matters |
| 15 | np.logspace() | Logarithmic spacing | np.logspace(1,3,5) | Start/stop exp | 1D array | Fixed length | Log progression | Scientific computing | Engineering uses |
| 16 | np.meshgrid() | Create coordinate grid | np.meshgrid(x,y) | Arrays | Grid arrays | Expanded grid | Useful in plotting | 3D surfaces | Visualization |
| 17 | np.indices() | Create index grid | np.indices((3,3)) | Shape | Index arrays | Multi-dimensional | Matrix coordinates | Image processing | Advanced indexing |






# ADVANCED LEVEL FUNCTIONS

----------

## 18. `np.fromiter()`

**Signature**

`np.fromiter(iterable, dtype)`

Efficient creation from generators.

----------

## 19. `np.fromfunction()`

**Signature**

`np.fromfunction(function, shape)`

Generates array based on formula.

----------

## 20. `np.asarray()`

Converts input to array without copying if possible.

Memory efficient.

----------

## 21. `np.asanyarray()`

Similar to asarray but preserves subclasses.

----------

## 22. `np.random.randint()`

Random integers.

----------

## 23. `np.random.randn()`

Normal distribution values.

----------

## 24. `np.random.choice()`

Sampling from dataset.

----------

## 25. `np.random.uniform()`

Uniform distribution random numbers.


## Table (Advance Level)


  

| S. No. | Method | Purpose | Example | Input | Output | Key Idea | Performance Benefit | Typical Use | Important Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18 | np.fromiter() | Create array from iterator | np.fromiter(range(5), int) | Iterable | 1D array | Stream processing | Memory efficient | Large data streams | dtype required |
| 19 | np.fromfunction() | Generate array using formula | np.fromfunction(lambda i,j:i+j,(3,3)) | Function + shape | Computed array | Index-based creation | Vectorized generation | Mathematical modeling | Very powerful |
| 20 | np.asarray() | Convert without copying | np.asarray(data) | Sequence | Array | Memory sharing | Avoid duplication | Performance tuning | Faster conversion |
| 21 | np.asanyarray() | Preserve subclasses | np.asanyarray(data) | Array-like | Array/subclass | Flexible conversion | Specialized arrays | Advanced workflows | Rare in beginners |
| 22 | np.random.randint() | Random integers | np.random.randint(0,10,(3,3)) | Range + shape | Integer array | Discrete random | Dataset generation | Simulations | ML datasets |
| 23 | np.random.randn() | Gaussian distribution | np.random.randn(3,3) | Shape | Numeric array | Normal distribution | Statistical modeling | ML initialization | Standard normal |
| 24 | np.random.choice() | Random sampling | np.random.choice(a,5) | Dataset | Random array | Sampling method | Supports probabilities | Data science | With/without replacement |
| 25 | np.random.uniform() | Uniform distribution | np.random.uniform(0,5,10) | Range + size | Numeric array | Continuous random | Flexible distribution | Simulations | Common in statistics |























