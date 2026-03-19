

### Research Question

**Topic: The Universal Ancestry of the `object` Class**

> **Question:** "Investigate the role of the `object` class as the ultimate base class in Python's type hierarchy. How does the 'Implicit Inheritance' of `object` provide every Python entity with its fundamental capabilities (such as identity, string representation, and attribute storage), and how can we programmatically prove that even primitive types like `int` and `str` are descendants of this root?"

----------

#### Discussion/ Solution

#### **The Root of the Ecosystem**

In Python, `object` is the most humble yet powerful class. It is a built-in class that serves as the base for all other classes.

-   **Implicit vs. Explicit:** In Python 3, writing `class Pet:` is exactly the same as writing `class Pet(object):`. The interpreter automatically plugs `object` in as the parent.
    
-   **What `object` provides:** It introduces "Dunder" methods that all objects need. For example:
    
    -   `__new__`: To physically create the object in memory.
        
    -   `__init__`: To allow initialization.
        
    -   `__repr__` and `__str__`: To give the object a string name.
        
    -   `__eq__`: To allow objects to be compared using `==`.
        
-   **The MRO (Method Resolution Order):** Every class has an attribute called `__mro__`. If you look at the MRO of any class, the very last entry will always be `<class 'object'>`. This is the "Full Stop" of Python's look-up logic.
    

----------

#### Script: Proving the Ancestry

This script demonstrates the difference between explicit and implicit inheritance and proves that even built-in types are "objects."



