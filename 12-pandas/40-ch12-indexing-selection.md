


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

### Step 1: Import Libraries and Load Dataset

```python
import pandas as pd  # Step1 Import libraries and load dataset
import seaborn as sns

# Load dataset
df = sns.load_dataset("penguins")
```

### Step 2: Understanding the Data Structure

```python
# Step 2:  Understanding the Data Structure
# 2. A. df.info() gives us a concise summary of the DataFrame, including the number of non-null entries, 
# data types of each column, and memory usage. 
# This is crucial for understanding the structure of our dataset and identifying any potential 
# issues such as missing values or incorrect data types.
print("df.info():->", df.info())  

"""Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 344 entries, 0 to 343
Data columns (total 7 columns): 
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----
 0   species          344 non-null    object
 1   island           344 non-null    object
 2   bill_length_mm   342 non-null    float64
 3   bill_depth_mm    342 non-null    float64
 4   flipper_length_mm 342 non-null    float64
 5   body_mass_g      342 non-null    float64
 6   sex              333 non-null    object
dtypes: float64(4), object(3)
memory usage: 18.9+ KB
"""
# df.info():-> None. This method prints the summary information to the console but does not return any value, hence it outputs None.



```










