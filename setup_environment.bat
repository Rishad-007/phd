@echo off
REM Machine Learning Lab Environment Setup Script for Windows
REM This script sets up the complete environment for machine learning labs

echo 🚀 Starting Machine Learning Lab Environment Setup...
echo =================================================

REM Check if Python is installed
echo 🐍 Checking Python Installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH!
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Found Python %PYTHON_VERSION%

REM Check if pip is installed
echo 📦 Checking pip Installation...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip is not installed!
    echo Installing pip...
    python -m ensurepip --default-pip
    if %errorlevel% neq 0 (
        echo ❌ Failed to install pip
        pause
        exit /b 1
    )
)

echo ✅ pip is available

REM Check if virtual environment already exists
echo 🏠 Setting up Virtual Environment...
if exist "ml_lab_env" (
    echo ⚠️ Virtual environment 'ml_lab_env' already exists
    set /p RECREATE="Do you want to recreate it? (y/N): "
    if /i "%RECREATE%" == "y" (
        echo 🗑️ Removing existing virtual environment...
        rmdir /s /q ml_lab_env
    ) else (
        echo ✅ Using existing virtual environment...
        goto activate_env
    )
)

REM Create virtual environment
echo 📁 Creating virtual environment 'ml_lab_env'...
python -m venv ml_lab_env
if %errorlevel% neq 0 (
    echo ❌ Failed to create virtual environment
    pause
    exit /b 1
)
echo ✅ Virtual environment created successfully!

:activate_env
REM Activate virtual environment
echo 🔄 Activating Virtual Environment...
call ml_lab_env\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ❌ Failed to activate virtual environment
    pause
    exit /b 1
)
echo ✅ Virtual environment activated!

REM Upgrade pip
echo ⬆️ Upgrading pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo ⚠️ Failed to upgrade pip, continuing anyway...
)

REM Install packages from requirements.txt
echo 📚 Installing Required Packages...
if exist "requirements.txt" (
    echo 📄 Installing packages from requirements.txt...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ❌ Some packages failed to install
        echo ⚠️ This might be due to system compatibility issues
        echo 💡 Try running this script as Administrator
        pause
        exit /b 1
    )
) else (
    echo 📄 requirements.txt not found! Creating basic requirements...
    (
        echo numpy^>=1.21.0
        echo pandas^>=1.3.0
        echo matplotlib^>=3.4.0
        echo seaborn^>=0.11.0
        echo scikit-learn^>=1.0.0
        echo opencv-python^>=4.5.0
        echo Pillow^>=8.3.0
        echo jupyter^>=1.0.0
        echo torch^>=1.9.0
        echo torchvision^>=0.10.0
        echo ipykernel^>=6.0.0
    ) > requirements.txt
    
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ❌ Package installation failed
        pause
        exit /b 1
    )
)

echo ✅ All packages installed successfully!

REM Install Jupyter kernel
echo 🪐 Setting up Jupyter Kernel...
python -m ipykernel install --user --name=ml_lab_env --display-name="ML Lab Environment"
if %errorlevel% neq 0 (
    echo ⚠️ Failed to install Jupyter kernel
)

REM Verify installation
echo ✅ Verifying Installation...
python -c "
import sys
print(f'Python version: {sys.version}')

packages = [
    'numpy', 'pandas', 'matplotlib', 'seaborn', 'sklearn', 
    'cv2', 'PIL', 'torch', 'jupyter'
]

failed = []
for package in packages:
    try:
        __import__(package)
        print(f'✓ {package}: OK')
    except ImportError as e:
        print(f'✗ {package}: FAILED - {e}')
        failed.append(package)

if failed:
    print(f'\n❌ Installation verification failed for: {failed}')
    input('Press Enter to continue anyway...')
else:
    print('\n🎉 All packages installed and working correctly!')
"

REM Create activation batch file
echo 📝 Creating Easy Activation Script...
(
    echo @echo off
    echo REM Quick activation script for ML Lab environment
    echo.
    echo echo 🚀 Activating ML Lab Environment...
    echo.
    echo if exist "ml_lab_env\Scripts\activate.bat" ^(
    echo     call ml_lab_env\Scripts\activate.bat
    echo     echo ✅ Environment activated!
    echo     echo 📚 Available commands:
    echo     echo   - jupyter lab       : Start Jupyter Lab
    echo     echo   - jupyter notebook  : Start Jupyter Notebook  
    echo     echo   - python script.py  : Run Python scripts
    echo     echo   - deactivate        : Exit virtual environment
    echo     echo.
    echo     echo 💡 To start Jupyter Lab, type: jupyter lab
    echo     cmd /k
    echo ^) else ^(
    echo     echo ❌ Virtual environment not found!
    echo     echo Please run setup_environment.bat first
    echo     pause
    echo ^)
) > activate_ml_env.bat

echo ✅ Activation script created: activate_ml_env.bat

REM Final instructions
echo.
echo 🎉 Setup Complete!
echo =================================================
echo ✅ Your ML Lab environment is ready!
echo.
echo 🚀 To activate the environment in future sessions:
echo    Double-click: activate_ml_env.bat
echo    Or run: activate_ml_env.bat
echo.
echo 📚 To start Jupyter Lab:
echo    1. Run activate_ml_env.bat
echo    2. Type: jupyter lab
echo.
echo 🔄 To deactivate:
echo    Type: deactivate
echo.
echo Happy coding! 🚀
echo.
pause
