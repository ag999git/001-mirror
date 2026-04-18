




# Data Cleaning: Structural Changes

## Research Topic: The Penguin Data Standardization Protocol

**Research Question:** _How can one transform a raw, unstructured dataset into a clean, analysis-ready format using Pandas structural manipulation methods?_

**Project Scenario:** Imagine the Palmer Penguin dataset has been collected by three different research assistants. As a result, the dataset contains:

1.  Inconsistent column naming conventions.
2.  Numeric data stored as text strings.
3.  Accidental duplicate entries.
4.  A messy default index (0, 1, 2...) instead of a unique identifier for each penguin.

**Task:** Download the Palmer Penguins dataset via Seaborn and write a Python script to perform the following structural changes to prepare the data for analysis.

----------

## 1. Concepts

Before proceeding to the solution, it is essential to understand the mechanics of structural cleaning.

### A. Renaming Columns and Indices (`.rename()`)

The `.rename()` method allows for the alteration of axis labels. It accepts a dictionary (mapper) where keys are the old names and values are the new names.

  

  

| Parameter | Description | Usage |
| --- | --- | --- |
| mapper | Dictionary or function to rename labels. | `{'old_name': 'new_name'}` |
| index | Alternative to mapper for index labels. | `index={0: 'first_row'}` |
| columns | Alternative to mapper for column labels. | `columns={'A': 'Alpha'}` |
| inplace | Modifies the DataFrame directly if True. | `inplace=True` |


### B. Changing Data Types (`.astype()`)

Data type casting is crucial for memory optimization and mathematical operations.
  

| Target Type | Conversion Function | Use Case |
| --- | --- | --- |
| Numeric | astype('float64') / astype('int64') | Converting text numbers ("12.5") to actual numbers. |
| Categorical | astype('category') | Columns with low cardinality (few unique values). |
| String | astype('str') | Standardizing text formats. |


```python
# Example of an error when casting non-numeric strings to integers
# df['bill_length_mm'].astype(int) 
# This raises ValueError because of 'NaN' values, which cannot be int.
# Solution: Use 'float64' or fill NaNs first.
```
### C. Handling Duplicates (`.duplicated()` & `.drop_duplicates()`)

Duplicate data can skew statistical results. Pandas identifies duplicates based on row content.

  

| Method | Option | Description |
| --- | --- | --- |
| .duplicated() | `keep='first' (Default)` | Marks the first occurrence as False (unique) and subsequent ones as True (duplicate). |
|  | `keep='last'` | Marks the last occurrence as False. |
|  | `keep=False` | Marks all duplicates as True. |
| .drop_duplicates() | `subset=[...]` | Only consider specific columns to identify duplicates. |

### D. Resetting and Setting Index (`.set_index()` & `.reset_index()`)

The index is the "address" of a row.

  

| Operation | Method | Effect |
| --- | --- | --- |
| Set Index | df.set_index('col_name') | Moves a column into the index. Replaces the default numeric range. |
| Reset Index | df.reset_index() | Moves the current index back to a column. Restores default range (0, 1, 2...). |



# Script 

```python
# IMPORT LIBRARIES AND LOAD DATASET
print("\n STEP 0. IMPORT LIBRARIES AND LOAD DATASET")
import pandas as pd
import seaborn as sns

# Load the clean dataset first
df_raw = sns.load_dataset('penguins')
# Get column names and data types
print("=== ORIGINAL DATA ===")
print("Original dataset df_raw columns:->", df_raw.columns)  # Index(['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex'], dtype='object') 
print("Original dataset df_raw dtypes:->", df_raw.dtypes)  # 
print("Original dataset df_raw head:->", df_raw.head())

# PHASE 1: CREATING MESSY DATA BY DELIBERATE MANIPULATION
# We will simulate common data issues such as 
# (1) inconsistent column names, 
# (2) incorrect data types, and 
# (3) duplicates.

# 1(1). Create inconsistent column names (Simulate bad data entry)
df_raw.columns = ['Species', 'Island', 'BLmm', 'BDmm', 'FLmm', 'BMg', 'Sex']

# 1(2). Convert numerical columns to strings (Simulate data import error)
# 'BLmm' (bill_length_mm) is currently numeric. We will convert it to string to simulate a data import error.
df_raw['BLmm'] = df_raw['BLmm'].astype(str)

# 1(3). Create duplicates by appending the first 5 rows to the end
# We use pd.concat to concatenate the original DataFrame with a subset of itself (the first 5 rows).
# df_raw.head(5) gives us the first 5 rows, and we concatenate it to the original DataFrame df_raw.
# ignore_index=True resets the index in the resulting DataFrame to be sequential.
df_messy = pd.concat([df_raw, df_raw.head(5)], ignore_index=True)

print("=== INITIAL MESSY DATA ===")
print("Messy dataset df_messy head:->", df_messy.head(7))  # Shows the first 7 rows, which includes the original first 5 rows and then the duplicates starting from row 344 to 348.   
print(f"Messy dataset df_messy shape:-> {df_messy.shape} (Contains 5 duplicates)") # The original dataset had 344 rows, and we added 5 duplicates, so now we have 349 rows.    
print(f"Messy dataset df_messy Data Types:\n{df_messy.dtypes}")


# PHASE 2: STRUCTURAL CLEANING

# STEP 2(1): RENAMING COLUMNS
print("\n STEP 2(1): RENAMING COLUMNS ================")
# We want to rename the columns back to their original descriptive names.
# We use a dictionary to map the bad names to descriptive names.
# 'inplace=True' saves the change to the variable immediately.
# The rename_map dictionary is a mapping of the messy column names to the clean, descriptive names we want to use.
rename_map = {  
    'Species': 'species',
    'Island': 'island',
    'BLmm': 'bill_length_mm',
    'BDmm': 'bill_depth_mm',
    'FLmm': 'flipper_length_mm',
    'BMg': 'body_mass_g',
    'Sex': 'sex'
}

df_messy.rename(columns=rename_map, inplace=True)

# ERROR EXAMPLE (Commented out):
# If we try to rename a column that doesn't exist, Pandas ignores it.
# df_messy.rename(columns={'ghost_col': 'real_col'}, inplace=True)
# This would run silently with no result unless errors='raise' is used.

print("\n=== AFTER RENAMING COLUMNS BACK TO ORIGINAL ===")
print("After renaming columns of df_messy back to original:->\n", df_messy.columns)


# STEP 2(2): CHANGING DATA TYPES BACK TO NUMERIC
print("\n STEP 2(2): CHANGING DATA TYPES ================")
# 'bill_length_mm' is currently string (object) due to our simulation.
# We must convert it back to float to perform math.
df_messy['bill_length_mm'] = df_messy['bill_length_mm'].astype(float)

# Convert 'sex' and 'island' to 'category' to optimize memory
# Column 'sex' was originally an object (string) type, but since it has a limited number of unique values 
# (Male, Female), converting it to 'category' reduces memory usage.
df_messy['sex'] = df_messy['sex'].astype('category')
# Column 'island' was also originally an object type, and since it has a limited number of unique values 
# (Torgersen, Biscoe, Dream), converting it to 'category' also optimizes memory usage.
df_messy['island'] = df_messy['island'].astype('category')

print("\n=== AFTER TYPE CONVERSION ===")
print("After type conversion: df_messy dtypes:->\n", df_messy.dtypes)


# STEP 2(3): REMOVING DUPLICATES
print("\n STEP 2(3): REMOVING DUPLICATES ================")
# First, identify which rows are duplicates.
# We use keep=False to see ALL rows involved in duplication.
# keep=False marks all duplicates as True, including the first occurrence. 
# This allows us to see all rows that are duplicated in the dataset.   
duplicates_mask = df_messy.duplicated(keep=False)

print("\n=== DUPLICATE ROWS (keep=False) ===")
# This prints the original rows AND their duplicates
print("df_messy duplicate rows before dropping duplicates:->\n", df_messy[duplicates_mask])

# Now, remove the duplicates.
# By default, keep='first', which keeps the first occurrence and removes subsequent ones.
# But since we added duplicates at the end, we can safely use keep='first' to remove the duplicates we added.
df_clean = df_messy.drop_duplicates(keep='first')

print("\n=== AFTER DROPPING DUPLICATES ===")
print(f"df_clean shape after dropping duplicates:-> {df_clean.shape} (Duplicates removed)")
print("df_clean head:->\n", df_clean.head())

# STEP 2(4): SETTING AND RESETTING INDEX
print("\n STEP 2(4): SETTING AND RESETTING INDEX ================")
# We will create a new unique identifier for each penguin and set it as the index.
# Create a unique 'penguin_id' column based on the current row index
# This will create a new column 'penguin_id' with values like 'ID_0', 'ID_1', ..., 
# 'ID_n' where n is the number of rows in df_clean minus one.
df_clean['penguin_id'] = ['ID_' + str(i) for i in range(len(df_clean))]

# SET INDEX: Use 'penguin_id' as the row label
df_final = df_clean.set_index('penguin_id')

print("\n=== AFTER SETTING INDEX ===")
print("df_final head after setting index:->", df_final.head())

# RESET INDEX: Move 'penguin_id' back to a regular column
# df_reset = df_final.reset_index() 
# print("df_reset head:->", df_reset.head())


```





