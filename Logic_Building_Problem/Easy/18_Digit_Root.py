
"""
Problem: Find the Digital Root of a Number.

Concepts:
- Variables
- Functions
- While Loop
- Conditional Statements
- Modulus Operator (%)
- Floor Division (//)
- Mathematical Properties

Approach 1: Using Repeated Digit Addition
Time Complexity: O(d^2) worst case
Space Complexity: O(1)

Approach 2: Using Mathematical Formula
Time Complexity: O(1)
Space Complexity: O(1)

Where d = Number of digits.

Formula:
Digital Root = 1 + (n - 1) % 9, for n > 0.
"""


def digital_root_using_loop(number: int) -> int:
    """Calculate the digital root using repeated digit addition."""

    number = abs(number)

    result = 0

    while number > 0 or result > 9:

        # Start another iteration with the previous digit sum
        if number == 0:
            number = result
            result = 0

        result += number % 10
        number //= 10

    return result


def digital_root_using_formula(number: int) -> int:
    """Calculate the digital root using the mathematical formula."""

    number = abs(number)

    if number == 0:
        return 0

    return 1 + (number - 1) % 9


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    result_loop = digital_root_using_loop(number)
    result_formula = digital_root_using_formula(number)

    print(f"Digital Root using Loop: {result_loop}")
    print(f"Digital Root using Formula: {result_formula}")
