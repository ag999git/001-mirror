

## Online resource:
It contains a user-registration validation example together with a detailed walkthrough covering:

-   What the script does
-   Why each validation rule exists
-   How the implementation works
-   Exception-handling techniques
-   Testing strategies using pytest.raises()
-   Key software engineering concepts such as input validation, defensive programming, and fail-fast design

Readers are encouraged to study both the source code and the accompanying discussion to gain a deeper understanding of how exception testing is used in real-world applications.


## Folder structure 
It should be something similar to as given below:

```python
ch16-scripts/
│
├── user_registration.py
└── test_user_registration.py

```

##  user_registration.py. This module contains the create_user function that we want to test. 


```python

# user_registration.py
# This module contains the create_user function that we want to test.
import re  # Importing the regular expression module to validate email addresses

def create_user(username, age, email):  # This function creates a user dictionary after validating the input parameters.
    if not username:   # If the username is empty, we raise a ValueError with a specific message.
        raise ValueError("Username cannot be empty")  #

    if age < 13:  # If the age is less than 13, we raise a ValueError with a specific message.
        raise ValueError("User must be at least 13 years old")

    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):  # If the email is not valid, we raise a ValueError with a specific message.
        raise ValueError("Invalid email address")

    # If all validations pass, we return a dictionary representing the user.
    return {
        "username": username,
        "age": age,
        "email": email,
    }

```







## test_user_registration.py. This is the file used to test user_registration.py

```python
# test_user_registration.py
# To run the tests in this file, use the command: pytest test_user_registration.py
import pytest
# user_registration.py contains the create_user function that we are testing.
from user_registration import create_user

def test_empty_username():  # Test that creating a user with an empty username raises ValueError
    with pytest.raises(ValueError):  # Test that ValueError is raised when username is empty
        create_user("", 20, "alice@example.com")  # This should raise ValueError because username cannot be empty

def test_username_message():  # Test that the exception message for empty username is correct
    with pytest.raises(
        ValueError,
        match="Username cannot be empty"  # Assert that the exception message contains "Username cannot be empty"
    ):
        create_user("", 20, "alice@example.com")  # This should raise ValueError with the correct message


def test_underage_user():  # Test that creating a user under 13 years old raises ValueError
    with pytest.raises(ValueError) as excinfo:
        create_user("alice", 10, "alice@example.com")

    assert excinfo.type is ValueError  # Assert that the exception type is ValueError
    assert "13 years old" in str(excinfo.value)  # Assert that the exception message contains "13 years old"


def test_invalid_email():  # Test that creating a user with an invalid email raises ValueError
    with pytest.raises(
        ValueError,
        match="Invalid email address"  # Assert that the exception message contains "Invalid email address"
    ):
        create_user("alice", 20, "bad-email")  # This should raise ValueError with the correct message


def test_valid_user():  # Test that creating a valid user returns the correct user dictionary
    user = create_user(
        "alice",
        20,
        "alice@example.com"
    )

    assert user["username"] == "alice"  # Assert that the username in the returned user dictionary is correct
    assert user["age"] == 20  # Assert that the age in the returned user dictionary is correct
    assert user["email"] == "alice@example.com"  # Assert that the email in the returned user dictionary is correct

```









