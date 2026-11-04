
"""
Problem: Sum of Squares of First N Natural Numbers.

Concepts:
- Variables
- While Loop
- Functions
- Mathematical Formula
- Arithmetic Operators

Approach 1: Using While Loop
Time Complexity: O(n)
Space Complexity: O(1)

Approach 2: Using Mathematical Formula
Time Complexity: O(1)
Space Complexity: O(1)
"""


def sum_of_squares_using_loop(number: int) -> int:
    """Calculate the sum of squares using a while loop."""

    total = 0
    start = 1

    while start <= number:
        square = start * start
        total += square
        start += 1

    return total


def sum_of_squares_using_formula(number: int) -> int:
    """Calculate the sum of squares using a mathematical formula."""

    return number * (number + 1) * (2 * number + 1) // 6


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    if number < 0:
        print("Please enter a non-negative number.")

    else:
        result_loop = sum_of_squares_using_loop(number)
        result_formula = sum_of_squares_using_formula(number)

        print(f"Sum of Squares using While Loop: {result_loop}")
        print(f"Sum of Squares using Formula: {result_formula}")
