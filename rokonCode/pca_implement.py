import torch

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None
    
    def fit(self, X):
        # Convert to torch if numpy array
        if not isinstance(X, torch.Tensor):
            X = torch.tensor(X, dtype=torch.float32)

        # Step 1: Center the data
        self.mean = torch.mean(X, dim=0)
        X_centered = X - self.mean

        # Step 2: Compute covariance matrix (features × features)
        cov_matrix = (X_centered.T @ X_centered) / (X_centered.shape[0] - 1)

        # Step 3: Eigen decomposition
        eigenvalues, eigenvectors = torch.linalg.eigh(cov_matrix)

        # Step 4: Sort eigenvectors by descending eigenvalues
        sorted_indices = torch.argsort(eigenvalues, descending=True)
        self.components = eigenvectors[:, sorted_indices[:self.n_components]]
    
    def transform(self, X):
        if not isinstance(X, torch.Tensor):
            X = torch.tensor(X, dtype=torch.float32)

        X_centered = X - self.mean
        return X_centered @ self.components


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from sklearn import datasets

    # Load dataset
    data = datasets.load_iris()
    X = data.data
    Y = data.target

    # Run PCA
    pca = PCA(n_components=3)
    pca.fit(X)
    X_projected = pca.transform(X)

    print("Shape of X:", X.shape)
    print("Shape of X_projected:", X_projected.shape)

    # Plot results
    x1 = X_projected[:, 0]
    x2 = X_projected[:, 1]
    x3 = X_projected[:, 2]

    plt.scatter(
        x1, x2, x3, c=Y, edgecolors="none", alpha=0.8, cmap=plt.cm.get_cmap("viridis",3)
    )
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.colorbar()
    plt.show()
