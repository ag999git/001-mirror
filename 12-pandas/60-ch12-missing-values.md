

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



## **Conceptual Understanding**

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






