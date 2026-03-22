




## `__new__()` versus `__init__()`



-   Object creation in Python happens in **two steps**:
- Step 1: `__new__()` → creates the object.
- Step 2: `__init__()` → initializes the object

----------

### Simple Definition

-   `__new__()`:
    
    > Creates and returns a **new object (instance)**
    
-   `__init__()`:
    
    > Initializes the **attributes of the object**


### Comparative table

  

| Feature | __new__() | __init__() |
| --- | --- | --- |
| Purpose | Creates object | Initializes object |
| Type | Static-like method | Instance method |
| First parameter | cls (class) | self (object) |
| Called when | Before object exists | After object exists |
| Return value | Must return object | Must return None |
| Controls | Object creation | Object customization |
| Called first? | Yes | No |
| Can skip next step? | Yes | No |








