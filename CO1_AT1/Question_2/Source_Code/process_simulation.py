#!/usr/bin/env python3
"""
process_simulation.py
Simulate and time an algorithm following the recurrence T(n) = 4 T(n/2) + n.
This script implements a recursive "process_side" that splits the input size in half
and calls itself four times (to model 4T(n/2)) plus a linear amount of work O(n).
It times runs for a sequence of n values and prints time and time / n^2 to show
that T(n) is Theta(n^2) as predicted by the master theorem.

Usage examples:
  python3 process_simulation.py --min-k 4 --max-k 9
  python3 process_simulation.py --n 256 --repeats 5

This file belongs in: CO1_AT1/Question_2/Source_Code/process_simulation.py
"""

import time
import argparse
import sys


def process_side(n):
    """Work that uses 4 recursive calls on half-size plus linear work.

    For this simulation we do the "recursive" part by actually calling
    process_side on n//2 four times, and do Theta(n) local work by looping.
    For very small n we just do the base-case linear work.
    """
    if n <= 1:
        # base work: constant time
        return None

    # do Theta(n) local work (simple loop) to simulate the + n term
    s = 0
    for i in range(n):
        s += (i & 1)

    # recursive part: 4 calls on n/2
    half = n // 2
    # if n is odd, floor keeps sizes integral; for this simulation we prefer powers of two.
    process_side(half)
    process_side(half)
    process_side(half)
    process_side(half)
    return None


def time_run(n, repeats=1):
    """Time a single run of process_side(n). Repeat to reduce noise."""
    # Warmup run (not timed) for JIT/OS effects (less important in CPython, but okay)
    # Note: skip warmup when n is large to avoid extra cost
    if repeats > 1 and n <= 512:
        process_side(n)

    t0 = time.perf_counter()
    for _ in range(repeats):
        process_side(n)
    t1 = time.perf_counter()
    return (t1 - t0) / repeats


def main():
    parser = argparse.ArgumentParser(description="Simulate recurrence T(n)=4T(n/2)+n and time runs.")
    parser.add_argument("--min-k", type=int, default=4,
                        help="minimum exponent k for n=2^k (default 4 -> n=16)")
    parser.add_argument("--max-k", type=int, default=9,
                        help="maximum exponent k for n=2^k (default 9 -> n=512)")
    parser.add_argument("--n", type=int, default=None,
                        help="run a single n instead of a range of powers of two")
    parser.add_argument("--repeats", type=int, default=3,
                        help="number of repeats for each timed run to reduce noise")

    args = parser.parse_args()

    if args.n is not None:
        ns = [args.n]
    else:
        if args.min_k > args.max_k:
            print("min-k must be <= max-k", file=sys.stderr)
            return
        ns = [2 ** k for k in range(args.min_k, args.max_k + 1)]

    print("Simulating recurrence T(n)=4T(n/2)+n")
    print("Note: keep n modest (powers of two recommended) to avoid huge runtimes.")
    print("{:>8} {:>12} {:>12}".format("n", "time (s)", "time / n^2"))
    for n in ns:
        # choose repeats to reduce noise for very small n
        repeats = args.repeats
        if n <= 64 and repeats < 5:
            repeats = 5
        # caution: large n may take long; warn and confirm
        if n > 2048:
            print(f"warning: n={n} may take a very long time. Skipping. (Use smaller n)", file=sys.stderr)
            continue
        t = time_run(n, repeats=repeats)
        ratio = t / (n * n) if n > 0 else float('inf')
        print("{:8d} {:12.6f} {:12.6e}".format(n, t, ratio))

    print("\nInterpretation:")
    print("If the algorithm follows T(n)=4T(n/2)+n, theory predicts T(n) = Theta(n^2).")
    print("The column 'time / n^2' should be approximately constant across n (subject to overheads).")


if __name__ == "__main__":
    main()
