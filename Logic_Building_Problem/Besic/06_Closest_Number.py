
"""
Problem: Find the Closest Multiple of M to N.

Concepts:
- Variables
- Functions
- Floor Division (//)
- Absolute Value (abs)
- Conditional Statements
- List and max()

Approach: Using Floor Division and Distance Comparison

Time Complexity: O(1)
Space Complexity: O(1)
"""


def closest_multiple(n: int, m: int) -> int:
    """Return the closest multiple of M to N."""

    if m == 0:
        raise ValueError("M cannot be zero.")

    # Find quotient
    quotient = n // abs(m)

    # Find two nearby multiples
    first_multiple = quotient * abs(m)
    second_multiple = (quotient + 1) * abs(m)

    # Compare distances
    if abs(n - first_multiple) < abs(n - second_multiple):
        return first_multiple

    elif abs(n - first_multiple) == abs(n - second_multiple):
        return max(first_multiple, second_multiple, key=abs)

    else:
        return second_multiple


if __name__ == "__main__":

    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

    try:
        result = closest_multiple(n, m)
        print(f"The closest multiple of {m} to {n} is: {result}")

    except ValueError as error:
        print(error)
