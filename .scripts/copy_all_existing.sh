#!/bin/bash
# Copy ALL existing exercises to Level 1 (beginner) starting from 101

cd /Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026/01_core_python

counter=101

# Process each problem file
for problem_file in problems/*.md; do
    # Extract filename without extension
    filename=$(basename "$problem_file" .md)
    
    # New name with counter
    new_name=$(printf "%03d_%s" $counter "${filename#*_}")
    
    # Copy problem
    cp "problems/${filename}.md" "level_1_beginner/problems/${new_name}.md"
    
    # Copy solution if exists
    if [ -f "solutions/${filename}.py" ]; then
        cp "solutions/${filename}.py" "level_1_beginner/solutions/${new_name}.py"
    fi
    
    # Copy test if exists
    if [ -f "tests/test_${filename}.py" ]; then
        cp "tests/test_${filename}.py" "level_1_beginner/tests/test_${new_name}.py"
    fi
    
    echo "✅ Copied: ${filename} → ${new_name}"
    ((counter++))
done

echo ""
echo "🎉 Copied $((counter - 101)) exercises!"
echo "Total exercises:"
echo "  Level 1: $(ls -1 level_1_beginner/problems/*.md 2>/dev/null | wc -l)"
echo "  Level 2: $(ls -1 level_2_intermediate/problems/*.md 2>/dev/null | wc -l)"
echo "  Level 3: $(ls -1 level_3_advanced/problems/*.md 2>/dev/null | wc -l)"
