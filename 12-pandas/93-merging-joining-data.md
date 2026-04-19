



# Merging and Joining Data

## Research Topic: Integrating Disparate Research Logs

**Research Question:** _How can one integrate fragmented datasets collected from different research teams using concatenation and database-style merging operations?_
## Project Scenario:
The Palmer Penguin data is split into two separate Excel files saved by different research assistants:

1.  **`df_measurements`:** Contains physical dimensions (bill, flipper, mass) and a unique `penguin_id`.
2.  **`df_tags`:** Contains categorical data (species, island, sex) and the same `penguin_id`.

Due to a data entry error, the `df_tags` file is missing the last few penguins recorded in `df_measurements`. The goal is to:

1.  Concatenate new observations vertically.
2.  Merge the two tables using the `penguin_id`.
3.  Compare **Inner Join** (clean intersection) vs **Left Join** (preserving all measurements).

### Task: Simulate the split datasets, perform concatenation, and apply different types of merges (Inner, Left, Outer) to reconstruct the master dataset and analyze the impact on data retention.



## 1. Conceptual Deep Dive
<details>

<summary> Conceptual Deep Dive </summary>

Data integration is handled primarily by two functions: `pd.concat()` and `pd.merge()`.

### 2. `pd.concat()` — Detailed Explanation

----------

#### 2.1 Purpose

> Combine multiple DataFrames **along rows or columns**

----------

#### 2.2 Signature

```python
pd.concat(  
  objs,  
  axis=0,  
  join='outer',  
  ignore_index=False,  
  keys=None,  
  levels=None,  
  names=None,  
  verify_integrity=False,  
  sort=False,  
  copy=True  
)
```
----------

#### 2.3 Key Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| objs | List of DataFrames | [df1, df2] |
| axis | 0 = rows, 1 = columns | axis=0 |
| join | outer' (default), 'inner' | Column alignment |
| ignore_index | Reset index | TRUE |
| keys | Add hierarchical index | keys=['A','B'] |
| verify_integrity | Check duplicate index | TRUE |
| sort | Sort columns | FALSE |

#### 2.4 Output Behavior

| Axis | Output |
| --- | --- |
| axis=0 | More rows |
| axis=1 | More columns |
| Mismatch columns | NaN values introduced |


#### Example to understand `.concat`

<details>
<summary> Example 1 (Click to expand)</summary>

#### Example code
```python
import  pandas  as  pd  
  
# Create two simple DataFrames  
df1  =  pd.DataFrame({  
'A': [1, 2],  
'B': [3, 4]  
})  
  
df2  =  pd.DataFrame({  
'A': [5, 6],  
'B': [7, 8]  
})  
  
# Concatenate them  
df_concat  =  pd.concat([df1, df2], axis=0, ignore_index=True)  
  
print(df_concat)

```
#### Output

```python
   A  B
0  1  3
1  2  4
2  5  7
3  6  8
```
#### Step-by-Step Explanation of What Happened

#### **Step 1: Input DataFrames**

**df1**
```
 A  B  
0  1  3  
1  2  4
```

**df2**
```
 A  B  
0  5  7  
1  6  8
```
----------

#### Step 2: Column Alignment

-   Pandas checks column names in both DataFrames
-   Both have same columns → `A`, `B`  
 >No mismatch, so no `NaN` values introduced

----------

#### Step 3: Row-wise Stacking (axis=0)

-   `axis=0` means **stack rows vertically**
-   df2 is placed **below** df1

Intermediate idea:

df1  
----  
```
1 3  
2 4  
```
df2  
----  
```
5 7  
6 8
```

Combined:
```
1 3  
2 4  
5 7  
6 8
```
----------

### **Step 4: Index Handling (ignore_index=True)**

-   Old indices (0,1 and 0,1) are **removed**
-   New index is created:

0  
1  
2  
3

>**Clean, continuous indexing**

----------

#### Step 5: Final Output Created

-   A **new DataFrame** is returned
-   Original `df1` and `df2` remain unchanged

Final result:
```
 A  B  
0  1  3  
1  2  4  
2  5  7  
3  6  8
```


</details>

<details>
<summary> Example 2 </summary>

#### What If Columns Differ? (Mini Example)
```python
df1  =  pd.DataFrame({'A': [1, 2]})  
df2  =  pd.DataFrame({'B': [3, 4]})  
pd.concat([df1, df2], ignore_index=True)
```
### Output:
```
 A    B  
0  1.0  NaN  
1  2.0  NaN  
2  NaN  3.0  
3  NaN  4.0
```
>Missing columns are automatically filled with `NaN`

----------

#### Key Learning

-   First: **See the result**
-   Then: Understand:
    1.  Columns aligned
    2.  Rows stacked
    3.  Index reset

**In one sentence:**

> `pd.concat(..., axis=0)` means “append rows”, and `ignore_index=True` means “renumber them cleanly.”



</details>




#### Typical use case

| Use Case | Description |
| --- | --- |
| Append new data | Add rows |
| Combine datasets | Stack similar tables |
| Side-by-side analysis | axis=1 |

#### Dos and Donts
**Dos**
| Do | Why |
| --- | --- |
| Use ignore_index=True | Clean index |
| Ensure column consistency | Avoid NaN explosion |
| Use list of DataFrames | Required input |


**Donts**
| Don’t | Why |
| --- | --- |
| Pass non-iterable | Raises error |
| Ignore column mismatch | Leads to NaN |
| Confuse with merge | No key logic here |

#### Common Errors

##### Error 1: Wrong Input

`pd.concat(df1, df2) # TypeError`

`pd.concat([df1, df2])  # Correct`

----------

#### Error 2: Duplicate Index

`pd.concat([df1, df2], verify_integrity=True)  # ValueError if index duplicates exist`

----------

----------

### 3. `pd.merge()` — Detailed Explanation

----------

#### 3.1 Purpose

> Combine DataFrames using **common keys (like database joins)**

----------

#### 3.2 Signature

```python
pd.merge(  
  left,  
  right,  
  how='inner',  
  on=None,  
  left_on=None,  
  right_on=None,  
  left_index=False,  
  right_index=False,  
  sort=False,  
  suffixes=('_x', '_y'),  
  copy=True,  
  indicator=False,  
  validate=None  
)
```
----------

#### 3.3 Key Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| left, right | DataFrames | df1, df2 |
| how | join type | inner', 'left' |
| on | common column | id' |
| left_on/right_on | different column names | id', 'user_id' |
| left_index/right_index | join on index | TRUE |
| suffixes | handle duplicate column names | ('_x','_y') |
| indicator | shows merge source | TRUE |
| validate | check join type | 1:1' |

#### 3.4 Join Types (Very Important)

| Join | Description | Result |
| --- | --- | --- |
| Inner | Common keys only | Intersection |
| Left | All left keys | Left preserved |
| Right | All right keys | Right preserved |
| Outer | All keys | Union |

#### 3.5 Output Behavior

| Case | Result |
| --- | --- |
| Missing match | NaN |
| Duplicate keys | Row multiplication |
| Same column names | Suffix added |

#### 3.8 Typical Use Cases
| Use Case | Description |
| --- | --- |
| Combine datasets | Based on ID |
| Data enrichment | Add columns |
| Database-style joins | SQL-like operations |

#### 3.9 Dos and Don’ts

##### DOs

| Do | Why |
| --- | --- |
| Ensure key columns exist | Avoid KeyError |
| Use validate | Prevent duplication errors |
| Check duplicates in keys | Avoid explosion |

##### Donts

| Don’t | Why |
| --- | --- |
| Merge without keys | Wrong results |
| Ignore duplicates | Row explosion |
| Forget suffixes | Column confusion |

#### 3.10 Common Errors

----------

####  Error 1: Missing Key

`pd.merge(df1, df2, on='id')  # KeyError if 'id' not present`

----------

#### Error 2: Cartesian Explosion

`pd.merge(df1, df2, left_index=True, right_index=True)  # If index not meaningful → huge dataset`

----------

#### Error 3: Duplicate Columns

Without suffix: columns  overlap  but  no  suffix  specified

----------

----------

#### 4. `concat()` vs `merge()` — Detailed Comparison

| Feature | concat() | merge() |
| --- | --- | --- |
| Logic | Axis-based | Key-based |
| Similar to | Append | SQL JOIN |
| Requires keys | No | Yes |
| Output shape | Add rows/columns | Depends on join |
| Missing data | Possible | Controlled |
| Use case | Stack data | Relational combine |


#### 5. Output Behavior Comparison

| Scenario | concat | merge |
| --- | --- | --- |
| New rows | OK | Not OK |
| New columns | OK | OK |
| Key matching | Not OK | OK |
| NaN creation | Yes | Yes |
| Row multiplication | No | Yes (if duplicates) |


#### 6. Visual Summary

| Operation | Input | Output |
| --- | --- | --- |
| concat(axis=0) | df1 + df2 | More rows |
| concat(axis=1) | df1 + df2 | More columns |
| merge(inner) | df1 + df2 | Common rows |
| merge(left) | df1 + df2 | All left rows |


#### 7. Best Practices Summary

| Topic | Recommendation |
| --- | --- |
| concat | Use for stacking |
| merge | Use for relational joins |
| keys | Always verify |
| duplicates | Check before merge |
| debugging | Use indicator=True |

</details>


## Script
<details>
<summary> Script whichclearly explains merging and joining of tables (Left, Right, Inner, Outer) (Click to expand) </summary>

```python

"""
PROJECT: Merging and Joining Data in Pandas
DATASET: Palmer Penguins

OBJECTIVE:
1. Understand LEFT vs RIGHT tables in merge()
2. Simulate real-world data loss
3. Perform INNER and LEFT joins
4. Analyze impact of row mismatch

KEY IDEA:
pd.merge(LEFT, RIGHT, ...) → FIRST argument is ALWAYS LEFT table
"""

# ==========================================================
# STEP 0: LOAD DATA AND CREATE UNIQUE ID
# ==========================================================

print("\nSTEP 0: LOAD DATA")

import pandas as pd
import seaborn as sns

# Create unique key for merging
# We reset the index to create a new column called 'index' which will serve as a unique identifier for each row.
df_original = sns.load_dataset('penguins').reset_index()
# We rename the 'index' column to 'penguin_id' to make it clear that this column will be used as a unique identifier for each penguin in our dataset.
df_original = df_original.rename(columns={'index': 'penguin_id'})

print("Original Shape:", df_original.shape)
# OUTPUT HINT: (344, 8). Rows = 344, Columns = 8 (including new 'penguin_id')


# ==========================================================
# STEP 1: CREATE LEFT AND RIGHT TABLES
# ==========================================================

print("\nSTEP 1: DEFINE LEFT AND RIGHT TABLES")

# ----------------------------------------------------------
# STEP 1.1: LEFT TABLE (Main Dataset → MUST BE PRESERVED)
# ----------------------------------------------------------
# LEFT TABLE = df_measurements
# Reason:
# - Contains critical numeric data
# - We do NOT want to lose this data


# We are selecting only the columns related to measurements and the unique identifier 'penguin_id' to create 
# a separate DataFrame that focuses on the physical characteristics of the penguins.
# This is the left table because it contains the main data we want to preserve. 
# We will perform merges using this table as the base, ensuring that all rows from this table are 
# retained in the final merged result, even if there are missing matches in the right table.
df_measurements = df_original[
    ['penguin_id', 'bill_length_mm', 'bill_depth_mm',
    'flipper_length_mm', 'body_mass_g']
]

print("\nLEFT TABLE (df_measurements)")
print("Shape:", df_measurements.shape)
# OUTPUT HINT: (344, 5)


# ----------------------------------------------------------
# STEP 1.2: RIGHT TABLE (Secondary Dataset → MAY HAVE LOSS)
# ----------------------------------------------------------
# RIGHT TABLE = df_tags
# We simulate data loss HERE (not in LEFT)
# Reason:
# - Contains categorical data (tags)
# The resulting DataFrame will contain only the categorical attributes along with the 'penguin_id'. 
# We will simulate data loss by dropping the last 5 rows, which means that the tags for the last 5 penguins 
# will be missing. This will allow us to demonstrate the effects of different types of merges 
# (inner vs left) in the next steps, as we will see how the missing tag data affects the results of the merges. 
# By having a separate tags table with some missing data, we can illustrate the importance of choosing the 
# right merge strategy based on the completeness of your data and the specific analysis you want to perform.   

df_tags = df_original[
    ['penguin_id', 'species', 'island', 'sex']
].iloc[:-5]   # ❗ Remove last 5 rows

print("\nRIGHT TABLE (df_tags) - AFTER DATA LOSS")
print("Shape:", df_tags.shape)
# OUTPUT HINT: (339, 4). Columns reduced from 8 to 4, and rows reduced from 344 to 339 due to simulated data loss.


# ----------------------------------------------------------
# WHY REDUCE RIGHT AND NOT LEFT?
# ----------------------------------------------------------
"""
IMPORTANT TEACHING POINT:

We intentionally reduced rows in RIGHT table because:

1. LEFT table = MAIN data → should NOT lose rows
2. RIGHT table = SUPPORTING data → may be incomplete

Real-world analogy:
- LEFT = Bank transaction records (critical). Loss here is catastrophic.
- RIGHT = Customer details (may be missing). Loss here is common and can be handled.

If we removed rows from LEFT:
- We would simulate "loss of main data"
- That is less common and less useful for teaching LEFT JOIN

So:
Reduce RIGHT → simulate missing auxiliary data
Do NOT reduce LEFT → preserve core dataset
"""


# ==========================================================
# STEP 2: UNDERSTAND LEFT vs RIGHT IN MERGE
# ==========================================================

print("\nSTEP 2: UNDERSTANDING MERGE STRUCTURE")

"""
GENERAL FORM:

pd.merge(LEFT, RIGHT, on='key', how='type')

IMPORTANT:
- FIRST argument = LEFT table
- SECOND argument = RIGHT table
"""


# ==========================================================
# STEP 3: INNER JOIN. KEEPS ONLY MATCHING ROWS
# ==========================================================

print("\nSTEP 3: INNER JOIN")

# Perform inner merge
# This will keep only rows where 'penguin_id' exists in BOTH tables.
# Inner join simulates a scenario where we only want to analyze penguins for which we have both 
# measurements and tags.
# Inner join is useful when we want to focus on a subset of data that has complete information across both datasets,
# but it can lead to loss of crucial data if one of the tables has missing rows.
# Inner join should not be used if we want to preserve all rows from the main dataset (LEFT), 
# especially when the right dataset has missing data.

df_inner = pd.merge(
    df_measurements,   # ← LEFT TABLE
    df_tags,           # ← RIGHT TABLE
    on='penguin_id',
    how='inner'
)

print("Inner Join Shape:", df_inner.shape)
# OUTPUT HINT: (339, 8). The inner join keeps only the 339 rows where 'penguin_id' exists in both tables.

"""
EXPLANATION:

- Keeps ONLY matching keys
- Since RIGHT is missing 5 rows:
- → Those 5 rows are DROPPED

RESULT:
LEFT (344) ∩ RIGHT (339) = 339 rows
"""


# ==========================================================
# STEP 4: LEFT JOIN. PRESERVES LEFT, FILLS MISSING RIGHT WITH NaN
# ==========================================================

print("\nSTEP 4: LEFT JOIN")

df_left = pd.merge(
    df_measurements,   # ← LEFT TABLE (preserved)
    df_tags,           # ← RIGHT TABLE
    on='penguin_id',
    how='left'
)

print("Left Join Shape:", df_left.shape)
# OUTPUT HINT: (344, 8). The left join preserves all 344 rows from the LEFT table, filling missing RIGHT data with NaN.

print("\nRows with missing RIGHT data:")
print(df_left[df_left['species'].isna()])

"""
EXPLANATION:

- ALL rows from LEFT are preserved (344 rows)
- Missing matches in RIGHT → filled with NaN

So:
LEFT (344) + missing RIGHT → still 344 rows

Last 5 rows:
→ species, island, sex = NaN
"""


# ==========================================================
# STEP 5: WHAT IF LEFT > RIGHT OR LEFT < RIGHT?
# ==========================================================

print("\nSTEP 5: UNDERSTANDING ROW MISMATCH CASES")

"""
CASE 1: LEFT > RIGHT  (Current Scenario)

LEFT = 344 rows
RIGHT = 339 rows

INNER JOIN → 339 rows. Only rows with matching penguin_id in both tables are kept, 
so we lose the 5 rows that are missing in the RIGHT table.

LEFT JOIN  → 344 rows (NaN added). All rows from the LEFT table are preserved, and the 
5 rows that do not have a match in the RIGHT table will have NaN values for the columns from the RIGHT table.

----------------------------------------

CASE 2: LEFT < RIGHT (Reverse Scenario)

If RIGHT had MORE rows than LEFT:

Example:
LEFT = 300
RIGHT = 350

INNER JOIN:
→ Only common keys (≤ 300)

LEFT JOIN:
→ Still 300 rows (LEFT preserved)

RIGHT JOIN:
→ 350 rows (RIGHT preserved)

OUTER JOIN:
→ All keys from both → up to 350+

----------------------------------------

KEY RULE:

JOIN TYPE decides which table is preserved:

INNER → Intersection
LEFT  → Preserve LEFT
RIGHT → Preserve RIGHT
OUTER → Preserve BOTH
"""


# ==========================================================
# STEP 6: VISUAL SUMMARY
# ==========================================================

print("\nSTEP 6: FINAL SUMMARY")

print("""
LEFT TABLE  = df_measurements (MAIN DATA)
RIGHT TABLE = df_tags (SUPPORTING DATA)

MERGE RULE:
pd.merge(LEFT, RIGHT, ...)

JOIN BEHAVIOR:

INNER → Only matching rows
LEFT  → All LEFT rows + matching RIGHT
RIGHT → All RIGHT rows + matching LEFT
OUTER → All rows from both

BEST PRACTICE:

- Put IMPORTANT dataset on LEFT
- Use LEFT JOIN to avoid losing critical data
- Always check shape after merge
""")


```



</details>


