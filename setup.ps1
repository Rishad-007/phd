# Install uv
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Add uv to PATH for current session and permanently
$uvPath = "$env:USERPROFILE\.local\bin"
$env:PATH = "$uvPath;$env:PATH"
[Environment]::SetEnvironmentVariable("PATH", "$uvPath;$([Environment]::GetEnvironmentVariable('PATH', 'User'))", "User")

# Initialize uv project
uv init

# Install Python packages
uv add numpy matplotlib scikit-image torch scikit-learn pandas opencv-python pillow jupyter notebook seaborn
