



# Case Study: Organizing a Large Photo Archive into a Structured Tensor


## 1. Research Scenario

Alex, a field researcher and photographer, has collected thousands of images over several years. His dataset includes photographs from different domains such as:

### Collections (`C`)

1.  **Wildlife Expedition**
2.  **Family Events**
3.  **Urban Landscapes**

----------

### Categories within each collection (K)

#### Wildlife Expedition

-   Safari (daytime animals)
-   Night Watch (nocturnal animals)

#### Family Events

-   Weddings
-   Birthdays

#### Urban Landscapes

-   Architecture
-   Street Life

----------

### Images within each category (N)

Each category contains multiple images:

Example (Wildlife → Safari):

-   `lion_01.jpg`
-   `elephant_02.jpg`
-   `deer_03.jpg`
-   `zebra_04.jpg`

Example (Urban → Street Life):

-   `market_01.jpg`
-   `traffic_02.jpg`
-   `vendor_03.jpg`
-   `crowd_04.jpg`

----------

## 2. Research Problem

Alex wants to:

> Convert this unstructured collection of images into a structured format suitable for machine learning analysis.

----------

### 3. Constraints

To process the data using **NumPy**, the dataset must satisfy:

-   All images must have the **same resolution** → `(H, W)`
-   All images must have **3 channels (RGB)**
-   Each category must contain the **same number of images (N)**

----------

### 4. Target Tensor Structure

`(C, K, N, H, W, 3)`

  

| Symbol | Meaning |
| --- | --- |
| C | Collections |
| K | Categories per collection |
| N | Images per category |
| H | Height |
| W | Width |
| 3 | RGB channels |


### 5. Task

#### Objective

Convert the dataset into a **6D tensor** of shape:

(3, 2, 4, 64, 64, 3)

----------

#### Tasks

1.  Assume:
    -   3 collections
    -   2 categories per collection
    -   4 images per category
    -   Resolution = 64 × 64
    -   RGB channels = 3
2.  Simulate image data using random numbers
3.  Build:
    -   One collection → `(2, 4, 64, 64, 3)`
    -   Multiple collections → stack into `(3, 2, 4, 64, 64, 3)`
4.  Verify shapes at each step

----------

## 6. Conceptual Theory (Step-by-Step)**


### Step 1: Pixel Level

[R, G, B]

----------

### Step 2: Image Level

(H, W, 3)

----------

### Step 3: Category Level

(N, H, W, 3)

----------

### Step 4: Collection Level

(K, N, H, W, 3)

----------

### Step 5: Dataset Level

(C, K, N, H, W, 3)

----------

### Conceptual visualization

```
Dataset
│
├── Collection 1 (Wildlife)
│   ├── Safari
│   │   ├── lion_01
│   │   ├── elephant_02
│   │   └── ...
│   └── Night Watch
│
├── Collection 2 (Family)
│   ├── Wedding
│   └── Birthday
│
└── Collection 3 (Urban)
    ├── Architecture
    └── Street Life
```

## 7. Full Script with Explanation

### 7.(A) How a Tensor with random integers is created
Before writing the script, let us understand how a tensor can be created 

### 7.(B) The complete script









