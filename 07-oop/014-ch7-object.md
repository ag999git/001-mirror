



### Research Question: The "Single Root" Architecture of Python

**Part A: Universal Ancestry and Implicit Inheritance** Investigate the role of the `object` class as the ultimate base class in Python's type hierarchy. How does the "Implicit Inheritance" of `object` provide every Python entity—whether a user-defined class or a primitive type like `int` and `str`—with its fundamental capabilities (such as identity, string representation, and memory allocation)?

**Part B: Programmatic Proof and the MRO** How do the `__mro__` (Method Resolution Order) attribute and the `issubclass()` function prove this architecture? Explain why Python 3 made inheritance from `object` implicit and identify which essential "dunder" methods are inherited even by an empty class.

----------

#### Discussion/ Solution

#### **Part A: The Foundation of Every Entity**

In Python, **everything is an object**. To make this possible, Python 3 utilizes a "Single Root" hierarchy where the built-in class `object` sits at the very top.

-   **Fundamental Capabilities:** By inheriting from `object`, every class automatically gains "low-level" logic. For instance, `__new__` handles the physical creation of the object in RAM, and `__repr__` provides a default way to display the object (e.g., `<__main__.Cat object at 0x...>`).
    
-   **Consistency:** This architecture ensures that integers, strings, and custom pets all share a common "DNA," allowing the Python interpreter to treat them uniformly in memory.
    

#### **Part B: Proving the Hierarchy**

-   **The MRO Proof:** The `__mro__` attribute (or `.mro()` method) lists the search path Python follows to find methods. No matter how complex the inheritance, the last stop is always `<class 'object'>`.
    
-   **Implicit Inheritance:** Python 3 introduced "New-Style Classes." Writing `class Cat:` is now shorthand for `class Cat(object):`. This was done to simplify syntax and ensure all classes benefit from modern OOP features like properties and descriptors.
    
-   **Inherited Dunder Methods:** An empty class still possesses over 20 methods inherited from `object`, including `__dir__` (to list attributes), `__eq__` (for equality checks), and `__init__` (the constructor).
    

----------

#### Script

This script gives a clear, "Level-based" view of ancestry.













