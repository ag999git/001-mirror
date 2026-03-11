


### Part 2 — Advanced Concepts of Generators

This section presumes a basic understanding of the idea of `yield`.

----------

#### 1. What Happens When a Generator Finishes?

When a generator finishes producing values, Python raises a special exception called: 

`StopIteration`

This is **not an error in your program**.

It simply signals that **no more values remain**.

#### Example Demonstrating StopIteration


