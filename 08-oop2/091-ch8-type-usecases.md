## Using metaclasses (Advance topic)


### Use Case 1: Enforce Rules on Classes












### Use Case 2: Automatic Registration

Example: The following script shows a use case where every `Pet` class must have a `speak()` method
It creates 2 classes `Dog` and `Cat`. The `Dog` class implements `speak()` so it works. But the `Cat` class does not implement `speak()` so it doesnt work and throws an error

```python

# In Python, a metaclass is a class of a class that defines how a class behaves. 
# A class is an instance of a metaclass. The most common use of metaclasses is 
# to create APIs, enforce coding standards, or implement design patterns. 
# A metaclass can be defined by inheriting from the built-in `type` class 
# and overriding its methods to customize class creation. 

# 1. Define a metaclass that checks for the presence of a specific method (e.g., speak()) in any class that uses it as a metaclass. If the method is not implemented, raise an error at the time of class creation.
class PetMeta(type):
    def __new__(mcs, name, bases, dct):
        if "speak" not in dct:
            raise TypeError(f"{name} must implement speak()")  # Check if speak() method is implemented in the class
        return super().__new__(mcs, name, bases, dct)  # Create the class using the standard type.__new__ method

# 2. Create Dog that implements speak() 
# PetMeta is a metaclass that checks if any class that uses it as a metaclass implements the speak() method.
# Since Dog implements speak(), it will be created successfully.
class Dog(metaclass=PetMeta):  # Dog class uses PetMeta as its metaclass
    def speak(self):
        print("Bark")

# 3. Create Cat that does NOT implement speak()
# Our PetMeta metaclass checks for the presence of the speak() method in any class that uses it as a metaclass.
# If a class does not implement speak(), a TypeError is raised at the time of class creation.
# Error here at class creation because Cat does not implement speak() method, 
# so we cannot create an object of Cat class.
class Cat(metaclass=PetMeta):
    pass   #  TypeError: Cat must implement speak() 







```



### Use Case 3: Automatically Add Methods/Attributes






### Use Case 4: Framework-Level Magic. Example: Django ORM












