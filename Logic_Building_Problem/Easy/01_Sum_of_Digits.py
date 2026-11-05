
"""
Problem: Find the Sum of Digits of a Number.

Concepts:
- Variables
- Functions
- For Loop
- While Loop
- Type Conversion
- Modulus Operator (%)
- Floor Division (//)

Approach 1: Using For Loop
Time Complexity: O(d)
Space Complexity: O(d)

Approach 2: Using While Loop
Time Complexity: O(d)
Space Complexity: O(1)

Where d = Number of digits.
"""


def sum_of_digits_using_for(number: int) -> int:
    """Calculate the sum of digits using a for loop."""

    total = 0

    for digit in str(abs(number)):
        total += int(digit)

    return total


def sum_of_digits_using_while(number: int) -> int:
    """Calculate the sum of digits using a while loop."""

    number = abs(number)
    total = 0

    while number != 0:
        digit = number % 10
        total += digit
        number //= 10

    return total


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    result_for = sum_of_digits_using_for(number)
    result_while = sum_of_digits_using_while(number)

    print(f"Sum of Digits using For Loop: {result_for}")
    print(f"Sum of Digits using While Loop: {result_while}")
