





## **Problem Statement**

### Design a Python program that demonstrates all major properties of inheritance, including: (1) Is-A relationship. (2) Code reuse. (3) Method Resolution Order (MRO). (4) Overriding. (5) Polymorphism. (6) super(). (7) Constructor behavior. (8) Dynamic binding. (9) Encapsulation. (10) Extensibility. (11) Maintainability.

### The given script does the following
### 1. Creates Base Class: `Pet`

This class includes:

-   Attribute: `name`
    
-   Private attribute: `__secret`
    
-   Methods:
    
    -   `walk()` → prints a message
        
    -   `speak()` → generic message
        
    -   Constructor `__init__()`
        

----------

### 2. Creates derived Class: `Dog`
This class does the following
-   Inherits from `Pet`
    
-   Adds attribute: `color`
    
-   Overrides:
    
    -   `speak()`
        
    -   `walk()`
        
-   Uses `super()` in constructor and methods
    

----------

### 3. Creates derived Class: `Cat`
This does the following
-   Inherits from `Pet`
    
-   Overrides `speak()`
    

----------



### The script also demonstrates:

----------

#### 1. Is-A Relationship

-   Shows that `Dog` and `Cat` are types of `Pet`
    

----------

#### 2. Does code reuse

-   Uses inherited `walk()` where applicable
    

----------

#### 3. Overrides 

-   Shows different `speak()` implementations
    

----------

### 4. Implements polymorphism

-   Creates a list of pets and call `speak()` using a loop
    

----------

### 5. Shows usage of `super()`

-   Calls parent constructor and methods
    

----------

### 6. Shows constructor Behavior

-   Shows how constructors behave in parent and child
    

----------

### 7. Uses MRO

-   Prints method resolution order
    

----------

### 8. Shows encapsulation

-   Accesses private variable using a method
    

----------

### 9. Shows dynamic binding

-   Demonstrates runtime method selection
    

----------

### 10. Shows extensibility

-   Adds a new attribute in child class
    

----------

### 11. Shows maintainability

-   Shows how modifying parent affects child









