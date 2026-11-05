
"""
Problem: Reverse a Number.

Concepts:
- Variables
- Functions
- String Slicing
- While Loop
- Modulus Operator (%)
- Floor Division (//)

Approach 1: Using String Slicing
Time Complexity: O(d)
Space Complexity: O(d)

Approach 2: Using Mathematical Operations
Time Complexity: O(d)
Space Complexity: O(1)

Where d = Number of digits.
"""


def reverse_using_string(number: int) -> int:
    """Reverse a number using string slicing."""

    reversed_number = str(abs(number))[::-1]

    result = int(reversed_number)

    return -result if number < 0 else result


def reverse_using_loop(number: int) -> int:
    """Reverse a number using mathematical operations."""

    sign = -1 if number < 0 else 1
    number = abs(number)

    reversed_number = 0

    while number > 0:
        digit = number % 10

        reversed_number = reversed_number * 10 + digit

        number //= 10

    return sign * reversed_number


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    result_string = reverse_using_string(number)
    result_loop = reverse_using_loop(number)

    print(f"Reversed Number using String Slicing: {result_string}")
    print(f"Reversed Number using While Loop: {result_loop}")
