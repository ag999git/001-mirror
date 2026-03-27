




## PROJECT: Study of Exceptions using `sys` and `traceback`**

----------

### RESEARCH QUESTION: “How does Python internally represent exceptions, and how can the `sys` and `traceback` modules be used to extract, analyze, and present detailed information about errors?”

----------

### Details of the problem:

1.  What is an **exception object**
2.  Role of:
    -   `sys.exc_info()`
    -   `traceback` module
3.  Structure of:
    -   Exception type
    -   Exception value
    -   Traceback object
4.  How Python builds a **stack trace**
5.  Difference between:
    -   Basic error message (`str(e)`)
    -   Full traceback
6.  Practical uses:
    -   Debugging
    -   Error reporting

----------

## ANSWER

### 1. Exception Representation in Python

-   Exceptions are **objects created from classes**
-   When an error occurs:
    -   Python creates an **exception object**
    -   Stores:
        -   Type
        -   Message
        -   Traceback

----------

### 2. sys.exc_info()

`(type, value, traceback) =  sys.exc_info()`












