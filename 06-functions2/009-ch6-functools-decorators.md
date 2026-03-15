


## Functools

`functools` is a Python standard library module that provides tools for working with functions, especially higher-order functions such as decorators. These **higher-order functions**—functions **operate on other functions** (for example modifying them, wrapping them, or combining them).

The function `functools.wraps()` is commonly used in decorators to preserve the metadata of the original function.



#### Uses of functool
It is especially useful for:

-   **Decorators**
    
-   **Function caching**
    
-   **Partial functions**
   
-   **Functional programming utilities**



#### Commonly used tools in `functools` include:

| Function | Purpose |
| --- | --- |
| wraps | Used when writing decorators to preserve metadata |
| lru_cache | Caches function results for faster repeated calls |
| partial | Fixes some arguments of a function |
| reduce | Applies a function cumulatively to items of an iterable |
| total_ordering | Simplifies writing comparison methods in classes |


#### Why `functools` is important for **decorators**

When we create a decorator, the **original function gets wrapped by another function**.

Without `functools`, some important information about the original function is **lost**, such as:

-   function name
    
-   docstring
    
-   help documentation
    

`functools.wraps()` **copies this metadata from the original function to the wrapper function**.








