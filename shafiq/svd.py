import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def getImgMat():
    img_path = 'sample.png'
    img = Image.open(img_path).convert('L')
    return np.array(img,dtype="float")

def svd_compute_manual(A):
    # Step 1: Compute A^T A
    At_A = A.T @ A

    # Step 2: Eigen decomposition of A^T A
    eigenvalues, V = np.linalg.eigh(At_A)

    # Step 3: Sort by eigenvalues
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    V = V[:,idx]

    # Step 4: Singular valuse
    singular_values = np.sqrt(np.clip(eigenvalues, 0, None))

    # Step 5: Left singular vector U
    U = []
    for i,sigma in enumerate(singular_values):
        if sigma > 1e-10:
            u = (A @ V[:,i]) / sigma
            U.append(u)
    U = np.column_stack(U)
    print(U)
    return U,singular_values, V


# Original image matrix
img_mat = getImgMat()

# Decompose
U,S,V = svd_compute_manual(img_mat)

# Define k
k = 20 

# Reconstrcuted for top K components
Ak = U[:,:k] @ np.diag(S[:k]) @ V[:,:k].T

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(img_mat, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(Ak,cmap="gray")
plt.title("Compressed")
plt.axis("off")

plt.tight_layout()
plt.show()