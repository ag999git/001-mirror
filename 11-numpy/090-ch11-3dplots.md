


# PROJECT: Visualizing Surfaces using NumPy and Matplotlib

----------

## Objective

Understand how:

-   `linspace()` creates values
-   `meshgrid()` creates coordinate grids
-   functions 
$$Z=f(X,Y)$$ 
create surfaces
-   Matplotlib visualizes them

----------

## PART A — Conceptual Study

### Study the following:

1.  What does `np.linspace()` do?
2.  How does `np.meshgrid()` convert 1D arrays into 2D grids?
3.  What does each of these represent:
    -   X → x-coordinates
    -   Y → y-coordinates
    -   Z → height (function output)

----------

### Study these matplotlib functions

| Function | Purpose |
| --- | --- |
| plt.figure() | Create a figure |
| add_subplot(projection='3d') | Enable 3D plotting |
| plot_surface(X, Y, Z) | Plot surface |
| set_xlabel(), set_ylabel(), set_zlabel() | Label axes |
| set_title() | Add title |
| plt.show() | Display plot |


<details>
  <summary> Matplotlib Functions Used (Explained Simply- Click to expand)   </summary>
  
  ## Matplotlib Functions Used (Explained Simply)

----------

### 1. `plt.figure()`

**Role:**  
Creates a new drawing canvas (called a _figure_).

**Purpose:**  
To start a new plot. Without it, plots may overlap or reuse old figures.

**Input parameters (common):**

-   `figsize=(width, height)` → optional size of figure

**Output:**  
Returns a figure object (stored as `fig`)

**Example:**

fig  =  plt.figure()

**Key Idea:**

> Think of this as opening a blank page for drawing.

----------

### 2. `fig.add_subplot(projection='3d')`

**Role:**  
Adds a plotting area (axes) inside the figure.

**Purpose:**  
Enables **3D plotting**.

**Input parameters:**

-   `projection='3d'` → required for 3D plots

**Output:**  
Returns an axes object (stored as `ax`)

**Example:**

ax  =  fig.add_subplot(projection='3d')

**Key Idea:**

> Converts the blank page into a 3D coordinate system.

----------

### 3. `ax.plot_surface(X, Y, Z)`

**Role:**  
Plots a 3D surface.

**Purpose:**  
To visualize a function Z=f(X,Y)Z = f(X,Y)Z=f(X,Y)

**Input parameters:**

-   `X, Y, Z` → NumPy arrays of same shape

**Output:**  
Draws a surface plot on the axes

**Example:**

ax.plot_surface(X, Y, Z)

**Key Idea:**

> Uses grid points (X,Y) and heights (Z) to draw a surface.

----------

### 4. `ax.set_xlabel()`, `set_ylabel()`, `set_zlabel()`

**Role:**  
Labels the axes.

**Purpose:**  
To make plots understandable.

**Input parameters:**

-   A string (label name)

**Output:**  
Updates axis labels

**Example:**

ax.set_xlabel("X")  
ax.set_ylabel("Y")  
ax.set_zlabel("Z")

**Key Idea:**

> Always label axes—otherwise plots are meaningless.

----------

### 5. `ax.set_title()`

**Role:**  
Adds a title to the plot.

**Purpose:**  
To describe what the plot represents.

**Input:**

-   A string

**Output:**  
Displays title above plot

**Example:**

ax.set_title("Z = X + Y")

----------

### 6. `plt.show()`

**Role:**  
Displays the plot window.

**Purpose:**  
To render all figures created

**Input:**  
None

**Output:**  
Shows the final plot

**Example:**

plt.show()

**Key Idea:**

> Without this, plots may not appear.

  

| Function | Role | Input | Output |
| --- | --- | --- | --- |
| figure() | Create canvas | optional size | figure |
| add_subplot() | Create axes | projection | axes |
| plot_surface() | Draw surface | X,Y,Z arrays | 3D plot |
| set_xlabel() etc | Label axes | string | labeled axes |
| set_title() | Add title | string | titled plot |
| show() | Display plot | none | visible output |


</details>















