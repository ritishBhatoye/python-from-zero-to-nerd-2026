# NumPy Setup Guide

## ✅ NumPy is Already Installed!

NumPy 2.5.5 is installed in the project's virtual environment.

---

## 🚀 Quick Start

### Activate Virtual Environment

**Every time you open a new terminal**, activate the virtual environment:

```bash
# From project root
source .venv/bin/activate
```

Or use the helper script:
```bash
source activate_venv.sh
```

### Verify NumPy Works

```bash
python -c "import numpy as np; print(f'NumPy {np.__version__} ready!')"
```

---

## 💻 Running NumPy Exercises

### Method 1: From Terminal (Recommended)

```bash
# 1. Activate virtual environment
source .venv/bin/activate

# 2. Run solution
python 14_data_engineering/01_numpy_fundamentals/level_1_beginner/solutions/001_import_numpy.py

# 3. Run test
pytest 14_data_engineering/01_numpy_fundamentals/level_1_beginner/tests/test_001_import_numpy.py -v
```

### Method 2: From VS Code

VS Code should automatically detect the `.venv` folder.

1. Open Command Palette (Cmd+Shift+P)
2. Type "Python: Select Interpreter"
3. Choose: `Python 3.x.x ('.venv': venv)`

Now you can run files directly in VS Code!

---

## 📚 Your Workflow

```bash
# Terminal 1: Keep auto-push running
# (already running)

# Terminal 2: Work on exercises
source .venv/bin/activate
cd 14_data_engineering/01_numpy_fundamentals/level_1_beginner

# Edit solution
vim solutions/001_import_numpy.py

# Run it
python solutions/001_import_numpy.py

# Test it
pytest tests/test_001_import_numpy.py -v
```

---

## 🎯 Editor vs Jupyter

### ✅ Use This Editor (VS Code/Kiro) - Recommended
- All exercises are already set up
- Tests are ready
- Git integration
- Auto-commit running
- Consistent workflow

### 📓 Optional: Jupyter for Experimentation

If you want to experiment with NumPy interactively:

```bash
# Install Jupyter (in venv)
source .venv/bin/activate
pip install jupyter

# Start Jupyter
jupyter notebook
```

**But keep doing exercises in the editor!**

---

## ⚠️ Important Notes

1. **Always activate venv** before running Python scripts:
   ```bash
   source .venv/bin/activate
   ```

2. **Check if venv is active**: Your prompt should show `(.venv)`

3. **Deactivate venv** when done:
   ```bash
   deactivate
   ```

---

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'numpy'"

**Solution:** Activate the virtual environment first!
```bash
source .venv/bin/activate
```

### VS Code not finding NumPy

**Solution:** Select the correct Python interpreter:
1. Cmd+Shift+P
2. "Python: Select Interpreter"
3. Choose `.venv/bin/python`

### Want to reinstall?

```bash
source .venv/bin/activate
pip install --upgrade numpy pytest
```

---

## ✨ You're All Set!

NumPy is ready. Start with exercise 001 and work your way up! 🚀

```bash
source .venv/bin/activate
python 14_data_engineering/01_numpy_fundamentals/level_1_beginner/solutions/001_import_numpy.py
```
