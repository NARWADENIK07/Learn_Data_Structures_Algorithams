
"""
Problem: Check Whether a Number Is Divisible by 11

Description:
Check whether a given number is exactly divisible by 11.

Concepts Used:
- Conditional Statements
- Modulo Operator (%)

Time Complexity: O(1)
Auxiliary Space: O(1)
"""


def is_divisible_by_11(number: int) -> bool:
    """Return True if the number is divisible by 11."""
    return number % 11 == 0


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    if is_divisible_by_11(number):
        print(f"{number} is divisible by 11.")
    else:
        print(f"{number} is not divisible by 11.")
