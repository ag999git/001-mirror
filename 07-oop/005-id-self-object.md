

In Python, every object created is stored at a specific unique address in the computer's memory. 

The `id()` function returns this "memory address." 
The address of the object outside the class is **identical** to the address of `self` inside the class. 
This shows that `self` isn't some magical Python command—it is literally just a nickname for the object itself.

### The "Same Address" Experiment

Here is a script that proves that an object created has same id as `self`.






