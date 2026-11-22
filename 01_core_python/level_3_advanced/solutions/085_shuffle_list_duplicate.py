"""Exercise 085 — Shuffle List Duplicate.

Shuffle and print list [3,6,7,8] (duplicate).
"""

import random


def shuffle_list():
    numbers = [3, 6, 7, 8]
    random.shuffle(numbers)
    print(numbers)


if __name__ == "__main__":
    shuffle_list()
