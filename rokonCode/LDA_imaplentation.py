import torch

class LDA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.scalings = None
        self.mean = None
    
    def fit(self, X, y):
        # Convert to torch if numpy arrays
        if not isinstance(X, torch.Tensor):
            X = torch.tensor(X, dtype=torch.float32)
        if not isinstance(y, torch.Tensor):
            y = torch.tensor(y, dtype=torch.int64)

        n_features = X.shape[1]
        class_labels = torch.unique(y)

        # Overall mean
        mean_overall = torch.mean(X, dim=0)

        # Initialize scatter matrices
        Sw = torch.zeros((n_features, n_features), dtype=torch.float32)  # within-class scatter
        Sb = torch.zeros((n_features, n_features), dtype=torch.float32)  # between-class scatter

        # Compute scatter matrices
        for c in class_labels:
            X_c = X[y == c]
            mean_c = torch.mean(X_c, dim=0)
            
            # Within-class scatter
            X_centered = X_c - mean_c
            Sw += X_centered.T @ X_centered

            # Between-class scatter
            n_c = X_c.shape[0]
            mean_diff = (mean_c - mean_overall).reshape(-1, 1)
            Sb += n_c * (mean_diff @ mean_diff.T)

        # Solve generalized eigenvalue problem: Sb * v = λ * Sw * v
        eigenvalues, eigenvectors = torch.linalg.eig(torch.linalg.pinv(Sw) @ Sb)

        # Keep real part (sometimes small imaginary noise appears)
        eigenvalues = eigenvalues.real
        eigenvectors = eigenvectors.real

        # Sort by eigenvalues (descending)
        sorted_indices = torch.argsort(eigenvalues, descending=True)
        self.scalings = eigenvectors[:, sorted_indices[:self.n_components]]
        self.mean = mean_overall
    
    def transform(self, X):
        if not isinstance(X, torch.Tensor):
            X = torch.tensor(X, dtype=torch.float32)

        X_centered = X - self.mean
        return X_centered @ self.scalings


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from sklearn import datasets

    # Load dataset
    data = datasets.load_iris()
    X = data.data
    y = data.target

    # Run LDA
    lda = LDA(n_components=2)  # with 3 classes, max = 2 components
    lda.fit(X, y)
    X_projected = lda.transform(X)

    print("Shape of X:", X.shape)
    print("Shape of X_projected:", X_projected.shape)

    # Plot results (2D)
    x1 = X_projected[:, 0]
    x2 = X_projected[:, 1]

    plt.scatter(
        x1, x2, c=y, edgecolors="none", alpha=0.8, cmap=plt.cm.get_cmap("viridis", 3)
    )
    plt.xlabel("Linear Discriminant 1")
    plt.ylabel("Linear Discriminant 2")
    plt.colorbar()
    plt.show()
