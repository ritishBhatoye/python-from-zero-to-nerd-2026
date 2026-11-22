# NumPy Fundamentals

Master NumPy, the foundation of scientific computing and data science in Python.

## 📚 What You'll Learn

- NumPy array creation and manipulation
- Vectorized operations for fast computation
- Array indexing, slicing, and boolean masking
- Broadcasting and shape manipulation
- Matrix operations and linear algebra
- Advanced array techniques and optimization

## 🎯 Exercise Distribution

### Level 1 — Beginner (33 exercises)
**Difficulty:** ★☆☆

Basic NumPy operations, array creation, and simple manipulations.

**Topics:**
- Importing and configuring NumPy
- Creating arrays (zeros, ones, ranges)
- Basic array operations
- Indexing and slicing
- Simple statistics (min, max, mean)
- Identity matrices and basic shapes

**Exercises:** 001-033

---

### Level 2 — Intermediate (33 exercises)
**Difficulty:** ★★☆

Array manipulation, structured arrays, and data transformations.

**Topics:**
- In-place operations
- Array reshaping and manipulation
- Structured arrays and custom dtypes
- Coordinate transformations
- File I/O with NumPy
- Sorting and searching
- Statistical operations on axes

**Exercises:** 034-066

---

### Level 3 — Advanced (34 exercises)
**Difficulty:** ★★★

Complex operations, optimization, and advanced NumPy techniques.

**Topics:**
- Multi-dimensional indexing
- Advanced broadcasting
- Sliding windows and rolling operations
- Matrix computations
- Geometric calculations
- Algorithm implementations
- Performance optimization
- Einsum operations

**Exercises:** 067-100

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install numpy pytest
```

### Theory
Read the comprehensive theory guide:
```bash
cat 14_data_engineering/01_numpy_fundamentals/theory.md
```

### Running Exercises

**Individual exercise:**
```bash
# Run solution
python 14_data_engineering/01_numpy_fundamentals/level_1_beginner/solutions/001_import_numpy.py

# Run test
pytest 14_data_engineering/01_numpy_fundamentals/level_1_beginner/tests/test_001_import_numpy.py -v
```

**All tests for a level:**
```bash
pytest 14_data_engineering/01_numpy_fundamentals/level_1_beginner/tests/ -v
```

**All NumPy tests:**
```bash
pytest 14_data_engineering/01_numpy_fundamentals/ -v
```

---

## 📂 Directory Structure

```
01_numpy_fundamentals/
├── README.md                    # This file
├── theory.md                    # Comprehensive NumPy guide
├── level_1_beginner/
│   ├── problems/                # 33 beginner exercises
│   ├── solutions/               # Solution stubs
│   └── tests/                   # Test files
├── level_2_intermediate/
│   ├── problems/                # 33 intermediate exercises
│   ├── solutions/               # Solution stubs
│   └── tests/                   # Test files
└── level_3_advanced/
    ├── problems/                # 34 advanced exercises
    ├── solutions/               # Solution stubs
    └── tests/                   # Test files
```

---

## 💡 Learning Tips

1. **Start with theory** - Read `theory.md` first
2. **Practice in order** - Exercises build on each other
3. **Test frequently** - Run tests to verify your solutions
4. **Use NumPy docs** - Official documentation is excellent
5. **Think vectorized** - Avoid Python loops when possible
6. **Experiment in Jupyter** - Great for exploring arrays

---

## 🎓 Learning Path

### Week 1-2: Beginner (Level 1)
- Array basics and creation
- Indexing and slicing
- Simple operations
- **Goal:** Complete exercises 001-033

### Week 3-4: Intermediate (Level 2)
- Array manipulation
- Structured data
- File operations
- **Goal:** Complete exercises 034-066

### Week 5-6: Advanced (Level 3)
- Complex algorithms
- Performance optimization
- Real-world applications
- **Goal:** Complete exercises 067-100

---

## 🔗 Resources

### Official Documentation
- [NumPy Official Docs](https://numpy.org/doc/)
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy API Reference](https://numpy.org/doc/stable/reference/)

### Additional Learning
- [NumPy Illustrated](https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d)
- [From Python to NumPy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/)
- [100 NumPy Exercises (Original)](https://github.com/rougier/numpy-100)

### Community
- [NumPy Discussions](https://github.com/numpy/numpy/discussions)
- [Stack Overflow - NumPy Tag](https://stackoverflow.com/questions/tagged/numpy)

---

## 🏆 Challenge Yourself

After completing all exercises:

1. **Speed Challenge**: Optimize solutions for maximum performance
2. **No-Loop Challenge**: Rewrite all solutions without any Python loops
3. **Memory Challenge**: Minimize memory usage in your solutions
4. **Real Data**: Apply NumPy to real datasets (images, CSV files)

---

## 📊 Progress Tracking

Track your progress:

- [ ] Read theory.md
- [ ] Level 1 Beginner (0/33)
- [ ] Level 2 Intermediate (0/33)
- [ ] Level 3 Advanced (0/34)

**Total:** 0/100 exercises completed

---

## 🤝 Contributing

Found a better solution? Want to add more examples?
See [CONTRIBUTING.md](../../../CONTRIBUTING.md) in the repo root.

---

## 📝 Notes

- All exercises are self-contained
- Solutions should use NumPy efficiently
- Tests verify correctness but not optimal performance
- Advanced exercises may have multiple valid approaches

---

**Source:** Based on the excellent [numpy-100](https://github.com/rougier/numpy-100) by Nicolas P. Rougier

**Happy NumPy Learning! 🐍✨**
