



### **Research Question**

> Investigate the difference between `__str__()` and `__repr__()` methods in Python classes.  
> When should each method be used? What happens when only one of them is defined?



In this chapter in the book, we learned how to define the string representation of an object using the `__str__()` method. However, Python provides another important method called `__repr__()`.

Although the difference between these two methods is subtle, it is very important.

### Key Differences

-   `__str__()`
    
    -   Called by the built-in function `str()` and by `print()`
        
    -   Provides a **user-friendly (informal)** string representation
        
    -   Intended for end users
        
-   `__repr__()`
    
    -   Called by the built-in function `repr()`
        
    -   Provides an **official (formal)** string representation
        
    -   Intended for developers (debugging, logging)
        

### Important Rule

If a class defines `__repr__()` but does **not** define `__str__()`, then calling `str()` (or `print()`) will automatically use the `__repr__()` method.

### **Task Instructions**

1.  Create a class `Pet` with attributes like `name` and `type`.
    
2.  Implement both `__str__()` and `__repr__()` methods.
    
3.  Observe outputs of:
    
    -   `print(object)`
        
    -   `str(object)`
        
    -   `repr(object)`
        
4.  Remove the `__str__()` method and observe the change.
    
5.  Write your conclusions.

----------

### Case 1: When both __str__() and __repr__() are defined
The following script shows the output when both`__str__()` and `__repr__()`are defined


### Case : When both __str__() is not defined nut `__repr__()` is defined:
The following script shows the output when str__() is not defined nut `__repr__()` is defined:






