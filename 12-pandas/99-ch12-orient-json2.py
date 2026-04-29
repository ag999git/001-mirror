




# Project: Understanding JSON Orientations in Pandas

## Learning Objectives

After completing this exercise, you will be able to:

1.  Understand how Pandas stores data in different JSON formats
2.  Compare various `orient` options (`records`, `columns`, `index`, `split`)
3.  Convert DataFrame → JSON → DataFrame correctly
4.  Interpret raw JSON structures
5.  Understand that **data representation ≠ data content**

----------

## Concept Overview

A Pandas DataFrame is a **tabular structure**, but JSON is **flexible**.

 Therefore, the same data can be stored in multiple JSON formats.

> The `orient` parameter controls _how_ the DataFrame is converted into JSON.

## Comparison of JSON Orientations


## STEP 1: LOAD DATA FROM CSV

### Code Snippet

```python
df  =  pd.read_csv(url)  
print(df.head())
```
### What happens

-   `pd.read_csv()` reads a CSV file from a URL
-   Converts it into a **DataFrame (tabular structure)**

### Output Structure (Tabular)

```python
total_bill   tip   sex     smoker  
16.99        1.01  Female  No  
10.34        1.66  Male    No
```
### 🔹 Concept

This is **flat (2D) data**

-   Rows = observations
-   Columns = variables

----------

## STEP 2: SAVE INTO DIFFERENT JSON FORMATS

### Code Snippet

```python
df.to_json("tips_records.json", orient="records")  
df.to_json("tips_columns.json", orient="columns")  
df.to_json("tips_index.json", orient="index")  
df.to_json("tips_split.json", orient="split")
```


### What happens

-   `to_json()` converts DataFrame → JSON
-   `orient` controls **structure of JSON**

### Concept

>Same data → **4 different storage structures**

----------

## STEP 3: READ JSON (records)

###  Code Snippet

```python
df_records  =  pd.read_json("tips_records.json", orient="records")
```

### What happens

-   `read_json()` reconstructs DataFrame
-   Uses `orient='records'`

### Output

Same as original table

### Concept

>Pandas understands **row-wise JSON**

----------

## STEP 4: RAW JSON (records)

### Code Snippet

```python
data_records  =  json.load(f)  
print(data_records[:2])
```

### Actual JSON Structure

```python
[  
 {"total_bill": 16.99, "tip": 1.01, "sex": "Female"},  
 {"total_bill": 10.34, "tip": 1.66, "sex": "Male"}  
]
```

### Concept

>This **is nested JSON (Level 2 nesting)**

Structure:

-   List → rows
-   Each element → dictionary

Hierarchy:

```python
list  
 ├── dict (row1)  
 ├── dict (row2)
```
----------

## STEP 5: READ JSON (columns)

### Code Snippet

```python
df_columns  =  pd.read_json("tips_columns.json", orient="columns")
```

### Concept

>Pandas reconstructs from **column-wise storage**

----------

## STEP 6: RAW JSON (columns)

### Structure

```python
{  
 "total_bill": {"0": 16.99, "1": 10.34},  
 "tip": {"0": 1.01, "1": 1.66}  
}
```

#### Concept

>Nested JSON (Level 2)

Hierarchy:

```python
dict (columns)  
 ├── dict (row index → value)
```

>Column → Row → Value

----------

## STEP 7: READ JSON (index)

### Code Snippet

```python
df_index  =  pd.read_json("tips_index.json", orient="index")

```
### Concept

>Rebuild DataFrame from row-based dictionary

----------

## STEP 8: RAW JSON (index)

### Structure

```python
{  
 "0": {"total_bill": 16.99, "tip": 1.01},  
 "1": {"total_bill": 10.34, "tip": 1.66}  
}
```

### Concept

>Nested JSON (Level 2)

Hierarchy:
```python
dict (rows)  
 ├── dict (columns)
```
>Row → Column → Value

----------

## STEP 9: READ JSON (split)

### Code Snippet

```python
df_split  =  pd.read_json("tips_split.json", orient="split")
```
#### Concept

>Uses metadata + data separation

----------

## STEP 10: RAW JSON (split)

### Structure

```python
{  
 "columns": ["total_bill", "tip"],  
 "index": [0, 1],  
 "data": [[16.99, 1.01], [10.34, 1.66]]  
}
```

### Concept

>Semi-nested structure

Hierarchy:

```python
dict  
 ├── list (columns)  
 ├── list (index)  
 ├── list of lists (data)
```
----------

## STEP 11: VERIFY EQUALITY

### Code Snippet

```python
df_records.equals(df_columns)
```

### Output

```python
True  
True  
True
```
### Concept

>Different formats → **same data**

----------

## STEP 12: ABOUT NESTED JSON

Note that in this data set of tips, we **did see nested JSON**, but only **simple nesting (2 levels)**
To see nested JSON, a nested JSON structure has been created as follows:-
```python
nested_json  = [  
 {  
  "name": "Alice",  
  "grades": {"math": 90, "english": 85}  
 },  
 {  
  "name": "Bob",  
  "grades": {"math": 80, "english": 75}  
 }  
]  
  
df_nested  =  pd.json_normalize(nested_json)  
print(df_nested)
```
### Output

```python
name   grades.math   grades.english  
Alice       90              85  
Bob         80              75
```


















