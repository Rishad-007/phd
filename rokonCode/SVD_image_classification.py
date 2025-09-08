import cv2
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --- Parameters ---
img_size = (28, 28)  # Resize all images to 28x28
k = 20  # Number of singular values to use

# --- Load dataset ---
def load_images_from_folder(folder_path):
    images = []
    labels = []
    for label in os.listdir(folder_path):
        label_path = os.path.join(folder_path, label)
        if not os.path.isdir(label_path):
            continue
        for filename in os.listdir(label_path):
            img_path = os.path.join(label_path, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, img_size)
                images.append(img.flatten())
                labels.append(label)  # Keep string labels
    return np.array(images), np.array(labels)

dataset_folder = "Dataset_path"  # Contains "cat" and "dog" folders
X, y = load_images_from_folder(dataset_folder)

# --- Train/Test split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42, stratify=y)
print(X_test.shape, X_train.shape, y_train.shape, y_test.shape)

# --- Feature extraction using top singular values ---
def top_singular_values(img, k=k):
    A = img.reshape(img_size)
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    return S[:k]

X_train_svd = np.array([top_singular_values(x, k) for x in X_train])
X_test_svd  = np.array([top_singular_values(x, k) for x in X_test])

# --- Nearest neighbor classifier based on SVD ---
def nearest_classification(test_features, train_features, train_labels):
    preds = []
    for tf in test_features:
        dists = np.linalg.norm(train_features - tf, axis=1)
        preds.append(train_labels[np.argmin(dists)])
    return np.array(preds)

y_pred = nearest_classification(X_test_svd, X_train_svd, y_train)

print("Accuracy:", accuracy_score(y_test, y_pred))
