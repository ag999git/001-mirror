

#### Recursive function to find a number is even or not. (Not very efficient)

We can test a number to be even or odd by recursion also. The steps are as follows:-

 - If number is negative, reverse its sign. 
 - Base condition is when    number is 0 or 1. If 0 it is even, if 1 it is odd.
 - Recursively subtract 2 from the number until it becomes less than 2

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












