





## Part 1: Research Question: Study the Python `requests` library and explain how it simplifies reading files/data from the internet compared to `urllib`.

----------

### Instructions

1.  What is the `requests` library?
2.  How is it different from `urllib`?
3.  Study the following:
    -   `requests.get()`
    -   `response.text`
    -   `response.content`
    -   `response.status_code`
4.  What is:
    -   `raise_for_status()`?
5.  Identify common exceptions:
    -   `RequestException`
    -   `HTTPError`
    -   `ConnectionError`
    -   `Timeout`
6.  Write a small script to:
    -   Read and display first 100 characters from a GitHub file

----------

### Answer (Key Points)

-   `requests` is a **third-party library**
-   It provides a **simple and readable API**
-   `get()` → sends HTTP request
-   `response.text` → string data
-   `response.content` → raw bytes
-   `raise_for_status()`:
    -   Raises error for HTTP issues (like 404)

----------

## Part 2: Project Question (Applied Learning)

### Project Task

> Develop a Python program using `requests` that:

1.  Downloads a file from GitHub (raw URL)
2.  Displays part of the content
3.  Handles:
    -   Invalid URL
    -   Network failure
    -   Timeout
    -   HTTP errors (404, 500)
4.  Demonstrates:
    -   Successful execution
    -   Multiple error scenarios

----------

## Part 3: Script









