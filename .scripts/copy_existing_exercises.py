#!/usr/bin/env python3
"""
Copy existing custom exercises into the level directories.
Numbers them from 101+ to avoid conflict with the 100 collection exercises.
"""

import shutil
from pathlib import Path

base = Path("/Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026/01_core_python")

# Define which existing exercises go to which level (based on name analysis)
# Level 1: Basic operations, simple calculations
LEVEL_1_EXERCISES = [
    "01_personal_expense_calculator",
    "02_temperature_converter",
    "03_age_calculator",
    "04_simple_bill_splitter",
    "05_number_classifier",
    "06_greeting_formatter",
    "07_discount_calculator",
    "08_tip_calculator",
    "09_even_or_odd",
    "10_max_of_three",
    "11_divisible_by_7_not_5",
    "12_factorial_calculator",
    "13_square_dictionary",
    "14_comma_separated_to_collection",
    "15_digit_repetition_sum",
    "23_absolute_value_calculator",
    "24_power_calculator",
    "25_integer_division_remainder",
    "26_string_length_calculator",
    "27_list_sum_calculator",
    "28_list_max_finder",
    "29_list_min_finder",
    "30_list_average_calculator",
    "31_string_uppercase_converter",
    "32_string_lowercase_converter",
    "33_string_title_case_converter",
    "34_string_replace_word",
    "35_list_element_counter",
    "36_list_concatenation",
    "37_list_repetition",
    "38_tuple_creation",
    "39_tuple_unpacking",
    "40_set_creation",
]

# Level 2: String processing, list operations, file handling
LEVEL_2_EXERCISES = [
    "16_formula_calculator",
    "17_letter_and_digit_counter",
    "18_case_counter",
    "19_string_reverser",
    "20_palindrome_checker",
    "21_list_reverser",
    "22_list_sorter",
    "41_set_operations",
    "42_dictionary_creation",
    "43_dictionary_lookup",
    "44_dictionary_update",
    "45_dictionary_keys_list",
    "46_dictionary_values_list",
    "47_dictionary_items_list",
    "48_nested_dictionary",
    "49_word_frequency",
    "50_unique_elements",
    "51_list_intersection",
    "52_list_union",
    "53_list_difference",
    "54_character_frequency",
    "55_anagram_checker",
    "56_vowel_counter",
    "57_consonant_counter",
    "58_digit_sum",
    "59_armstrong_number",
    "60_perfect_number_checker",
]

# Level 3: Advanced algorithms, OOP, complex data structures
LEVEL_3_EXERCISES = [
    "61_prime_number_checker",
    "62_prime_numbers_generator",
    "63_fibonacci_generator",
    "64_lcm_calculator",
    "65_gcd_calculator",
    "66_binary_converter",
    "67_octal_converter",
    "68_hexadecimal_converter",
    "69_decimal_converter",
    "70_matrix_addition",
    "71_matrix_multiplication",
    "72_transpose_matrix",
    "73_determinant_calculator",
    "74_file_word_counter",
    "75_file_line_counter",
    "76_file_character_counter",
    "77_file_copy",
    "78_file_merge",
    "79_directory_lister",
    "80_file_search",
    "81_json_reader",
    "82_json_writer",
    "83_csv_reader",
    "84_csv_writer",
    "85_exception_handler",
    "86_custom_exception",
    "87_class_definition",
    "88_inheritance_example",
]

def copy_exercise(old_name, new_number, level):
    """Copy an exercise from old structure to new level directory."""
    level_dir = {
        1: "level_1_beginner",
        2: "level_2_intermediate",
        3: "level_3_advanced"
    }[level]
    
    # Extract the name without number prefix
    name_parts = old_name.split('_', 1)
    if len(name_parts) > 1:
        name = name_parts[1]
    else:
        name = old_name
    
    new_name = f"{new_number:03d}_{name}"
    
    # Copy problem
    old_problem = base / "problems" / f"{old_name}.md"
    new_problem = base / level_dir / "problems" / f"{new_name}.md"
    if old_problem.exists():
        shutil.copy2(old_problem, new_problem)
        print(f"✅ Copied problem: {old_name} → {new_name} (Level {level})")
    
    # Copy solution
    old_solution = base / "solutions" / f"{old_name}.py"
    new_solution = base / level_dir / "solutions" / f"{new_name}.py"
    if old_solution.exists():
        shutil.copy2(old_solution, new_solution)
    
    # Copy test
    old_test = base / "tests" / f"test_{old_name}.py"
    new_test = base / level_dir / "tests" / f"test_{new_name}.py"
    if old_test.exists():
        shutil.copy2(old_test, new_test)

def main():
    """Copy all existing exercises to level directories."""
    exercise_num = 101
    
    print("🚀 Copying Level 1 exercises...")
    for ex_name in LEVEL_1_EXERCISES:
        copy_exercise(ex_name, exercise_num, 1)
        exercise_num += 1
    
    print("\n🚀 Copying Level 2 exercises...")
    for ex_name in LEVEL_2_EXERCISES:
        copy_exercise(ex_name, exercise_num, 2)
        exercise_num += 1
    
    print("\n🚀 Copying Level 3 exercises...")
    for ex_name in LEVEL_3_EXERCISES:
        copy_exercise(ex_name, exercise_num, 3)
        exercise_num += 1
    
    total = len(LEVEL_1_EXERCISES) + len(LEVEL_2_EXERCISES) + len(LEVEL_3_EXERCISES)
    print(f"\n🎉 Copied {total} custom exercises!")
    print(f"   Total exercises now: 100 (collection) + {total} (custom) = {100 + total}")

if __name__ == "__main__":
    main()
