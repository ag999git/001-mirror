
## Write a regexp which places certain restrictions on a password that a user may select



### Problem:- Write a regexp which places the following restrictions on a password that a user may select:-

The password should have the following:-

-  At least one small alphabet ie [a-z]

-  At least one large (capital) alphabet ie [A-Z]

-  At least one digit ie [0-9]

-  At least one special character from [!@#$%^&*]

-  The password should have a minimum length of 6 and maximum of 12 characters


## The script is as follows:-


```python
import re

# Complete password validation pattern
password_pattern = (
    r'^'                    # Start of string
    r'(?=.*[a-z])'           # At least one lowercase letter
    r'(?=.*[A-Z])'           # At least one uppercase letter
    r'(?=.*[0-9])'           # At least one digit
    r'(?=.*[!@#$%^&*])'      # At least one special character
    r'[A-Za-z0-9!@#$%^&*]'   # Allowed characters
    r'{6,12}$'               # Length between 6 and 12
)

# List of test passwords
test_passwords = [
    #  Valid passwords
    "Ab1@xy",
    "Good1@Pwd",
    "Xy9#Ab",
    "Pass1$word",
    "Z9@abc",

    #  Invalid passwords
    "abc123@",          # No uppercase letter
    "ABC123@",          # No lowercase letter
    "Abcdef@",          # No digit
    "Ab1xyz",           # No special character
    "Ab1@x",            # Too short
    "Ab1@xyzabcdef",    # Too long
    "Ab1@xy!",          # Too long (7 but extra special allowed? no length OK — keep for discussion)
    "Ab1@xy ",          # Contains space
    "Ab1@xy?",          # Invalid special character '?'
    "123@ABC",          # No lowercase
]

# Validate each password
for pwd in test_passwords:
    if re.match(password_pattern, pwd):
        print(f"{pwd:15} → GOOD")
    else:
        print(f"{pwd:15} → BAD")

```


```python
Ab1@xy          → GOOD
Good1@Pwd       → GOOD
Xy9#Ab          → GOOD
Pass1$word      → GOOD
Z9@abc          → GOOD
abc123@         → BAD
ABC123@         → BAD
Abcdef@         → BAD
Ab1xyz          → BAD
Ab1@x           → BAD
Ab1@xyzabcdef   → BAD
Ab1@xy!         → GOOD
Ab1@xy          → BAD
Ab1@xy?         → BAD
123@ABC         → BAD

```











