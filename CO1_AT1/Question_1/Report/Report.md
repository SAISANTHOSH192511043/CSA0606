# Report — Q38: Application: Image Processing System

Problem (Q38).
An image processing algorithm divides images recursively:

T(n) = 4 T(n/2) + n.

Apply the Master Theorem to find the time complexity. Clearly identify parameters and case selection. Analyze how performance changes with image size.

---

Step-by-step solution

1) Identify a, b, and f(n).
   - a = 4 (number of subproblems)
   - b = 2 (each subproblem has size n/2)
   - f(n) = n (the extra work outside recursion at each level)

2) Compute n^{log_b a}.
   - log_b a = log_2 4 = 2
   - therefore n^{log_b a} = n^2

3) Compare f(n) with n^{log_b a}.
   - f(n) = n
   - n = O(n^{2 - 1}) = O(n^{2 - epsilon}) with epsilon = 1
   - So f(n) is polynomially smaller than n^{log_b a} (case 1 of the Master Theorem)

4) Apply Master Theorem (Case 1).
   - Case 1: if f(n) = O(n^{log_b a - epsilon}) for some epsilon > 0,
     then T(n) = Theta(n^{log_b a}).
   - Here, T(n) = Theta(n^2).

5) Interpretation for image processing (how performance changes with image size)
   - Two common interpretations of the variable n:
     a) n is the linear dimension (width) of the image (e.g., an n x n image):
        - The recurrence T(n) = 4T(n/2) + n fits the divide-into-quadrants model where
          each recursive call handles one quadrant of linear size n/2, and the extra work
          at each level (f(n)) is proportional to the boundary or a linear pass over
          rows/columns (hence f(n)=Theta(n)).
        - Master Theorem gives T(n) = Theta(n^2). If the image has W x W pixels and n=W,
          then runtime is Theta(W^2) — proportional to the total number of pixels.
     b) n is the total number of pixels (N = W^2):
        - If we reparameterize with N pixels, note that dividing into 4 subimages means
          each subproblem has N/4 pixels; the recurrence in terms of N would be
          T(N) = 4 T(N/4) + sqrt(N). This changes the comparison; after re-analysis,
          you still get T(N) = Theta(N) (equivalently Theta(W^2)). The key point is
          the algorithm runs proportional to the total number of pixels.

   - Practical meaning: doubling the linear image dimension (width) multiplies the work
     by ~4 (quadratic). Doubling the total number of pixels (keeping width proportional)
     doubles the work.

6) Final complexity
   - T(n) = Theta(n^2) (when n is the linear dimension). Equivalently, runtime is
     Theta(N) where N is the number of pixels (N = n^2).

---

Files provided
- Source code: master_theorem_demo.py (in Source_Code folder) — runs a small numeric demo showing T(n)/n^2 tends to a constant.
- Four placeholder photos are included in Supporting_files/ as SVG images. Replace them with your real photos/screenshots if required.

Notes for submission
- The repository follows the requested structure:
  CO1_AT1/
  └─ Question_1/
     ├─ Source_Code/
     ├─ Report/
     └─ Supporting_files/

- To demonstrate the program output, run the Python demo. The SVG files are vector images and can be opened in a browser.

