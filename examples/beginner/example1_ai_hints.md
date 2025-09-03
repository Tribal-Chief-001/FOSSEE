# AI Debugging Hints: Beginner Example 1

## Goal
- Sum all numbers in a list.
- Observe the loop and indexing.

## Triage
- Possible bug: Indexing error when accessing list elements.
- Check loop boundaries.

## Guided Checks
1. Print `len(numbers)` and `i` inside the loop.
2. Print `numbers[i]` instead of `numbers[i+1]`.
3. Test loop with a smaller list (2-3 elements).

## Concept Nudge
- Lists are **0-indexed**.
- Using `i+1` might skip or go out of range.

## Probing Questions
1. What happens when `i` reaches the last index?
2. Can you access the last element safely?
3. How could `range()` be adjusted?

## Next Steps
- Try printing each element individually.
- Adjust indexing so all elements are included safely.
