



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







