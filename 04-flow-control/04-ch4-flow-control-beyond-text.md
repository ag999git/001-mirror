


### This is the solution to the Beyond Text problem given In Chapter 4 Flow Control

In Python, we often use for loops to go through lists or strings. But have you ever wondered how the for loop actually "talks" to the list? It uses the **Iterator Protocol**.

The task is to study (1) Iterable (2) Iterators (3) Using the iter() function to create an iterator. (4) Understand how to use the next() function to grab the next item.

**Assignment: The "No-For-Loop" Challenge**

**Objective**

Your goal is to simulate how Python's for loop works "under the hood." You will process a collection of items manually by managing the data pointer yourself.

**The Task**

Write a Python script that iterates through a list of three colors: **"Red"**, **"Green"**, and **"Blue"**. You must print each color individually, but there is a catch: **You are not to use the `for` keyword.**

**Constraints & Rules**

*   **No `for` loops:** You must use a while True: loop to handle the repetition.
*   **Manual Tracking:** Use the `iter()` function to initialize an iterator object from your list.
*   **Manual Retrieval:** Use the `next()` function to retrieve each item from the iterator.
*   **Error Handling:** You must use a `try...except` block to catch the specific exception that Python raises when it runs out of items.
*   **Clean Exit:** When the end of the list is reached, print a "Loop Finished" message and use break to exit the loop gracefully.

**Implementation Hints**

1.  **The Iterator:** Think of the list as a book and the result of iter() as a bookmark that remembers the current page.
2.  **The Trigger:** When `next()` is called on an empty iterator, it doesn't return None; it gives an error called `StopIteration`.
3.  **The Safety Net:** Your except block should specifically look for `StopIteration` to know exactly when to stop the while loop.

The expected **identical logic** to be used is:

1.  **Initialize** the pointer (iter).
2.  **Attempt** the action (try + next).
3.  **Handle** the boundary condition (except StopIteration).
4.  **Terminate** the process (break).

```python

# --- BEYOND TEXT: MANUAL ITERATION ---

# 1. The Iterable (The Data)
colors = ["Red", "Green", "Blue"]  # A list of colors

# 2. Creating the Iterator (The Pointer/Bookmark)
# This creates a 'list_iterator' object that remembers its position.
color_cursor = iter(colors)  # This is like a bookmark that starts at the beginning of the list.

print("Starting Manual Loop...")
print("-" * 20)

# 3. Simulating the 'for' loop logic
while True:
    try:
        # Attempt to get the next item from the bookmark
        current_color = next(color_cursor)  # This moves the bookmark forward and returns the current item. 
        print(f"Processing color: {current_color}")
        
    except StopIteration:  # This exception is raised when there are no more items to iterate over.
        # This exception is raised automatically when next() 
        # is called but there are no items left.
        print("-" * 20)
        print("End of list reached! Stopping loop.")
        break

print("Program continues normally...")


```




