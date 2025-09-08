import cv2
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# --- Parameters ---
img_size = (64, 64)  # Resize all images (slightly larger for SVM)
k = 20                # Number of singular values if using SVD

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
                images.append(img.flatten())  # Flatten image
                labels.append(label)          # Keep string labels
    return np.array(images), np.array(labels)

dataset_folder = "Dataset_path"  # contains "cat" and "dog"
X, y = load_images_from_folder(dataset_folder)

# --- Train/Test split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# --- Scale features ---
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# --- Train SVM classifier ---
svm_clf = SVC(kernel='linear', C=1.0)  # Linear kernel for simplicity
svm_clf.fit(X_train, y_train)

# --- Predictions ---
y_pred = svm_clf.predict(X_test)

# --- Evaluation ---
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
