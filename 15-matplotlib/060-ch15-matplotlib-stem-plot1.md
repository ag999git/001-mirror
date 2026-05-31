




# Stem Plots

## Introduction

A **stem plot** displays data using vertical lines (called stems) extending from a baseline to individual data values.

Unlike a line graph, consecutive points are **not connected**. Each observation is shown separately.

Stem plots are useful when:

-   data values are discrete
-   the order of observations is important
-   we wish to emphasize individual values rather than trends

Common applications include:

-   signal processing
-   digital electronics
-   sampled data
-   time-series measurements

----------

## What Does a Stem Plot Look Like?

```
Value

  8 |        ●
  7 |
  6 |    ●
  5 |
  4 |          ●
  3 | ●
  2 |
  1 |
    +----------------
      1  2  3  4
```

Each marker is connected to the baseline by a vertical stem.

----------

## Stem Plot vs Line Plot

| Feature | Line Plot | Stem Plot |
| --- | --- | --- |
| Connects points | Yes | No |
| Shows trend | Excellent | Moderate |
| Shows individual values | Moderate | Excellent |
| Best for continuous data | Yes | No |
| Best for discrete samples | No | Yes |

### Common Parameters

| Parameter | Affects | Result | Useful For | Example |
| --- | --- | --- | --- | --- |
| stem(x,y) | Plot | Creates stem plot | Discrete data | Basic usage |
| linefmt="r-" | Stem lines | Changes stem style | Formatting | Red stems |
| markerfmt="bo" | Markers | Changes marker style | Highlight points | Blue circles |
| basefmt="k-" | Baseline | Changes baseline style | Visibility | Black baseline |

## Simplified Signatures

### State-Based

```python
plt.stem(x, y)
```

### OOP-Based

```python
ax.stem(x, y)
```

## Script

```python

# Stem Plot Example

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6]
y = [3, 7, 4, 8, 5, 6]

# Create figure and subplot
fig, ax = plt.subplots()

# Create stem plot
ax.stem(
    x,
    y,
    linefmt="b-",      # Blue stems
    markerfmt="ro",    # Red circle markers
    basefmt="k-"       # Black baseline
)

# Add title and labels
ax.set_title("Stem Plot Example")
ax.set_xlabel("Sample Number")
ax.set_ylabel("Value")

# Add grid
ax.grid(True)

# Display graph
plt.show()


```

### Output plot (From above script)

# FIGURE


## What This Script Demonstrates

-   creating a stem plot
-   displaying individual observations
-   customizing stems and markers
-   comparing discrete values

----------

## When Should We Use Stem Plots?

Use a stem plot when:

-   observations occur at distinct positions
-   individual values are important
-   data represents sampled measurements
-   connecting points with lines would be misleading

Examples:

-   daily sensor readings
-   digital signals
-   stock price samples
-   laboratory measurements

----------

## Histogram vs Stem Plot vs Line Plot

| Feature | Histogram | Stem Plot | Line Plot |
| --- | --- | --- | --- |
| Shows frequencies | Yes | No | No |
| Shows individual values | No | Yes | Partly |
| Connects observations | No | No | Yes |
| Best for distributions | Yes | No | No |
| Best for sampled data | No | Yes | Yes |


## Key Idea

A stem plot may be viewed as a compromise between a scatter plot and a line plot:

```python
Scatter Plot
      ↓
Stem Plot
      ↓
Line Plot
```

It preserves individual observations while making the magnitude of each value easy to compare.













