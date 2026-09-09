"""Exercise 009 — Capitalize Lines.

Read lines until empty line, print all in uppercase.
"""

# Your implementation here
pass

import sys

lines = sys.stdin.read().splitlines()


for line in lines:
    print(line.upper())
