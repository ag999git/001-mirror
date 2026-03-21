







## PROJECT: Designing a Robust Pet System Using Abstract Classes

----------

### Problem Statement

Design a system where:

-   All pets must implement:
    
    -   `speak()`
        
    -   `move()`
        
-   Some pets:
    
    -   Walk
        
    -   Swim
        
    -   Do both (multiple inheritance)
        

----------

### Requirements

#### 1. Create Abstract Base Class `Pet`

-   Methods:
    
    -   `speak()` → abstract
        
    -   `move()` → abstract
        

----------

#### 2. Create Classes

##### Dog

-   speak → Bark
    
-   move → Walk
    

##### Fish

-   speak → (silent or "blub")
    
-   move → Swim
    

----------

#### 3. Multiple Inheritance

Create:

`class  Amphibian(Walker, Swimmer)`

-   Should:
    
    -   Walk AND Swim
        
    -   Use `super()` properly
        

----------

#### 4. Enforce Rules

-   Use `ABC` and `@abstractmethod`
    
-   Ensure:
    
    -   Cannot create incomplete classes
        

----------

#### 5. Show Output

-   Create objects
    
-   Call methods
    
-   Print MRO
    

----------

### ANSWER



#### Comparison of Basic Abstract (Usong NotImplementedError) to ABC Module
  

| Feature | Basic Abstract | ABC Module |
| --- | --- | --- |
| Enforcement | Weak | Strong |
| Error Time | Runtime | Instantiation |
| Standard Practice | No | Yes |
| Used in Industry | Rare | Very Common |




  

  #### Role of various components

| Concept | Role |
| --- | --- |
| Abstract Class | Defines rules |
| Child Class | Implements behavior |
| super() | Chains execution |
| MRO | Controls order |






