





## `super()` in Multiple Inheritance (Advanced Notes)

----------

### Core Idea

In single inheritance:

> `super()` → calls the immediate parent

In multiple inheritance:

> `super()` → calls the **next class in MRO**

----------

### Why This Matters

-   Ensures **each class runs exactly once**
    
-   Avoids duplicate calls (especially in diamond structure)
    
-   Enables **cooperative inheritance**
    

----------

### Diamond Structure
```python

       Pet  
     /     \  
 Walker  Swimmer  
     \     /  
      Dog
```

Both `Walker` and `Swimmer` inherit from `Pet`  
`Dog` inherits from both

----------

### Correct Way Using `super()` (Cooperative Design)

----------

#### Script (Highly Important)

























