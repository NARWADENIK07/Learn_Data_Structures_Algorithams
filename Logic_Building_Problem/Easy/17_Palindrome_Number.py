
"""
Problem: Check Whether a Number Is a Palindrome.

Concepts:
- Variables
- Functions
- Conditional Statements
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


def is_palindrome_using_string(number: int) -> bool:
    """Check whether a number is palindrome using string slicing."""

    reversed_number = int(str(number)[::-1])

    return number >= 0 and reversed_number == number


def is_palindrome_using_loop(number: int) -> bool:
    """Check whether a number is palindrome using mathematical operations."""

    if number < 0:
        return False

    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10

        reversed_number = reversed_number * 10 + digit

        number //= 10

    return original_number == reversed_number


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    result_string = is_palindrome_using_string(number)
    result_loop = is_palindrome_using_loop(number)

    print(
        f"String Approach: {number} is "
        f"{'a Palindrome' if result_string else 'not a Palindrome'}."
    )

    print(
        f"Mathematical Approach: {number} is "
        f"{'a Palindrome' if result_loop else 'not a Palindrome'}."
    )
