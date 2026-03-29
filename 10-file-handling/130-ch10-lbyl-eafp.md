


## Question 1

**Q.**  
Python supports two important programming styles for handling errors:

-   **LBYL (Look Before You Leap)**
-   **EAFP (Easier to Ask Forgiveness than Permission)**

You are required to:

1.  Explain both approaches in the context of file handling
2.  Write Python scripts to:
    -   Check if a file exists before opening it (LBYL)
    -   Open a file directly and handle errors using exception handling (EAFP)
3.  Compare both approaches in terms of:
    -   Performance
    -   Readability
    -   Reliability
4.  Identify possible errors/exceptions that may occur
5.  Suggest best practices for using each approach

----------

## Concept Explanation

### LBYL (Look Before You Leap)

-   Check conditions **before performing an operation**
-   Example: Check if file exists before opening
-   Uses functions like:
    -   `os.path.isfile()`

**Idea:** Prevent errors before they happen

----------

### EAFP (Easier to Ask Forgiveness than Permission)

-   Perform operation directly
-   Handle errors **if they occur**
-   Uses:
    -   `try-except`

**Idea:** Assume success, handle failure



