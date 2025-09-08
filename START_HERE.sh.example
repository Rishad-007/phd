#!/bin/bash

# ML Lab Launcher - One-click solution to start working  
# This script handles everything: setup, activation, and launching Jupyter

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

# Clear screen and show banner
clear
echo -e "${BLUE}"
echo "  ███╗   ███╗██╗         ██╗      █████╗ ██████╗ "
echo "  ████╗ ████║██║         ██║     ██╔══██╗██╔══██╗"
echo "  ██╔████╔██║██║         ██║     ███████║██████╔╝"
echo "  ██║╚██╔╝██║██║         ██║     ██╔══██║██╔══██╗"
echo "  ██║ ╚═╝ ██║███████╗    ███████╗██║  ██║██████╔╝"
echo "  ╚═╝     ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═════╝ "
echo -e "${NC}"
echo -e "${CYAN}🚀 Machine Learning Lab Environment Launcher${NC}"
echo "============================================"
echo

# Check if setup is needed
if [ ! -d "ml_lab_env" ]; then
    echo -e "${YELLOW}🏗️ Environment not found. Running setup...${NC}"
    echo
    chmod +x setup_environment.sh
    ./setup_environment.sh
    
    if [ $? -ne 0 ]; then
        echo -e "${RED}❌ Setup failed!${NC}"
        read -p "Press Enter to exit..."
        exit 1
    fi
    
    echo
    echo -e "${GREEN}✅ Setup completed successfully!${NC}"
    echo
fi

# Activate environment
echo -e "${YELLOW}🔄 Activating ML Lab environment...${NC}"
source ml_lab_env/bin/activate

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to activate environment!${NC}"
    echo -e "${YELLOW}💡 Try running ./setup_environment.sh${NC}"
    read -p "Press Enter to exit..."
    exit 1
fi

echo -e "${GREEN}✅ Environment activated successfully!${NC}"
echo

# Menu function
show_menu() {
    echo -e "${CYAN}📚 What would you like to do?${NC}"
    echo
    echo -e "${GREEN} 1️⃣  Start Jupyter Lab (Recommended)${NC}"
    echo -e "${GREEN} 2️⃣  Start Jupyter Notebook${NC}"
    echo -e "${GREEN} 3️⃣  Test Environment${NC}"
    echo -e "${GREEN} 4️⃣  Python Shell${NC}"
    echo -e "${GREEN} 5️⃣  Command Line${NC}"
    echo -e "${GREEN} 6️⃣  Exit${NC}"
    echo
}

# Main loop
while true; do
    show_menu
    read -p "Enter your choice (1-6): " choice
    
    case $choice in
        1)
            echo
            echo -e "${CYAN}🚀 Starting Jupyter Lab...${NC}"
            echo -e "${YELLOW}💡 Your browser will open automatically${NC}"
            echo -e "${YELLOW}🔄 Press Ctrl+C to stop Jupyter Lab${NC}"
            echo
            jupyter lab
            echo
            ;;
        2)
            echo
            echo -e "${CYAN}📓 Starting Jupyter Notebook...${NC}"
            echo -e "${YELLOW}💡 Your browser will open automatically${NC}"
            echo -e "${YELLOW}🔄 Press Ctrl+C to stop Jupyter Notebook${NC}"
            echo
            jupyter notebook
            echo
            ;;
        3)
            echo
            echo -e "${CYAN}🧪 Testing environment...${NC}"
            echo
            python test_environment.py
            echo
            read -p "Press Enter to continue..."
            ;;
        4)
            echo
            echo -e "${CYAN}🐍 Starting Python shell...${NC}"
            echo -e "${YELLOW}💡 Type 'exit()' to return to menu${NC}"
            echo
            python
            echo
            ;;
        5)
            echo
            echo -e "${CYAN}💻 Command line ready!${NC}"
            echo -e "${YELLOW}📚 Available commands:${NC}"
            echo "  - jupyter lab       : Start Jupyter Lab"
            echo "  - jupyter notebook  : Start Jupyter Notebook"
            echo "  - python script.py  : Run Python scripts"
            echo "  - python            : Python shell"
            echo "  - deactivate        : Exit environment"
            echo "  - exit              : Return to launcher"
            echo
            bash
            echo
            ;;
        6)
            echo
            echo -e "${GREEN}👋 Thanks for using ML Lab Environment!${NC}"
            echo -e "${YELLOW}📚 Remember: Run ./START_HERE.sh anytime to start working${NC}"
            echo
            exit 0
            ;;
        *)
            echo -e "${RED}❌ Invalid choice. Please try again.${NC}"
            echo
            ;;
    esac
done
