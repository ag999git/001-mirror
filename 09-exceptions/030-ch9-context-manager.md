





## Research Question: How does Python’s `with` statement implement the context management protocol using `__enter__()` and `__exit__()` methods, and how does it ensure proper resource handling and exception management?


### Sub-Questions

Students must explore:

1.  What is a **context manager**?
2.  What is the **context management protocol**?
3.  What is the role of:
    -   `__enter__()`
    -   `__exit__()`
4.  What values does `__exit__()` receive?
5.  How does `with` internally behave like `try-finally`?
6.  What happens:
    -   when **no exception occurs**
    -   when **exception occurs**
7.  What is the effect of returning:
    -   `True`
    -   `False` from `__exit__()`?
8.  How does a context manager ensure **resource cleanup**?
9.  Compare:
    -   `with` vs manual `try-finally`
10.  Give **at least 2 real-life use cases**

----------

## Expected Output

-   Conceptual write-up (2–3 pages)
-   Example scripts

----------

## PART 2: Project / Coding Task



> _Design a custom context manager class named `SafeFileHandler` that:_
> 
> 1.  Opens a file in `__enter__()`
> 2.  Closes the file in `__exit__()`
> 3.  Demonstrates behavior for:
>     -   Normal execution
>     -   Exception during file operation
> 4.  Demonstrates how exceptions:
>     -   propagate
>     -   can optionally be suppressed
> 
> _Write test cases to clearly show all execution paths._

----------

## PART 3: Answer 



## 1. Custom Context Manager**
























