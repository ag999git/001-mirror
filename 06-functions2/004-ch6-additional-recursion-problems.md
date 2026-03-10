### Additional Problems on recursion

### 1. Recursive Function to Compute $a^b$

Another useful example of recursion is computing the value of:

$a^b$, where $a$ (base) and $b$ (exponent) are non-negative integers.

For example:

$2^5 = 2 × 2 × 2 × 2 × 2 = 32$

<div align="left">
 
$$
a^b = \begin{cases} 
1 & \text{if } b = 0 \\ 
a \times a^{(b-1)} & \text{if } b > 0 
\end{cases}
$$

</div>


Key Components of the Recursive Algorithm

| Component | Description |
| --- | --- |
| Base case | When b=0b = 0b=0, return 1 |
| Recursive case | Multiply a by the result of ab−1a^{b-1}ab−1 |
| Progress toward base case | The exponent decreases by 1 in each call |


```python

# Recursive function to compute a^b (base raised to exponent)
# The exponent is reduced by 1 in every recursive call
# until the base case (exponent = 0) is reached.

def power_recursive(base, exponent):
    
    # Returns base raised to the power exponent using recursion.
    
    # ---------- BASE CASE ----------
    # Any number raised to the power 0 is equal to 1
    if exponent == 0:
        print("Reached base case: exponent = 0 → returning 1")
        return 1

    # ---------- RECURSIVE CASE ----------
    # Reduce the exponent and call the function again
    print(f"Computing {base}^{exponent} → calling {base}^{exponent - 1}")

    # Recursive call with smaller exponent
    partial_result = power_recursive(base, exponent - 1)

    # Multiply base with result returned from recursion
    result = base * partial_result

    # Show the computation during the return phase
    print(f"Returning: {base}^{exponent} = {base} × {partial_result} = {result}")

    return result

# Test cases
# Each tuple contains (base, exponent)

test_cases = [
    (2, 5),   # 2^5 = 32
    (3, 4),   # 3^4 = 81
    (5, 0),   # 5^0 = 1
    (7, 1),   # 7^1 = 7
    (4, 3)    # 4^3 = 64
]

# Run the recursive function on each test case in the list and print the results
for base, exponent in test_cases:

    print("\n----------------------------------")
    print(f"Computing {base}^{exponent}")

    result = power_recursive(base, exponent)

    print(f"Final Result: {base}^{exponent} = {result}")

```


### 2. Using Recursion to Check Whether a String Is a Palindrome

A palindrome is a word, phrase, or sequence of characters that reads the same forward and backward.

Examples:
```python
madam
level
racecar

```

Each of these strings remains the same when the characters are reversed.

Idea Behind the Recursive Solution

A string is a palindrome if:

The first character and last character are the same.

The remaining middle portion of the string is also a palindrome.

For example:

```python
madam
Step-by-step comparison:

m   ada   m
↑         ↑
match
Now check the inner string:

ada
Again:

a  d  a
↑     ↑
match
Now check:
d
A single character is always a palindrome.

```

**Recursive Logic**

  

| Condition | Result |
| --- | --- |
| Length ≤ 1 | Palindrome (base case) |
| First ≠ Last | Not a palindrome |
| First = Last | Recursively check the inner substring |


Thus the recursion continues until the string becomes empty or one character long.

##### Recursive Python Implementation

```python


# Recursive function to check whether a string is a palindrome
# A palindrome reads the same forward and backward.

def is_palindrome(text):

    # Returns True if 'text' is a palindrome, otherwise False.

    # ---------- BASE CASE ----------
    # If the string has length 0 or 1,
    # it is automatically a palindrome
    if len(text) <= 1:
        return True

    # ---------- MISMATCH CHECK ----------
    # Compare the first and last characters
    if text[0] != text[-1]:
        return False   # characters differ → not a palindrome

    # ---------- RECURSIVE CASE ----------
    # Remove first and last characters
    # and test the remaining substring
    inner_text = text[1:-1]

    return is_palindrome(inner_text)



# Testing the palindrome function.

print(is_palindrome("level"))            # True
print(is_palindrome("madam"))            # True
print(is_palindrome("racecar"))          # True
print(is_palindrome("python"))           # False
print(is_palindrome("neveroddoreven"))   # True
print(is_palindrome(""))                 # True (empty string)
print(is_palindrome("a"))                # True (single character)

```


#### Optional Improvement (Often Done in Real Programs)

Real programs often ignore spaces and case differences.

Example:
```python
"Never Odd Or Even"
```

To handle this, we convert the string to lowercase and remove spaces before checking.

Example preprocessing:

`text = text.lower().replace(" ", "")`




### 3. Recursive function to find a number is even or not. (Not very efficient)

We can test a number to be even or odd by recursion also. The steps are as follows:-

 - If number is negative, reverse its sign. 
 - Base condition is when    number is 0 or 1. If 0 it is even, if 1 it is odd.
 - Recursively subtract 2 from the number until it becomes less than 2

> [!TIP]
A number can be tested for **evenness or oddness** using recursion.  
However, this is mainly useful **for learning recursion**, not for efficiency. In practice, Python programmers normally use the **modulus operator (`%`)**.

Idea Behind the Recursive Method. The recursive method is based on the following observations:

  

| Observation | Explanation |
| --- | --- |
| Even numbers differ by 2 | If a number is even, subtracting 2 repeatedly will eventually reach 0 |
| Odd numbers differ by 2 | If a number is odd, subtracting 2 repeatedly will eventually reach 1 |


Thus we use the following rules:

1.  If the number is **negative**, convert it to positive (because even/odd property does not change).  
2.  If the number becomes **0**, it is **even**. _(Base case)_
    
3.  If the number becomes **1**, it is **odd**. _(Base case)_
    
4.  Otherwise subtract **2** and repeat the process recursively.

Recursive Logic

  

  

| Condition | Result |
| --- | --- |
| n = 0 | number is even |
| n = 1 | number is odd |
| n > 1 | check (n − 2) recursively |

```python

# ------------------------------------------------------------
# Recursive function to determine whether a number is even
# ------------------------------------------------------------
# The function repeatedly subtracts 2 from the number
# until it reaches one of the base cases (0 or 1).
# ------------------------------------------------------------

def is_even_recursive(n):
    """
    Returns True if the number is even
    Returns False if the number is odd
    Uses recursion for demonstration purposes.
    """

    # Convert negative numbers to positive
    # (Even/odd property does not change with sign)
    n = abs(n)

    # ---------- Base Cases ----------
    # If n becomes 0, the number is even
    if n == 0:
        return True

    # If n becomes 1, the number is odd
    if n == 1:
        return False

    # ---------- Recursive Case ----------
    # Reduce the problem size by subtracting 2
    return is_even_recursive(n - 2)


# ------------------------------------------------------------
# Example calls
# ------------------------------------------------------------

print("-92 is even?  ", is_even_recursive(-92))   # True  (-92 → 92 → even)
print("17 is even?  ", is_even_recursive(17))    # False (odd)
print("100 is even?  ", is_even_recursive(100))   # True  (even)

```

##### Example Trace: Checking if 7 is Even

The recursive calls proceed as follows:

  

| Step | Function Call |
| --- | --- |
| 1 | is_even_recursive(7) |
| 2 | is_even_recursive(5) |
| 3 | is_even_recursive(3) |
| 4 | is_even_recursive(1) |
| 5 | Base case reached → return False |
  


##### Visual Representation of the Recursion

```python

is_even_recursive(7)
      ↓
is_even_recursive(5)
      ↓
is_even_recursive(3)
      ↓
is_even_recursive(1)
      ↓
Base case → return False

```

##### Why This Method Is Not Efficient

Although recursion works here, it is not efficient for large numbers.

Example:

`is_even_recursive(1,000,000)`

This would require 500,000 recursive calls.

The efficient method is:

`n % 2 == 0`

which completes in one step.























