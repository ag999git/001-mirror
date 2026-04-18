




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









