# Machine Learning Lab Environment

This repository contains machine learning lab exercises and assignments with automated environment setup.

## 🚀 Quick Setup (One-Click Installation)

### For Windows Users (Lab PC):

1. Download/clone this repository
2. **Double-click** `setup_environment.bat`
3. Wait for installation to complete
4. **Double-click** `activate_ml_env.bat` to start working

### For macOS/Linux Users:

1. Download/clone this repository
2. Open terminal in the project folder
3. Run: `chmod +x setup_environment.sh && ./setup_environment.sh`
4. Run: `./activate_ml_env.sh` to start working

## 📋 What Gets Installed

The setup script automatically installs:

### Core Scientific Computing

- **NumPy** - Numerical computing
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Plotting and visualization
- **Seaborn** - Statistical data visualization

### Machine Learning

- **Scikit-learn** - Machine learning algorithms
- **SciPy** - Scientific computing

### Computer Vision

- **OpenCV** - Computer vision library
- **Pillow (PIL)** - Image processing
- **scikit-image** - Image processing algorithms

### Deep Learning

- **PyTorch** - Deep learning framework
- **TorchVision** - Computer vision with PyTorch

### Development Environment

- **Jupyter Lab** - Interactive development environment
- **Jupyter Notebook** - Notebook interface
- **IPython** - Enhanced Python shell

## 📁 Project Structure

```
Lab/
├── Dataset/                    # Image datasets
│   ├── Cat/                   # Cat images
│   └── Dog/                   # Dog images
├── rokonCode/                 # Implementation files
│   ├── SVM_image_classification.py
│   ├── SVD_image_classification.py
│   ├── LDA_imaplentation.py
│   ├── pca_implement.py
│   ├── image_compression_svd.py
│   └── linear_regression.py
├── *.ipynb                    # Jupyter notebooks
├── requirements.txt           # Python dependencies
├── setup_environment.sh       # Setup script (Mac/Linux)
├── setup_environment.bat      # Setup script (Windows)
├── activate_ml_env.sh         # Quick activation (Mac/Linux)
└── activate_ml_env.bat        # Quick activation (Windows)
```

## 🎯 Notebooks Included

1. **leastsquare.ipynb** - Least squares image classification
2. **Bay_Titanic_lab.ipynb** - Bayesian analysis on Titanic dataset
3. **Bay_EmailSpam_lab.ipynb** - Email spam classification with Bayesian methods
4. **pca.ipynb** - Principal Component Analysis
5. **pca_lda.ipynb** - PCA and LDA comparison
6. **svd.ipynb** - Singular Value Decomposition
7. **LDA_Lab.ipynb** - Linear Discriminant Analysis

## 🛠️ Usage Instructions

### First Time Setup:

**Windows (Lab PC):**

```bash
# Just double-click these files:
1. setup_environment.bat     # One-time setup
2. activate_ml_env.bat       # Every time you work
```

**macOS/Linux:**

```bash
# One-time setup
chmod +x setup_environment.sh
./setup_environment.sh

# Every time you work
./activate_ml_env.sh
```

### Working with Notebooks:

1. Activate the environment (use activation scripts above)
2. Start Jupyter Lab:
   ```bash
   jupyter lab
   ```
3. Open any `.ipynb` file and start coding!

### Running Python Scripts:

1. Activate the environment
2. Run any Python file:
   ```bash
   python rokonCode/SVM_image_classification.py
   ```

## 🔧 Manual Installation (If Needed)

If the automated setup fails, you can install manually:

```bash
# Create virtual environment
python -m venv ml_lab_env

# Activate (Windows)
ml_lab_env\Scripts\activate

# Activate (macOS/Linux)
source ml_lab_env/bin/activate

# Install packages
pip install -r requirements.txt

# Install Jupyter kernel
python -m ipykernel install --user --name=ml_lab_env
```

## 🐛 Troubleshooting

### Common Issues:

1. **"Python not found"**

   - Install Python 3.8+ from [python.org](https://python.org)
   - Make sure to check "Add Python to PATH"

2. **"Permission denied" (Windows)**

   - Right-click setup script → "Run as Administrator"

3. **"Package installation failed"**

   - Check internet connection
   - Try running setup script again
   - For Windows: Install Visual Studio Build Tools

4. **"Jupyter kernel not found"**
   - In Jupyter, go to Kernel → Change Kernel → "ML Lab Environment"

### Getting Help:

1. Check that Python 3.8+ is installed: `python --version`
2. Verify virtual environment exists: Look for `ml_lab_env` folder
3. Try manual installation steps above
4. Restart terminal/command prompt and try again

## 📚 Dependencies Explained

| Package      | Purpose                        | Used In                  |
| ------------ | ------------------------------ | ------------------------ |
| NumPy        | Numerical operations, arrays   | All notebooks            |
| Pandas       | Data manipulation, CSV reading | Titanic, Spam datasets   |
| Matplotlib   | Basic plotting                 | All visualizations       |
| Seaborn      | Statistical plots              | Data analysis            |
| Scikit-learn | ML algorithms (SVM, PCA, etc.) | Most ML notebooks        |
| OpenCV       | Image processing               | Image classification     |
| PyTorch      | Deep learning, tensors         | LDA, PCA implementations |
| Jupyter      | Interactive notebooks          | Development environment  |

## 🎓 Learning Path

Recommended order for notebooks:

1. **pca.ipynb** - Learn dimensionality reduction
2. **leastsquare.ipynb** - Basic classification
3. **svd.ipynb** - Matrix decomposition
4. **LDA_Lab.ipynb** - Advanced classification
5. **Bay_Titanic_lab.ipynb** - Bayesian methods
6. **Bay_EmailSpam_lab.ipynb** - Real-world application

## 💡 Tips for Lab Work

1. **Always activate the environment first** before running any code
2. **Save your work frequently** in Jupyter notebooks
3. **Use the Dataset folder** for consistent file paths
4. **Check the activation script** if you get import errors
5. **Restart kernel** if you install new packages mid-session

Happy Learning! 🚀
