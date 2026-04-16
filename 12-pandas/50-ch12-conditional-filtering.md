


## Research Question

> **How can conditional filtering techniques in Pandas (Boolean indexing, logical operators, `.isin()`, and string-based filtering using `.str.contains()`) be used to efficiently extract meaningful subsets of data from a real-world dataset such as the Palmer Penguins dataset, and what are their comparative advantages, limitations, and common sources of error?**

### PROJECT: Conditional Filtering in Pandas
DATASET: Palmer Penguins

>OBJECTIVE:
>To demonstrate:
>1. Boolean indexing
>2. Logical operators (&, |, ~)
>3. .isin() method
>4. .str.contains() for string filtering
>5. Common errors and handling

----------

## Task / Project Description

You are required to:

1.  Load and explore the **Palmer Penguins dataset**
2.  Apply **basic Boolean filtering**
3.  Combine multiple conditions using:
    -   `&` (AND)
    -   `|` (OR)
    -   `~` (NOT)
4.  Use `.isin()` for filtering multiple values
5.  Use `.str.contains()` for string-based filtering
6.  Identify and handle **common errors**
7.  Present findings using:
    -   Tables
    -   Code with comments
    -   Flowcharts

----------

## Solution


### STEP 0: Import Libraries and Load Dataset**

#### Why this step is done

This step initializes the working environment. Without loading the required libraries and dataset, no data analysis can be performed.

#### How it is done

-   Import `pandas` for data manipulation
-   Import `seaborn` to access the Palmer Penguins dataset
-   Load dataset into a DataFrame

#### What to do

-   Use standard aliases (`pd`, `sns`)
-   Ensure dataset loads correctly

#### What not to do

-   Avoid reloading dataset multiple times unnecessarily
-   Avoid modifying original dataset unintentionally

----------

#### Key Features / Sub-steps

-   Library import
-   Dataset loading
-   Initial inspection (`head()` optional)

----------

#### Methods / Attributes

 **`sns.load_dataset(name)`**

-   **Input:** Dataset name (string)
-   **Output:** Pandas DataFrame
-   **Limitation:** Requires internet (in some environments)

## Script
The script is broken up into steps to explain each step in details

### Script for implementing STEP 0 

```python
# STEP 0: IMPORT LIBRARIES AND LOAD DATASET
print("\n STEP 0. IMPORT LIBRARIES AND LOAD DATASET")
import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")

print("\n--- FIRST 5 ROWS ---")
print("df.head()->", df.head())  # Display the first 5 rows of the dataset to understand its structure and columns

```
**Output**

```python
 STEP 0. IMPORT LIBRARIES AND LOAD DATASET

--- FIRST 5 ROWS ---
df.head()->   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female

```



###


###


###


###


###


###














