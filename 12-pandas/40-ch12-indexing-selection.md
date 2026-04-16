


# Research Project: Advanced Indexing and Selection in Pandas using Palmer Penguins Dataset


## Research Question

> **How can different indexing and selection techniques in Pandas (`[]`, `.`, `.loc[]`, `.iloc[]`, and slicing) be used to efficiently extract, filter, and manipulate structured data, and what are their comparative advantages, limitations, and appropriate use cases when working with real-world datasets such as the Palmer Penguins dataset?**

----------

## Task / Project Brief

You are required to:

1.  Load and explore the **Palmer Penguins dataset**
2.  Perform **column selection** using:
    -   Bracket `[]`
    -   Dot `.` notation
3.  Perform **row selection** using:
    -   `.loc[]` (label-based indexing)
    -   `.iloc[]` (position-based indexing)
4.  Perform **combined slicing of rows and columns**
5.  Compare all methods in terms of:
    -   Syntax
    -   Flexibility
    -   Limitations
6.  Handle possible **errors/exceptions**
7.  Document your findings with:
    -   Tables
    -   Code with comments
    -   Flowcharts

----------

# Model Solution

----------

## Step 1: Import Libraries and Load Dataset

```python
import pandas as pd  # Step1 Import libraries and load dataset
import seaborn as sns

# Load dataset
df = sns.load_dataset("penguins")

```








