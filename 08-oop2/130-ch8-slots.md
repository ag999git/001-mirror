


# PROJECT TASK — `__slots__` (Memory Optimization)



## “Optimizing Pet Objects Using `__slots__` in Python”

----------

## OBJECTIVE 

By completing this you will:

-   Understand **why `__dict__` consumes memory**
-   Learn how `__slots__` **removes `__dict__`**
-   Compare behavior of:
    -   Normal class
    -   Class with `__slots__`
-   Understand **limitations and trade-offs**

----------

## TASK DESCRIPTION. You are required to:

### STEP 1: Create a normal class

-   Create class `PetNormal`
-   Add:
    -   `name`
    -   `age`
-   Store them using `self.name`, `self.age`

----------

### STEP 2: Create a class using `__slots__`

-   Create class `PetSlots`
-   Define:

`__slots__  = ['name', 'age']`

-   Use same attributes as above

----------

### STEP 3: Create objects

-   Create:
    -   `p1 = PetNormal("Tommy", 5)`
    -   `p2 = PetSlots("Bruno", 3)`

----------

### STEP 4: Compare namespaces

-   Print: `print(p1.__dict__)`

-   Try: `print(p2.__dict__)`

Observe and explain difference

----------

### STEP 5: Add new attribute dynamically

-   Try:

`p1.color =  "Brown"  `
`p2.color =  "Black"`

Observe:

-   Which works?
-   Which fails?

----------

### STEP 6: Memory comparison (conceptual)

-   Use:


```python
import  sys  
print(sys.getsizeof(p1))  
print(sys.getsizeof(p2))
```
Compare sizes (even if small difference)



### STEP 7: Write explanation

Student must explain:

-   What is `__dict__`
-   What `__slots__` does
-   Why dynamic attributes fail
-   When to use `__slots__`

----------

### 8. DOs and DON’Ts

#### DO:

-   Use same attributes in both classes
-   Print outputs clearly
-   Add comments explaining behavior

#### DON’T:

-   Don’t use different attribute names
-   Don’t skip error handling
-   Don’t assume `__slots__` improves speed (focus on memory)

----------

### 9. HINTS (Very Important)

-   `__slots__` → **removes instance `__dict__`**
-   Without `__dict__` → no dynamic attributes
-   Think:  Fixed structure vs flexible structure”

----------

### Expected Observations

  

| Feature | `PetNormal` | `PetSlots` |
| --- | --- | --- |
| Has `__dict__` | Yes | No |
| Dynamic attributes | Allowed | Not allowed |
| Memory usage | Higher | Lower |
| Flexibility | High | Low |














