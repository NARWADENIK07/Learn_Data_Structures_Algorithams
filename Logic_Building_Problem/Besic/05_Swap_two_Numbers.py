
"""
Problem: Swap Two Numbers.

Concepts:
- Variables
- Functions
- Tuple Unpacking
- Multiple Assignment

Approach: Using Python Tuple Unpacking

Time Complexity: O(1)
Space Complexity: O(1)
"""


def swap_numbers(a: int, b: int) -> tuple[int, int]:
    """Swap two numbers and return their updated values."""

    a, b = b, a

    return a, b


if __name__ == "__main__":

    a = int(input("Enter first number (a): "))
    b = int(input("Enter second number (b): "))

    a, b = swap_numbers(a, b)

    print(f"After swapping:")
    print(f"a = {a}")
    print(f"b = {b}")
