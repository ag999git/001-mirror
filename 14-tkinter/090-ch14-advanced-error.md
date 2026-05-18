

Welcome file
Welcome file

# Research / Project Question

## Professional Error Handling in Tkinter

Modern GUI applications should be able to:

-   validate user input automatically,
-   record errors for debugging,
-   safely handle unexpected failures.

Tkinter supports these features using: `loggingsys.excepthooktrace_add()`


## Part A — Theory

Research and explain the following:

### 1. What is: `logging` and why is it used instead of: `print()`?

### 2. What is: `sys.excepthook` and what is its purpose?

### 3. What is: `trace_add()` and why is it useful with: `StringVar()`?

### 4. Explain: `live validation` with one example.

### 5. Why do professional applications log errors instead of only displaying them?


## Part B — Script Writing

Write a Tkinter program that:

1.  Creates an Entry widget for numeric input.
2.  Validates input while typing using: `trace_add()`
3.  Shows: `Valid input` or `Numbers only` in real time.

4.  Logs activity into: `app_log.txt` 

5.  Uses: `sys.excepthook` for global exception handling.

6.  Adds a button: `Trigger Error` to deliberately create an uncaught error.

7.  Shows a friendly popup instead of crashing.

----------

# Theory Solution

## 1. What is `logging`?

Logging means:

> recording program activity and errors in a file.

Example:

```python
logging.info("User clicked")
```

Unlike:

```python
print()
```

logs remain saved after the program closes.

### Why not `print()`?
| print() | logging |
| --- | --- |
| Temporary | Permanent |
| Screen only | Saved to file |
| Hard to debug later | Useful for debugging |

## 2. What is `sys.excepthook`?

`sys.excepthook` is Python’s:

> global exception handler

It controls what Python does when: `uncaught exception` happens.

Normally the sequence of execution is as follows:

```python
Error
↓
Traceback shown
↓
Program crashes
```

But: `sys.excepthook =handle_error` changes the route.

Now the sequence is as follows:

```python
Error
↓
Custom function runs
↓
Popup + log
```

This improves application safety.

----------

## 3. What is `trace_add()`?

`trace_add()` monitors a Tkinter variable.

Example:

```python
name_var.trace_add("write", validate)
# Meaning: Whenever variable changes,run validate()
```

It is commonly used with: `StringVar()` because Entry widgets use variables.

----------

## 4. What is Live Validation?

Live validation means:

> checking input while the user is typing.

Example:

Instead of waiting for: `Submit button` program checks immediately.

  -  Suppose we have incorrect Input: `abc`, we immediately get an Output: `Numbers only` 

  -  Suppose we have correct Input: `25` we get Output: `Valid input` 

This improves user experience.


## 5. Why Do Professional Apps Log Errors?

Errors may happen unexpectedly.
Examples of unexpected errors are:
```python
user enters bad data
network fails
program bug appears
```
A popup helps the user. But developers also need technical details.

Logs help programmers:

-   debug problems,
-   understand failures,
-   improve software.

----------

## Script 3 — Advanced Tkinter Safety

Research / Project Question
Professional Error Handling in Tkinter
Modern GUI applications should be able to:
  -  validate user input automatically,
  -  record errors for debugging,
  -  safely handle unexpected failures.
  -  Tkinter supports these features using: loggingsys.excepthooktrace_add()

## Part A — Theory
### Research and explain the following:

1. What is: logging and why is it used instead of: print()?
2. What is: sys.excepthook and what is its purpose?
3. What is: trace_add() and why is it useful with: StringVar()?
4. Explain: live validation with one example.
5. Why do professional applications log errors instead of only displaying them?

### Part B — Script Writing
Write a Tkinter program that:
  -  Creates an Entry widget for numeric input.
  -  Validates input while typing using: trace_add()
  -  Shows: Valid input or Numbers only in real time.
  -  Logs activity into: app_log.txt
  -  Uses: sys.excepthook for global exception handling.
  -  Adds a button: Trigger Error to deliberately create an uncaught error.
  -  Shows a friendly popup instead of crashing.

## Theory Solution
### 1. What is logging?
Logging means:
>recording program activity and errors in a file.

```python
# Example:
logging.info("User clicked") # logs remain saved after the program closes.
# However 
print() # logs not saved
```


Why not print()?
print()	logging

| print() | logging |
| --- | --- |
| Temporary | Permanent |
| Screen only | Saved to file |
| Hard to debug later | Useful for debugging |

### 2. What is sys.excepthook?
sys.excepthook is Python’s:

global exception handler

It controls what Python does when: uncaught exception happens.

Normally the sequence of execution is as follows:

```python
Error
↓
Traceback shown
↓
Program crashes
```
But: sys.excepthook =handle_error changes the route.

Now the sequence is as follows:

```python
Error
↓
Custom function runs
↓
Popup + log
```
This improves application safety.

### 3. What is trace_add()?
trace_add() monitors a Tkinter variable.

Example:

`name_var.trace_add("write", validate)`
Meaning: Whenever variable changes,run validate()
It is commonly used with: StringVar() because Entry widgets use variables.

### 4. What is Live Validation?
Live validation means:

checking input while the user is typing.

Example:

Instead of waiting for: Submit button program checks immediately.

Suppose we have incorrect Input: abc, we immediately get an Output: Numbers only

Suppose we have correct Input: 25 we get Output: Valid input

This improves user experience.

### 5. Why Do Professional Apps Log Errors?
Errors may happen unexpectedly.
Examples of unexpected errors are:

user enters bad data
network fails
program bug appears
A popup helps the user. But developers also need technical details.

Logs help programmers:

debug problems,
understand failures,
improve software.
Script 3 — Advanced Tkinter Safety
Markdown 3076 bytes 461 words 163 lines Ln 157, Col 24HTML 2272 characters 393 words 85 paragraphs



