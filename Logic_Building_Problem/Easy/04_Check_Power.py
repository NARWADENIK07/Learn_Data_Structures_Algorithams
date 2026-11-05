
"""
Problem: Check Whether Y Is a Power of X.

Concepts:
- Variables
- Functions
- Conditional Statements
- While Loop
- Modulus Operator (%)
- Floor Division (//)

Approach: Using Repeated Division

Time Complexity: O(log_x(y))
Space Complexity: O(1)
"""


def is_power_of_number(x: int, y: int) -> bool:
    """Check whether Y is a power of X."""

    if x <= 0 or y <= 0:
        return False

    if x == 1:
        return y == 1

    while y > 1 and y % x == 0:
        y //= x

    return y == 1


if __name__ == "__main__":

    x = int(input("Enter the base number (x): "))
    y = int(input("Enter the number to check (y): "))

    result = is_power_of_number(x, y)

    if result:
        print(f"{y} is a power of {x}.")
    else:
        print(f"{y} is not a power of {x}.")
