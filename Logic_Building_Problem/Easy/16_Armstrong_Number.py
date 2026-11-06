
"""
Problem: Check Whether a Number Is an Armstrong Number.

Concepts:
- Variables
- Functions
- For Loop
- While Loop
- String Conversion
- Modulus Operator (%)
- Floor Division (//)
- Exponentiation Operator (**)

Approach 1: Using String Conversion
Time Complexity: O(d)
Space Complexity: O(d)

Approach 2: Using Mathematical Operations
Time Complexity: O(d)
Space Complexity: O(1)

Where d = Number of digits.
"""


def is_armstrong_using_string(number: int) -> bool:
    """Check whether a number is Armstrong using string conversion."""

    digits = str(number)
    power = len(digits)

    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == number


def is_armstrong_using_loop(number: int) -> bool:
    """Check whether a number is Armstrong using mathematical operations."""

    if number < 0:
        return False

    original_number = number
    power = len(str(number))
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** power
        number //= 10

    return total == original_number


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    result_string = is_armstrong_using_string(number)
    result_loop = is_armstrong_using_loop(number)

    print(
        f"String Approach: {number} is "
        f"{'an Armstrong Number' if result_string else 'not an Armstrong Number'}."
    )

    print(
        f"Mathematical Approach: {number} is "
        f"{'an Armstrong Number' if result_loop else 'not an Armstrong Number'}."
    )
