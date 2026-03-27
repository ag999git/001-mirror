





## Research Question: How does Python’s `with` statement implement the context management protocol using `__enter__()` and `__exit__()` methods, and how does it ensure proper resource handling and exception management?


### Sub-Questions

Explore:

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
The following script shows the use of custom context manager

```python

# Custom Context Manager

class SafeFileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Resource acquisition
        print("1. __enter__(): Opening file")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        # Cleanup (always executed)
        print("3. __exit__(): Closing file")

        if self.file:
            self.file.close()

        # Exception handling behavior
        if exc_type:
            print("Exception occurred:", exc_type.__name__)

            # Example: suppress ValueError only
            if exc_type == ValueError:  # Handle ValueError and suppress it
                print("ValueError handled inside __exit__")
                return True   # suppress exception

        return False   # propagate exceptions other than ValueError

# Example usage of the custom context manager
fileName = r"example.txt"  # Make sure this file exists for the test    
with SafeFileHandler(fileName, "r") as f:
    content = f.read()  # This will read the file content. If the file does not exist, it will raise FileNotFoundError which will be handled by __exit__.
    print(content)  
    # Uncomment the next line to simulate an exception inside the with block
    # raise ValueError("Simulated ValueError")  # This will be handled by __exit__  
    # Uncomment the next line to simulate an exception that is not handled by __exit__
    # raise KeyError("Simulated KeyError")  # This will propagate and not be handled by __exit__


```





















