



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

```python

# Demonstration of os.walk()

import os
from os.path import join, getsize  # Import join and getsize functions from os.path module for handling file paths and getting file sizes

# Define directory path
path = "."  # Current directory (you can change this to any directory you want to traverse)

# Traverse directory tree
for root, dirs, files in os.walk(path):  # os.walk() generates a tuple of (root, dirs, files) for each directory in the tree

    # Print current directory
    print("Directory:", root)  # Print the current directory being traversed

    # Calculate total size of files
    total_size = 0  # Initialize total size variable to accumulate the size of files in the current directory

    for file in files:  # Iterate through each file in the current directory
        full_path = join(root, file)  # Get full path of the file by joining root and file name

        # Add file size
        total_size += getsize(full_path)  # Get size of the file and add it to total_size

    print("Total size:", total_size, "bytes")  # Print total size of files in the current directory
    print("Number of files:", len(files))  # Print number of files in the current directory
    print("Subdirectories:", dirs)  # Print list of subdirectories in the current directory
    print("Files:", files)  # Print list of files in the current directory
    print("-" * 40)

    # Exclude a directory from traversal
    if "__pycache__" in dirs:  # Check if __pycache__ directory is in the list of subdirectories
        dirs.remove("__pycache__")   # prevents traversal into __pycache__ directories


```





