

# Time Series Basics 

## Research Topic: Temporal Analysis of Airline Passenger Traffic

**Research Question:** _How can raw multi-column temporal data be converted into a Datetime Index to facilitate analysis of seasonal fluctuations and long-term growth trends?_

**Project Scenario:** The "Airline Passenger Traffic" dataset (`flights`) provides monthly counts of airline passengers from 1949 to 1960. While the dataset contains time information, it is currently split across two distinct columns: `year` (Integer) and `month` (String). To perform effective time series analysis, one must first engineer a unified datetime object. The objective is to:

1.  **Construct a single Datetime Index** from the separate year and month columns.
2.  **Slice the data** to isolate specific eras (e.g., the 1950s).
3.  **Resample the data** to convert noisy monthly data into smoothed quarterly and yearly averages, allowing for a clearer analysis of long-term trends.

**Task:** Using the Seaborn `flights` dataset, write a Python script to:

1.  Load the data and inspect its structure.
2.  Create a function or logic to combine the `year` and `month` columns into a single `datetime` column.
3.  Set this new column as the DataFrame Index.
4.  Resample the data to calculate the **Quarterly Average** and **Yearly Total** number of passengers.
5.  Print the resampled data to compare the volatility of monthly data versus the trend in yearly data.

----------

## 1. Conceptual Deep Dive

#### The Challenge of Multi-Column Dates

Real-world datasets often split dates. The `flights` dataset has `year: 1949` and `month: 'January'`. Pandas cannot perform time-slicing or resampling until these are merged into a single `datetime64` object representing a specific point in time (e.g., `1949-01-01`).

### Resampling Logic

Resampling is the process of changing the frequency of time-series observations.

-   **Upsampling:** Increasing frequency (e.g., Monthly -> Daily). Requires interpolation.
-   **Downsampling:** Decreasing frequency (e.g., Monthly -> Yearly). Requires aggregation (Sum, Mean, Max).

**Table of Resampling Offsets for Flights Data**

| Alias | Description | Logical Output for Flights |
| --- | --- | --- |
| M' | Month End | Original data (already monthly). |
| Q' | Quarter End | Smoother trend (3-month averages). |
| Y' / 'A' | Year End | Shows total passengers per year (Annual growth). |
| MS' | Month Start | Shifts index to 1st of month (purely for formatting). |






