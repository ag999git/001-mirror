


### Research Question 1: What is a Circular Reference in Python?

Explain why it poses a challenge to the standard Reference Counting mechanism and how Python’s Garbage Collector handles it.

**Answer:**

A **Circular Reference** occurs when two (or more) objects hold references to each other.

-   **The Problem:** If Object A points to Object B, and Object B points to Object A, their reference counts will never drop to zero, even if you delete the external labels (del p1, del p2).
-   **The Result:** They become "Islands of Isolation." They are unreachable by your code, but because they are "holding onto each other," the standard reference counter thinks they are still in use.
-   **The Solution:** Python has a secondary **Generational Garbage Collector**. It periodically searches for these "islands" and breaks the circular links manually to free the memory.

The following script shows the creation of circular reference and how to break it:-

```python

import gc
import sys

class Pet:
    def __init__(self, name):
        self.name = name
        self.friend = None
        print(f"--- Pet object-> {self.name} is created.")

    def __del__(self):
        # This will only print if the Garbage Collector breaks the circle!
        print(f"--- [CLEANUP] Memory for {self.name} finally cleared.")

# 1. Setup the circle
dog = Pet("Tiger")
cat = Pet("Kitty")

# Creating the 'Mutual Life Support' link
dog.friend = cat
cat.friend = dog

print(f"Tiger's Ref Count: {sys.getrefcount(dog) - 1}") # Expect 2 (dog label + Kitty's friend link)

# 2. Break the external links
print("ACTION: Deleting external labels 'dog' and 'cat'...")
del dog
del cat

# IMPORTANT: At this point, Tiger and Kitty still exist in memory! 
# They are holding each other's reference counts at 1.
print("Labels are gone, but __del__ was not called yet (Deadlock).")

# 3. Force the Garbage Collector to find the 'Island'
print("ACTION: Forcing Garbage Collection...")
gc.collect() 
print("End of Script.")



```



