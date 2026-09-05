# Complete Exercise Reorganization Plan

## ⚠️ IMPORTANT: This is a MAJOR restructuring

**Scope:** 100 exercises from zhiwehu collection + your custom exercises  
**Files affected:** ~300+ files (problems, solutions, tests)  
**Time required:** This needs to be done in multiple sessions

---

## 🎯 Goal

Replace the current exercise numbering with the complete 100+ Python exercises collection, organized by difficulty:

1. **Exercises 01-32**: Level 1 (Beginner)
2. **Exercises 33-72**: Level 2 (Intermediate)
3. **Exercises 73-100+**: Level 3 (Advanced)
4. **Exercises 101+**: Your custom exercises (expense calculator, etc.)

---

## 📊 Current State

- **88 exercises** currently in `01_core_python/`
- Mix of zhiwehu-inspired and custom exercises
- Numbering doesn't follow the original collection order

---

## 🚧 Why This Is Complex

Creating 100 exercises × 3 files each (problem, solution, test) = **300 files** in one session exceeds practical limits for:
- Token budget
- API rate limits  
- Session stability
- Your ability to review changes

---

## ✅ Recommended Approach: Phased Implementation

### Phase 1: Backup & Preparation (DONE)
- ✅ Backup existing exercises to `.backup/before_reorganization/`
- ✅ Document current state

### Phase 2: Level 1 (Beginner) - Questions 1-32
**Create 32 exercises:**
- Q1-Q5: Basic operations
- Q23-Q32: Simple functions
- Q33-Q41: Lists, tuples, dicts

**Action items:**
1. Create 32 problem `.md` files
2. Create 32 empty solution `.py` files
3. Create 32 test files

### Phase 3: Level 2 (Intermediate) - Questions 6-22, 42-49
**Create ~40 exercises:**
- Q6-Q17: Data processing
- Q42-Q49: filter/map/lambda

### Phase 4: Level 3 (Advanced) - Questions 18-22, 50-100
**Create ~50 exercises:**
- Advanced algorithms
- OOP
- Regex, exceptions, etc.

### Phase 5: Custom Exercises
- Move your existing exercises to 101+
- Update all references

---

##  Alternative: Quick Start Approach

Instead of full reorganization, I can:

1. **Keep your existing exercises** as-is (01-88)
2. **Create a new section** `01_core_python/basics_collection/` with all 100 exercises
3. **Update README** to recommend starting with basics_collection first

This way:
- ✅ No massive file reorganization
- ✅ Both curricula available
- ✅ You choose which path to follow
- ✅ Can be done in this session

---

## 🤔 Decision Required

**Option A: Full Reorganization (Your Request)**
- Pros: Clean, single curriculum following the 100+ collection
- Cons: 300+ files, multiple sessions required, complex
- Time: 3-4 sessions of focused work

**Option B: Parallel Curricula (Recommended)**
- Pros: Quick, preserves existing work, both available
- Cons: Two paths might be confusing
- Time: Can finish today

**Option C: Gradual Migration**
- Create exercises 001-100 (pad with zeros for sorting)
- Keep existing exercises as 01-88
- You can phase out old ones as you complete new ones

---

## 📋 If Proceeding with Option A

Due to scope, this needs to be broken into manageable chunks:

**Session 1 (Today):**
- Create exercises 01-20 (Level 1 part 1)

**Session 2:**
- Create exercises 21-40 (Level 1 part 2 + Level 2 part 1)

**Session 3:**
- Create exercises 41-70 (Level 2 part 2)

**Session 4:**
- Create exercises 71-100 (Level 3)

**Session 5:**
- Renumber and integrate your custom exercises (101+)
- Update all cross-references
- Update README and documentation

---

## 💡 My Recommendation

Given the scope and your immediate need to start learning, I suggest:

**🎯 Modified Option B:**

Create: `01_core_python/exercises_by_level/`
```
exercises_by_level/
├── level_1_beginner/
│   ├── 001_divisible_by_7_not_5/
│   │   ├── problem.md
│   │   ├── solution.py
│   │   └── test_solution.py
│   ├── 002_factorial/
│   └── ... (all 32 beginner exercises)
├── level_2_intermediate/
└── level_3_advanced/
```

Keep your existing `problems/`, `solutions/`, `tests/` for reference.

Add to README:
> **New to Python?** Start with `exercises_by_level/level_1_beginner/` (100+ collection basics)
> 
> **Have some experience?** Try the `problems/` exercises (curriculum originals)

This gives you:
- ✅ Complete 100+ collection, properly organized
- ✅ Your existing work preserved
- ✅ Clear learning path
- ✅ Can be completed today

---

## ❓ What Would You Like to Do?

Please choose:

1. **Full reorganization (Option A)** - Start Phase 1 today, continue over multiple sessions
2. **Parallel curricula (Option B/Modified)** - Complete today, both available
3. **Something else** - Tell me your preference

Respond with the option number, and I'll execute immediately.
