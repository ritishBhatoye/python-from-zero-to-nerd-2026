"""Exercise 065 — Recursive Function f(n)=f(n-1)+100.

Compute f(n)=f(n-1)+100 where f(0)=0.
"""

# Your implementation here
pass


def func(n):
    if n == 0:
        return 0
    if n > 0:
        return (n - 1) + 100
