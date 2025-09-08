#!/bin/bash

# Machine Learning Lab Environment Setup Script
# This script sets up the complete environment for machine learning labs
# Compatible with macOS and Linux

echo "🚀 Starting Machine Learning Lab Environment Setup..."
echo "================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}$1${NC}"
}

# Check if Python 3 is installed
check_python() {
    print_header "🐍 Checking Python Installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        print_status "Found: $PYTHON_VERSION"
        
        # Check if Python version is 3.8 or higher
        PYTHON_MAJOR=$(python3 -c 'import sys; print(sys.version_info.major)')
        PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')
        
        if [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -ge 8 ]; then
            print_status "Python version is compatible (3.8+)"
            return 0
        else
            print_error "Python 3.8+ is required. Found: $PYTHON_VERSION"
            return 1
        fi
    else
        print_error "Python 3 is not installed!"
        print_status "Please install Python 3.8+ from https://www.python.org/downloads/"
        return 1
    fi
}

# Check if pip is installed
check_pip() {
    print_header "📦 Checking pip Installation..."
    
    if command -v pip3 &> /dev/null; then
        PIP_VERSION=$(pip3 --version)
        print_status "Found: $PIP_VERSION"
        return 0
    elif command -v pip &> /dev/null; then
        PIP_VERSION=$(pip --version)
        print_status "Found: $PIP_VERSION"
        return 0
    else
        print_error "pip is not installed!"
        print_status "Installing pip..."
        
        # Try to install pip
        if command -v python3 &> /dev/null; then
            python3 -m ensurepip --default-pip
            return $?
        else
            print_error "Cannot install pip without Python"
            return 1
        fi
    fi
}

# Create virtual environment
create_virtual_env() {
    print_header "🏠 Setting up Virtual Environment..."
    
    if [ -d "ml_lab_env" ]; then
        print_warning "Virtual environment 'ml_lab_env' already exists"
        read -p "Do you want to recreate it? (y/N): " -r
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_status "Removing existing virtual environment..."
            rm -rf ml_lab_env
        else
            print_status "Using existing virtual environment..."
            return 0
        fi
    fi
    
    print_status "Creating virtual environment 'ml_lab_env'..."
    python3 -m venv ml_lab_env
    
    if [ $? -eq 0 ]; then
        print_status "Virtual environment created successfully!"
        return 0
    else
        print_error "Failed to create virtual environment"
        return 1
    fi
}

# Activate virtual environment
activate_virtual_env() {
    print_header "🔄 Activating Virtual Environment..."
    
    if [ -f "ml_lab_env/bin/activate" ]; then
        source ml_lab_env/bin/activate
        print_status "Virtual environment activated!"
        return 0
    else
        print_error "Virtual environment activation script not found"
        return 1
    fi
}

# Upgrade pip
upgrade_pip() {
    print_header "⬆️ Upgrading pip..."
    
    python -m pip install --upgrade pip
    
    if [ $? -eq 0 ]; then
        print_status "pip upgraded successfully!"
        return 0
    else
        print_warning "Failed to upgrade pip, continuing anyway..."
        return 0
    fi
}

# Install packages from requirements.txt
install_packages() {
    print_header "📚 Installing Required Packages..."
    
    if [ -f "requirements.txt" ]; then
        print_status "Installing packages from requirements.txt..."
        pip install -r requirements.txt
        
        if [ $? -eq 0 ]; then
            print_status "All packages installed successfully!"
            return 0
        else
            print_error "Some packages failed to install"
            return 1
        fi
    else
        print_error "requirements.txt not found!"
        print_status "Creating basic requirements.txt..."
        
        cat > requirements.txt << EOF
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=1.0.0
opencv-python>=4.5.0
Pillow>=8.3.0
jupyter>=1.0.0
torch>=1.9.0
torchvision>=0.10.0
EOF
        
        pip install -r requirements.txt
        return $?
    fi
}

# Install Jupyter kernel
setup_jupyter_kernel() {
    print_header "🪐 Setting up Jupyter Kernel..."
    
    python -m ipykernel install --user --name=ml_lab_env --display-name="ML Lab Environment"
    
    if [ $? -eq 0 ]; then
        print_status "Jupyter kernel installed successfully!"
        return 0
    else
        print_warning "Failed to install Jupyter kernel"
        return 1
    fi
}

# Verify installation
verify_installation() {
    print_header "✅ Verifying Installation..."
    
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
    sys.exit(1)
else:
    print('\n🎉 All packages installed and working correctly!')
"
    
    return $?
}

# Create activation script
create_activation_script() {
    print_header "📝 Creating Easy Activation Script..."
    
    cat > activate_ml_env.sh << 'EOF'
#!/bin/bash
# Quick activation script for ML Lab environment

echo "🚀 Activating ML Lab Environment..."

if [ -f "ml_lab_env/bin/activate" ]; then
    source ml_lab_env/bin/activate
    echo "✅ Environment activated!"
    echo "📚 Available commands:"
    echo "  - jupyter lab    : Start Jupyter Lab"
    echo "  - jupyter notebook : Start Jupyter Notebook"
    echo "  - python script.py : Run Python scripts"
    echo "  - deactivate     : Exit virtual environment"
else
    echo "❌ Virtual environment not found!"
    echo "Please run ./setup_environment.sh first"
fi
EOF
    
    chmod +x activate_ml_env.sh
    print_status "Activation script created: activate_ml_env.sh"
}

# Main installation process
main() {
    print_header "🔬 Machine Learning Lab Environment Setup"
    echo "This script will set up a complete Python environment for your ML labs"
    echo "================================================="
    
    # Check prerequisites
    check_python || exit 1
    check_pip || exit 1
    
    # Setup environment
    create_virtual_env || exit 1
    activate_virtual_env || exit 1
    upgrade_pip
    install_packages || exit 1
    setup_jupyter_kernel
    
    # Verify and finalize
    verify_installation || exit 1
    create_activation_script
    
    print_header "🎉 Setup Complete!"
    echo "================================================="
    print_status "Your ML Lab environment is ready!"
    echo ""
    print_status "To activate the environment in future sessions:"
    echo "  ./activate_ml_env.sh"
    echo ""
    print_status "To start Jupyter Lab:"
    echo "  source ml_lab_env/bin/activate"
    echo "  jupyter lab"
    echo ""
    print_status "To deactivate:"
    echo "  deactivate"
    echo ""
    echo "Happy coding! 🚀"
}

# Run main function
main "$@"
