

## Assignment: Detecting Prime Numbers Using Regular Expressions

### Objective

Use **regular expressions (regex)** to determine whether a given number is **prime**, **without using any arithmetic operations** such as division (`/`, `%`) or loops that test factors.

This assignment is designed to help you understand:

-   Pattern matching beyond simple text search
    
-   Capturing groups and **backreferences**
    
-   **Greedy vs non-greedy** quantifiers
    
-   Creative problem solving with regex
    

----------

### Problem Statement

Write a Python function:

`def  is_prime_unary(n: int) -> bool:
    ...` 

that returns:

-   `True` if `n` is a **prime number**
    
-   `False` otherwise
    

### Restrictions

You **must not**:

-   Use division, modulus, or factorization
    
-   Use libraries for primality testing
    
-   Hardcode prime numbers
    

You **must**:

-   Use the `re` module
    
-   Use **at least one capturing group** and a **backreference**
    
-   Base your solution primarily on a **regular expression**
    

----------

### Conceptual Insight

Prime numbers have **no equal factors other than 1 and themselves**.

If a number **can be broken into equal-sized repeating parts**, it is **not prime**.

----------

#### Hints (Progressive – Do Not Read All at Once)

#### Hint 1: Change the problem domain

Instead of working with numbers, convert the number into a **string**.

> Example:  
> `5 → "11111"`

This representation is called **unary**.

----------

#### Hint 2: Think in terms of repetition

A **composite number** can be written as:

`(block)(block)(block)...(block)` 

Example:

`9 → "111111111" → "111" + "111" + "111"` 

What regex feature allows you to match _repeated identical patterns_?

----------

#### Hint 3: Use capturing groups

Try capturing a block of `'1'` characters and check whether the **entire string** consists of repeated copies of that block.

Key idea:

`(captured_pattern)\1+` 

----------

#### Hint 4: Handle special cases

What about:

-   `n = 0`
    
-   `n = 1`
    

Are these prime?  
How can regex help detect very short strings?

----------

#### Hint 5: Greedy vs Non-Greedy

If your regex doesn’t work as expected, ask yourself:

-   Is the engine capturing **too much**?
    
-   Would a **non-greedy quantifier (`+?`)** help?
    

Try both and observe the difference.

----------

### Suggested Test Cases

You should test at least:

`0 → False
1 → False
2 → True
3 → True
4 → False
5 → True
6 → False
7 → True
9 → False
11 → True` 

----------

### Deliverables

You should submit:

1.  Python function code
    
2.  The regex pattern used
    
3.  A **written explanation** of:
    
    -   How the regex works
        
    -   Why it detects composite numbers
        
    -   Why primes fail to match





