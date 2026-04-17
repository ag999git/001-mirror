

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

### 1. (B) `.dropna()`

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
>> So, you need to be careful and know the consequences of using `.dropna()`
----------

### 1. (C) `.fillna()`

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






