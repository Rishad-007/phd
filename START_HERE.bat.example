@echo off
REM ML Lab Launcher - One-click solution to start working
REM This script handles everything: setup, activation, and launching Jupyter

title ML Lab Environment

echo.
echo  ███╗   ███╗██╗         ██╗      █████╗ ██████╗ 
echo  ████╗ ████║██║         ██║     ██╔══██╗██╔══██╗
echo  ██╔████╔██║██║         ██║     ███████║██████╔╝
echo  ██║╚██╔╝██║██║         ██║     ██╔══██║██╔══██╗
echo  ██║ ╚═╝ ██║███████╗    ███████╗██║  ██║██████╔╝
echo  ╚═╝     ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═════╝ 
echo.
echo  🚀 Machine Learning Lab Environment Launcher
echo  ============================================
echo.

REM Check if setup is needed
if not exist "ml_lab_env" (
    echo 🏗️ Environment not found. Running setup...
    echo.
    call setup_environment.bat
    if %errorlevel% neq 0 (
        echo ❌ Setup failed!
        pause
        exit /b 1
    )
    echo.
    echo ✅ Setup completed successfully!
    echo.
)

REM Activate environment
echo 🔄 Activating ML Lab environment...
call ml_lab_env\Scripts\activate.bat

if %errorlevel% neq 0 (
    echo ❌ Failed to activate environment!
    echo 💡 Try running setup_environment.bat
    pause
    exit /b 1
)

echo ✅ Environment activated successfully!
echo.

REM Show menu
:menu
echo 📚 What would you like to do?
echo.
echo  1️⃣  Start Jupyter Lab (Recommended)
echo  2️⃣  Start Jupyter Notebook  
echo  3️⃣  Test Environment
echo  4️⃣  Python Shell
echo  5️⃣  Command Line
echo  6️⃣  Exit
echo.
set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" goto jupyter_lab
if "%choice%"=="2" goto jupyter_notebook  
if "%choice%"=="3" goto test_env
if "%choice%"=="4" goto python_shell
if "%choice%"=="5" goto command_line
if "%choice%"=="6" goto exit
echo ❌ Invalid choice. Please try again.
goto menu

:jupyter_lab
echo.
echo 🚀 Starting Jupyter Lab...
echo 💡 Your browser will open automatically
echo 🔄 Press Ctrl+C to stop Jupyter Lab
echo.
jupyter lab
goto menu

:jupyter_notebook
echo.
echo 📓 Starting Jupyter Notebook...
echo 💡 Your browser will open automatically  
echo 🔄 Press Ctrl+C to stop Jupyter Notebook
echo.
jupyter notebook
goto menu

:test_env
echo.
echo 🧪 Testing environment...
echo.
python test_environment.py
echo.
pause
goto menu

:python_shell
echo.
echo 🐍 Starting Python shell...
echo 💡 Type 'exit()' to return to menu
echo.
python
goto menu

:command_line
echo.
echo 💻 Command line ready!
echo 📚 Available commands:
echo   - jupyter lab       : Start Jupyter Lab
echo   - jupyter notebook  : Start Jupyter Notebook
echo   - python script.py  : Run Python scripts  
echo   - python            : Python shell
echo   - deactivate        : Exit environment
echo   - exit              : Close window
echo.
cmd /k

:exit
echo.
echo 👋 Thanks for using ML Lab Environment!
echo 📚 Remember: Double-click this file anytime to start working
echo.
timeout /t 3 /nobreak >nul
