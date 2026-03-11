

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



### Task 5: Endianness in Computer Systems
In computer architecture, endianness refers to the order in which bytes are stored in memory when representing multi-byte data such as integers. Two common conventions are: (1) Big-endian – the most significant byte (MSB) is stored first. (2) Little-endian – the least significant byte (LSB) is stored first.
Your Tasks:- (1) Study the concepts big-endian and little-endian byte ordering. (2) Explain the difference between these two formats with the help of a small example (for instance, how the number 0x12345678 would be stored in memory). (3) Use Python to determine the endianness of your computer system using the sys module. (4) Write a short Python script that: (a) Prints the system’s byte order. (b) Demonstrates how a number is stored in both little-endian and big-endian formats.
Hint: The sys module contains an attribute called byteorder.

#### Answer

The `sys` module contains an attribute called `byteorder`.

`sys.byteorder`

Possible values are:

`"little"`  
`"big"`


#### A. Conceptual Explanation

When computers store numbers larger than one byte, they must decide **which byte goes first in memory**.

Suppose we want to store the **32-bit hexadecimal number**

`0x12345678`

This number contains **4 bytes**:

12   34   56   78

#### B. Big-Endian Representation

In **big-endian systems**, the **most significant byte is stored first**.

Memory order:

`12   34   56   78`

This format is sometimes called **network byte order** and is commonly used in network protocols.

----------

#### C. Little-Endian Representation

In **little-endian systems**, the **least significant byte is stored first**.

Memory order:

`78   56   34   12`

Most modern processors such as **Intel x86 and AMD** use **little-endian format**.

----------

#### D. How to Detect Endianness in Python

Python provides the attribute:

`sys.byteorder`

This returns either:

`"little"`

or

`"big"`

depending on the architecture of the computer.

----------

#### E. Python Demonstration Script

This script demonstrates both the **system byte order** and **how integers are stored in different endian formats**.

```python

# Demonstration of Endianness in Python

import sys

print("System Byte Order:", sys.byteorder)  # Shows the byte order of the system (either 'little' or 'big')
print("-" * 40)

# Example integer (32-bit number)
number = 0x12345678

print("Original number (hex):", hex(number))

# Convert integer into bytes using big-endian format
big_endian_bytes = number.to_bytes(4, byteorder='big')  # 4 bytes for a 32-bit integer

# Convert integer into bytes using little-endian format
little_endian_bytes = number.to_bytes(4, byteorder='little')  # 4 bytes for a 32-bit integer

print("Big-endian byte order:")  # In big-endian, the most significant byte (MSB) is stored first.
print(list(big_endian_bytes))  # Output will show the byte values in big-endian order

print("Little-endian byte order:")  # In little-endian, the least significant byte (LSB) is stored first.
print(list(little_endian_bytes))  # Output will show the byte values in little-endian order

# Display hexadecimal representation
print("Big-endian (hex):", big_endian_bytes.hex())  # Hexadecimal representation of big-endian bytes
print("Little-endian (hex):", little_endian_bytes.hex())  # Hexadecimal representation of little-endian bytes


```

### 6. Research Task: Implementing a Pseudo Random Number Generator in Python

Most programming languages provide built-in functions for generating random numbers. However, these numbers are not truly random; they are generated using algorithms called **Pseudo Random Number Generators (PRNGs)**. One of the earliest and simplest PRNG algorithms is the **Linear Congruential Generator (LCG)**. The algorithm generates a sequence of integers using the recurrence relation:
$$
X_{n+1} = (a \cdot X_n + c) \pmod m
$$

**Where:**
* $X$ is the sequence of pseudorandom values.
* $a$ is the multiplier, where $0 < a < m$.
* $c$ is the increment, where $0 < c < m$.
* $X_0$ is the start value (the seed).
* $m$ is the modulus.

Typical parameter values used in many systems are: 
(1) m = 2^31 
(2) a = 1103515245 
(3) c = 12345

(This problem uses OOP concept of Class, so you may do this after studying the chapter on OOP)

**Your Tasks: 
- (1)** Study the concept of **Pseudo Random Number Generators (PRNG)**. 
- (2) Understand how the **Linear Congruential Generator (LCG)** produces a sequence of numbers. 
- (3) Write a **Python class** that: 
    - (a) Stores the seed value. 
    - (b) Generates the next pseudorandom number using the LCG formula. 
- (4) Add a method that **scales the result to a floating-point number between 0 and 1**. 
- (5) Demonstrate the generator by printing the first **few values of the sequence**.

**Questions to Think About: (1)** What happens if the **seed value changes**? (2) Why are these numbers called **pseudo-random** instead of truly random?

























