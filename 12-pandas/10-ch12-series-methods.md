








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







