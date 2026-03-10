

### 1. `zip()` Function

#### Concept

The `zip()` function combines elements from **two or more iterables** into **tuples**.

Each tuple contains elements taken from the **same position** in the input iterables.

The function **stops when the shortest iterable is exhausted**.

Thus, `zip()` is often used when you want to **iterate over multiple sequences in parallel**.

----------

#### Syntax

`zip(*iterables)`

Where:

-   `iterables` may be lists, tuples, strings, ranges, etc.
    
-   The result is a **zip object (iterator)**.
    

----------

#### Key Properties

  

| Feature | Description |
| --- | --- |
| Works with any iterable | lists, tuples, strings, ranges |
| Returns | iterator object |
| Output format | tuples |
| Stops when | shortest iterable ends |
| Common use | parallel iteration |

Script Demonstrating `zip()`

```python

# Demonstration of the zip() function in Python

# 1. Zipping two lists")

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

z = zip(list1, list2)

print("Type of result:", type(z))  # <class 'zip'> - zip() returns an iterator of tuples
# Convert iterator to list to view contents
print("Zipped result:", list(z))  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# 2: Zipping sequences of unequal length

a = [10, 20, 30, 40]
b = ['x', 'y']

result = list(zip(a, b))

# Stops when shortest iterable finishes
print(result)  # [(10, 'x'), (20, 'y')]

# 3: Zipping three sequences

names = ["Alice", "Bob", "Charlie"]
ages = [21, 22, 23]
cities = ["Delhi", "Mumbai", "Kolkata"]

combined = list(zip(names, ages, cities))

print(combined)  # [('Alice', 21, 'Delhi'), ('Bob', 22, 'Mumbai'), ('Charlie', 23, 'Kolkata')]

# 4: Iterating with zip

numbers = [1,2,3]
letters = ['A','B','C']

for n, l in zip(numbers, letters):
    print(n, l)

# Output:
# 1 A
# 2 B
# 3 C

# 5: Unzipping sequences

pairs = [(1,'a'), (2,'b'), (3,'c')]

x, y = zip(*pairs)

print("Numbers:", x)  # (1, 2, 3)
print("Letters:", y)  # ('a', 'b', 'c')

# 6: Creating dictionary using zip

keys = ['name','age','city']
values = ['Rahul', 25, 'Delhi']

dictionary = dict(zip(keys, values))
print(dictionary)  # {'name': 'Rahul', 'age': 25, 'city': 'Delhi'}


```










