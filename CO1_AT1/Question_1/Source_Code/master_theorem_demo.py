"""
master_theorem_demo.py
A small demo to compute T(n) from the recurrence T(n) = 4 T(n/2) + n with T(1)=1
and show that T(n) = Theta(n^2). This script computes exact values for n = 2^k
and prints T(n) and the ratio T(n) / n^2 to show the growth.
"""

import math

from functools import lru_cache

@lru_cache(None)
def T(n):
    if n <= 1:
        return 1
    # ensure n is integer power of two
    return 4 * T(n // 2) + n


def main():
    print("Computing T(n) for recurrence T(n)=4*T(n/2)+n with T(1)=1")
    print("n\tT(n)\tT(n)/n^2")
    for k in range(0, 11):
        n = 2 ** k
        val = T(n)
        ratio = val / (n * n)
        print(f"{n}\t{val}\t{ratio:.6f}")

    print("\nConclusion: T(n)/n^2 approaches a constant => T(n) = Theta(n^2)")

if __name__ == '__main__':
    main()
