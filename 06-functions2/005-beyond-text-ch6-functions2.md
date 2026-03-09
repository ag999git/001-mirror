

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


#### Model Answers Task 1 — Investigate a Real Python Library Function

You can access Matplotlib documentation [here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)

Function signature (simplified):

`plot(x, y, *args, **kwargs)`

#### A. Mandatory arguments of the function

The **mandatory arguments** of the function are:

-   `x` → list/array of x-coordinates
    
-   `y` → list/array of y-coordinates
    

Example:

`plt.plot(x, y)`

These specify the **data points that must be plotted**. If you dont provide the data points, then obviously, the points cannot be plotted

----------

#### B. What can be passed using `*args`

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

But providing *args is optional. If you dont provide any *args, then the library will use the default values

#### C. What can be passed using `**kwargs`

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

#### D. Why this design helps when libraries add new features

If a library developer adds a new option such as:

`alpha=0.5`

the function can still accept it through `**kwargs`.

Old code like:

`plt.plot(x,y)`

continues to work without modification.

Thus `**kwargs` allows **future extension of the library**.

----------

#### E. How this helps backward compatibility

Backward compatibility means **old programs continue to run after library updates**.

Example: Old program:

`plt.plot(x,y)`

Later library version adds new parameter:

`plt.plot(x,y,alpha=0.7)`

Old programs still work because the new parameters are **optional keyword arguments stored in `**kwargs`**.





### Task 2 — Documentation Investigation


Visit the official Matplotlib documentation for:

	`matplotlib.pyplot.plot()`	

You can access Matplotlib documentation [here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)

Find and list **five keyword arguments** that can be passed to the function.

Example format:



| Keyword Argument | Purpose |
| --- | --- |
| color | Sets line color |
| linewidth | Sets thickness |
| marker | Controls point markers |
| linestyle | Controls line style |
| label | Text for legend |

#### Model solution Task 2 — Documentation Investigation

Example keyword arguments for `matplotlib.pyplot.plot()`:


| Keyword Argument | Purpose |
| --- | --- |
| color | Sets the color of the line |
| linewidth | Controls thickness of the line |
| marker | Specifies the marker symbol |
| linestyle | Defines the pattern of the line |
| label | Provides a label used in the legend |
| alpha | Controls transparency |
| markersize | Size of markers |
| markerfacecolor | Color inside markers |

Example usage:

`plt.plot(x, y, color="red", linewidth=2, marker="o")`

----------
### Task 3 — Programming Experiment

Write a Python program that calls `plot()` in **three different ways**:

1.  Using only **mandatory arguments**
    
2.  Using **`*args` formatting string**
    
3.  Using **`**kwargs` options**
    

Example template:

```python

import  matplotlib.pyplot  as  plt  
  
x  = [1,2,3,4]  
y  = [1,4,9,16]  
  
# Case 1: Mandatory arguments only  
plt.plot(x,y)  
  
# Case 2: Using *args formatting  
plt.plot(x,y,"ro--")  
  
# Case 3: Using **kwargs  
plt.plot(x,y,color="green",linewidth=3)  
  
plt.show()
```

Explain how each version changes the appearance of the plot.
#### Model solution Task 3 — Programming Experiment

Example script:

```python

import  matplotlib.pyplot  as  plt  
  
x  = [1,2,3,4]  
y  = [1,4,9,16]  
  
# Case 1: Mandatory arguments only  
plt.plot(x, y)  
  
# Case 2: Using *args formatting string  
plt.plot(x, y, "ro--")  

# Case 3: Using **kwargs  
plt.plot(x, y, color="green", linewidth=3)  
  
plt.show()
```

##### Explanation

| Case | Code | Result |
| --- | --- | --- |
| 1 | plt.plot(x,y) | Default blue line |
| 2 | plt.plot(x,y,"ro--") | Red dashed line with circle markers |
| 3 | plt.plot(x,y,color="green",linewidth=3) | Thick green line |

Observations:

-   `*args` provides **short style formatting**
    
-   `**kwargs` provides **detailed customization**
    

----------
### Task 4 — API Design Thinking

Suppose you are designing a library function for plotting data.

You could define the function in two ways.

##### Version A (Rigid)

`def  plot(x, y, color="blue", linewidth=1, marker=None,  
  linestyle="-", label=None, grid=False):`

##### Version B (Flexible)

`def  plot(x, y, *args, **kwargs):`

##### Question

Explain why **Version B is often preferred in large libraries** ?.

Discuss the following:

-   flexibility
    
-   future extension
    
-   backward compatibility
    
-   readability of documentation




#### Model Solution Task 4 — API Design Thinking

Two possible designs:

##### Version A (Rigid)


```python

def  plot(x, y, color="blue", linewidth=1, marker=None,  
  linestyle="-", label=None, grid=False):

```

##### Version B (Flexible)

`def  plot(x, y, *args, **kwargs):`

----------

##### Why Version B is preferred in large libraries

  

  

| Feature | Version A | Version B |
| --- | --- | --- |
| Flexibility | Limited | Very high |
| Future extension | Difficult | Easy |
| Backward compatibility | Harder | Easier |
| Parameter count | Fixed | Unlimited |












