
"""
Problem: Convert a Decimal Number to Binary.

Concepts:
- Variables
- Functions
- While Loop
- Lists
- String Join
- List Reversing
- Modulus Operator (%)
- Floor Division (//)
- Bitwise Operators

Approach 1: Using Repeated Division
Time Complexity: O(log n)
Space Complexity: O(log n)

Approach 2: Using Bitwise Operations
Time Complexity: O(log n)
Space Complexity: O(log n)
"""


def decimal_to_binary_using_division(number: int) -> str:
    """Convert a decimal number to binary using repeated division."""

    if number == 0:
        return "0"

    binary = []

    while number > 0:
        binary.append(str(number % 2))
        number //= 2

    return "".join(binary[::-1])


def decimal_to_binary_using_bitwise(number: int) -> str:
    """Convert a decimal number to binary using bitwise operations."""

    if number == 0:
        return "0"

    binary = []

    while number > 0:
        binary.append(str(number & 1))
        number >>= 1

    return "".join(binary[::-1])


if __name__ == "__main__":

    number = int(input("Enter a decimal number: "))

    if number < 0:
        print("Please enter a non-negative number.")

    else:
        result_division = decimal_to_binary_using_division(number)
        result_bitwise = decimal_to_binary_using_bitwise(number)

        print(f"Binary using Division: {result_division}")
        print(f"Binary using Bitwise Operations: {result_bitwise}")
