
"""
Problem: Print the Multiplication Table of a Number.

Concepts:
- Functions
- For Loop
- Range Function
- Arithmetic Operators

Time Complexity: O(1) - Fixed 10 iterations
Space Complexity: O(1)
"""


def multiplication_table(number: int) -> None:
    """Print the multiplication table of the given number."""

    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    multiplication_table(number)
