



## Methods of Series in Pandas
For easy understanding and usage, I have divided the methods of Series in Pandas into "Pillars" or "macro-groups".
The 4 "pillars" or "macro-groups" are shown in table below:

| Macro-Group | What it means | Merges these old categories |
| --- | --- | --- |
| 1. Inspection & Retrieval | "Show me the data, or give it to me in a different format." | Accessing/Viewing, Conversion/Export |
| 2. Analysis & Summarization | "Give me the big picture. What are the trends and totals?" | Descriptive Statistics, Counts/Unique |
| 3. Cleaning & Manipulation | "Fix the errors, remove the bad rows, and change the values." | Missing Data, Transformation, Filtering, Sorting |
| 4. Type-Specific Operations | "This is text/time, treat it with special tools." | String Operations (.str), DateTime Operations (.dt) |



## These 4 "Pillars" or "Macro-groups" contain a number of categories which are given below
1. Viewing & Accessing
2. Conversion & Export
3. Descriptive Statistics
4. Counts & Unique Values
5. Handling Missing Data
6. Filtering & Conditions
7. Transformation
8. Sorting & Ranking
9. String Methods (.str)
10. DateTime Methods (.dt)


## The Key methods of each category are given below:

| Pillar | Category | Key Methods | Brief Purpose |
| --- | --- | --- | --- |
| 1. Inspection & Retrieval | Viewing & Accessing | .loc[], .iloc[] | Select data by label or integer position. |
|  |  | .head(), .tail() | Preview the first or last n elements. |
|  |  | .get() | Safe access (returns default if label is missing). |
|  | Conversion & Export | .to_list() | Convert Series to a standard Python list. |
|  |  | .to_dict() | Convert Series to a Python dictionary. |
|  |  | .to_frame() | Convert a 1D Series into a 2D DataFrame. |
| 2. Analysis & Summarization | Descriptive Statistics | .sum(), .min(), .max() | Basic arithmetic aggregates. |
|  |  | .mean(), .median(), .std() | Calculate central tendency and spread. |
|  |  | .describe() | Generate a complete summary statistics table. |
|  | Counts & Unique Values | .value_counts() | Count the frequency of each unique value. |
|  |  | .unique(), .nunique() | Get array of unique values or count of them. |
| 3. Cleaning & Manipulation | Handling Missing Data | .isna() (or .isnull()) | Detect missing values (returns boolean mask). |
|  |  | .fillna() | Fill NaN values with a specific value/method. |
|  |  | .dropna() | Remove rows that contain missing values. |
|  | Filtering & Conditions | .between() | Filter values within a specific range. |
|  |  | .isin() | Filter values present in a given list. |
|  |  | .duplicated() | Flag rows that have appeared before. |
|  | Transformation | .map() | Substitute values using a dict or function. |
|  |  | .apply() | Apply a custom function to all elements. |
|  |  | .replace() | Swap out exact values (e.g., replace(1, 100)). |
|  |  | .astype() | Cast the Series to a different data type. |
|  | Sorting & Ranking | .sort_values() | Sort the Series by its actual data values. |
|  |  | .sort_index() | Sort the Series by its index labels. |
|  |  | .rank() | Assign a competitive rank to each value. |
| 4. Type-Specific Operations | String Methods (.str) | .str.upper(), .str.lower() | Convert string case. |
|  |  | .str.contains() | Check if a substring/pattern exists. |
|  |  | .str.replace() | Replace parts of a string. |
|  | DateTime Methods (.dt) | .dt.year, .dt.month | Extract specific date components as integers. |
|  |  | .dt.day_name() | Extract the name of the day (e.g., 'Monday'). |
|  |  | .dt.strftime() | Format dates into custom string formats. |


## Flowchart
The following diagram shows all the key methods grouped into categories and "Pillars"

![Flowchart of Methods of Series](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch12-pandas-series-methods.png)

![Flowchart of Methods of Series](/resources/ch12-pandas-series-methods.png)




