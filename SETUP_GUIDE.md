# 🚀 Quick Setup Guide - Python Learning Environment

Follow these steps to get your development environment ready.

## ✅ Step 1: Install Extensions (Choose ONE method)

### 🎯 **EASIEST: Use VS Code Recommendations** (Recommended)

1. In VS Code, press `Cmd + Shift + X` (or click Extensions icon in sidebar)
2. In the search box, type: `@recommended`
3. You'll see **"WORKSPACE RECOMMENDATIONS"** section
4. Click the **cloud download icon** next to it
5. Wait for all 20 extensions to install (takes 2-3 minutes)
6. Click **"Reload"** when done

**That's it!** All extensions are now installed.

---

### Alternative: Wait for VS Code Prompt

1. Close this workspace
2. Reopen it
3. VS Code will show: _"Do you want to install recommended extensions?"_
4. Click **"Install All"**

---

## ✅ Step 2: Select Python Interpreter

1. Press `Cmd + Shift + P` (macOS) or `Ctrl + Shift + P` (Windows)
2. Type: `Python: Select Interpreter`
3. Choose: `.venv/bin/python` (if you have virtual environment)
   - Or: Your system Python

---

## ✅ Step 3: Verify Setup

### Test Python Extension
1. Open any `.py` file (e.g., `01_core_python/solutions/01_personal_expense_calculator.py`)
2. You should see:
   - ✓ Colorful syntax highlighting
   - ✓ Python version in bottom-left corner
   - ✓ Auto-complete when typing
   - ✓ Type hints when hovering

### Test Formatting
1. Open a Python file
2. Make it messy (random spaces, weird indentation)
3. Press `Cmd + S` (save)
4. **File auto-formats!** ✨

### Test Testing
1. Open View → Test Explorer (or press `Cmd + Shift + T`)
2. You should see test files in sidebar
3. Click any test to run it

---

## ✅ Step 4: Start Learning!

### Open Your First Exercise
```bash
# File to open:
01_core_python/problems/01_personal_expense_calculator.md
```

### Read the problem

### Implement solution
```bash
# Create/edit:
01_core_python/solutions/01_personal_expense_calculator.py
```

### Run tests
```bash
# In terminal:
pytest 01_core_python/tests/test_01_personal_expense_calculator.py -v
```

Or click the test in Test Explorer sidebar!

---

## 📚 Helpful Resources

- **Extensions Guide**: `.vscode/EXTENSIONS_GUIDE.md` - Detailed info
- **VS Code Basics**: `.vscode/README.md` - Quick reference
- **Install Help**: `.vscode/INSTALL_EXTENSIONS.md` - Installation methods
- **Auto-Commit**: `.kiro/AUTO_COMMIT_SETUP.md` - Git automation

---

## ⌨️ Essential Shortcuts

| Action | Shortcut (Mac) | Shortcut (Win/Linux) |
|--------|---------------|---------------------|
| Command Palette | `Cmd + Shift + P` | `Ctrl + Shift + P` |
| Run File | `Cmd + Shift + B` | `Ctrl + Shift + B` |
| Debug | `F5` | `F5` |
| Save (auto-format) | `Cmd + S` | `Ctrl + S` |
| Toggle Terminal | `` Ctrl + ` `` | `` Ctrl + ` `` |
| Find | `Cmd + F` | `Ctrl + F` |

---

## 🎯 What You Get

### When You Type
- **Auto-complete** suggests functions/variables
- **Type hints** show what types are expected
- **Docstrings** appear on hover

### When You Save
- **Auto-formats** your code (Ruff)
- **Organizes imports** automatically
- **Fixes linting** issues

### When You Test
- **Visual test runner** in sidebar
- **Green/red indicators** for pass/fail
- **Click to run** individual tests
- **Debug tests** with breakpoints

---

## ❓ Troubleshooting

### Extensions Not Installing?
- Check internet connection
- Try Method 5 in `.vscode/INSTALL_EXTENSIONS.md`
- Reload VS Code

### Python Not Found?
1. `Cmd/Ctrl + Shift + P`
2. "Python: Select Interpreter"
3. Choose your Python

### Tests Not Showing?
1. Install pytest: `pip install pytest`
2. Reload VS Code
3. Check Test Explorer (View → Test)

### Formatting Not Working?
1. Check Ruff extension is installed
2. Check settings: "python.defaultFormatter" should be "charliermarsh.ruff"
3. Save file to trigger

---

## 🎓 Learning Path

1. ✅ Setup environment (you're here!)
2. 📖 Read exercise problem (`.md` file)
3. 💻 Implement solution (`.py` file)
4. ✓ Run tests (pytest or Test Explorer)
5. 🐛 Debug if needed (F5)
6. ♻️ Refactor and improve
7. 📝 Reflect on learning
8. ➡️ Next exercise!

---

## 🚀 Ready to Start?

Open your first exercise:
```
01_core_python/problems/01_personal_expense_calculator.md
```

**Good luck and happy learning!** 🎉
