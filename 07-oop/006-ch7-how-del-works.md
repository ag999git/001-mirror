

### How `del` command and **`__del__()`** work

To understand how `del` command and **`__del__()`** work, one needs to understand how objects are stored in Python.

·       In Python there are the objects that live in a specific location in memory (the "Heap").

·       **The Heap:** This is a large area of memory where the actual objects live. This is where the "Pet" data (name, breed, etc.) is stored.

·       **The Reference:** Is just a pointer (a label) stored in the "Stack" that tells Python where the object is.

·       **The Stack:** This is a small, fast area of memory. It stores the names of your variables (like p1 and p2). Think of it as a **list of pointers**.

·       **The "Link":** In Python, a variable in the Stack simply holds the memory address of the object in the Heap.

·       **The del Action**: When you call del p1, Python removes the entry from the Stack. The object in the Heap remains untouched until the very last link is snapped.

·       **Manual Deletion:** Suppose you have an object of **Pet** class named **p1** and an alias to **p1** named **p2**. When you type **del p1**, you aren't touching the memory space. You are just cutting the link (Think of a wire connecting the reference to object in heap) that connects the reference to that memory space. It is a common misconception that the del command deletes an object. It does not.

·       **Automatic Deletion:** The memory space is only reclaimed by the **Garbage Collector** when the object’s "Reference Count" drops to zero. So till both p1 and p2 are deleted the space occupied by the object will not be reclaimed by the Garbage collector.

*   **The del command:** This only removes a **label** (alias) from an object. It unbinds the name from the memory address.
*   **The `__del__()` method:** This is the **Destructor**. It is called by the Python interpreter only when the "Reference Count" of an object hits zero—meaning there are no more labels attached to it. So if you do del p1, \_\_del\_\_() wont be triggered because p2 exists. But once you also do del p2, then \_\_del\_\_() will be triggered automatically.
*   **The Difference between del and `__del__()`:** del is a manual action to remove a label (reference). `__del__()` is an automatic reaction by Python to remove the object from memory.
*   **The Zero-Threshold**: The Destructor (`__del__()`) is a "patient" method. It waits until the absolute last link is broken before it clears the memory.
*   You don't know exactly when `__del__()` will run. While it usually happens as soon as the count hits zero, Python's Garbage Collector might wait a few milliseconds if it's busy doing other things. This is why we call it Automatic Memory Management.

**Counting Aliases with** **sys.getrefcount()**:- In Python, the **sys.getrefcount(obj)** function returns the number of references to an object. Note that this function always returns a count one higher than you expect. This is because passing the object to the getrefcount() function itself creates a temporary alias inside the function.

The following script shows hoe del and `__del__()`work. To do reference counting we use sys.getrefcount() . So we have to import sys.










