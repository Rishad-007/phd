### Environment Setup Instructions

1. **Install Dependencies**

   - Open `setup.ps1` in PowerShell.
   - This script will automatically install all required dependencies.

2. **Initialize in a Different Folder**

   - To set up the environment in another folder, copy `setup.ps1` to that folder and run it in PowerShell.
   - This will create a `.venv` (virtual environment) in the target folder.
   - If you use VS Code for Jupyter notebooks, select the newly created environment as your Python interpreter.

3. **Launch Jupyter Notebook**

   - To open Jupyter Notebook in your browser, run:
     ```
     uv run jupyter notebook
     ```

4. **Connect Jupyter Server to VS Code**

   - To start only the Jupyter Notebook server and connect it to VS Code, run the above command and use the connection details in VS Code.

5. **Run Any Python Code**

   - To run any Python script or command in the activated environment, use:
     ```
     uv run python your_script.py
     ```

   or directly

   ```
      uv run your_script.py
   ```
