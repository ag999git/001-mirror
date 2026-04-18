


## STEP 0: Import Libraries and Load Dataset

### Purpose

To initialize the environment and bring the dataset into a Pandas DataFrame for further processing.

### Methods Used

### `sns.load_dataset(name)`

`df  =  sns.load_dataset("penguins")`

  

| Aspect | Detail |
| --- | --- |
| Input | Dataset name (string) |
| Output | Pandas DataFrame |
| Limitation | May require internet |

### MethodsAttributes `df.head()`, `df.columns`, `df.dtypes`


  

| Method | Purpose |
| --- | --- |
| `head()` | Preview data |
| `columns` | Column names |
| `dtypes` | Data types |

## PHASE 1: Creating Messy Data (Simulation)

----------

### STEP 1.1: Inconsistent Column Names

#### Why

Real-world data often has **non-standard naming conventions**

#### Method Used

`df.columns = [...]`

  

| Feature | Detail |
| --- | --- |
| Type | Attribute assignment |
| Effect | Directly modifies DataFrame |
| Risk | Overwrites original names |

## STEP 1.2: Incorrect Data Types

### Why

Simulates data import issues (e.g., CSV → strings)

### Method Used

`df['col'].astype(str)`

### `.astype()` Signature

`Series.astype(dtype)`

-    Input → Target data type  
-     Output → Converted Series   
-    Limitation → Fails if incompatible

## STEP 1.3: Creating Duplicates

### Why

Duplicates are common in real datasets

### Method Used

`pd.concat([df1, df2], ignore_index=True)`

| Parameter | Meaning |
| --- | --- |
| `ignore_index=True` | Resets row numbering |

----------

## PHASE 2: Structural Cleaning

----------

## STEP 2.1: Renaming Columns

###  Why

Improves readability and consistency

### Method Used

`df.rename(columns=dict)`

### Signature

`DataFrame.rename(columns=None, index=None)`

-    Input → Dictionary   
-    Output → New DataFrame   
-    Limitation → Silent failure if column missing

----------

##  STEP 2.2: Fixing Data Types

### Why

Correct types are essential for:

-   Computation
-   Memory efficiency

----------

### Methods Used

####  Numeric conversion

`df['col'].astype(float)`

####  Category conversion

`df['col'].astype('category')`

----------

### Comparison: Data Types

| Type | Use Case | Benefit |
| --- | --- | --- |
| float | Numeric | Calculations |
| object | Mixed | Flexible |
| category | Repeated text | Memory efficient |

## STEP 2.3: Handling Duplicates

### Why

Duplicates distort analysis

----------

### Methods Used

####  `.duplicated()`

`df.duplicated(keep=False)`

-    Output → Boolean Series   
-    Use → Identify duplicates 

----------

####  `.drop_duplicates()`

`df.drop_duplicates()`

-    Output → Clean DataFrame   
-    Default → `keep='first'`

----------

### Duplicate Handling Summary

| Method | Purpose |
| --- | --- |
| `duplicated()` | Detect |
| `drop_duplicates()` | Remove |

## STEP 2.4: Index Management

### Why

Index improves:

-   Data access
-   Identification

----------

### Methods Used

####  `.set_index()`

>`df.set_index('column')`

####  `.reset_index()`

>`df.reset_index()`

----------

### Index Comparison

| Operation | Result |
| --- | --- |
| `set_index` | Column → Index |
| `reset_index` | Index → Column |


## STEP 3: Summary

### Purpose

To consolidate learning and reinforce best practices
### Comparison Table

| Operation | Method | Risk | Best Practice |
| --- | --- | --- | --- |
| Rename | `.rename()` | Silent failure | Verify columns |
| Type Conversion | `.astype()` | Conversion error | Check data |
| Duplicates | `.drop_duplicates()` | Data loss | Inspect first |
| Index | `.set_index()` | Confusion | Reset when needed |












