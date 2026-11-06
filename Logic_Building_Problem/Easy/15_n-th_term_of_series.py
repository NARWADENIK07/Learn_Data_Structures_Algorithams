
"""
Problem: Find the Nth Term of the Triangular Number Series.

Series:
1, 3, 6, 10, 15, 21, 28, ...

Concepts:
- Variables
- Functions
- For Loop
- Arithmetic Operators
- Mathematical Formula

Approach 1: Using For Loop
Time Complexity: O(n)
Space Complexity: O(1)

Approach 2: Using Mathematical Formula
Time Complexity: O(1)
Space Complexity: O(1)

Formula:
Nth Term = n * (n + 1) // 2
"""


def find_nth_term_using_loop(number: int) -> int:
    """Find the Nth term using a for loop."""

    total = 0

    for i in range(1, number + 1):
        total += i

    return total


def find_nth_term_using_formula(number: int) -> int:
    """Find the Nth term using a mathematical formula."""

    return number * (number + 1) // 2


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    if number <= 0:
        print("Please enter a positive number.")

    else:
        result_loop = find_nth_term_using_loop(number)
        result_formula = find_nth_term_using_formula(number)

        print(f"Nth Term using Loop: {result_loop}")
        print(f"Nth Term using Formula: {result_formula}")
