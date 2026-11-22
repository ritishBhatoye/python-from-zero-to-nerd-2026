#!/bin/zsh
# Quick script to activate virtual environment

source .venv/bin/activate
echo "✅ Virtual environment activated!"
echo "📦 NumPy version: $(python -c 'import numpy; print(numpy.__version__)')"
echo ""
echo "💡 Now you can run:"
echo "   python <your_script>.py"
echo "   pytest <test_file>.py"
