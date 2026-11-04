
"""
Problem: Check Whether a Number Is Even or Odd.

Concepts:
- Functions
- Conditional Statements
- Modulus Operator (%)

Time Complexity: O(1)
Space Complexity: O(1)
"""


def is_even_or_odd(number: int) -> str:
    """Return Even or Odd based on the given number."""

    if number % 2 == 0:
        return "Even"

    return "Odd"


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    result = is_even_or_odd(number)

    print(f"{number} is {result}.")
