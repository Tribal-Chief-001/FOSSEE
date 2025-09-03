# AI Debugging Hints: Advanced Example 1

## Goal
- Compute factorial of any non-negative integer.

## Triage
- Bug likely due to **incorrect base case** for recursion.

## Guided Checks
1. Test `factorial(0)` and `factorial(1)`.
2. Print recursive calls with `n` at each step.
3. Verify termination condition.

## Concept Nudge
- Factorial of 0 is defined as 1.
- Base case must cover all stopping conditions.

## Probing Questions
1. What happens if n=0?
2. How does recursion stop?
3. Can base case include multiple values?

## Next Steps
- Adjust base case.
- Test edge cases (0, 1, 5, 10).
