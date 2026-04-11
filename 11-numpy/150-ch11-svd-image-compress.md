


## Beyond Text

In this project, we move from theory to practical application. Singular Value Decomposition (SVD) is an efficient algorithm for "Dimension Reduction." and can be used to perform **Digital Image Compression.** Think of an image not as a picture, but as a massive grid of numbers—a matrix. By decomposing this matrix into its fundamental "singular values," one can identify which parts of the image are essential structure and which are mere noise.

"How much information is required to recognize an image? Investigate the relationship between the 'Rank' of a matrix and visual clarity. Using Singular Value Decomposition (SVD), decompose a high-resolution image into its constituent U, **Σ**, and $V^T$ components. Conduct an experiment to determine the 'Critical Compression Threshold'—the point where the number of singular values (k) is reduced so much that the image becomes unrecognizable. Your project must compare the original RGB data, a grayscale baseline, and a reconstructed low-rank matrix version."

### The Workflow

1.  **Acquisition:** Fetch an image from a web URL or your local drive.
2.  **Preprocessing:** Convert the colorful image data into a 2D grayscale matrix using the **Pillow (PIL)** library.
3.  **Decomposition:** Use np.linalg.svd() to break your image into three components: $U$, $Σ$ and $V^T$
4.  **Compression:** Trim the singular values. In this experiment, we start by keeping only **1/20th** of the original data.
5.  **Reconstruction:** Use matrix multiplication to re-assemble the image and visualize the results side-by-side using Matplotlib.

### The Solution Script
This version uses modern NumPy conventions (np.asarray) which replaces the multi-step getdata() process (Note the earlier 2019 used the multi-step getdata() process , making the code much more efficient

```python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

# --- 1. Load Image (Local Path or Web Link) ---
# Replace this URL with any image link (e.g., from Unsplash or GitHub)
url = "https://raw.githubusercontent.com/numpy/numpy/main/branding/logo/primary/numpylogo.png"

try:
    response = requests.get(url)  # Fetch image from the internet
    img = Image.open(BytesIO(response.content))  # raw data → image format
except:
    print("Web link failed, please check URL or internet connection.")
    # Fallback: create a dummy array if link fails
    img = Image.fromarray(np.uint8(np.random.rand(500,500)*255))

width, height = img.size
print(f"Original Dimensions: Width={width}, Height={height}")

# --- 2. Color Conversion ---
# 'L' mode converts image to grayscale (8-bit pixels, black and white)
img_gray = img.convert('L')

# --- 3. Matrix Conversion (The Modern Way) ---
# Instead of getdata() and lists, np.asarray() is much faster and more direct
img_mat = np.asarray(img_gray)

# --- 4. SVD Decomposition ---
# U: Left singular vectors (Rotations)
# S: Singular values (Importance/Energy of each feature)
# Vt: Right singular vectors (Rotations)
U, S, Vt = np.linalg.svd(img_mat, full_matrices=False)

# --- 5. Compression / Dimension Reduction ---
# We define 'k' as the number of singular values to keep.
# Let's use 1/20th (5%) of the available singular values.
k = int(len(S) / 20)
print(f"Total Singular Values: {len(S)} | Retained for Compression (k): {k}")

# Reconstruct the matrix using only the top 'k' components
# Formula: U_k * Sigma_k * Vt_k
img_compressed = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))

# --- 6. Visualization ---
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Subplot 1: Original Color
axes[0].imshow(img)
axes[0].set_title("Original Color")
axes[0].axis('off')

# Subplot 2: Grayscale Baseline
axes[1].imshow(img_gray, cmap='gray')
axes[1].set_title("Grayscale (Uncompressed)")
axes[1].axis('off')

# Subplot 3: SVD Compressed
axes[2].imshow(img_compressed, cmap='gray')
axes[2].set_title(f"SVD Compressed (k={k})")
axes[2].axis('off')

plt.tight_layout()
plt.show()


```

### The (1) original image (2)  Its grey scale version and its (3) SVD compressed version are shown in figure below:

![SVD Image compression](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-svd-image-compression.png)
















