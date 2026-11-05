
"""
Problem: Find the Factorial of a Number.

Concepts:
- Variables
- Functions
- While Loop
- Recursion
- Conditional Statements
- Multiplication

Approach 1: Using While Loop
Time Complexity: O(n)
Space Complexity: O(1)

Approach 2: Using Recursion
Time Complexity: O(n)
Space Complexity: O(n)
"""


def factorial_using_loop(number: int) -> int:
    """Calculate the factorial of a number using a while loop."""

    factorial = 1
    i = 2

    while i <= number:
        factorial *= i
        i += 1

    return factorial


def factorial_using_recursion(number: int) -> int:
    """Calculate the factorial of a number using recursion."""

    if number == 0 or number == 1:
        return 1

    return number * factorial_using_recursion(number - 1)


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    if number < 0:
        print("Factorial is not defined for negative numbers.")

    else:
        result_loop = factorial_using_loop(number)
        result_recursion = factorial_using_recursion(number)

        print(f"Factorial using While Loop: {result_loop}")
        print(f"Factorial using Recursion: {result_recursion}")
