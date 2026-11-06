
"""
Problem: Find the Nth Fibonacci Number.

Concepts:
- Variables
- Functions
- For Loop
- Recursion
- Conditional Statements
- Multiple Assignment

Approach 1: Using Iteration
Time Complexity: O(n)
Space Complexity: O(1)

Approach 2: Using Recursion
Time Complexity: O(2^n)
Space Complexity: O(n)

Fibonacci Series:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""


def fibonacci_using_loop(number: int) -> int:
    """Find the Nth Fibonacci number using iteration."""

    if number <= 1:
        return number

    prev1 = 1
    prev2 = 0

    for i in range(2, number + 1):
        curr = prev1 + prev2

        prev2 = prev1
        prev1 = curr

    return curr


def fibonacci_using_recursion(number: int) -> int:
    """Find the Nth Fibonacci number using recursion."""

    if number <= 1:
        return number

    return (
        fibonacci_using_recursion(number - 1)
        + fibonacci_using_recursion(number - 2)
    )


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    if number < 0:
        print("Please enter a non-negative number.")

    else:
        result_loop = fibonacci_using_loop(number)
        result_recursion = fibonacci_using_recursion(number)

        print(f"Fibonacci using Loop: {result_loop}")
        print(f"Fibonacci using Recursion: {result_recursion}")
