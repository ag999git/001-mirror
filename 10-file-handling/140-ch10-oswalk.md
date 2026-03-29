



# Research Question

**Q.**  
The `os.walk()` function in Python is used to traverse a directory tree.

You are required to:

1.  Explain the working of `os.walk()` with its parameters:
    -   `top`, `topdown`, `onerror`, `followlinks`
2.  Describe the meaning of the returned values:
    -   `dirpath`, `dirnames`, `filenames`
3.  Write a Python script to:
    -   Traverse a given directory
    -   Calculate total size of files in each directory
4.  Modify the script to:
    -   Exclude a specific directory (e.g., `__pycache__` or `CVS`)
5.  Identify possible errors and explain how to handle them

----------

## Concept Explanation

### What is `os.walk()`?

-   A **generator function**
-   Traverses directory tree **recursively**
-   Yields a tuple given below:
`(dirpath, dirnames, filenames)`

----------

### Key Idea

Instead of manually writing recursion, Python gives it built-in.

----------

## Script







