





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

```python

# A. Manual registration of pet classes in a registry
class PetRegistryManual:  # Manual registration of pet classes
    registry = {}  # This is a class attribute that will hold the mapping of pet names to their corresponding classes. It is shared across all instances of the PetRegistryManual class.

    @classmethod
    def register(cls, name, pet_class):  # (class method) This is a class method that allows us to register a pet class with a specific name. The cls parameter refers to the class itself (PetRegistryManual), and it is used to access the class attribute registry.
        cls.registry[name] = pet_class

# B. Define pet classes to be registered
class Dog:
    def speak(self):  # This is an instance method that defines the behavior of the Dog class when the speak() method is called. It will print "Dog barks" to indicate that the dog is barking.
        print("Dog barks")

# C. Define another pet class
class Cat:
    def speak(self):  # This is an instance method that defines the behavior of the Cat class when the speak() method is called. It will print "Cat meows" to indicate that the cat is meowing.
        print("Cat meows")


# D. Manual registration of pet classes in the registry
PetRegistryManual.register("dog", Dog)  # This line registers the Dog class with the name "dog" in the PetRegistryManual registry. It allows us to later retrieve the Dog class using the name "dog" from the registry.
PetRegistryManual.register("cat", Cat)  # This line registers the Cat class with the name "cat" in the PetRegistryManual registry. It allows us to later retrieve the Cat class using the name "cat" from the registry.

# E. Dynamic usage of the registry to create pet objects and call their speak() method
# E1. Create Dog object using registry
PetClass = PetRegistryManual.registry["dog"]  # This line retrieves the Dog class from the PetRegistryManual registry using the name "dog" and assigns it to the variable PetClass. Now, PetClass holds a reference to the Dog class, and we can use it to create an instance of the Dog class.
pet = PetClass() # This line creates an instance of the Dog class by calling the constructor of the Dog class (which is now referenced by PetClass). The parentheses () indicate that we are calling the constructor to create an object of the Dog class, and the resulting object is assigned to the variable pet.    
pet.speak()  # This line calls the speak() method on the pet object, which is an instance of the Dog class. It will print "Dog barks" to indicate that the dog is barking.

# E2. Create Cat object using registry
PetClass = PetRegistryManual.registry["cat"]  # This line retrieves the Cat class from the PetRegistryManual registry using the name "cat" and assigns it to the variable PetClass. Now, PetClass holds a reference to the Cat class, and we can use it to create an instance of the Cat class.
pet = PetClass() # This line creates an instance of the Cat class by calling the constructor of the Cat class (which is now referenced by PetClass). The parentheses () indicate that we are calling the constructor to create an object of the Cat class, and the resulting object is assigned to the variable pet.
pet.speak()  # This line calls the speak() method on the pet object, which is an instance of the Cat class. It will print "Cat meows" to indicate that the cat is meowing.





```














