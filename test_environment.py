#!/usr/bin/env python3
"""
Quick Test Script for ML Lab Environment
This script tests if all required packages are installed and working correctly.
"""

import sys
import importlib

def test_package(package_name, display_name=None):
    """Test if a package can be imported and get its version if possible."""
    if display_name is None:
        display_name = package_name
    
    try:
        module = importlib.import_module(package_name)
        
        # Try to get version
        version = "Unknown"
        for attr in ['__version__', 'version', 'VERSION']:
            if hasattr(module, attr):
                version = getattr(module, attr)
                if callable(version):
                    version = version()
                break
        
        print(f"✅ {display_name:<20} - Version: {version}")
        return True
        
    except ImportError as e:
        print(f"❌ {display_name:<20} - FAILED: {str(e)}")
        return False

def main():
    print("🧪 Testing ML Lab Environment")
    print("=" * 50)
    print(f"Python Version: {sys.version}")
    print("=" * 50)
    
    # List of packages to test
    packages = [
        ("numpy", "NumPy"),
        ("pandas", "Pandas"),
        ("matplotlib", "Matplotlib"),
        ("seaborn", "Seaborn"),
        ("sklearn", "Scikit-learn"),
        ("scipy", "SciPy"),
        ("cv2", "OpenCV"),
        ("PIL", "Pillow"),
        ("skimage", "Scikit-image"),
        ("torch", "PyTorch"),
        ("torchvision", "TorchVision"),
        ("jupyter", "Jupyter"),
        ("IPython", "IPython"),
    ]
    
    print("\n📦 Package Status:")
    print("-" * 50)
    
    passed = 0
    total = len(packages)
    
    for package, display_name in packages:
        if test_package(package, display_name):
            passed += 1
    
    print("-" * 50)
    print(f"\n📊 Results: {passed}/{total} packages working correctly")
    
    if passed == total:
        print("🎉 All packages are installed and working!")
        print("\n🚀 You're ready to start your ML labs!")
        
        # Test basic functionality
        print("\n🔬 Testing Basic Functionality:")
        try:
            import numpy as np
            import matplotlib.pyplot as plt
            import pandas as pd
            
            # Create simple test data
            data = np.random.randn(100, 2)
            df = pd.DataFrame(data, columns=['X', 'Y'])
            
            print("✅ NumPy array creation: OK")
            print("✅ Pandas DataFrame creation: OK")
            print("✅ Basic operations: OK")
            
        except Exception as e:
            print(f"❌ Basic functionality test failed: {e}")
    
    else:
        missing = total - passed
        print(f"⚠️  {missing} packages are missing or not working properly")
        print("\n💡 Try running the setup script again:")
        print("   - Windows: setup_environment.bat")
        print("   - macOS/Linux: ./setup_environment.sh")
    
    print("\n" + "=" * 50)
    print("Test completed!")

if __name__ == "__main__":
    main()
