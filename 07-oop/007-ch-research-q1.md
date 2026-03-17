


#### Research Question 1: What is a Circular Reference in Python?

Explain why it poses a challenge to the standard Reference Counting mechanism and how Python’s Garbage Collector handles it.

**Answer:**

A **Circular Reference** occurs when two (or more) objects hold references to each other.

-   **The Problem:** If Object A points to Object B, and Object B points to Object A, their reference counts will never drop to zero, even if you delete the external labels (del p1, del p2).
-   **The Result:** They become "Islands of Isolation." They are unreachable by your code, but because they are "holding onto each other," the standard reference counter thinks they are still in use.
-   **The Solution:** Python has a secondary **Generational Garbage Collector**. It periodically searches for these "islands" and breaks the circular links manually to free the memory.

The following script shows the creation of circular reference and how to break it:-





