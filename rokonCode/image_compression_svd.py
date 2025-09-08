import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color

# Load grayscale image
image = io.imread("image_path")  # Use raw string for Windows paths
gray = color.rgb2gray(image)

h, w = gray.shape

# SVD decomposition
U, S, VT = np.linalg.svd(gray, full_matrices=False)

# Choose k
k = 20  # Number of singular values to keep

# Reconstruct image using k singular values
S_k = np.diag(S[:k])
U_k = U[:, :k]
VT_k = VT[:k, :]
compressed_image = np.dot(U_k, np.dot(S_k, VT_k))

# Calculate memory sizes in MB
original_size_mb = gray.size * gray.itemsize / (1024 * 1024)
# Compressed size using SVD components
compressed_size_mb = (U_k.size + S_k.size + VT_k.size) * gray.itemsize / (1024*1024)

print(f"Original image size: {original_size_mb:.2f} MB")
print(f"Compressed image size (SVD storage with k={k}): {compressed_size_mb:.2f} MB")

# Display original and compressed images
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.title(f"Original\n{original_size_mb:.2f} MB")
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title(f"Compressed (k={k})\n{compressed_size_mb:.2f} MB")
plt.imshow(compressed_image, cmap='gray')
plt.axis('off')

plt.show()
