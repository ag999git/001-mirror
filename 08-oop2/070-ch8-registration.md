





## RESEARCH / PROJECT QUESTION:- Design a Pet Registration System Using 3 Approaches

You are required to design a **Pet Management System** that demonstrates three different ways of registering classes in Python.

----------

### Requirements

#### Part A: Manual Registration

1.  Create a class `PetRegistryManual`
    
2.  Maintain a dictionary `registry`
    
3.  Provide a method `register(name, cls)`
    
4.  Create classes:
    
    -   `Dog`
        
    -   `Cat`
        
5.  Manually register them
    
6.  Dynamically create objects and call `speak()`
    

----------

#### Part B: Decorator-Based Registration

1.  Create a class `PetRegistryDecorator`
    
2.  Implement a decorator method `register(name)`
    
3.  Register classes using `@decorator`
    
4.  Create:
    
    -   `Bird`
        
    -   `Fish`
        
5.  Dynamically call their methods
    

----------

#### Part C: Automatic Registration (`__init_subclass__`)

1.  Create base class `Pet`
    
2.  Automatically register subclasses using:
    
    `__init_subclass__()`
    
3.  Create:
    
    -   `Horse`
        
    -   `Cow`
        
4.  Print all registered subclasses
    
5.  Dynamically create objects
    

----------

#### Final Task

-   Compare all 3 approaches
    
-   State advantages and disadvantages
    

----------

## PART 2: SOLUTION/ EXPLANATION


### Core Idea

All three approaches aim to:

> Store class references so they can be used dynamically

----------

### Approach 1: Manual Registration

#### Idea

-   Programmer explicitly registers classes
    

#### Why used?

-   Simple and easy for beginners
    

----------

### Approach 2: Decorator Registration

#### Idea

-   Registration happens automatically at class definition
    

#### Why used?

-   Cleaner and safer
    

----------

### Approach 3: Automatic Registration

#### Idea

-   Base class tracks all subclasses automatically
    

#### Why used?

-   Best for large systems and frameworks
    

----------

## PART 3: SCRIPTS



### 1. Manual Registration
















