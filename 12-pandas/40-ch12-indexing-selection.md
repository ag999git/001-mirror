


# Research Project: Advanced Indexing and Selection in Pandas using Palmer Penguins Dataset


## Research Question

> **How can different indexing and selection techniques in Pandas (`[]`, `.`, `.loc[]`, `.iloc[]`, and slicing) be used to efficiently extract, filter, and manipulate structured data, and what are their comparative advantages, limitations, and appropriate use cases when working with real-world datasets such as the Palmer Penguins dataset?**

----------

## Student Task / Project Brief

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
import pandas as pd
import seaborn as sns

# Load dataset
df = sns.load_dataset("penguins")

# Display first 5 rows. 
print(df.head())

```

#### The output is:

```python
  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female

```

From the output you can see that
-   Dataset contains 8 columns, namely: species, island, bill dimensions, flipper length, body mass, sex
-   Contains missing values → important for real-world handling








