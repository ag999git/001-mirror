


### 1. Mathematical Constants

These are fixed attributes rather than functions (they take no parameters). The following table gives details of the mathematical constants in the math module

| Constant | Value | Description | GitHub Usage |
| --- | --- | --- | --- |
| `math.pi` | 3.141592... | Ratio of circle circumference to diameter | `area = math.pi * r**2` |
| `math.e` | 2.718281... | Base of natural logarithms | `val = math.e ** 2` |
| `math.tau` | 6.283185... | Full circle constant ($2\pi$) | `circ = math.tau * r` |
| `math.inf` | inf | Floating-point positive infinity |` my_inf = math.inf` |
| `math.nan` | nan | "Not a Number" (undefined) | `if math.isnan(x):` |


### 2. Number-Theoretic & Representation 

These functions are used for rounding, signs, and basic integer logic. The following table give details of these functions:-
  

| Function | Input Parameters | Output | Simple Example |
| --- | --- | --- | --- |
| `math.ceil(x)` | Single number $x$ | Smallest integer $\geq x$ | math.ceil(4.2) $\to$ 5 |
| math.floor(x) | Single number $x$ | Largest integer $\leq x$ | math.floor(4.8) $\to$ 4 |
| `math.fabs(x)` | Single number $x$ | Absolute value (as float) | math.fabs(-5) $\to$ 5.0 |
| `math.gcd(a, b)` | Two integers $a, b$ | Greatest Common Divisor | math.gcd(12, 18) $\to$ 6 |
| `math.isclose(a, b)` | Two floats $a, b$ | Boolean (True/False) | math.isclose(0.1+0.2, 0.3) $\to$ True |


### 3. Power and Logarithmic Functions

Essential for handling growth, roots, and scaling.



| Function | Input Parameters | Output | Simple Example |
| --- | --- | --- | --- |
| `math.sqrt(x)` | Single number $x$ | Square root of $x$ | math.sqrt(25) $\to$ 5.0 |
| `math.pow(x, y)` | Base $x$, Exponent $y$ | $x$ raised to power $y$ | math.pow(2, 3) $\to$ 8.0 |
| `math.exp(x)` | Single number $x$ | $e$ raised to power $x$ | math.exp(1) $\to$ 2.718... |
| `math.log(x, [base])` | Number $x$, optional base | Logarithm of $x$ | math.log(100, 10) $\to$ 2.0 |
| `math.log10(x)` | Single number $x$ | Base-10 logarithm | math.log10(1000) $\to$ 3.0 |



### 4. Trigonometric & Angular Functions

Used for calculating angles and distances. Note: All trig functions use radians.






| Function | Input Parameters | Output | Simple Example |
| --- | --- | --- | --- |
| `math.sin(x)` | Angle $x$ in radians | Sine of $x$ | math.sin(math.pi/2) $\to$ 1.0 |
| `math.cos(x)` | Angle $x$ in radians | Cosine of $x$ | math.cos(0) $\to$ 1.0 |
| `math.hypot(x, y)` | Sides $x$ and $y$ | Hypotenuse $\sqrt{x^2+y^2}$ | math.hypot(3, 4) $\to$ 5.0 |
| `math.degrees(x)` | Radians $x$ | Value in degrees | math.degrees(math.pi) $\to$ 180.0 |
| `math.radians(x)` | Degrees $x$ | Value in radians | math.radians(180) $\to$ 3.1415... |




### 5. Hyperbolic & Special Functions

Advanced functions used in specialized engineering and statistics.

| Function | Input Parameters | Output | Simple Example |
| --- | --- | --- | --- |
| math.sinh(x) | Single number $x$ | Hyperbolic sine | math.sinh(0) $\to$ 0.0 |
| math.cosh(x) | Single number $x$ | Hyperbolic cosine | math.cosh(0) $\to$ 1.0 |
| math.gamma(x) | Single number $x$ | Gamma function $\Gamma(x)$ | math.gamma(5) $\to$ 24.0 |
| math.erf(x) | Single number $x$ | Gaussian Error Function | math.erf(0) $\to$ 0.0 |










