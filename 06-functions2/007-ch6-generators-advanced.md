


### Part 2 — Advanced Concepts of Generators

This section presumes a basic understanding of the idea of `yield`.

----------

#### 1. What Happens When a Generator Finishes?

When a generator finishes producing values, Python raises a special exception called: 

`StopIteration`

This is **not an error in your program**.

It simply signals that **no more values remain**.

#### Example Demonstrating StopIteration.

The following diagram shows how StopIteration works in generator functions.

![StopIteration Diagram](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch6-generators-stopiteration.png)

```python


# Demonstration of a simple generator and StopIteration

# 1. This generator function has multiple yield statements and print statements to show the flow of execution.
def simple_generator():
    """Generator with three yield statements."""

    print("Generator started")

    yield "yielding 1"     # First value returned
    print("Resuming after first yield")

    yield "yielding 2"     # Second value returned
    print("Resuming after second yield")

    yield "yielding 3"     # Third value returned
    print("Generator is about to finish")

# 2. Creating the generator object
gen = simple_generator()   # Function does NOT execute yet
print("Generator object created\n")


# 3. Manually retrieving values using next()
print("First next() call:")
print(next(gen))   # Generator starts executing
print("Second next() call:")
print(next(gen))
print("Third next() call:")
print(next(gen))

# 4. Generator is now exhausted
# Calling next() again raises StopIteration
print("Fourth next() call:")

try:
    print(next(gen))
except StopIteration:
    print("StopIteration raised → No more values left in generator!")

# 5. Using a generator inside a for-loop
print("Using generator in a for-loop:")

for value in simple_generator():
    print(value)

print("In a for-loop, StopIteration happens internally and is NOT shown.")


```

