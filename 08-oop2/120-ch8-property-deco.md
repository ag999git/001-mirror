



## PROJECT 2: Property Decorators (`@property`)



### Task

Modify a `Pet` class to implement **encapsulation using property decorators**.

----------

### Instructions

-   Use attribute:

     -  `_age`

-   Provide:
    -   Getter
    -   Setter
    -   (Optional) Deleter


#### Hints

-   Use:

    -    `@property  `
    -    `@age.setter`

-   Raise error if:

`age  <  0`

----------

#### Dos and Don’ts

-  Use `_age` internally  
-  Validate age  
-  Do not assign `self.age = value` inside setter


### Answer/ Solution

-   Property allows controlled access to attributes.
-   It replaces getter/setter methods.
-   Validation logic can be added without changing syntax.



### Table

  

| Feature | Traditional | Property |
| --- | --- | --- |
| Access | `get_age()` | `obj.age` |
| Modify | `set_age()` | `obj.age = value` |
| Validation | Manual | Built-in |















