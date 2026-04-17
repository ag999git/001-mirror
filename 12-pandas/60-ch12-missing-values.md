

# Project: Handling Missing Values in Pandas using Palmer Penguins Dataset

----------

## Research Question

> **How can missing data in a real-world dataset such as the Palmer Penguins dataset be identified, analyzed, and handled using Pandas techniques like `.isna()`, `.dropna()`, and `.fillna()`, and what are the conceptual and practical trade-offs between dropping and imputing missing values?**

----------

## Task / Project Description

You are required to:

1.  Identify missing values in the dataset
2.  Quantify and analyze missing data
3.  Apply strategies to handle missing data:
    -   Dropping missing values
    -   Filling (imputing) missing values
4.  Compare different strategies (Mean, Median, Mode)
5.  Understand when to use each method
6.  Document findings with:
    -   Code and comments
    -   Tables
    -   Flowcharts



## 1. Important Methods with Signatures

----------

### 1. (A) `.isna()`

`df.isna()`

-   Returns: Boolean DataFrame
-   Limitation: Needs aggregation for counts

----------

### 1. (B) `.dropna(axis = 0)` for `axis =0`

`df.dropna(axis=0, how='any')`

-   `axis=0` → rows
-   `axis=1` → columns
-   `how='any'` or `'all'`
-   Returns: New DataFrame


#### Pandas removes the entire row even if just one value in that row is missing.
#### When you run:

`df_drop_rows  =  df.dropna()`

Pandas applies the default behavior:

`df.dropna(axis=0, how='any')`

#### Interpretation:

-   `axis=0` → operate on **rows**
-   `how='any'` → if **any column in a row has NaN**, drop that row

>Row is treated as a unit. If any part is incomplete, the whole row is removed.
>You may lose a lot of data unintentionally
>In real datasets (like penguins), many rows have at least one missing value.
> So, you need to be careful and know the consequences of using `.dropna()`
----------

### 1. (C) `.dropna(axis = 1)` for axis =1

#### When you run:

`df_drop_cols  =  df.dropna(axis=1)`

Pandas internally treats it as:

`df.dropna(axis=1, how='any')`

----------

#### Interpretation

-   `axis=1` → operate on **columns**
-   `how='any'` → if **any row in a column has NaN**, drop that column


> In `.dropna(axis=1)` Column is treated as a unit. If any value is missing anywhere in that column, the whole column is removed.


#### Why this is risky

In real datasets (like Penguins):

-   Many columns have at least one missing value
-   Using this blindly may **remove most of your dataset**

#### For example:

-   `sex` column has missing values → will be dropped
-   numeric columns may also be dropped if any NaN exists



### 1. (D) `.fillna()`

`df.fillna(value)`

-   Input: scalar, dict, or method
-   Returns: New DataFrame
-   Limitation: May introduce bias







## 2. Conceptual Understanding

### Identifying Missing Values

| Method | Description | Output |
| --- | --- | --- |
| .isna() | Detect missing values | Boolean DataFrame |
| .isnull() | Same as .isna() | Boolean DataFrame |
| .sum() | Count missing values | Series |

* * *

### Dropping vs Filling

| Aspect | Dropping (dropna) | Filling (fillna) |
| --- | --- | --- |
| Data Loss | High | Low |
| Simplicity | Easy | Moderate |
| Bias Risk | Low | Possible |
| Use Case | Small missing data | Large missing data |

* * *

### Imputation Techniques

| Method | Suitable For | Advantage | Limitation |
| --- | --- | --- | --- |
| Mean | Numeric data | Simple | Affected by outliers |
| Median | Numeric data | Robust | Ignores distribution |
| Mode | Categorical data | Works for strings | May be ambiguous |


# Script (in steps) and explanation of each step

## STEP 1: IMPORT LIBRARIES AND LOAD DATASET

----------

### Why this step is done

This step prepares the environment for data analysis.  
Before performing any operation on data, the required libraries must be loaded and the dataset must be brought into a Pandas DataFrame.

Without this step, no further data inspection, cleaning, or analysis is possible.

----------

### How it is done

-   The `pandas` library is imported for data manipulation
-   The `seaborn` library is used to load the Palmer Penguins dataset
-   The dataset is stored in a DataFrame (`df`)

----------

### What to do

-   Use standard aliases:
    -   `import pandas as pd`
    -   `import seaborn as sns`
-   Load dataset once and reuse it
-   Display initial rows using `head()`
-   Check shape using `.shape` to understand size

----------

### What not to do

-   Avoid reloading dataset multiple times
-   Avoid modifying original dataset without creating a copy
-   Avoid skipping initial inspection

----------

### Important Features / Sub-steps

-   Import libraries
-   Load dataset
-   Store in DataFrame
-   Perform initial inspection (`head()`, `shape`)

----------

### Methods / Attributes

----------

#### `sns.load_dataset(name)`

`df  =  sns.load_dataset("penguins")`

-   **Input:** Dataset name (string)
-   **Output:** Pandas DataFrame
-   **Use:** Loads built-in dataset

----------

#### `df.head(n=5)`

`df.head()`

-   **Input:** Number of rows (optional)
-   **Output:** First `n` rows
-   **Use:** Quick inspection

----------

####  `df.shape`

`df.shape`

-   **Output:** Tuple `(rows, columns)`
-   **Use:** Understand dataset size

----------

### Limitations

-   `sns.load_dataset()` may require internet access in some environments
-   `head()` shows only a small sample, not full dataset
-   Initial inspection does not reveal deeper data issues

----------

### Role of Step 1

> “The first step in any data analysis task is to load the dataset and understand its basic structure, as this forms the foundation for all subsequent operations.”

### Script for Step 1

```python

# STEP 1: IMPORT LIBRARIES AND LOAD DATASET
print("\n STEP 1. IMPORT LIBRARIES AND LOAD DATASET")

import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")
# The dataset contains information about penguins, including their species, island, bill length, 
# bill depth, flipper length, body mass, and sex

print("\n--- FIRST 5 ROWS OF ORIGINAL DATAFRAME ---")
print(df.shape)  # (344, 7) - 344 rows and 7 columns
print("df.head()->", df.head())  # First 5 rows of the original DataFrame.

```

#### Output for Step 1

```python
STEP 1. IMPORT LIBRARIES AND LOAD DATASET

--- FIRST 5 ROWS OF ORIGINAL DATAFRAME ---
(344, 7)
df.head()->   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female

```



## STEP 2: IDENTIFYING MISSING VALUES

----------

### Why this step is done

Before cleaning data, it is essential to **detect and quantify missing values**. Without this step, any cleaning strategy would be uninformed and potentially harmful.

----------

## 2(A) `.isna()` – Detect Missing Values

### What it does

Creates a Boolean DataFrame:

-   `True` → Missing value
-   `False` → Present value

### How it is done

`df.isna()`

### Output

-   Same shape as original DataFrame
-   Boolean values

----------

### What to do

-   Use `.head()` to avoid large output
-   Use it for visual inspection

### What not to do

-   Avoid printing full DataFrame for large datasets

----------

### Method Signature

DataFrame.isna()

-   **Input:** None
-   **Output:** DataFrame (Boolean)
-   **Limitation:** Does not give counts directly

### Script for 2(A)

```python
# 2(A) Use .isna() to check missing values (True -> missing, False -> not missing)
print("\nMissing values (True/False):->")
# .isna() detects missing values in the DataFrame and returns a DataFrame of the same shape as df, where each 
# cell contains True if the original cell in df is NaN (missing) and False otherwise.   
print("df.isna().head()->", df.isna().head()) 
# This allows us to quickly see which values are missing in the dataset. 
# For example, if the 'bill_length_mm' column has a missing value in the 4th row, the corresponding cell 
# in the output will show True for that position. 

```
### Output for Step 2(A)

```python
Missing values (True/False):->
df.isna().head()->    species  island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g    sex
0    False   False           False          False              False        False  False
1    False   False           False          False              False        False  False
2    False   False           False          False              False        False  False
3    False   False            True           True               True         True   True
4    False   False           False          False              False        False  False

```





## 2(B) `.isna().sum()` – Count Missing Values

### Why

To quantify missing data per column

### How

`df.isna().sum()`

>This is **method chaining**

----------

### Output

-   Pandas Series
-   Index → column names
-   Values → count of missing values

----------

### Method Signatures

`df.isna() # Assume df is a DataFrame`  

-   Returns a **DataFrame of the same shape**
-   Each value is:
    -   `True` → if original value is missing (NaN)
    -   `False` → if value is present



`DataFrame.sum(axis=0)`
This tells us:

-   Method name → `sum`
-   Parameter → `axis`
-   Default value → `axis=0`

>The default value of `axis =0`. This means that if you dont give any value for axis parameter, it will take a default of `axis =0` and therefore add/ Sum down rows (column-wise).
>But you can override/ change this behavior by giving axis =1. This will add/ Sum across columns (row-wise). 

  

| Parameter | Meaning |
| --- | --- |
| axis=0 | Sum down rows (column-wise) |
| axis=1 | Sum across columns (row-wise) |



----------

### Limitations

-   Works column-wise by default
-   Requires understanding Boolean arithmetic

----------

### Script for 2(B)

```python
# 2(B) Use .isna().sum() to count missing values per column
# We are "method chaining" .isna() with .sum() to get a count of how many missing values are in each column.
# The result is a Series where the index is the column names and the values are the count of missing values 
# in each column.
print("\nMissing values count per column:->")
print("df.isna().sum()->", df.isna().sum())
# This shows how many missing values are in each column. For example, if 'body_mass_g' has 2 missing values, 
# it will show 2 for that column.

```

### Output for Step 2(B)

```python
Missing values count per column:->
df.isna().sum()-> species               0
island                0
bill_length_mm        2
bill_depth_mm         2
flipper_length_mm     2
body_mass_g           2
sex                  11
dtype: int64

```




## 2(C) `.isnull()`

### Why

Alternative to `.isna()`

### Key Point

> `.isnull()` and `.isna()` are identical

### Script for 2(C)

```python
# 2(C) Use .isnull() to check missing values (same as .isna())
print("\nUsing isnull():->")
# We are "method chaining" .isnull() with .sum() to confirm that it gives the same result as .isna().
print("df.isnull().sum()->", df.isnull().sum())
# Output will be the same as using isna(), confirming that both methods are interchangeable 
# for detecting missing values.

```


### Output for Step 2(C)

```python
Using isnull():->
df.isnull().sum()-> species               0
island                0
bill_length_mm        2
bill_depth_mm         2
flipper_length_mm     2
body_mass_g           2
sex                  11
dtype: int64

```


## STEP 3: DROPPING MISSING VALUES

### Why this step is done

To remove incomplete data when missing values are small or insignificant.

----------

## 3(A) Drop Rows → `.dropna(axis=0)`

### How

`df.dropna(axis=0)`

----------

### Meaning

-   Remove row if **any value is missing**

----------

### Signature

`DataFrame.dropna(axis=0, how='any', subset=None)`

-   **`axis=0`** → rows (This is the default value.)
-   **`how='any'`** → default

----------

### Limitations

-   Can remove large amount of data
-   May introduce bias

----------

### What to do

-   Check `.shape` before and after

### What not to do

-   Avoid blind usage

----------

## 3(B) Drop Columns → `.dropna(axis=1)`

### How

`df.dropna(axis=1)`

----------

### Meaning

-   Remove column if **any value is missing**

----------

### Limitations

-   May remove important features
-   Very aggressive

----------

### Important Parameters

`df.dropna(axis=1, how='all', thresh=n)`


| Parameter | Meaning |
| --- | --- |
| how='all' | Drop only if all values missing |
| thresh | Minimum non-null values required |















