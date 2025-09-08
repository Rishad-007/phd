import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
data = pd.read_csv('dataset_path')

# Check the first few rows
print(data.head())

# Extract features and target
X = data[['Height']].values  # shape (n_samples, 1)
y = data['Weight'].values    # shape (n_samples,)

# Linear Regression using Least Squares
class LinearRegressionLSE:
    def __init__(self):
        self.weights = None  # Includes bias

    def fit(self, X, y):
        # Add bias term
        X_bias = np.c_[X, np.ones(X.shape[0])]
        # Use pseudo-inverse for stability
        self.weights = np.linalg.pinv(X_bias) @ y

    def predict(self, X):
        X_bias = np.c_[X, np.ones(X.shape[0])]
        return X_bias @ self.weights

# Train the model
model = LinearRegressionLSE()
model.fit(X, y)

print("Weights (slope and bias):", model.weights)

# Make predictions
y_pred = model.predict(X)

# Compare first 5 predictions
comparison = pd.DataFrame({'Actual': y[:5], 'Predicted': y_pred[:5]})
print(comparison)

# Plot
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Predicted')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Linear Regression (Least Squares)')
plt.legend()
plt.show()
