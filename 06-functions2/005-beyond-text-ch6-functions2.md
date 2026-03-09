

### Task 1 — Investigate a Real Python Library Function

The plotting function in **Matplotlib** has the following simplified form:

`plot(x, y, *args, **kwargs)`

#### Research Question

Explain why the designers of Matplotlib chose to use `*args` and `**kwargs` in this function instead of defining a very long list of parameters.

Your explanation should address the following points:

1.  What are the **mandatory arguments** in `plot()`?
2.  What types of values can be passed using **`*args`**?
3.  What types of options are typically passed using **`**kwargs`**?
4.  Why is this design useful when a library **adds new features in later versions**?
5.  How does this design help **old programs continue to run without modification**?


### Model Answers Task 1 — Investigate a Real Python Library Function

Function signature (simplified):

`plot(x, y, *args, **kwargs)`

#### 1. Mandatory arguments

The **mandatory arguments** are:

-   `x` → list/array of x-coordinates
    
-   `y` → list/array of y-coordinates
    

Example:

`plt.plot(x, y)`

These specify the **data points that must be plotted**.

----------

#### 2. What can be passed using `*args`

`*args` allows additional **positional arguments**.

In Matplotlib, these are usually **formatting strings** that control:

-   color
    
-   marker style
    
-   line style
    

Example:

`plt.plot(x, y, "ro--")`


  
Meaning: 

| Symbol | Meaning |
| --- | --- |
| r | red color |
| o | circle marker |
| -- | dashed line |

So `*args` allows **compact style specifications**.

#### 3. What can be passed using `**kwargs`

`**kwargs` allows **keyword arguments** for many optional settings.

Examples:

`plt.plot(x, y, color="green", linewidth=3, marker="o")`

Common keyword parameters include:

  

| Parameter | Purpose |
| --- | --- |
| color | Line color |
| linewidth | Line thickness |
| marker | Marker shape |
| linestyle | Line pattern |
| label | Legend label |

These options make the plot **highly customizable**.

----------

#### 4. Why this design helps when libraries add new features

If a library developer adds a new option such as:

`alpha=0.5`

the function can still accept it through `**kwargs`.

Old code like:

`plt.plot(x,y)`

continues to work without modification.

Thus `**kwargs` allows **future extension of the library**.

----------

#### 5. How this helps backward compatibility

Backward compatibility means **old programs continue to run after library updates**.

Example: Old program:

`plt.plot(x,y)`

Later library version adds new parameter:

`plt.plot(x,y,alpha=0.7)`

Old programs still work because the new parameters are **optional keyword arguments stored in `**kwargs`**.
