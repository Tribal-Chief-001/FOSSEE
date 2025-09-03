# AI Debugging Hints: Intermediate Example 1

## Goal
- Compute squares of all numbers in a list.

## Triage
- Bug likely caused by **removing elements unintentionally**.

## Guided Checks
1. Print `squared` after loop but before `pop()`.
2. Comment out the `pop()` line and see output.
3. Verify number of elements in `squared`.

## Concept Nudge
- `.pop()` removes an element; ensure it's intended.
- Check workflow: loop → append → modification.

## Probing Questions
1. Why is the last element missing?
2. Do you need `pop()` at all?
3. Could `.append()` already do the job?

## Next Steps
- Remove unintended modification.
- Validate list length and content.
