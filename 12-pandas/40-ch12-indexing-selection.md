


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

## Step 2: Understanding the Data Structure

```python
# A. df.info() gives us a concise summary of the DataFrame, including the number of non-null entries, 
# data types of each column, and memory usage. 
# This is crucial for understanding the structure of our dataset and identifying any potential 
# issues such as missing values or incorrect data types.
print("df.info():->", df.info())  

# B. df.describe() provides a statistical summary of the numerical columns in the DataFrame, 
# including count, mean, standard deviation, minimum, and maximum values.
print("df.describe():->\n", df.describe())

# C. df.columns and df.index provide information about the column names and row indices of the DataFrame, respectively.
print("df.columns:->", df.columns)

# D. df.index gives us the row labels of the DataFrame, which can be useful for accessing specific rows or understanding 
# the structure of the data.
print("df.index:->", df.index)
```

The output is:-

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 344 entries, 0 to 343
Data columns (total 7 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   species            344 non-null    object 
 1   island             344 non-null    object 
 2   bill_length_mm     342 non-null    float64
 3   bill_depth_mm      342 non-null    float64
 4   flipper_length_mm  342 non-null    float64
 5   body_mass_g        342 non-null    float64
 6   sex                333 non-null    object
dtypes: float64(4), object(3)
memory usage: 18.9+ KB
df.info():-> None
df.describe():->
        bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g
count      342.000000     342.000000         342.000000   342.000000
mean        43.921930      17.151170         200.915205  4201.754386
std          5.459584       1.974793          14.061714   801.954536
min         32.100000      13.100000         172.000000  2700.000000
25%         39.225000      15.600000         190.000000  3550.000000
50%         44.450000      17.300000         197.000000  4050.000000
75%         48.500000      18.700000         213.000000  4750.000000
max         59.600000      21.500000         231.000000  6300.000000
df.columns:-> Index(['species', 'island', 'bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g', 'sex'],
      dtype='object')
df.index:-> RangeIndex(start=0, stop=344, step=1)
```























