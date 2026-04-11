


## Beyond Text

In this project, we move from theory to practical application. Singular Value Decomposition (SVD) is an efficient algorithm for "Dimension Reduction." and can be used to perform **Digital Image Compression.** Think of an image not as a picture, but as a massive grid of numbers—a matrix. By decomposing this matrix into its fundamental "singular values," one can identify which parts of the image are essential structure and which are mere noise.

"How much information is required to recognize an image? Investigate the relationship between the 'Rank' of a matrix and visual clarity. Using Singular Value Decomposition (SVD), decompose a high-resolution image into its constituent U, **Σ**, and $V^T$ components. Conduct an experiment to determine the 'Critical Compression Threshold'—the point where the number of singular values (k) is reduced so much that the image becomes unrecognizable. Your project must compare the original RGB data, a grayscale baseline, and a reconstructed low-rank matrix version."

### The Workflow

1.  **Acquisition:** Fetch an image from a web URL or your local drive.
2.  **Preprocessing:** Convert the colorful image data into a 2D grayscale matrix using the **Pillow (PIL)** library.
3.  **Decomposition:** Use np.linalg.svd() to break your image into three components: $U$, $Σ$ and $V^T$
4.  **Compression:** Trim the singular values. In this experiment, we start by keeping only **1/20th** of the original data.
5.  **Reconstruction:** Use matrix multiplication to re-assemble the image and visualize the results side-by-side using Matplotlib.













