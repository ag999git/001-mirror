


### Research Question 2: Compare and contrast Shallow Copy and Deep Copy. When should a programmer use one over the other when working with nested objects (like a list of Pet objects)?

**Answer:**

In Python, the copy module provides two ways to duplicate data:

1.  **Shallow Copy (`copy.copy()`):** It creates a new collection object, but it fills it with **references** to the same child objects. If you change a pet's name in the copy, it changes in the original too.
2.  **Deep Copy (`copy.deepcopy()`):** It creates a new collection **and** recursively creates new copies of every object found inside. It is a total, independent clone.



  

| Feature | Shallow Copy | Deep Copy |
| --- | --- | --- |
| New Container? | Yes | Yes |
| New Inner Objects? | No (Shared) | Yes (Independent) |
| Performance | Fast | Slower (More memory) |


