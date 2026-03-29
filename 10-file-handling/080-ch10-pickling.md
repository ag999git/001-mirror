




## PROJECT/ TASK QUESTION

## Title

**“Study of Object Serialization in Python using Pickle: Features, Limitations, and Security Concerns”**

----------

## Problem Statement

Design a Python program to explore **pickling and unpickling** of different Python objects and analyze:

1.  Behavior with multiple data types
2.  Binary representation of stored data
3.  Security risks of unpickling
4.  Error handling

----------

## Objectives

### A. Functional Study

-   Pickle and unpickle:
    -   List
    -   Dictionary
    -   Custom class object

----------

### B. Binary Inspection

-   Read raw file content using `read()`
-   Analyze byte stream

----------

### C. Error Demonstration

-   Try:
    -   Loading from empty file
    -   Loading corrupted file

----------

### D. Security Awareness

-   Understand why unpickling untrusted data is dangerous

----------

## ANSWER (CONCEPTUAL)

### Key Observations

1.  Pickle stores:
    -   Object data
    -   Instructions to reconstruct object
2.  Unpickling:
    -   Recreates object instance
    -   Restores attributes
3.  Pickle is:
    -   Python-specific
    -   Not secure for untrusted data

----------

### Table of common errors and their causes in Pickling/ Unpickling


  

| Error | Cause |
| --- | --- |
| `EOFError` | Empty file |
| `pickle.UnpicklingError` | Corrupted file |
| `AttributeError` | Class not defined |


## Script










