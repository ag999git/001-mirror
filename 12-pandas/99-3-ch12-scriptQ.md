



Part 1: Questions Based on Chapter Topics
### 1. How does the "Vectorized" nature of Pandas operations differ from standard Python loops, and why does this distinction significantly impact performance when processing large datasets?
Write a Python script that demonstrates the difference in execution time between iterating through a Pandas Series with a for loop to multiply values by 2, versus using the vectorized multiplication operator (*). Use the time module to measure the duration of both operations on a Series with at least 1 million elements.

```python

import pandas as pd
import numpy as np
import time

# Create a large Series with 1 million random numbers
data = pd.Series(np.random.randint(1, 100, size=1_000_000))

# --- Method 1: Standard Python Loop ---
# We convert to a list first because looping directly through 
# a Pandas Series is even slower!
start_time = time.time()
result_list = []
for value in data:
    result_list.append(value * 2)
result_loop = pd.Series(result_list)
loop_duration = time.time() - start_time

# --- Method 2: Pandas Vectorized Operation ---
start_time = time.time()
result_vectorized = data * 2
vectorized_duration = time.time() - start_time

# Results display
print(f"Loop Duration: {loop_duration:.4f} seconds")
print(f"Vectorized Duration: {vectorized_duration:.4f} seconds")
print(f"Vectorized is {loop_duration / vectorized_duration:.1f}x faster")

# Verify results are identical (using np.array_equal to ignore index issues)
assert np.array_equal(result_loop.values, result_vectorized.values), "Results differ!"
print("Verification Success: Both methods produced the same values!")
```

**Output**


```python
Loop Duration: 1.6913 seconds
Vectorized Duration: 0.0060 seconds
Vectorized is 282.5x faster
Verification Success: Both methods produced the same values!

```

**EXPLANATION**

This script compares two ways of multiplying 1 million numbers by 2. First, it creates a large Pandas Series using random integers. In Method 1, a standard Python loop processes each value one by one, which is slow for large datasets. In Method 2, a vectorized operation (data * 2) is used, where Pandas applies the operation to all values at once using optimized internal code, making it much faster. The script measures and prints the time taken by both methods and shows how many times faster the vectorized approach is. Finally, it verifies that both methods produce identical results. The key takeaway is that vectorized operations in Pandas are significantly more efficient than Python loops for data processing.

### 2. What is the fundamental structural difference between a Pandas Series and a DataFrame, and how does the concept of "heterogeneous data" apply specifically to DataFrames but not typically to NumPy arrays?
Write a script that creates a NumPy array containing only integers (homogeneous), a Pandas Series containing mixed types (integers and strings), and a Pandas DataFrame containing multiple columns of different types (integers, floats, and strings). Print the dtype of each object to demonstrate this difference.

```python

import pandas as pd
import numpy as np

# 1. NumPy Array (Homogeneous - Integers only)
np_array = np.array([10, 20, 30, 40])
print(f"NumPy Array dtype: {np_array.dtype}") # Output: int32 or int64

# 2. Pandas Series (Can hold mixed types, but usually homogeneous per Series)
# Note: A single Series typically holds one type, but object dtype can hold anything
s_mixed = pd.Series([10, "Hello", 30, "World"])
print(f"Series dtype (mixed): {s_mixed.dtype}") # Output: object

# 3. Pandas DataFrame (Heterogeneous - Different types per column)
df_data = {
    'ID': [1, 2, 3],           # Integers
    'Price': [10.5, 20.5, 30.5], # Floats
    'Name': ['Apple', 'Banana', 'Cherry'] # Strings
}
df = pd.DataFrame(df_data)
print("\nDataFrame Dtypes:")
print(df.dtypes)
# Output: ID(int64), Price(float64), Name(object)
```
**OUTPUT**

```python
NumPy Array dtype: int64
Series dtype (mixed): object

DataFrame Dtypes:
ID         int64
Price    float64
Name      object
dtype: object

```
**EXPLANATION**
A Pandas Series is a one-dimensional structure (like a single column), while a DataFrame is a two-dimensional structure (like a full table with rows and columns). The key structural difference is that a DataFrame is essentially a collection of Series, where each column is its own Series.

Now, regarding heterogeneous data:

A NumPy array is designed to be homogeneous, meaning all elements must be of the same data type (e.g., all integers or all floats). This makes NumPy very fast but less flexible.
A Pandas Series can hold mixed types, but when it does, it converts everything into a common type (usually object), which reduces efficiency. So, in practice, a Series is usually kept homogeneous.
A Pandas DataFrame, however, is inherently heterogeneous. Each column can have a different data type (e.g., integers, floats, strings), because each column is a separate Series. This makes DataFrames ideal for real-world datasets where different kinds of data coexist.

In the script:

The NumPy array contains only integers, so its dtype is int64 (or similar), showing homogeneity.
The Series contains both integers and strings, so Pandas assigns it a single dtype object, meaning it can hold mixed Python objects.
The DataFrame has three columns (ID, Price, Name), each with a different dtype (int64, float64, object), clearly demonstrating heterogeneity across columns.

The key takeaway is:

NumPy enforces uniform data types, a Series usually behaves like a single typed column, but a DataFrame allows different data types across its columns, making it suitable for structured, real-world data.

### 3. Explain the difference between creating a Pandas Series using a "Dictionary Approach" versus a "List Approach" regarding index assignment, and demonstrate how the dictionary keys automatically become the index labels.
Write a script that creates two Series containing the same data values (100, 200, 300). The first Series should be created from a list (resulting in a default numeric index), and the second Series should be created from a dictionary mapping specific labels ('Q1', 'Q2', 'Q3') to those values. Print both Series to visualize the index difference.

```python

import pandas as pd

# Common data values
values = [100, 200, 300]

# --- Approach 1: List Approach (Default Index) ---
# When using a list, Pandas assigns a default RangeIndex (0, 1, 2...)
s_list = pd.Series(values)
print("Series from List (Default Index):")
print(s_list)

# --- Approach 2: Dictionary Approach (Custom Index) ---
# When using a dictionary, the keys become the Index
data_dict = {'Q1': 100, 'Q2': 200, 'Q3': 300}
s_dict = pd.Series(data_dict)
print("\nSeries from Dictionary (Custom Index):")
print(s_dict)

# Verification
print("\nIndex of List Series:", s_list.index.tolist())
print("Index of Dict Series:", s_dict.index.tolist())
```
**OUTPUT**

```python
Series from List (Default Index):
0    100
1    200
2    300
dtype: int64

Series from Dictionary (Custom Index):
Q1    100
Q2    200
Q3    300
dtype: int64

Index of List Series: [0, 1, 2]
Index of Dict Series: ['Q1', 'Q2', 'Q3']

```
**EXPLANATION**

The key difference between the List Approach and the Dictionary Approach when creating a Pandas Series lies in how the index (labels) is assigned.

When you create a Series from a list, Pandas has only the values and no labels. So it automatically assigns a default numeric index starting from 0 (called a RangeIndex). This means the data is accessed using positions like 0, 1, 2.

In contrast, when you create a Series from a dictionary, each value is already associated with a key. Pandas uses these dictionary keys as index labels. So instead of numeric positions, the Series is labeled with meaningful names like 'Q1', 'Q2', 'Q3'. This makes the data easier to understand and access, especially in real-world datasets.

In the given script:

The list-based Series (s_list) displays values with default indices [0, 1, 2].
The dictionary-based Series (s_dict) uses 'Q1', 'Q2', 'Q3' as index labels, showing how keys automatically become the index.
The final print statements confirm this difference by explicitly displaying the index values of both Series.

The important takeaway is:

A list provides only data → Pandas creates a default index.
A dictionary provides both labels and data → Pandas uses the keys as the index automatically.

This is why the dictionary approach is often preferred when you want labeled, meaningful data representation.

### 4. How does the inplace=True parameter alter the behavior of DataFrame manipulation methods, and why is it crucial to understand whether a new object is created or the existing one is modified?
Write a script that creates a DataFrame, drops a column using inplace=False (saving to a new variable), and drops another column using inplace=True (modifying the original). Print the id() of the DataFrames before and after operations to prove if the object identity has changed.

```python

import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}
df = pd.DataFrame(data)

print(f"Original ID: {id(df)}") # Original object ID

# --- Operation 1: inplace=False (Default) ---
# This creates a NEW DataFrame and does NOT modify 'df'
df_new = df.drop(columns=['A'], inplace=False)
print(f"ID after drop with inplace=False: {id(df)}") # ID remains the same
print(f"ID of new variable 'df_new': {id(df_new)}")   # New object created

# --- Operation 2: inplace=True ---
# This modifies 'df' directly and returns None
df.drop(columns=['B'], inplace=True)
print(f"\nID after drop with inplace=True: {id(df)}") 
print("Current df columns:", df.columns.tolist())
```
**OUTPUT**


```python
Original ID: 1716517650384
ID after drop with inplace=False: 1716517650384
ID of new variable 'df_new': 1716823647680

ID after drop with inplace=True: 1716517650384
Current df columns: ['A', 'C']

```
**EXPLANATION**

The parameter inplace=True determines whether a DataFrame operation modifies the original object or creates a new one.

With inplace=False (default), the operation returns a new DataFrame and leaves the original unchanged. In the script, df_new = df.drop(columns=['A']) creates a new object. This is confirmed by id(df_new) being different from id(df), while the original df still has all its columns.
With inplace=True, the operation modifies the same DataFrame in memory and returns None. In the script, df.drop(columns=['B'], inplace=True) removes column 'B' directly from df. The id(df) remains the same, proving no new object was created.

Understanding this is important because:

It helps avoid mistakes (e.g., forgetting to assign the result when inplace=False)
It clarifies whether memory is reused or a new object is created

Key idea:
inplace=False → new object (different id)
inplace=True → same object modified (same id)


### 5. When reading a CSV file using pd.read_csv, how does the header parameter interact with the names parameter, and what happens if header=None is used without providing custom names?
Write a script that creates a temporary CSV string in memory (using io.StringIO) containing data with no header row. Read this CSV once with header=None (which generates default integer column names) and once with header=None combined with the names parameter (which assigns your custom labels). Print the columns of both resulting DataFrames.

```python

import pandas as pd
import io

# Simulate a CSV file with NO header row (just raw data)
csv_content = """10,20,30
40,50,60"""

# --- Case 1: header=None without names ---
# Pandas infers that there is no header, so it creates default int names (0, 1, 2...)
df_default = pd.read_csv(io.StringIO(csv_content), header=None)
print("Columns with header=None (Default Integers):")
print(df_default.columns.tolist())

# --- Case 2: header=None with custom names ---
# We tell Pandas there is no header (don't skip row 0), but HERE are the names
custom_names = ['Col_A', 'Col_B', 'Col_C']
df_custom = pd.read_csv(io.StringIO(csv_content), header=None, names=custom_names)
print("\nColumns with header=None AND names parameter:")
print(df_custom.columns.tolist())
```

**OUTPUT**

```python
Columns with header=None (Default Integers):
[0, 1, 2]

Columns with header=None AND names parameter:
['Col_A', 'Col_B', 'Col_C']

```

**EXPLANATION**

When using `pd.read_csv()`, the **`header`** and **`names`** parameters control how column labels are assigned.

-   **`header`** tells Pandas **which row (if any) contains column names**.
-   **`names`** allows you to **manually assign column names**.

----------

#### Case 1: `header=None` (no names provided)

```
df_default = pd.read_csv(io.StringIO(csv_content), header=None)
```

-   Pandas is told: **“There is NO header row in the file.”**
-   So it treats **all rows as data**
-   Since no column names are given, Pandas assigns **default integer labels**:

```
[0, 1, 2]
```

Meaning: columns are named by position (0, 1, 2)

----------

#### Case 2: `header=None` with `names`

```
df_custom = pd.read_csv(io.StringIO(csv_content), header=None, names=custom_names)
```

-   Pandas is still told: **“There is NO header row.”**
-   But now you **explicitly provide column names**
-   These names replace the default integer labels:

```
['Col_A', 'Col_B', 'Col_C']
```

First row remains data, not header

----------

#### Important Concept

What if you **don’t use `header=None` but provide `names`?**

-   Then Pandas assumes the first row is a header and may **override or skip it**, which can lead to confusion.

----------

#### Key Takeaways

-   `header=None` → no header in file → all rows are data
-   No `names` → Pandas creates default column names `[0, 1, 2]`
-   With `names` → your labels are used as column names

----------

#### One-line summary

> `header=None` tells Pandas “no column names in file,” and `names` lets you supply your own—otherwise default numeric labels are assigned.


### 6. In the context of the pd.read_json() function, explain how the orient='records' parameter structures the input JSON data compared to orient='columns', and write a script that converts a DataFrame to both formats to illustrate the structural difference.
Write a script that loads the 'tips' dataset (using Seaborn), converts it to a JSON string with orient='records' (a list of objects), and then converts the same DataFrame to a JSON string with `orient='columns' (a dictionary of columns). Print the first 100 characters of both JSON strings to show the structural difference.

```python

import pandas as pd
import seaborn as sns

# Load the dataset
df = sns.load_dataset('tips')

# --- Export 1: orient='records' ---
# List of Dictionaries: [{col1: val, col2: val}, {col1: val, col2: val}]
json_records = df.to_json(orient='records')

# --- Export 2: orient='columns' ---
# Dictionary of Lists: {col1: [val, val], col2: [val, val]}
json_columns = df.to_json(orient='columns')

print("--- orient='records' Structure (List of Objects) ---")
print(json_records[:100] + "...")

print("\n--- orient='columns' Structure (Dict of Lists) ---")
print(json_columns[:100] + "...")
```

**OUTPUT**

```python
--- orient='records' Structure (List of Objects) ---
[{"total_bill":16.99,"tip":1.01,"sex":"Female","smoker":"No","day":"Sun","time":"Dinner","size":2},{...

--- orient='columns' Structure (Dict of Lists) ---
{"total_bill":{"0":16.99,"1":10.34,"2":21.01,"3":23.68,"4":24.59,"5":25.29,"6":8.77,"7":26.88,"8":15...

```

**EXPLANATION**

The `orient` parameter in `pd.read_json()` / `to_json()` defines **how tabular data is structured inside JSON**. The same DataFrame can be represented in very different ways depending on this setting.

----------

#### `orient='records'` (Row-wise structure)

-   Data is stored as a **list of dictionaries**
-   Each dictionary represents **one row**
-   Keys = column names, Values = row values

```
[  {"total_bill":16.99, "tip":1.01, "sex":"Female", ...},  {"total_bill":10.34, "tip":1.66, "sex":"Male", ...}]
```

Think: **Row-wise (record by record)**  

Common in APIs and web data exchange

----------

#### `orient='columns'` (Column-wise structure)

-   Data is stored as a **dictionary of columns**
-   Each column is a key
-   Values are **nested dictionaries of index:value pairs**

```
{  "total_bill": {"0":16.99, "1":10.34, ...},  "tip": {"0":1.01, "1":1.66, ...}}
```

Think: **Column-wise (column by column)**  

Preserves index information explicitly

----------

#### What the script shows

-   `json_records[:100]` begins with:
    
    ```
    [{"total_bill":16.99,"tip":1.01,"sex":"Female",...}
    ```
    
    Clearly a **list `[ ... ]` of row objects**
    
-   `json_columns[:100]` begins with:
    
    ```
    {"total_bill":{"0":16.99,"1":10.34,...}
    ```
    
    Clearly a **dictionary `{ ... }` of columns**




### 7. How does the .loc[] indexer differ from .iloc[] when accessing data in a DataFrame, particularly when the DataFrame index has been customized to non-integer labels?
Write a script that creates a DataFrame with a custom string index (e.g., fruit names). Demonstrate selecting a row using .loc[] with the string label and .iloc[] with the integer position. Explain via comments which method is safer if the row order changes but labels stay the same.

```python

import pandas as pd

# Create a DataFrame with a Custom String Index
data = {'Quantity': [10, 20, 15], 'Price': [1.5, 0.5, 2.0]}
df = pd.DataFrame(data, index=['Apple', 'Banana', 'Cherry'])

print("Original DataFrame:")
print(df)

# --- Selection 1: .loc[] (Label-based) ---
# Safe if labels are unique, even if rows are reordered
print("\nSelecting 'Banana' using .loc['Banana']:")
print(df.loc['Banana'])

# --- Selection 2: .iloc[] (Integer Position-based) ---
# Safe if you know the physical position, but risky if rows move
print("\nSelecting second row using .iloc[1]:")
print(df.iloc[1])

# Note: If we sort the DataFrame, .iloc[1] might point to a different fruit!
# .loc['Banana'] will always point to Banana data regardless of sorting.
```
**OUTPUT**

```python
Original DataFrame:
        Quantity  Price
Apple         10    1.5
Banana        20    0.5
Cherry        15    2.0

Selecting 'Banana' using .loc['Banana']:
Quantity    20.0
Price        0.5
Name: Banana, dtype: float64

Selecting second row using .iloc[1]:
Quantity    20.0
Price        0.5
Name: Banana, dtype: float64

```


### 8. What is the "Split-Apply-Combine" philosophy behind the groupby() operation in Pandas, and how does the .agg() function facilitate the "Apply" step for multiple statistics simultaneously?
Write a script using the 'tips' dataset that groups the data by the 'day' column. Use the .agg() method to calculate the mean of 'total_bill' and the sum of 'tip' in a single step, rather than calculating them separately. Print the resulting summary DataFrame.

```python

import pandas as pd
import seaborn as sns

# Load dataset
df = sns.load_dataset('tips')

# --- Split-Apply-Combine using groupby and agg ---
# 1. Split: Data is divided into groups (Thur, Fri, Sat, Sun)
# 2. Apply: We calculate Mean(Total Bill) AND Sum(Tip) for each group
# 3. Combine: Results are merged into a new DataFrame
result = df.groupby('day')[['total_bill', 'tip']].agg(
    {
        'total_bill': 'mean',  # Calculate average bill per day
        'tip': 'sum'          # Calculate total tips per day
    }
)

print("Aggregated Statistics per Day:")
print(result)
```
**OUTPUT**

```python
  result = df.groupby('day')[['total_bill', 'tip']].agg(
Aggregated Statistics per Day:
      total_bill     tip
day                     
Thur   17.682742  171.83
Fri    17.151579   51.96
Sat    20.441379  260.40
Sun    21.410000  247.39

```


### 9. How does the .pivot_table() function transform "Long" format data into "Wide" format, and what is the specific role of the index, columns, and values parameters in this transformation?
Write a script that converts the 'flights' dataset (which is in Long format: year, month, passengers) into a Wide format Pivot Table where 'year' is the index, 'month' is the column header, and the sum of 'passengers' is the cell value. This effectively creates a matrix of traffic over time.

```python

import pandas as pd
import seaborn as sns

# Load flights dataset (Long format)
df = sns.load_dataset('flights')

# --- Transform Long to Wide using pivot_table ---
# index: Rows (Years), columns: Columns (Months), values: Data (Passenger Counts)
pivot_df = df.pivot_table(
    index='year', 
    columns='month', 
    values='passengers', 
    aggfunc='sum' # Sum passengers if duplicates exist (though dataset is clean)
)

print("Pivot Table (Wide Format - Years vs Months):")
print(pivot_df.head())
```
**OUTPUT**

```python
  pivot_df = df.pivot_table(
Pivot Table (Wide Format - Years vs Months):
month  Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec
year                                                             
1949   112  118  132  129  121  135  148  148  136  119  104  118
1950   115  126  141  135  125  149  170  170  158  133  114  140
1951   145  150  178  163  172  178  199  199  184  162  146  166
1952   171  180  193  181  183  218  230  242  209  191  172  194
1953   196  196  236  235  229  243  264  272  237  211  180  201

```


### 10. What is the functional difference between using .dropna() to handle missing data versus using .fillna(), and in which scenario would preserving data volume (fillna) be preferred over data quality (dropna)?
Write a script that creates a DataFrame with missing values (NaN) in two columns. Apply .dropna() to the first column to remove rows with gaps, and apply .fillna(0) to the second column to preserve the row count but replace the gap with zero. Compare the shape of the DataFrame before and after operations.

```python

import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4, 5], # Column with gaps
    'B': [10, np.nan, 30, 40, 50]  # Column with gaps
}
df = pd.DataFrame(data)

print(f"Original Shape: {df.shape}")

# --- Handling Strategy 1: dropna() (Data Quality) ---
# Removes rows where 'A' is NaN. Reduces total rows.
df_dropped = df.dropna(subset=['A'])
print(f"\nShape after dropna on 'A': {df_dropped.shape}")

# --- Handling Strategy 2: fillna(0) (Data Volume) ---
# Keeps all rows, but replaces NaN in 'B' with 0. Preserves volume.
df_filled = df.copy()
df_filled['B'] = df_filled['B'].fillna(0)
print(f"Shape after fillna(0) on 'B': {df_filled.shape}")

print("\nResulting DataFrames:")
print(df_dropped)
print(df_filled)
```

**OUTPUT**

```python
Original Shape: (5, 2)

Shape after dropna on 'A': (4, 2)
Shape after fillna(0) on 'B': (5, 2)

Resulting DataFrames:
     A     B
0  1.0  10.0
1  2.0   NaN
3  4.0  40.0
4  5.0  50.0
     A     B
0  1.0  10.0
1  2.0   0.0
2  NaN  30.0
3  4.0  40.0
4  5.0  50.0

```


### 11. How does the .str accessor allow vectorized string manipulations on a Pandas Series, and why is this more efficient than applying a Python function using .apply()?
Write a script that creates a Series of messy email addresses (e.g., "USER@EXAMPLE.COM"). Use the .str accessor methods .lower() and .strip() to clean them. Then, compare this syntax to using .apply() with a lambda function to achieve the same result.

```python

import pandas as pd

# Create a Series of messy email strings
emails = pd.Series(['  ALICE@EXAMPLE.COM  ', '  BOB@TEST.NET  ', '  CHARLIE@DOMAIN.ORG  '])

# --- Method 1: Vectorized String Accessor (.str) ---
# Efficient, optimized C-code execution
clean_emails_str = emails.str.lower().str.strip()

# --- Method 2: Python Apply with Lambda ---
# Slower, due to Python interpreter overhead for every row
clean_emails_apply = emails.apply(lambda x: x.lower().strip())

print("Resulting Clean Emails (Identical):")
print(clean_emails_str)

# Verify they are the same
assert clean_emails_str.equals(clean_emails_apply), "Methods produced different results!"
```

**OUTPUT**

```python
Resulting Clean Emails (Identical):
0     alice@example.com
1          bob@test.net
2    charlie@domain.org
dtype: object

```


### 12. When performing a pd.merge() operation, what distinguishes an "Inner Join" from a "Left Join," and write a script that demonstrates the data retention difference between these two methods?
Write a script that creates two DataFrames: df_orders (Order ID and Date) and df_customers (Order ID and Customer Name). Perform an Inner Join (keep only matching IDs) and a Left Join (keep all orders, even if customer is missing). Print the length of both resulting DataFrames to show the data loss in the Inner Join.

```python

import pandas as pd

# --- Dataset 1: Orders ---
orders = pd.DataFrame({
    'Order_ID': [101, 102, 103, 104],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']
})

# --- Dataset 2: Customers ---
# Note: Order 104 is missing from this dataset
customers = pd.DataFrame({
    'Order_ID': [101, 102, 103],
    'Customer_Name': ['Alice', 'Bob', 'Charlie']
})

# --- Merge 1: Inner Join (Intersection) ---
# Only keeps rows where Order_ID exists in BOTH DataFrames
inner_join = pd.merge(orders, customers, on='Order_ID', how='inner')

# --- Merge 2: Left Join (Preserve Left) ---
# Keeps ALL rows from 'orders', filling missing customer info with NaN
left_join = pd.merge(orders, customers, on='Order_ID', how='left')

print("Inner Join Result (Strict Match):")
print(inner_join)

print("\nLeft Join Result (Preserve Orders):")
print(left_join)

print(f"\nInner Join Count: {len(inner_join)}")
print(f"Left Join Count: {len(left_join)}")
```

**OUTPUT**
```python
Inner Join Result (Strict Match):
   Order_ID        Date Customer_Name
0       101  2023-01-01         Alice
1       102  2023-01-02           Bob
2       103  2023-01-03       Charlie

Left Join Result (Preserve Orders):
   Order_ID        Date Customer_Name
0       101  2023-01-01         Alice
1       102  2023-01-02           Bob
2       103  2023-01-03       Charlie
3       104  2023-01-04           NaN

Inner Join Count: 3
Left Join Count: 4

```



### 13. What is the role of the pd.to_datetime() function when working with the 'flights' dataset, and how does setting a Datetime Index unlock specific time-series slicing capabilities?
Write a script that loads the 'flights' dataset. Create a new column 'Date' by combining the 'year' and 'month' columns using pd.to_datetime(). Set this new 'Date' column as the DataFrame Index. Demonstrate how you can now slice the data using date strings (e.g., '1950') instead of integer positions.

```python
import pandas as pd
import seaborn as sns

# Load dataset
df = sns.load_dataset('flights')

# --- Create a Datetime object ---
# FIX: Explicitly convert 'month' to string to avoid the TypeError.
# The 'year' column is int, so we convert to str. 'month' is category, so we convert to str.
df['Date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str), format='%Y-%b')

# --- Set Datetime as Index ---
# This enables powerful time-series features
df.set_index('Date', inplace=True)

print("DataFrame with Datetime Index:")
print(df.head())

# --- Demonstrate Time-Series Slicing ---
# We can now select data for a whole year using a string slice
print("\nData for the year 1960:")
print(df.loc['1960'])

```

**OUTPUT**

```python
1949-02-01  1949   Feb         118
1949-03-01  1949   Mar         132
1949-04-01  1949   Apr         129
1949-05-01  1949   May         121

Data for the year 1960:
            year month  passengers
Date                              
1960-01-01  1960   Jan         417
1960-02-01  1960   Feb         391
1960-03-01  1960   Mar         419
1960-04-01  1960   Apr         461
1960-05-01  1960   May         472
1960-06-01  1960   Jun         535
1960-07-01  1960   Jul         622
1960-08-01  1960   Aug         606
1960-09-01  1960   Sep         508
1960-10-01  1960   Oct         461
1960-11-01  1960   Nov         390
1960-12-01  1960   Dec         432

```

### 14. How does the .dt accessor differ from the .str accessor in terms of the data types they operate on, and write a script extracting the 'Day of the Week' and 'Month' from a Datetime Index?
Write a script that generates a Datetime Index representing a full week. Use the .dt accessor to extract the name of the day (e.g., 'Monday') and the month number (e.g., 1) into new columns.

```python

import pandas as pd

# Create a Datetime Index for a week
dates = pd.date_range(start='2023-10-01', periods=7, freq='D')
df = pd.DataFrame({'Value': range(7)}, index=dates)
df.index.name = 'Date'

print("Original DataFrame:")
print(df)

# --- Use .dt accessor to extract temporal properties ---
df['Weekday_Name'] = df.index.day_name() # e.g., Monday
df['Month_Number'] = df.index.month      # e.g., 10

print("\nDataFrame with Extracted Temporal Features:")
print(df)
```

**OUTPUT**

```python
Original DataFrame:
            Value
Date             
2023-10-01      0
2023-10-02      1
2023-10-03      2
2023-10-04      3
2023-10-05      4
2023-10-06      5
2023-10-07      6

DataFrame with Extracted Temporal Features:
            Value Weekday_Name  Month_Number
Date                                        
2023-10-01      0       Sunday            10
2023-10-02      1       Monday            10
2023-10-03      2      Tuesday            10
2023-10-04      3    Wednesday            10
2023-10-05      4     Thursday            10
2023-10-06      5       Friday            10
2023-10-07      6     Saturday            10

```

### 15. In the context of read_html(), why does the function return a List of DataFrames rather than a single DataFrame, and how do the match and attrs parameters help in isolating a specific table from a webpage?
Write a script that attempts to read tables from a hypothetical URL (e.g., Wikipedia). Use the match='Population' parameter to filter for a specific table and the attrs={'class': 'wikitable'} parameter to target tables with a specific CSS class. Explain how these parameters filter the list before you even access index [0].

```python

import pandas as pd

# Note: This URL is hypothetical for the structure of the example
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population'

# --- Read HTML with Filtering Parameters ---
# match='Population' : Only return tables containing this string
# attrs={'class': 'wikitable'} : Only return tables with this class
tables = pd.read_html(url, match='Population', attrs={'class': 'wikitable'})

# read_html returns a LIST of DataFrames
print(f"Number of tables found matching criteria: {len(tables)}")

if len(tables) > 0:
    # Access the first (and likely only) table in the filtered list
    df_population = tables[0]
    print("\nFiltered DataFrame:")
    print(df_population.head())
else:
    print("No tables matched the criteria.")

```


### 16. Explain the concept of "Wide" vs "Long" format data, and write a script that uses the .melt() function to convert a "Wide" DataFrame (sales per month across columns) into a "Long" DataFrame (Month and Value columns).
Write a script that creates a "Wide" DataFrame representing sales where columns are 'Jan', 'Feb', 'Mar'. Use pd.melt() to reshape this into a "Long" format with columns 'Month' and 'Sales'.

```python

import pandas as pd

# Create a Wide Format DataFrame (Columns are time periods)
wide_data = {
    'Product': ['A', 'B'],
    'Jan': [100, 200],
    'Feb': [150, 250],
    'Mar': [120, 220]
}
df_wide = pd.DataFrame(wide_data)

print("Original Wide Format:")
print(df_wide)

# --- Convert to Long Format using melt ---
# id_vars: Columns to keep (Product)
# value_vars: Columns to unpivot (Jan, Feb, Mar)
df_long = df_wide.melt(
    id_vars=['Product'], 
    value_vars=['Jan', 'Feb', 'Mar'], 
    var_name='Month', 
    value_name='Sales'
)

print("\nReshaped Long Format:")
print(df_long)
```


**OUTPUT**

```python
Original Wide Format:
  Product  Jan  Feb  Mar
0       A  100  150  120
1       B  200  250  220

Reshaped Long Format:
  Product Month  Sales
0       A   Jan    100
1       B   Jan    200
2       A   Feb    150
3       B   Feb    250
4       A   Mar    120
5       B   Mar    220

```


### 17. What is the dtype_backend='pyarrow' parameter in modern Pandas, and what specific advantages does Apache Arrow offer over the traditional NumPy backend for handling missing data?
Write a script that loads the 'tips' dataset using both the default NumPy backend and the PyArrow backend. Print the dtypes of the 'total_bill' column in both to show how PyArrow uses dedicated nullable types (like double[pyarrow] or int64[pyarrow]) compared to standard NumPy types.

```python

import pandas as pd
import seaborn as sns

# --- Load with Default Backend (NumPy) ---
df_numpy = sns.load_dataset('tips')
print("NumPy Backend Dtypes:")
print(df_numpy.dtypes)

# --- Load with PyArrow Backend ---
# PyArrow uses a standardized type system that handles nulls (NA) consistently
df_arrow = sns.load_dataset('tips').convert_dtypes(dtype_backend='pyarrow')
print("\nPyArrow Backend Dtypes:")
print(df_arrow.dtypes)

# Note: PyArrow types often explicitly state they are nullable/arrow-backed
```

**OUTPUT**
```python
NumPy Backend Dtypes:
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
dtype: object

PyArrow Backend Dtypes:
total_bill    double[pyarrow]
tip           double[pyarrow]
sex                  category
smoker               category
day                  category
time                 category
size           int64[pyarrow]
dtype: object

```



### 18. How does the parse_dates parameter in read_csv automate data cleaning, and what is the risk of relying solely on automatic date parsing without specifying a format?
Write a script that creates a CSV string with dates in a non-standard format (DD-MM-YYYY). Attempt to read it with parse_dates=True (which tries to infer) and explicitly with dayfirst=True to guide the parser. Compare the resulting dtype of the date column.

```python

import pandas as pd
import io

csv_data = """Date,Value
01-01-2023,100
02-01-2023,200"""

# --- Attempt 1: Automatic Inference (Risky) ---
# Might parse incorrectly depending on system locale (YYYY-DD-MM vs DD-MM-YYYY)
df_auto = pd.read_csv(io.StringIO(csv_data), parse_dates=['Date'])
print(f"Inferred Date Type: {df_auto['Date'].dtype}")
print(df_auto.head())

# --- Attempt 2: Explicit Format/Params (Safe) ---
# dayfirst=True ensures consistency if data is DD-MM-YYYY
df_safe = pd.read_csv(io.StringIO(csv_data), parse_dates=['Date'], dayfirst=True)
print(f"\nExplicit Date Type: {df_safe['Date'].dtype}")
print(df_safe.head())
```

**OUTPUT**

```python
Inferred Date Type: datetime64[ns]
        Date  Value
0 2023-01-01    100
1 2023-02-01    200

Explicit Date Type: datetime64[ns]
        Date  Value
0 2023-01-01    100
1 2023-01-02    200

```


### 19. What is the functionality of the .stack() and .unstack() methods in relation to MultiIndex DataFrames, and how do they facilitate switching between analysis and reporting formats?
Write a script that creates a MultiIndex DataFrame (index: Year, columns: Quarter). Use .stack() to pivot it into a Long format Series, and then use .unstack() to convert it back to the Wide format DataFrame.

```python

import pandas as pd

# Create a MultiIndex DataFrame (Wide Format: Years x Quarters)
index = pd.Index([2021, 2022], name='Year')
columns = pd.Index(['Q1', 'Q2', 'Q3', 'Q4'], name='Quarter')
data = [[10, 20, 30, 40], [15, 25, 35, 45]]
df = pd.DataFrame(data, index=index, columns=columns)

print("Original Wide Format (MultiIndex Columns):")
print(df)

# --- Operation 1: stack() ---
# Converts columns (Q1, Q2...) into a new index level. Result is a Series.
stacked_series = df.stack()
print("\nAfter stack() (Long Format Series):")
print(stacked_series.head())

# --- Operation 2: unstack() ---
# Converts the index level created by stack() back into columns.
unstacked_df = stacked_series.unstack()
print("\nAfter unstack() (Back to Wide Format DataFrame):")
print(unstacked_df)
```

**OUTPUT**

```python
Original Wide Format (MultiIndex Columns):
Quarter  Q1  Q2  Q3  Q4
Year                   
2021     10  20  30  40
2022     15  25  35  45

After stack() (Long Format Series):
Year  Quarter
2021  Q1         10
      Q2         20
      Q3         30
      Q4         40
2022  Q1         15
dtype: int64

After unstack() (Back to Wide Format DataFrame):
Quarter  Q1  Q2  Q3  Q4
Year                   
2021     10  20  30  40
2022     15  25  35  45

```


### 20. How does the inplace=True parameter affect memory management and readability in Pandas scripts, and write a script comparing chaining operations without inplace versus sequential operations with inplace?
Write a script that performs a standard cleaning workflow: fill missing values, rename a column, and drop a duplicate. Perform this once using method chaining (no inplace) and once using sequential steps with inplace=True. Assign the final results to new variables and print them to show they are equivalent.

```python
import pandas as pd
import numpy as np

# Setup Dummy Data
data = {'A': [1, np.nan, 3], 'B': [4, 5, 5]}

# --- FIX: Initialize df1 and df2 as DataFrames ---
# Do not use data.copy() on the dictionary. Instead, wrap it in pd.DataFrame()
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data)

# --- Method 1: Method Chaining (Functional Style) ---
# No inplace, returns new object every time
df_chain = (
    df1.fillna(0)
    .rename(columns={'A': 'Alpha'})
    .drop_duplicates()
)

# --- Method 2: Sequential inplace (Procedural Style) ---
# Modifies df2 directly in memory step-by-step
df2.fillna(0, inplace=True)
df2.rename(columns={'A': 'Alpha'}, inplace=True)
df2.drop_duplicates(inplace=True)

print("Chained Result (Functional):")
print(df_chain)

print("\nInplace Result (Procedural):")
print(df2)

# Both produce the same data, but the 'id' of df_chain is different from df2

```

**OUTPUT**

```python
Chained Result (Functional):
   Alpha  B
0    1.0  4
1    0.0  5
2    3.0  5

Inplace Result (Procedural):
   Alpha  B
0    1.0  4
1    0.0  5
2    3.0  5

```



### 21. Explain the purpose of the na_values parameter in read_csv and how it allows standardizing various representations of missing data (e.g., "NA", "NULL", "-1") into the standard Pandas NaN.
Write a script that creates a CSV string where missing values are represented by the string "MISSING" and -9999. Use read_csv with the na_values parameter to ensure both are recognized as NaN upon loading. Verify by checking if the cells contain actual NaN values.

```python

import pandas as pd
import io
import numpy as np

# CSV with non-standard missing values
csv_data = """ID,Value
1,100
2,MISSING
3,-9999
4,200"""

# --- Read with na_values parameter ---
# Treats "MISSING" and -9999 as NaN
df = pd.read_csv(
    io.StringIO(csv_data), 
    na_values=['MISSING', -9999]
)

print("DataFrame with Standardized NaN:")
print(df)

# Check if actual NaN values exist
print("\nCheck for NaN:")
print(df.isna().sum())

```

**OUTPUT**

```python
DataFrame with Standardized NaN:
   ID  Value
0   1  100.0
1   2    NaN
2   3    NaN
3   4  200.0

Check for NaN:
ID       0
Value    2
dtype: int64

```


### 22. What is the significance of the usecols parameter in read_csv for memory efficiency when dealing with wide datasets containing hundreds of columns?
Write a script that generates a wide DataFrame with 50 columns of random numbers. Time the reading of this dataset using read_csv (simulated via String IO) loading all columns, and then loading only 5 specific columns using usecols. Print the memory usage reduction (though simulated via shape) to demonstrate the concept.

```python

import pandas as pd
import io
import numpy as np

# Create a wide CSV with 50 columns (simulated)
# Just to demonstrate the concept of selecting specific columns
wide_csv = ",".join([f"Col{i}" for i in range(50)]) + "\n"
wide_csv += ",".join([str(x) for x in np.random.randint(1, 100, 50)])

# --- Read All Columns (Inefficient for Memory) ---
df_all = pd.read_csv(io.StringIO(wide_csv))
print(f"Read All Columns Shape: {df_all.shape}") # 1 Row, 50 Columns

# --- Read Specific Columns (Memory Efficient) ---
# Only reads necessary data into RAM
df_subset = pd.read_csv(io.StringIO(wide_csv), usecols=['Col0', 'Col1', 'Col2', 'Col3', 'Col4'])
print(f"Read Subset Shape: {df_subset.shape}") # 1 Row, 5 Columns

```

**OUTPUT**

```python
Read All Columns Shape: (1, 50)
Read Subset Shape: (1, 5)

```

### 23. How does the .query() method differ from standard Boolean Indexing in terms of syntax and potential performance benefits when filtering large datasets?
Write a script that creates a DataFrame with sales data. Filter this data to find sales greater than 500 in the 'East' region using both Boolean Indexing (standard df[]) and the .query() method. Print the results of both to verify they are identical.

```python

import pandas as pd

# Setup Data
data = {
    'Region': ['East', 'West', 'East', 'North', 'East'],
    'Sales': [600, 400, 700, 300, 550]
}
df = pd.DataFrame(data)

# --- Method 1: Boolean Indexing ---
mask = (df['Region'] == 'East') & (df['Sales'] > 500)
filtered_bool = df[mask]

# --- Method 2: Query Method ---
# String expression is often more readable and can be faster
filtered_query = df.query("Region == 'East' and Sales > 500")

print("Boolean Indexing Result:")
print(filtered_bool)

print("\nQuery Method Result:")
print(filtered_query)

# Verify equality
assert filtered_bool.equals(filtered_query), "Results do not match!"

```

**OUTPUT**

```python
Boolean Indexing Result:
  Region  Sales
0   East    600
2   East    700
4   East    550

Query Method Result:
  Region  Sales
0   East    600
2   East    700
4   East    550

```


### 24. In the context of Excel I/O, how does the openpyxl engine facilitate writing Pandas DataFrames to .xlsx files, and what are the requirements for reading files with multiple sheets?
Write a script that creates two simple DataFrames. Write both to a single Excel file using pd.ExcelWriter with two different sheet names ('Sheet1', 'Sheet2'). Then, read the file back specifying sheet_name='Sheet2' to verify only that sheet's data is loaded.

```python

import pandas as pd

# Create sample DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'X': [10, 20], 'Y': [30, 40]})

# --- Write to Multi-Sheet Excel ---
# ExcelWriter allows managing multiple sheets in one file object
with pd.ExcelWriter('multi_sheet.xlsx', engine='openpyxl') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)

print("Excel file 'multi_sheet.xlsx' created.")

# --- Read Specific Sheet ---
# You can specify sheet name or index (0 for first, 1 for second)
df_loaded = pd.read_excel('multi_sheet.xlsx', sheet_name='Sheet2')

print("Data loaded from Sheet2:")
print(df_loaded)

```

**OUTPUT**

```python
Excel file 'multi_sheet.xlsx' created.
Data loaded from Sheet2:
    X   Y
0  10  30
1  20  40

```


### 25. How does the .astype('category') data type conversion improve performance and memory usage for columns with low cardinality (few unique values repeated many times), compared to the standard object dtype?
Write a script that creates a DataFrame with a 'Department' column containing only 3 unique values (HR, IT, Sales) repeated 1,000 times. Print the memory usage (using .info()) before and after converting the 'Department' column to category.

```python

import pandas as pd
import numpy as np

# --- Create data with low cardinality (Corrected) ---
# FIX: We need exactly 1000 items for both columns.
# Use np.random.choice to pick random departments for 1000 rows.
dept_list = np.random.choice(['HR', 'IT', 'Sales'], size=1000)

df = pd.DataFrame({
    'Department': dept_list,
    'Employee_ID': range(1000)
})

print("--- Memory Usage Before Conversion (Object dtype) ---")
print(df.info(memory_usage='deep'))

# --- Convert to Category ---
# Dramatically reduces memory by storing integers instead of strings
df['Department'] = df['Department'].astype('category')

print("\n--- Memory Usage After Conversion (Category dtype) ---")
print(df.info(memory_usage='deep'))

```

**OUTPUT**

```python
--- Memory Usage Before Conversion (Object dtype) ---
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 2 columns):
 #   Column       Non-Null Count  Dtype 
---  ------       --------------  ----- 
 0   Department   1000 non-null   object
 1   Employee_ID  1000 non-null   int64 
dtypes: int64(1), object(1)
memory usage: 66.5 KB
None

--- Memory Usage After Conversion (Category dtype) ---
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 2 columns):
 #   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   Department   1000 non-null   category
 1   Employee_ID  1000 non-null   int64   
dtypes: category(1), int64(1)
memory usage: 9.2 KB
None

```

### 26. What is the encoding parameter in read_csv used for, and what common error occurs if the encoding of the file (e.g., 'latin-1') does not match the default system encoding (e.g., 'utf-8')?
Write a script that simulates reading a CSV file containing special characters (like accents) by defining a CSV string with 'latin-1' encoded text (simulated by passing raw bytes or just assuming the file exists). Use read_csv with the correct encoding to successfully read the file, demonstrating the fix for UnicodeDecodeError.

```python

import pandas as pd
import io

# Simulate a CSV with characters that might differ in encoding
# For this example, we just assume the file exists and has these values.
# In a real scenario, passing a path to a file with these chars is standard.
csv_content = "Name,City\nJosé,São Paulo\nFrançois,Zürich"

# --- Attempt 1: Wrong Encoding (Will simulate error context) ---
# If we treat UTF-8 bytes as Latin-1, or vice versa, we get errors.
# df_error = pd.read_csv(io.StringIO(csv_content.encode('latin-1')), encoding='utf-8')

# --- Attempt 2: Correct Encoding ---
# Specifying encoding='latin-1' matches the data source
df_correct = pd.read_csv(io.StringIO(csv_content), encoding='latin-1')

print("Successfully Read with Correct Encoding:")
print(df_correct)

```

**OUTPUT**

```python
Successfully Read with Correct Encoding:
       Name       City
0      José  São Paulo
1  François     Zürich

```


### 27. How does the chunksize parameter in read_csv enable processing of datasets that are larger than the available system RAM (Out-of-Core processing), and what is the typical workflow pattern?
Write a script that defines a generator function reading a large CSV (simulated here with a loop) in chunks of 10 rows. Aggregate the sum of a 'Value' column across all chunks to demonstrate processing data without ever holding the full dataset in memory.

```python

import pandas as pd
import io
import numpy as np

# Simulate a large CSV with 30 rows (representing "large" data)
large_csv = "ID,Value\n" + "\n".join([f"{i},{np.random.randint(10, 100)}" for i in range(30)])

# --- Out-of-Core Processing using Chunksize ---
# Returns an iterator, reading 10 rows at a time
chunk_iterator = pd.read_csv(io.StringIO(large_csv), chunksize=10)

total_sum = 0
chunk_count = 0

for chunk in chunk_iterator:
    # Process each chunk independently
    chunk_sum = chunk['Value'].sum()
    total_sum += chunk_sum
    chunk_count += 1
    print(f"Processed Chunk {chunk_count}: Sum = {chunk_sum}")

print(f"\nTotal Sum of all chunks: {total_sum}")

```

**OUTPUT**

```python
Processed Chunk 1: Sum = 582
Processed Chunk 2: Sum = 387
Processed Chunk 3: Sum = 537

Total Sum of all chunks: 1506

```


### 28. What is the difference between the keep_default_na and na_values parameters in read_csv when customizing missing value detection?
Write a script that creates a CSV containing "NA" (default missing) and "N/A" (custom missing). Read the CSV first with default settings (where only "NA" is detected), and then read it again providing na_values=['N/A']. Compare the count of NaN values in both DataFrames.

```python

import pandas as pd
import io

csv_data = """ID,Score
1,100
2,NA
3,N/A
4,200"""

# --- Read 1: Default Settings ---
# Only detects standard Pandas NA values
df_default = pd.read_csv(io.StringIO(csv_data))
print("Default Detection (NA only):")
print(df_default.isna().sum())

# --- Read 2: Custom na_values ---
# Explicitly adds "N/A" to the list of missing values
df_custom = pd.read_csv(io.StringIO(csv_data), na_values=['N/A'])
print("\nCustom Detection (NA and N/A):")
print(df_custom.isna().sum())

```

**OUTPUT**

```python
Default Detection (NA only):
ID       0
Score    2
dtype: int64

Custom Detection (NA and N/A):
ID       0
Score    2
dtype: int64

```

### 29. How does the converters parameter in read_csv allow for type coercion or custom parsing logic on specific columns during the import process?
Write a script that creates a CSV where a 'Price' column has a currency symbol '
' (e.g., "$50"). Use the `converters` parameter to apply a lambda function that removes the '
' and converts the result to a float during the loading phase itself.

```python

import pandas as pd
import io

csv_data = """Item,Price
Apple,$50
Banana,$20
Cherry,$35"""

# --- Define a Converter Function ---
# Logic: Remove '$' and convert to float
dollar_converter = lambda x: float(x.replace('$', ''))

# --- Apply Converter during Import ---
df = pd.read_csv(
    io.StringIO(csv_data), 
    converters={'Price': dollar_converter}
)

print("DataFrame with Parsed Prices:")
print(df)
print(f"\nPrice dtype: {df['Price'].dtype}")

```
**OUTPUT**

```python
DataFrame with Parsed Prices:
     Item  Price
0   Apple   50.0
1  Banana   20.0
2  Cherry   35.0

Price dtype: float64

```


### 30. What is the purpose of the skiprows parameter in read_csv when dealing with files that have metadata, header descriptions, or footer information before the actual data begins?
Write a script that simulates a CSV file where the first 2 lines are metadata headers (e.g., "Report Generated on...") and the actual data starts on row 3 (index 2). Use skiprows=2 to ignore the metadata and load only the structured data.

```python

import pandas as pd
import io

# Simulate CSV with metadata rows at the top
csv_content = """Annual Sales Report
Generated on 2023-01-01
Product,Sales
Widget,100
Gadget,200"""

# --- Read skipping the first 2 rows (Metadata) ---
df = pd.read_csv(io.StringIO(csv_content), skiprows=2)

print("Data after skipping metadata rows:")
print(df)
```
**OUTPUT**

```python
Data after skipping metadata rows:
  Product  Sales
0  Widget    100
1  Gadget    200

```






