



## Why Do We Need Violin Plots?

### The Problem with Box Plots

> **A box plot summarizes data using five numbers** (minimum, Q1, median, Q3, maximum), but it **hides the shape** of the distribution.

### Real Question A Beginner Asks:

>"I have a box plot. Can I tell if my data has one peak or two peaks?"                                                   Answer: NO! The box plot hides this information completely.     
Solution: Use a violin plot!   

### What Each Plot Type Reveals
| **Plot Type** | **Shows** | **Hides** |
| --- | --- | --- |
| **Histogram** | Exact frequencies, detailed shape | Takes more space, harder to compare multiple groups |
| **Box Plot** | Median, quartiles, outliers | Distribution shape, peaks, clusters |
| **Violin Plot** | Shape + summary statistics | Exact frequencies, individual data points |


## What Is a Violin Plot?

### Simple Definition

> A **violin plot** combines a **box plot** with a **density curve**. It shows both the statistical summary AND the shape of the data distribution.

### Why Is It Called a "Violin" Plot?

The graph often looks like a musical violin:

```python
     Wide section = Many data points here
         /\
        /  \
       /    \    ← Mirror image of density curve
       \    /
        \  /
         \/
     Narrow section = Few data points here
```

### Concept Box: Understanding Width

 - Width Does NOT Mean Value!  Common Mistake:  To think wider = larger value  
 - Correct Understanding: Wider = MORE observations at that value
 - Narrower = FEWER observations        
 - Think of it like a crowd: 
   - Wide area = crowded (many people).
   - Narrow area = empty (few people)

### Component Breakdown

| Component | What It Shows | Visual Appearance |
| --- | --- | --- |
| **Density curve** | Shape of distribution | Mirrored violin shape (blue) |
| **Median** | Centre value | Thick red line inside violin |
| **Mean** | Average value | Green triangle marker |
| **Q1 and Q3** | Quartiles (25th and 75th percentile) | Horizontal lines marking box edges |
| **Width** | Number of observations | Wider = more data points |


### From Histogram to Violin Plot: The Transformation

### Step-by-Step Process
![From Histogram to Violin Plot](/resources/ch15-matplotlib-violin-steps-in-making.png)



### What Happens at Each Step?


| Step | Action | Result |
| --- | --- | --- |
| 1 | Collect data | List of numbers (e.g., exam scores) |
| 2 | Create histogram | Bars show how many values in each range |
| 3 | Smooth the bars | Continuous curve replaces stepped bars |
| 4 | Mirror the curve | Flip curve horizontally to create symmetry |
| 5 | Add statistics | Overlay median, quartiles, mean |
| 6 | Final violin | Combines shape + summary in one view |


### Comparison: Histogram vs. Box Plot vs. Violin Plot

### Feature Comparison Table

| Feature | Histogram | Box Plot | Violin Plot |
| --- | --- | --- | --- |
| Shows frequencies | Yes (exact counts) | No | Indirectly (via width) |
| Shows median | No | Yes | Yes |
| Shows quartiles | No | Yes | Yes |
| Shows outliers | Difficult | Yes (clear) | Sometimes |
| Shows distribution shape | Yes (detailed) | No | Yes (smoothed) |
| Shows multiple peaks | Yes | No | Yes |
| Space required | More | Very little | Moderate |
| Compare multiple groups | Harder | Easy | Easy |
| Best for | Exploring one dataset | Quick summary | Shape + summary together |


### When Each Plot Shines
Choose Based on Your Goal:

 - Use HISTOGRAM when you need:  
   - Exact frequency counts To see every    detail of shape . 
   - To understand bin boundaries  
 - Use BOX PLOT when you need: 
   - Quick statistical summary 
   - To compare many groups
   - To identify outliers clearly Space-efficient display  
 - Use VIOLIN PLOT when you need:
   - Distribution shape + summary 
   - To detect multiple peaks 
   - To see skewness clearly Better than box plot but more compact than histogram

       


### Typical Violin Plot Shapes

### 1. Symmetric Distribution (Bell-Shaped)

**Characteristics:**

-   Widest in the middle
-   Narrow at both ends
-   Mirror image on top and bottom
-   Median in centre

**What It Means:** Data is evenly distributed around the centre (like a normal distribution).

### 2. Right-Skewed Distribution

**Characteristics:**

-   Wide at the bottom (lower values)
-   Long narrow tail at the top (higher values)
-   Median shifted toward bottom

**What It Means:** Most values are low, but a few very high values exist.

### 3. Left-Skewed Distribution

**Characteristics:**

-   Wide at the top (higher values)
-   Long narrow tail at the bottom (lower values)
-   Median shifted toward top

**What It Means:** Most values are high, but a few very low values exist.

### 4. Bimodal Distribution (Two Peaks) ⭐

**Characteristics:**

-   Two wide sections separated by a narrow section
-   Looks like two violins stacked

**What It Means:** Data has **two distinct groups or clusters**.

> **Critical Insight**: A box plot would completely hide the bimodal shape! This is the **"aha!" moment** for violin plots.

----------

## Basic Violin Plot Script

### What This Script Does

> Creates a simple violin plot showing exam scores with mean, median, and extreme values marked.

## Script

```python
# Step 1: Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 2: LAYER 1 - Prepare the DATA
# Set random seed for reproducible results
np.random.seed(10)

# Generate bell-shaped exam scores
# loc=70 means average score is 70
# scale=10 means standard deviation is 10
# size=100 means 100 students
scores = np.random.normal(loc=70, scale=10, size=100)

# Add a few unusual values (outliers)
scores = np.append(scores, [25, 30, 105])

# Step 3: Create figure and axis
fig, ax = plt.subplots(figsize=(7, 4))

# Step 4: LAYER 2 - Create violin plot with OPTIONS
ax.violinplot(
    scores,              # The data to plot
    showmeans=True,      # Show mean as green triangle. Green triangle is default marker for mean in violin plot
    showmedians=True,    # Show median as red line. Red line is default marker for median in violin plot
    showextrema=True     # Show minimum and maximum
)

# Step 5: LAYER 3 - Add CHART ELEMENTS
ax.set_title("Violin Plot of Exam Scores")
ax.set_ylabel("Marks")
ax.set_xlabel("Distribution")
# Add grid for better readability. 
# True means show grid, alpha=0.3 makes it lighter, axis='y' means only horizontal grid lines
ax.grid(True, alpha=0.3, axis='y')

# Step 6: Display the plot
plt.show()

```

### Output of the script

![Plot generated by above script](/resources/ch15-matplotlib-violin1.png)







