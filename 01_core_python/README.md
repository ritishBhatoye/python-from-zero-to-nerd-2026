# Phase 1 — Core Python

Exercises organized by difficulty level. Start with Level 1 and progress upward.

## 📚 Learning Path

### Level 1: Beginner
**Directory:** `level_1_beginner/`

Fundamental Python concepts. Perfect for someone who has just completed an introductory Python course.

**Topics:** Variables, loops, functions, basic data structures, simple classes

**Exercise Count:** 109 exercises

**Start here if:** You're new to Python or need to solidify basics

---

### Level 2: Intermediate  
**Directory:** `level_2_intermediate/`

More complex problems requiring multiple concepts. For those with basic Python knowledge and some programming background.

**Topics:** List comprehensions, file I/O, string processing, algorithms, functional programming

**Exercise Count:** 25 exercises

**Start here if:** You're comfortable with Level 1 concepts

---

### Level 3: Advanced
**Directory:** `level_3_advanced/`

Complex problems using standard library, algorithms, and advanced techniques.

**Topics:** OOP, generators, decorators, regex, exception handling, recursion, algorithms

**Exercise Count:** 56 exercises

**Start here if:** You've mastered Level 1 & 2

---

## 🎯 Quick Start

```bash
# Level 1: Start here
cd level_1_beginner
ls -la problems/

# Run first exercise
pytest tests/test_001_*.py -v
```

---

## 📁 Structure

Each level contains:
```
level_X_name/
├── problems/          # Exercise descriptions (.md files)
├── solutions/         # Your implementations (.py files)  
└── tests/            # Automated tests
```

---

## 🔄 Migration Status

- ✅ Level 1: 109 exercises (collection + originals)
- ✅ Level 2: 25 exercises (collection + originals)
- ✅ Level 3: 56 exercises (collection + originals)

**Total:** 190 exercises across all levels

---

## 📖 Exercise Naming

- `001-100`: From zhiwehu/Python-programming-exercises collection
- `101+`: Original curriculum exercises

All exercises indicate their source in the header.

---

## 🎓 How to Use

1. **Read the problem** (`problems/XXX_name.md`)
2. **Implement solution** (`solutions/XXX_name.py`)  
3. **Run tests** (`pytest tests/test_XXX_name.py -v`)
4. **Reflect and learn**
5. **Move to next exercise**

Progress through levels sequentially for best learning experience.
