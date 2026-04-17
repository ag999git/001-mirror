

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




















