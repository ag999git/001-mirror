### Table of Contents
- [1. Python Keywords — Meaning, Code Example, Real-Life Analogy](#1-python-keywords-meaning-code-example-real-life-analogy)
- [2 Comparison between Hash and triple quotes](#2-comparison-between-hash-and-triple-quotes)
- [3. Good Rules for Writing Identifiers in Python](#3-good-rules-for-writing-identifiers-in-python)
- [4. What are PEP and PEP 8 in Python? (Simple Explanation)](#4-what-are-pep-and-pep-8-in-python-simple-explanation)
- [5. Table: Identifiers vs Variables](#5-table-identifiers-vs-variables)

### 1. Python Keywords — Meaning, Code Example, Real-Life Analogy
The following table has 4 columns. 
* The first column gives the Python keyword.
* The second column gives Meaning/ Simple explanation for that keyword.
* The third column gives an Example sentence (Code) for that keyword.
* The fourth column gives a Real-life Example/ Analogy for that keyword.


| Keyword   | Meaning / Simple Explanation | Example Sentence (Code) | Real-Life Example / Analogy |
|-----------|------------------------------|--------------------------|------------------------------|
| and       | True only if both conditions are true | if a > 0 and b > 0: print("Both positive") | Like saying: *I will go only if it’s Saturday **and** it’s not raining.* |
| as        | Give a temporary name to something | import math as m | Like calling your friend "Raj" as "RJ" for convenience. |
| assert    | Check if something is true; stop if false | assert age > 0 | Like a teacher checking “Are you sure?” before proceeding. |
| break     | Exit a loop immediately | for x in arr: break | Like stopping a game in the middle. |
| class     | Create a blueprint for objects | class Car: pass | Like a form used to create many ID cards of the same design. |
| continue  | Skip the current loop step | if x < 0: continue | Like skipping one student’s turn and moving to the next. |
| def       | Define a function | def greet(): pass | Like defining a recipe you can use anytime. |
| del       | Delete a variable or item | del x | Like throwing something away from your cupboard. |
| elif      | Extra conditions after “if” fails | if a>0:… elif a==0:… | Like: “If not bus, **else if** auto is available…” |
| else      | Runs if all conditions fail | if rain:… else:… | Like: “If none of the above works, do this.” |
| except    | Handle errors | try:… except:… | Like catching a falling glass before it breaks. |
| False     | Boolean false value | flag = False | Like a switch turned OFF. |
| finally   | Code that always runs | finally: print("Done") | Like always locking your door when leaving home. |
| for       | Loop through items | for x in nums:… | Like checking names one by one in a list. |
| from      | Import a specific part of a module | from math import pi | Like taking only one book from a library shelf. |
| global    | Declare a variable as global | global count | Like sharing one notebook across all family members. |
| if        | Used for conditions | if score>50:… | Like deciding “If it rains, take umbrella.” |
| import    | Bring in external modules | import os | Like bringing a toolbox from another room. |
| in        | Check membership | if 'a' in word:… | Like checking if your name is in a list. |
| is        | Check object identity | if a is b:… | Like checking if two cups are actually the *same* cup. |
| lambda    | Create small anonymous functions | f = lambda x: x*2 | Like writing a one-line rule on a sticky note. |
| None      | Represents “nothing" | x = None | Like an empty seat with no one sitting. |
| nonlocal  | Use a variable from outer function | nonlocal x | Like borrowing your sibling’s stationery. |
| not       | Negation; opposite value | if not ready:… | Like saying “Not hungry.” |
| or        | True if at least one condition is true | if rain or snow:… | Like “I’ll play if it’s Saturday **or** Sunday.” |
| pass      | Empty placeholder | if x>0: pass | Like noting “To be decided later.” |
| raise     | Throw an error | raise ValueError | Like raising your hand to report a problem. |
| return    | Send back a value from function | return result | Like giving back a filled form. |
| True      | Boolean true value | flag = True | Like a switch turned ON. |
| try       | Test risky code | try: open(file) | Like cautiously testing if water is hot. |
| while     | Loop until condition becomes false | while x<5:… | Like “Keep running while timer is not finished.” |
| with      | Simplify resource handling | with open(...) as f:… | Like using a rented car and returning it automatically. |
| yield     | Produce value and pause function | yield x | Like giving items from a box one at a time. |





### 2 Comparison between Hash and triple quotes
Hash (#) and triple quotes (''' or """)

[Back to Table of Contents](#table-of-contents)

**1\. Hash (#) — Single-Line Comments**

*   Starts with # and continues to the end of the line.
*   Used mainly for explaining **logic**, **steps**, or **reasoning** inside the code.
*   Helpful for programmers who want to **understand, debug, or modify** the code.
*   Typically scattered throughout functions and code blocks.
*   Can be used for multi-line comments by repeating # on each line.
*   Ignored entirely by the Python interpreter.

**2\. Triple Quotes (''' or """) — Multi-Line Strings Used as Comments**

*   Written using triple single quotes ''' or triple double quotes """.
*   Technically creates a **multi-line string**, not a true comment — but becomes a "comment" only if unused.
*   Mainly used for **docstrings**: documentation for modules, classes, and functions.
*   Appears immediately after a def or class statement.
*   Describes **usage**, **purpose**, **arguments**, and **returns** — the _user interface_.
*   Tools like Sphinx, pydoc, and IDEs can automatically extract them.
*   Can also be placed on one line as a single-line docstring.

Comparison:-

| Feature / Purpose | # Single-Line Comment | ''’ / """ Multi-Line Comment (Docstring) |
| --- | --- | --- |
| Syntax | # comment | """ comment """ or ''' comment ''' |
| Type | True comment | Multi-line string used as a comment or docstring |
| Interpreter behavior | Completely ignored | Created as a string; ignored only if not assigned or used |
| Typical use | Explain logic or code steps | Document modules, classes, and functions |
| Audience | Programmers modifying/understanding code | Users who want to know how to use the code |
| Location | Anywhere in code | Usually immediately after def, class, or module top |
| Extraction by tools | Not extracted | Automatically extracted by documentation tools |
| Best for | Inline explanations and quick notes | Official documentation of API/usage |
| Multi-line use | Yes, by repeating # on each line | Naturally supports multi-line formatting |
| Single-line use | Yes | Possible by placing opening and closing quotes on the same line |

If you as a beginner are unable to follow/ understand some of the points, don’t worry. They will become clear to you as you progress.


### 3. Good Rules for Writing Identifiers in Python
Follow the basic legal rules
[Back to Table of Contents](#table-of-contents)
    
    These rules are required by Python itself:-
    
    1.  Use letters (A–Z, a–z), digits (0–9), and underscores (_)  
        Example: total_marks, value2, Student_Name
        
    2.  Identifier cannot start with a digit  
        1value is wrong, so is 2value
        
    3.  value1 is OK
        
    4.  Keywords cannot be identifiers  
        Examples you _cannot_ use:  
        for, while, print, break, class etc.
        
    5.  No special symbols  
        Cannot use-> age@school, first-name, price$
        
    6.  Python is case-sensitive  
        student ≠ Student ≠ STUDENT



### 4. What are PEP and PEP 8 in Python? (Simple Explanation)
[Back to Table of Contents](#table-of-contents)

#### 4.1 PEP = Python Enhancement Proposal

A **PEP is a document** that explains:

*   **new features** to be added to Python
*   **how** Python should work
*   **guidelines** and **best practices** for writing Python code
*   **changes** or **improvements** to the language

**Think of PEPs like a rulebook + suggestion box**  
They help Python stay organized, consistent, and easy to develop.

**Simple example (analogy):**

Imagine a school where teachers write proposals to improve rules:

*   "Let’s add a computer lab."
*   "Let’s change the uniform color."

Python developers do the same → they write **PEPs** to propose improvements.

#### 4.2 What is PEP 8
You can check out details of PEP 8 [here](https://peps.python.org/pep-0008/)

**PEP 8 = The official Style Guide for Python code**

PEP 8 tells Python programmers:

*   how to **format** their code
*   how to **name** variables, functions, and classes
*   how many spaces to use
*   where to put blank lines
*   how to write code that is clean, readable, and consistent

**Think of PEP 8 like English grammar rules but for Python.**  
Just like grammar makes English easier to read, PEP 8 makes Python code easier for everyone to understand.

#### 4.3  PEP  8

*   | PEP 8 Topic | What It Means | PEP 8 Example (Correct) | Non-PEP 8 Example (Incorrect) |
    | --- | --- | --- | --- |
    | Indentation | Use 4 spaces per indentation level | if x > 5:    print(x) | if x > 5:print(x) (with incorrect spacing or tabs in actual code) |
    | Tabs vs Spaces | Prefer spaces over tabs | if x > 5:    print(x) | if x > 5:    print(x) (using tab character) |
    | Maximum Line Length | Keep lines under 79 characters | # Short comment line | # Very long comment line that exceeds 79 characters and is hard to read |
    | Blank Lines | Use blank lines to separate sections | Two blank lines before class or function | No blank lines between sections |
    | Imports | Keep imports at the top, one per line | import os <br> import sys | import os, sys |
    | Import Order | Standard library → Third-party → Local | import os # Standard library <br> import numpy # Third party  <br>  import mymodule # Local | Random or mixed ordering |
    | Naming Conventions | For variable use snake_case, <br> For  Class name use PascalCase, <br> For Constant use UPPER_CASE | Variable: total_amount, <br> Class: BankAccount, <br> Constant: MAX_SIZE | TotalAmount, bank_account, maxsize |
    | Whitespace Rules | Avoid unnecessary spaces | a = b + c | a=b+c or a = b + c |
    | Comments | Write clear comments | # Calculate total price | #calc price <br> or obvious comments like <br> # increment i |
    | Docstrings | Use triple quotes to document functions | """Returns sum of two numbers.""" | Using # comments instead of docstrings |
    | Code Layout | Keep code clean and structured | Organised, readable code | Messy, inconsistent layout |
    | Boolean Comparisons | Use direct checks | if is_ready: | if is_ready == True: |
    | Compare with None using is/is not | Follow Pythonic way | if x is None: | if x == None: |
    | Function & Variable Names | Use lowercase_with_underscores | get_value(), student_age | GetValue(), StudentAge, studentAge |
    | Class Names | Use PascalCase | CarModel | carmodel, car_model, carModel |
    | Constant Names | Use UPPER_CASE | MAX_SPEED = 120 | maxspeed = 120 |
    | Spacing After Commas | Put a space after commas | sum(1, 2, 3) | sum(1,2,3) |
    | Single Statement per Line | Use one statement per line | x = 1; <br> y = 2 (preferred to split in two lines) | x = 1; y = 2 (not recommended in practice) |

#### 4.4 Pep 8 Vs Non-pep 8 Examples
[Back to Table of Contents](#table-of-contents)
##### The following code in Python gives example of use of PEP 8 versus non-PEP 8 for:-
*   Variables
  
*   Functions
    
*   Loops
    
*   Conditionals
    
*   Comments

```python

# PEP 8 vs Non-PEP 8 Python Code Examples

# -------------------------------
# Variables:- Use snake_case (lowercase_with_underscores)
# -------------------------------

# PEP 8 style
student_age = 20
total_score = 95
MAX_LIMIT = 100

# Non-PEP 8 style
StudentAge=20  # Avoid capital letters in variable names
totalScore=95  #Not following convention. Use underscores (_) instead
maxlimit=100  # variable names not following conventions


# -------------------------------
# Functions:- Also use snake_case
# -------------------------------

# PEP 8 style
def calculate_average(score1, score2, score3):
    total = score1 + score2 + score3
    return total / 3

# Non-PEP 8 style
def CalculateAverage(score1,score2,score3): total=score1+score2+score3;return total/3

# -------------------------------
# Class Names:- use PascalCase
# -------------------------------
# PEP 8 style
StudentRecord
AttendenceManager

# Non-PEP 8 style
studentRecord  # Class name should start with capital letter by convention
Attendence_Manager  # Avoid underscores in class names if possible

# -------------------------------
# Constants:- Use all UPPERCASE. Use Underscores (_) to seperate words
# -------------------------------
# PEP 8 style
MAX_MARKS = 100

# Non-PEP 8 style
max_marks = 100  # Avoid




# -------------------------------
# Loops
# -------------------------------

# PEP 8 style
for i in range(5):
    print(i)

# Non-PEP 8 style
for i in range(5): print(i)  # multiple statements in single line


# -------------------------------
# Conditionals
# -------------------------------

# PEP 8 style
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Non-PEP 8 style
x=10
if x>5: print("x>5")
elif x==5: print("x==5")
else: print("x<5")


# -------------------------------
# Comments
# -------------------------------

# PEP 8 style
# This function calculates the square of a number
def square(n):
    return n * n

# Non-PEP 8 style
def square(n): return n*n #function to calc square


# -------------------------------
# Private / Internal Names — begin with underscore (Not enforced by Python, but recommended.)
# -------------------------------

# PEP 8 style
_calculate_internal_grades()  # This function is to be used internally

# Non-PEP 8 style
calculate_internal_grades()  # This is an internal function/ private to the script. Should start with underscore


```


### 5. Table: Identifiers vs Variables
[Back to Table of Contents](#table-of-contents)

    
| Feature | Identifier | Variable |
| --- | --- | --- |
| **Definition** | A name used to identify something in Python | A memory location that stores a value |
| **What it represents** | Can represent variables, functions, classes, modules, etc. | Only represents data stored in memory |
| **Creation **| Created when you write a name (e.g., myFunc) | Created only after assignment (e.g., x = 10) |
| **Has value?** | No | Yes |
| **Has type?** | No | Yes (type of stored value) |
| **Has scope?** | Depends on what it names | Yes — local, global, class-level |
| **Example** | sum, my_list, print, Car | x = 5, name = "Anurag" |
| **Error if missing?** | Undefined identifier → NameError | Same, because variable name is an identifier |
| **Used for** | Naming program components | Storing and manipulating data |
    






### 6. 


### New addition below this
[Back toTable of Contents](#table-of-contents)
