

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

```python
# 1. Explicit Inheritance
class Dog(object):
    pass

# 2. Implicit Inheritance (Python 3 automatically adds object)
class Cat:
    pass

# Function to trace ancestry
def trace_ancestry(cls):
    print(f"Ancestry of {cls.__name__}:")
    # __mro__ shows the hierarchy from Child to Root
    for i, ancestor in enumerate(cls.mro()):
        print(f"  Level {i}: {ancestor}")
    print("-" * 30)

# --- Testing User Defined Classes ---
trace_ancestry(Dog)  # This will show that Dog inherits from object
# Output:
# Ancestry of Dog:
#   Level 0: <class '__main__.Dog'>
#   Level 1: <class 'object'>

trace_ancestry(Cat)  # This will show that Cat also inherits from object
# Output:
# Ancestry of Cat:
#   Level 0: <class '__main__.Cat'>
#   Level 1: <class 'object'>


# --- Testing Built-in Types ---
# This proves that even 'int' and 'str' are objects!
trace_ancestry(int)  # This will show that int inherits from object
# Output:
# Ancestry of int:
#   Level 0: <class 'int'>
#   Level 1: <class 'object'>
trace_ancestry(str)  # This will show that str inherits from object
# Output:
# Ancestry of str:
#   Level 0: <class 'str'>
#   Level 1: <class 'object'>
trace_ancestry(list)  # This will show that list inherits from object
# Output:
# Ancestry of list:
#   Level 0: <class 'list'>
#   Level 1: <class 'object'>

# --- The Ultimate Proof ---
print(f"Is Dog a subclass of object? {issubclass(Dog, object)}")
# Output: Is Dog a subclass of object? True

print(f"Is Cat a subclass of object? {issubclass(Cat, object)}")
# Output: Is Cat a subclass of object? True

print(f"Is int a subclass of object? {issubclass(int, object)}")
# Output: Is int a subclass of object? True



```















