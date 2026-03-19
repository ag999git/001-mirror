



## **Problem Statement**

You are required to design and implement a **Python-based Animal Management System** to demonstrate advanced concepts of **inheritance and object-oriented programming**.

Your solution must include multiple classes, inheritance relationships, and method implementations that collectively demonstrate key OOP features.


### PART A: CLASS DESIGN

#### 1. Create an Abstract Base Class

-   Create a class `Animal` using `ABC`
    
-   Include:
    
    -   `__init__(self, name)`
        
    -   A **private attribute** `__secret`
        
    -   A concrete method `walk()`
        
    -   An **abstract method** `speak()`
        

----------

#### 2. Create an Additional Class

-   Create a class `Friendly`
    
-   Include method:
    
    -   `nature()` → prints behavior of the animal
        

----------

#### 3. Create Derived Classes

**A. Class `Dog`**

-   Inherit from both `Animal` and `Friendly`
    
-   Add attribute `color`
    
-   Implement:
    
    -   Constructor using `super()` (**constructor chaining**)
        
    -   Override `speak()`
        
    -   Method `show_secret()` to access private variable
        

----------

**B. Class `Cat`**

-   Inherit from `Animal`
    
-   Override `speak()`
    

----------

### PART B: FUNCTIONAL REQUIREMENTS

Write code to demonstrate the following:

----------

#### 1. Code Reuse

-   Call `walk()` method using object of `Dog` and `Cat`
    

----------

#### 2. Method Overriding

-   Show that `Dog` and `Cat` override `speak()`
    

----------

#### 3. Polymorphism (Dynamic Binding)

-   Create a list of animals
    
-   Use a loop to call `speak()` for each object
    

----------

#### 4. Use of `super()`

-   Ensure parent constructor is called from child
    

----------

#### 5. Multiple Inheritance

-   Call `nature()` method using `Dog`
    

----------

#### 6. Encapsulation (Private Members)

-   Access private variable using method inside class
    

----------

#### 7. Type Checking

-   Use:
    
    -   `isinstance()`
        
    -   `issubclass()`
        

----------

#### 8. Method Resolution Order (MRO)

-   Print `__mro__` of class `Dog`
    

----------

### SOLUTION


**The following script implements all of above**




### PART C: ANALYSIS TABLE
















