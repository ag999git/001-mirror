



## 1. PROJECT “Study of seek(offset, whence) in Python and Its Behavior in Text vs Binary Files”



## Problem Statement

Write a Python program to investigate the behavior of the `seek()` method using different values of `offset` and `whence`.

Your program must:

### A. Understand Method Signature

Study and explain:

-   `seek(offset[, whence])`

Where:

-   **offset (Required):** Number of bytes to move the cursor
-   **whence (Optional):**
    -   `0 (SEEK_SET)` → from beginning
    -   `1 (SEEK_CUR)` → from current position
    -   `2 (SEEK_END)` → from end

----------

### B. Experimental Tasks

1.  Demonstrate:
    -   `seek(offset, 0)`
    -   `seek(offset, 1)`
    -   `seek(offset, 2)`
2.  Compare behavior in:
    -   Text mode
    -   Binary mode
3.  Show pointer movement using `tell()`

----------

### C. Critical Investigation 

Demonstrate the following caution:

> Seeking to an arbitrary byte offset in a multi-byte encoded file (like UTF-8) may land the cursor in the middle of a character, causing a `UnicodeDecodeError`.

----------

### D. Best Practices

-   Use `with` statement
-   Use proper encoding (`utf-8`)
-   Handle exceptions
-   Demonstrate correct vs incorrect usage

----------

## 2. EXPECTED ANSWER (CONCEPTUAL)

### Key Observations

1.  `seek(offset, 0)`
    -   Moves pointer relative to **start**
    -   Works in both text and binary modes
2.  `seek(offset, 1)` and `seek(offset, 2)`
    -   Reliable only in **binary mode**
    -   Limited or unsafe in text mode
3.  **Binary Mode Advantage**
    -   Precise byte-level control
    -   Suitable for random access
4.  **Text Mode Limitation**
    -   Encoding-dependent
    -   Pointer may not align with characters

----------

### Critical Insight

In UTF-8:

-   Some characters use **multiple bytes**
-   If `seek()` lands in the middle → decoding fails

----------

## 3.  Script










