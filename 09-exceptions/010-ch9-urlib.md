



## Project 1: Study Python’s `urllib` library and explain how files can be read from the internet

### Instructions

1.  Explain:
    -   What is `urllib`?
    -   What is `urlopen()`?
2.  Differentiate between:
    -   Local file reading (`open`)
    -   Internet file reading (`urlopen`)
3.  Study:
    -   `.read()`
    -   `.decode()`
4.  Identify possible errors:
    -   `URLError`
    -   `HTTPError`
5.  Write a small script to:
    -   Read first 100 characters from a GitHub file

----------

## Answer (Summary Points)

-   `urllib.request` is used to **access URLs**
-   `urlopen()`:
    -   Opens a connection to a URL
    -   Returns a response object
-   `.read()`:
    -   Reads data in **bytes**
-   `.decode()`:
    -   Converts bytes → string


----------

## Part 2: Project Question (Applied Learning)

### Project Task

> Write a Python program that:

1.  Downloads a file from GitHub (or any URL)
2.  Displays part of the content
3.  Handles:
    -   Invalid URL
    -   Network failure
    -   Wrong encoding
4.  Demonstrates:
    -   Error-free execution
    -   Error-prone execution

----------

## Part 3: Script
















