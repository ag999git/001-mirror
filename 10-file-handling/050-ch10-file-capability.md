



## 1. PROJECT

## Title: “Investigation of File Capability Methods in Python: `readable()`, `writable()`, and `seekable()`”

----------

## Problem Statement

Write a Python program to study and demonstrate the behavior of the following file object methods:

-   `file.readable()`
-   `file.writable()`
-   `file.seekable()`

----------

## Objectives

Your program must:

### A. Functional Study

1.  Open files in different modes:
    -   `'r'`, `'w'`, `'a'`, `'r+'`, `'rb'`
2.  For each mode, check:
    -   Whether file is readable
    -   Whether file is writable
    -   Whether file is seekable

----------

### B. Experimental Verification

-   Attempt operations based on capability:
    -   Call `read()` only if `readable() == True`
    -   Call `write()` only if `writable() == True`
    -   Call `seek()` only if `seekable() == True`

----------

### C. Error Demonstration

-   Show what happens if:
    -   You try to read from a non-readable file
    -   You try to write to a non-writable file
-   Include these as **commented (unhashed) lines**

----------

### D. Best Practices

-   Use `with` statement
-   Avoid unsafe operations
-   Use capability checks before operations

----------

## Learning Outcomes

By using  File Capability Methods in Python one can:

-   Predict file behavior based on mode
-   Write safe file-handling code
-   Avoid runtime errors using capability checks

----------

## 2. EXPECTED ANSWER (CONCEPTUAL)

### `readable()`

Returns `True` if the file is opened in a mode that allows reading.  
Example: `'r'`, `'r+'`, `'rb'`

----------

### `writable()`

Returns `True` if writing is allowed.  
Example: `'w'`, `'a'`, `'r+'`

----------

### `seekable()`

Returns `True` if the file supports random access (moving pointer).  
Most disk files return `True`.















