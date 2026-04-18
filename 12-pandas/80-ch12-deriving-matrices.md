



# Basic Data Manipulations

## Research Topic: Deriving Metrics and Organizing Penguin Morphology

**Research Question:** _How can derived metrics be constructed from existing data, irrelevant data be removed, and the resulting dataset be sorted to facilitate comparative biological analysis?_

**Project Scenario:** A marine biologist hypothesizes that the ratio of bill length to bill depth (the "Slenderness Index") varies significantly between species. To test this, the dataset must be manipulated to:

1.  Calculate a new column: `slenderness_index` (Bill Length / Bill Depth).
2.  Remove non-essential categorical data (`sex`, `island`) to focus purely on physical morphology.
3.  Sort the dataset to identify penguins with the most extreme body structures.

**Task:** Using the Palmer Penguins dataset, write a script to generate the new metric, clean the dataframe using both `inplace` and reassignment methods, and sort the results by species and body mass.

----------

## 1. Conceptual Deep Dive

Before execution, one must understand the mechanics of vectorization, deletion strategies, and sorting algorithms in Pandas.

### A. Adding New Columns

Pandas allows for **vectorized operations**, meaning one can perform math on entire columns without writing loops.

  

| Syntax | Description | Example |
| --- | --- | --- |
| `df['new'] = df['a'] + df['b']` | Element-wise addition (or any math). | `df['total'] = df['x'] + df['y']` |
| `df['new'] = df['col'].str.upper()` | String manipulation. | `df['name'] = df['name'].str.upper()` |

```python
# ERROR EXAMPLE: Mismatched lengths
# df['new_col'] = [1, 2, 3] 
# ValueError: Length of values (3) does not match length of index (344)
```

## B. Deleting Columns

There are two primary ways to remove data, with distinct behavioral differences.

| Method | Syntax | Behavior |
| --- | --- | --- |
| `.drop()` | `df.drop('col', axis=1)` | Returns a new DataFrame. Original remains unchanged unless inplace=True. Flexible (can drop rows too). |
| `del` | `del df['col']` | Directly deletes from the original DataFrame. Returns nothing. Permanent immediately. |


## C. Inplace vs. Reassignment

This is a fundamental concept in Python data science.


| Parameter | Mode | Explanation |
| --- | --- | --- |
| `inplace=True` | In-place | The operation modifies the object itself. No value is returned (returns None). |
| `inplace=False (Default)` | Copy | The operation creates a copy of the data, modifies it, and returns the new copy. The original object is untouched. |


## D. Sorting Data

The `.sort_values()` method arranges rows based on column values.

  

| Parameter | Option | Effect |
| --- | --- | --- |
| `by` | String or List | Determines which column(s) to sort by. |
| `ascending` | Boolean or List | True (Low to High), False (High to Low). Can differ per column in a list. |
| `na_position` | first' or 'last' | Where to place missing values (NaN). |


# Example script


```python

"""
PROJECT: Basic Data Manipulations in Pandas
DATASET: Palmer Penguins

OBJECTIVE:
1. Add calculated columns
2. Delete columns using different methods
3. Understand inplace vs reassignment
4. Sort data

NOTE:
This script is structured for teaching with detailed explanations.
"""

# ==========================================================
# STEP 0: IMPORT LIBRARIES AND LOAD DATASET
# ==========================================================

print("\nSTEP 0: IMPORT LIBRARIES AND LOAD DATASET")

import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')

print("\nInitial Data Overview:")
print(df.head())  # Display the first 5 rows to understand the structure and columns of the dataset.
print("Data types:\n", df.dtypes)  # Show the data types of each column to identify any potential issues for calculations or sorting.
print("Shape:", df.shape)  # Show the number of rows and columns in the dataset to understand its size and dimensionality.


# ==========================================================
# PHASE 1: DATA PREPARATION
# ==========================================================

print("\nPHASE 1: DATA PREPARATION")

# ----------------------------------------------------------
# STEP 1.1: Handling Missing Values (Basic Strategy)
# ----------------------------------------------------------
print("\nSTEP 1.1: Handling Missing Values")

# NOTE:
# Filling all missing values with 0 is simple but NOT always ideal.
# It is done here only to avoid division errors in teaching context.

df = df.fillna(0)  # This replaces all NaN values in the DataFrame with 0.
print("Missing values handled using fillna(0)")

# Better practice (not used here for simplicity):
# df['bill_length_mm'].fillna(df['bill_length_mm'].mean())


# ==========================================================
# PHASE 2: ADDING CALCULATED COLUMNS
# ==========================================================

print("\nPHASE 2: ADDING CALCULATED COLUMNS")

# ----------------------------------------------------------
# STEP 2.1: Create Slenderness Index
# ----------------------------------------------------------
print("\nSTEP 2.1: Creating 'slenderness_index'")

# Formula:
# slenderness_index = bill_length_mm / bill_depth_mm
# This new column will give us an idea of how slender the penguin's bill is.
# Potential issue: If 'bill_depth_mm' is 0 (after fillna), this will result in division by zero, 
# which will produce inf values in 'slenderness_index'.
df['slenderness_index'] = df['bill_length_mm'] / df['bill_depth_mm']

# In a real dataset, we would want to handle this more carefully 
# (e.g., by filling missing values with mean or median instead of 0, or 
# by adding a small constant to the denominator to avoid division by zero).
# If bill_depth_mm = 0 → division by zero → inf values

# ERROR EXAMPLE: Creating a new column based on non-existing columns will raise a KeyError.
# df['new_col'] = df['unknown_column'] * 2 
# This will raise an error because 'unknown_column' does not exist in the DataFrame. 

print("\nNew column preview:")
print(df[['bill_length_mm', 'bill_depth_mm', 'slenderness_index']].head())  
# Shows the original bill_length_mm and bill_depth_mm along with the new slenderness_index for the first 5 rows.


# ==========================================================
# PHASE 3: DELETING COLUMNS
# ==========================================================

print("\nPHASE 3: DELETING COLUMNS")

# ----------------------------------------------------------
# STEP 3.1: Using drop() with Reassignment
# ----------------------------------------------------------
print("\nSTEP 3.1: Using drop() with reassignment")

cols_to_remove = ['sex']  # We will only remove 'sex' here, leaving 'island' for the next step.

# drop() returns a new DataFrame with the specified columns removed, so we need to assign it back to a variable.
df_reassigned = df.drop(columns=cols_to_remove)

print(f"Does Original df have column for 'sex'?->: {'sex' in df.columns}") # True, because we haven't modified the original df yet.
print(f"Does df_reassigned have column for 'sex'?->: {'sex' in df_reassigned.columns}") # False, because we dropped 'sex' in df_reassigned. 


# ----------------------------------------------------------
# STEP 3.2: Using del (In-place Deletion)
# ----------------------------------------------------------
print("\nSTEP 3.2: Using del")

# 'del' permanently modifies the DataFrame
del df_reassigned['island']  # This will remove the 'island' column from df_reassigned permanently.

print(f"Has column 'island' been removed using del? -> {'island' not in df_reassigned.columns}")  # True, because 'island' has been deleted from df_reassigned.

# ERROR EXAMPLE: Using del on a non-existing column will raise a KeyError.
# del df['non_existing_column']


# ----------------------------------------------------------
# STEP 3.3: Using drop() with inplace=True
# ----------------------------------------------------------
print("\nSTEP 3.3: Using drop() with inplace=True")
# inplace=True modifies the DataFrame directly, so we don't need to assign it back to df_reassigned.
df_reassigned.drop(columns=['species'], inplace=True)

print(f"Has column 'species' been removed using inplace? -> {'species' not in df_reassigned.columns}")  # True, because 'species' has been deleted from df_reassigned.

# ERROR EXAMPLE: Using drop() without assignment or inplace=True will have no effect.
# df.drop(columns=['col'])  # No assignment → no effect


# ==========================================================
# PHASE 4: SORTING DATA
# ==========================================================

print("\nPHASE 4: SORTING DATA")

# NOTE:
# Sorting is performed on original df to preserve all columns


# ----------------------------------------------------------
# STEP 4.1: Single Column Sorting
# ----------------------------------------------------------
print("\nSTEP 4.1: Sorting by single column")

# Sort by body mass (descending)
df_heaviest = df.sort_values(by='body_mass_g', ascending=False)

print("\nTop 3 heaviest penguins:")
# This will show the top 3 rows of the DataFrame sorted by body mass in descending order, 
# which corresponds to the 3 heaviest penguins.
print(df_heaviest[['species', 'body_mass_g']].head(3))


# ----------------------------------------------------------
# STEP 4.2: Multi-Column Sorting
# ----------------------------------------------------------
print("\nSTEP 4.2: Sorting by multiple columns")

# Sort by species (ascending) and then by body mass (descending)
# This will sort the DataFrame first by 'species' in alphabetical order, and then within each species, 
# it will sort by 'body_mass_g' from heaviest to lightest. 
sort_criteria = ['species', 'body_mass_g']  # 
ascending_rules = [True, False]  # True for species (A-Z), False for body mass (heaviest to lightest)

df_sorted_complex = df.sort_values(by=sort_criteria, ascending=ascending_rules)

# Filter Adelie penguins
# After sorting, we filter the DataFrame to only include rows where the 'species' column is 'Adelie'.
adelies = df_sorted_complex[df_sorted_complex['species'] == 'Adelie']

print("\nLast 3 Adelie penguins (sorted by mass):")
# This will show the last 3 rows of the filtered DataFrame, which corresponds to the 
# 3 lightest Adelie penguins due to the sorting order because we had earlier sorted by body mass in descending order.
# So lightest Adelie penguins will be at the end of the Adelie group in the sorted DataFrame.
print(adelies[['species', 'body_mass_g', 'island']].tail(3))

# ERROR EXAMPLE: Sorting by a non-existing column will raise a KeyError.
# df.sort_values(by='non_existing_column')


# ==========================================================
# STEP 5: SUMMARY
# ==========================================================

print("\nSTEP 5: SUMMARY")

print("""
KEY LEARNINGS:

1. New columns can be derived using arithmetic operations
2. Columns can be deleted using drop() or del
3. inplace=True modifies the DataFrame directly
4. Sorting helps organize and analyze data efficiently

BEST PRACTICE:

- Prefer reassignment over inplace for clarity
- Always check column names before operations
- Handle missing values thoughtfully (avoid blind fillna(0))
""")


```





