




### **What is `__dict__`?**

-   In Python, most objects store their attributes in a special attribute called:

`__dict__`

-   It is a **dictionary** that contains:
    -   Attribute names → keys
    -   Attribute values → values

In simple words:

> `__dict__` is the **actual namespace dictionary of an object**

----------

### Key Idea

`object.attribute  ⇔  object.__dict__['attribute']`

Both refer to the same data.

----------

### Example 1: Instance Namespace

```python

# __dict__ Demonstration
# Every object in Python has a __dict__ attribute that stores its attributes and their values in a 
# dictionary format. This allows us to see the internal state of an object and how its attributes 
# are organized.    # In this example, we define a class called Pet with an __init__ method that 
# initializes the name and type attributes. When we create an instance of the Pet class and 
# print its __dict__, we can see the attributes and their corresponding values stored in a dictionary format.  
#
class Pet:
    def __init__(self, name):
        self.name = name
        self.type = "Animal"

p = Pet("Dog")

print(p.__dict__)
# Output: {'name': 'Dog', 'type': 'Animal'}


```


#### Example 2 script


```python

# A. CLASS DEFINITION
class Dog:
    species = "Pet"  # Class attribute 

    def __init__(self, name):
        self.name = name  # Instance attribute

# B. OBJECT CREATION
d = Dog("Tommy")  

# C. NAMESPACE DISPLAY
print("Class Namespace:->", Dog.__dict__)
# Output: Class Namespace:-> {'__module__': '__main__', 'species': 'Pet',....}
print("Instance Namespace:->", d.__dict__)
# Output: Instance Namespace:-> {'name': 'Tommy'}

# D. ADD NEW ATTRIBUTE by directly modifying the instance's __dict__
d.__dict__["color"] = "Brown"
print("Added attribute 'color':->", d.color)  # Added attribute 'color':-> Brown

# E. MODIFY ATTRIBUTE by directly modifying the instance's __dict__
d.__dict__["name"] = "Bruno"  # Modifying the 'name' attribute using __dict__
print("Modified name:->", d.name)  # Modified name:-> Bruno



```



### Explanatory Note: Understanding `__dict__` using Class and Object

-   This script demonstrates how Python internally stores attributes of a **class** and its **objects (instances)** using the special attribute `__dict__`.

#### 1. Class Definition

-   The class `Dog` contains:
    -   A **class attribute** → `species = "Pet"`
    -   An **instance attribute** → `name` (created inside `__init__()`)

**Important idea:**

-   Class attributes belong to the **class namespace**
-   Instance attributes belong to the **object (instance) namespace**


#### 2. Object Creation

`d  =  Dog("Tommy")`

-   When the object `d` is created:
    -   Python first creates the object
    -   Then calls `__init__()`
    -   The attribute `name = "Tommy"` is stored in the **instance namespace**

#### 3. Viewing Namespaces using `__dict__`

`Dog.__dict__`

-   Shows the **class namespace**
-   Contains:
    -   Class variables (`species`)
    -   Methods (`__init__`)
    -   Other built-in attributes

`d.__dict__`

-   Shows the **instance namespace**
-   Contains only:
    -   `{'name': 'Tommy'}`

**Point to be noted:**

> Class and instance maintain **separate namespaces**


#### 4. Adding Attribute using `__dict__`

`d.__dict__["color"] =  "Brown"`

-   Adds a new attribute `color` to the object `d`
-   This attribute is stored in the **instance namespace**

**The above statement is equivalent to:**

`d.color =  "Brown"`

#### 5. Modifying Attribute using `__dict__`

`d.__dict__["name"] =  "Bruno"`

-   Updates the existing attribute `name`
-   Since `name` is in the instance namespace, it gets modified there

**The Output confirms:**

`Bruno`



#### 6. Key Concepts Demonstrated by the script

-   `__dict__` is a **dictionary representing namespace**
-   Class and instance have **different `__dict__`**
-   Attributes can be:
    -   **Added dynamically**
    -   **Modified dynamically**
-   Attribute access:
    
   ` d.name ⇔  d.__dict__['name']`
    

----------

#### Conclusion

> The `__dict__` attribute is the internal storage mechanism that Python uses to manage attributes of classes and objects. By accessing it directly, we can see and even manipulate how Python stores data inside objects.








### LEGB

 - While the idea of a namespace as a dictionary is very useful for
   understanding, it is important to note that Python does not simply
   store values — it stores **references to objects**. 
   
 - This means that when we write a statement like `x = 10`, the name `x` does not    “contain” the value 10; instead, it **refers to an object** (with its    own unique `id`) that represents the integer 10. 
 - This explains many    important Python behaviors such as multiple variables referring to    the same object, object mutability, and memory efficiency.
 - Further, namespaces are **dynamic** in nature — entries can be added,    modified, or removed during program execution. This is why Python    provides functions like `locals()` and `globals()` to inspect these    mappings at runtime.
 - While a namespace can be understood as a simple dictionary mapping names to objects, it is important to realise that **Python does not search all namespaces at once**. 
 - Instead, it follows a **specific resolution order called the LEGB rule (Local → Enclosing → Global → Built-in)**. 
 - Whenever a variable is used, Python looks for its name step-by-step through these nested namespaces until it finds a match. This process is called **name resolution**. 
 - If the same variable name exists in multiple namespaces, the one found first in this order is used, leading to the concept of **shadowing**, where an inner variable hides an outer one. 
 - Also, assignment behaves differently from access—when you assign a value to a variable inside a function, Python by default creates a **new local variable**, unless explicitly instructed using keywords like `global` or `nonlocal`. 
 - Understanding this dynamic lookup and binding mechanism is crucial, because it explains many subtle behaviors in Python such as variable scope errors, closures, and function behavior.







