




## PROJECT: Study of Exceptions using `sys` and `traceback`**



### RESEARCH QUESTION: “How does Python internally represent exceptions, and how can the `sys` and `traceback` modules be used to extract, analyze, and present detailed information about errors?”



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
`sys.exc_info()` gives a tuple of 3 components in form of a tuple as shown below:
`(type, value, traceback) =  sys.exc_info()`


  The meaning of each component is shown in table below:

| Component | Meaning |
| --- | --- |
| Type | Exception class |
| Value | Exception object |
| Traceback | Call stack info |




### 3. traceback Module

-   It is used to extract and format stack traces

### Important Functions of traceback module are:

  

| Function | Purpose |
| --- | --- |
| extract_tb() | Structured traceback |
| format_exc() | Full formatted string |
| print_exc() | Print traceback |


### 4. Stack Trace Concept

-   A stack trace shows:
    -   Sequence of function calls
    -   Where error occurred



### 5. Basic vs Detailed Error
`str(e)` cannot give as much details as the `traceback` module. The difference beyween the two is shown in table below:
  

| Feature | str(e) | traceback |
| --- | --- | --- |
| Detail level | Low | High |
| Shows location | No | Yes |
| Shows call stack | No | Yes |

## PART 2: SCRIPT QUESTION

> Write a Python program that:
> 
> 1.  Defines at least **two nested functions**
> 2.  Intentionally generates an exception (e.g., division by zero)
> 3.  Uses:
>     -   `try-except`
>     -   `sys.exc_info()`
>     -   `traceback.extract_tb()`
> 4.  Prints:
>     -   Exception type
>     -   Exception message
>     -   File name
>     -   Line number
>     -   Function name
>     -   Code line causing error
> 5.  Also prints the **full formatted traceback**
> 6.  Ensures program continues after handling the exception



## SCRIPT (ANSWER)











