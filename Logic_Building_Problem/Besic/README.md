# Basic Python Logic-Building Exercises

This folder contains beginner-friendly Python programs for practicing
conditions, loops, arithmetic, functions, and simple problem-solving.

## Exercises

| File | Problem | Main concepts |
| --- | --- | --- |
| [`01_ Check_Even_or_Odd.py`](01_%20Check_Even_or_Odd.py) | Check whether a number is even or odd | Functions, conditionals, modulo |
| [`02_Multiplication_Table.py`](02_Multiplication_Table.py) | Print a multiplication table | Functions, `for` loops, `range()` |
| [`03_Sum_of_Natural_Numbers.py`](03_Sum_of_Natural_Numbers.py) | Sum the first *n* natural numbers | `while` loops, arithmetic formulas |
| [`04_Sum_of_Squares.py`](04_Sum_of_Squares.py) | Sum the squares of the first *n* natural numbers | `while` loops, arithmetic formulas |
| [`05_Swap_two_Numbers.py`](05_Swap_two_Numbers.py) | Swap two numbers | Functions, tuple unpacking |
| [`06_Closest_Number.py`](06_Closest_Number.py) | Find the multiple of *m* closest to *n* | Floor division, absolute values, conditionals |
| [`07_Dice_Problem.py`](07_Dice_Problem.py) | Find the opposite face of a standard die | Functions, validation, arithmetic |

## Run an exercise

Run a script from this folder with Python. For example:

```bash
python 07_Dice_Problem.py
```

Each script runs independently and asks for input where needed. Several
scripts also define functions that can be imported and tested separately.

## Suggested practice routine

1. Read the problem and identify its inputs and expected output.
2. Trace the approach with a small example before running the code.
3. Run the script with typical values and any relevant edge cases.
4. Compare alternative approaches where provided, such as a loop and a
   formula.
5. Explain the time and space complexity in your own words.

The loop-based summation solutions take `O(n)` time; their formula-based
alternatives take `O(1)` time. The multiplication-table script always prints
ten rows, so its work is constant with respect to the input.
