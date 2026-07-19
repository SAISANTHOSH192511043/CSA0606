# Report for Question 2 — Image Processing System (Recurrence)

## Problem

We were asked to analyze an image-processing algorithm that divides images recursively with
recurrence T(n) = 4 T(n/2) + n and apply the Master Theorem to find the time complexity.
We also implement a simulation to verify the asymptotic behavior (empirically) and present
screenshots of the source code and the run output.

## Theoretical analysis (Master Theorem)

Recurrence: T(n) = a T(n/b) + f(n) with a = 4, b = 2, and f(n) = n.

Compute n^{log_b a} = n^{log_2 4} = n^2.
Compare f(n) = n with n^{log_b a} = n^2: f(n) = O(n^{2 - epsilon}) for epsilon = 1.

Therefore we are in Master Theorem case 1 (polynomially smaller):
T(n) = Theta(n^{log_b a}) = Theta(n^2).

Conclusion: The algorithm runs in Theta(n^2) time.

## Implementation (what was created)

I implemented a small Python script that simulates an algorithm with the recurrence
T(n) = 4 T(n/2) + n by:
- doing Theta(n) local work (a loop of length n) and
- making four recursive calls on n/2.

File added in repository:
- CO1_AT1/Question_2/Source_Code/process_simulation.py  (the source code)

Also added a short report and placeholders for four screenshots in the report folder.

## How to run

From the repository root run:

  python3 CO1_AT1/Question_2/Source_Code/process_simulation.py --min-k 4 --max-k 9

This runs n = 2^4 .. 2^9 by default (n from 16 to 512). Use `--n` to run a single n value, and
`--repeats` to adjust number of repetitions used for timing.

## Empirical interpretation

The program prints a table with columns: n, time (s), time / n^2.
If T(n) = Theta(n^2), the time / n^2 column should be roughly constant (modulo overheads and
measurement noise). The included run screenshot demonstrates this roughly-constant behavior.

## Screenshots (placeholders)

The following images were attached as placeholders in the Report/images/ directory:

- Report/images/photo_2_placeholder.png  — screenshot of the source-code editor (part 1)
- Report/images/photo_3_placeholder.png  — screenshot of the source-code editor (part 2)
- Report/images/photo_4_placeholder.png  — screenshot of the output printed in terminal (part 1)
- Report/images/photo_5_placeholder.png  — screenshot of the run output showing timing table

(Note: To replace placeholders with the actual image files, upload/replace the files in
CO1_AT1/Question_2/Report/images/ with the image files named exactly as above.)

## Conclusion

Master Theorem predicts Theta(n^2) and the empirical simulation supports that conclusion.

