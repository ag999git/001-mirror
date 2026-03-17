



#### Research / Study Question

**Topic: Cryptographic Vulnerability in Pseudorandom Number Generators (PRNGs)**

> **Question:** "In the context of the Linear Congruential Generator (LCG), how does the mathematical relationship between successive outputs $(X_n, X_{n+1}, X_{n+2})$ allow an observer to reverse-engineer hidden parameters like the multiplier ($a$) and increment ($c$)? Discuss the implications of this predictability for security-sensitive applications and demonstrate the 'break' using a Python-based reconstruction script."

----------

#### Answer

**The Mathematical Vulnerability**

The LCG relies on a simple linear equation:

$$X_{n+1} = (a \cdot X_n + c) \pmod m$$

Because this is a linear relationship, knowing just a few consecutive outputs allows us to set up a system of equations.

1.  **Finding $c$ (Multiplier $a$ and Modulus $m$ are known):**
    
    If we have two consecutive numbers, $X_0$ and $X_1$, we can rearrange the formula:
    
    $$c \equiv (X_1 - a \cdot X_0) \pmod m$$
    
    In Python, we use the modulo operator `%` to ensure $c$ stays within the range $[0, m-1]$.
    
2.  **Finding $a$ and $c$ (Only Modulus $m$ is known):**
    
    With three consecutive numbers ($X_0, X_1, X_2$), we have:
    
    1.  $X_1 \equiv a \cdot X_0 + c \pmod m$
        
    2.  $X_2 \equiv a \cdot X_1 + c \pmod m$
        
    
    Subtracting (1) from (2) eliminates $c$:
    
    $$X_2 - X_1 \equiv a(X_1 - X_0) \pmod m$$
    
    To find $a$, we need to multiply $(X_2 - X_1)$ by the **Modular Multiplicative Inverse** of $(X_1 - X_0)$.
    
    _Note: In your original hint, simple division $(X_2 - X_1) / (X_1 - X_0)$ only works in standard algebra. In modular arithmetic, we must use `pow(diff_x, -1, m)`._
    

### **Implications**

This research shows that LCG is **not cryptographically secure**. If an attacker can see just three random values (like three session IDs or three "random" passwords), they can predict every future value the system will ever generate.

----------

#### 3. The Python Script (The "LCG Breaker")

This script implements the LCG class and then uses two "Breaker" functions to recover the hidden parameters.




