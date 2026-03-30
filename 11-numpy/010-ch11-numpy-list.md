


## Difference between Python lists and Numpy arrays

This script demonstrates the **key differences between Python Lists and NumPy Arrays**.  
Both are used to store collections of data, but they behave differently in terms of:

1.  Memory usage
2.  Data type flexibility
3.  Speed and operations
4.  Mathematical and statistical computations

Python lists are general-purpose containers, while NumPy arrays are designed for **scientific computing and numerical processing**.

By running this script, you will observe:

-   How much memory each structure uses
-   How data types are handled
-   How operations are performed differently
-   Why NumPy is widely used in data science, machine learning, and scientific programming

----------

## Libraries, Attributes, and Methods Used in the Script

### 1. NumPy Library

`NumPy` (Numerical Python) is a powerful library used for numerical computing.

Key functions used:


  

| Function / Attribute | Purpose |
| --- | --- |
| np.array() | Creates a NumPy array |
| np.arange() | Creates an array of evenly spaced values |
| np.sqrt() | Calculates square root of each element |
| np.sum() | Calculates total sum |
| np.mean() | Calculates average value |
| np.min() | Finds minimum value |
| np.max() | Finds maximum value |
| np.std() | Calculates standard deviation |
| .dtype | Shows data type of array elements |
| .nbytes | Shows memory used by the array |





### 2. sys Module

The built-in `sys` module provides system-related information.

  

| Function | Purpose |
| --- | --- |
| sys.getsizeof() | Returns memory size of an object in bytes |

### 3. Python Concepts Used

  

| Concept | Purpose |
| --- | --- |
| list(range()) | Generates list of numbers |
| List comprehension | Compact way to create lists |
| f-strings | Formatted printing |
| Loops | Iterating over elements |


### 4. Flow of Execution of the Script

The program runs in the following sequence:

Step 1 – Import required libraries  
Step 2 – Create a Python list and NumPy array  
Step 3 – Compare memory usage  
Step 4 – Demonstrate how lists and arrays handle mixed data types  
Step 5 – Perform element-wise operations  
Step 6 – Perform mathematical operations  
Step 7 – Use NumPy aggregation functions  
Step 8 – Display results


### Script







### Explanation of the Results

After running the script, you will observe the following important conclusions:

### 1. Memory Efficiency

NumPy arrays usually use **much less memory** than Python lists because:

-   Lists store references to objects
-   NumPy stores data in a **compact continuous block of memory**

This makes NumPy ideal for **large datasets**.

----------

### 2. Data Type Behavior

Python lists can store **mixed data types**, such as:

-   integers
-   strings
-   floats
-   booleans
-   even other lists

NumPy arrays, however, convert all elements into **one common data type** to improve performance.

----------

### 3. Operations

Operations on NumPy arrays are:

-   Faster
-   Simpler
-   More readable

Example:

`array * 2`

instead of writing loops.

This is called **vectorization**.

----------

### 4. Mathematical Capabilities

NumPy provides built-in mathematical functions such as:

-   square root
-   mean
-   sum
-   standard deviation

These are extremely useful in:

-   Data Science
-   Machine Learning
-   Statistics
-   Scientific computing

----------

### Final Conclusion

Python lists are best for:

-   General programming
-   Mixed data storage

NumPy arrays are best for:

-   Numerical computation
-   Data analysis
-   Performance-critical applications















