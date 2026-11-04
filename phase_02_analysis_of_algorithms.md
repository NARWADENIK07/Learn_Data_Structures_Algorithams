# Phase 2: Analysis of Algorithms

Algorithm analysis helps us measure how efficient code is. Instead of only checking whether the program works, we also ask how fast it is and how much memory it uses.

## Core Topics

- What is an Algorithm?
- Why Algorithm Analysis?
- Time Complexity
- Space Complexity
- Best, Average and Worst Cases
- Big O Notation
- Big Omega Notation
- Big Theta Notation
- Constant Complexity
- Linear Complexity
- Logarithmic Complexity
- Quadratic Complexity
- Nested Loop Analysis
- Recursive Complexity
- Recurrence Relations
- Master Theorem
- Amortized Analysis
- Complexity Comparison

## Why It Matters

Two solutions may both be correct, but one may be much better for large input sizes. Complexity helps compare them systematically.

## Common Notations

- O(1): constant time
- O(log n): logarithmic time
- O(n): linear time
- O(n log n): efficient sorting and divide-and-conquer
- O(n²): quadratic time
- O(2^n): exponential time

## Visual Intuition

Imagine a program handling 10, 100, 1000, or 1,000,000 elements.

- O(1): same cost regardless of input size
- O(log n): grows slowly
- O(n): proportional to input size
- O(n log n): common in efficient sorting algorithms
- O(n²): rapidly grows and becomes expensive

## Analysis Techniques

- Count basic operations
- Ignore constant factors
- Focus on dominant terms
- Consider nested loops carefully
- Use recurrence relations for recursion

## Example

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

This has O(n²) time because the inner loop runs n times for each outer iteration.

## Practice Questions

- Compare O(n), O(n log n), and O(n²)
- Analyze a recursive function
- Find time complexity of nested loops
- Explain best, average, and worst cases for searching

## Goal

By the end of this phase, you should be able to estimate complexity, identify inefficient patterns, and reason about time and space trade-offs.
