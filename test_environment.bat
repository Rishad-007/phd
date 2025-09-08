@echo off
REM Quick Test Script for ML Lab Environment (Windows)
REM This script tests if all required packages are installed and working correctly.

echo 🧪 Testing ML Lab Environment
echo ==================================================

REM Activate virtual environment if it exists
if exist "ml_lab_env\Scripts\activate.bat" (
    echo 🔄 Activating virtual environment...
    call ml_lab_env\Scripts\activate.bat
) else (
    echo ⚠️ Virtual environment not found, testing system Python...
)

REM Run the test script
python test_environment.py

echo.
echo 💡 If tests failed, run setup_environment.bat first
pause
