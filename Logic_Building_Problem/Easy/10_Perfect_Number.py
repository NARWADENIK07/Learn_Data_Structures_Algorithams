
"""
Problem: Check Whether a Number Is a Perfect Number.

Concepts:
- Variables
- Functions
- For Loop
- Conditional Statements
- Modulus Operator (%)
- Square Root
- Divisors

Approach 1: Using Basic Loop
Time Complexity: O(n)
Space Complexity: O(1)

Approach 2: Using Square Root Optimization
Time Complexity: O(sqrt(n))
Space Complexity: O(1)
"""


def is_perfect_basic(number: int) -> bool:
    """Check whether a number is perfect using a basic loop."""

    if number <= 1:
        return False

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    return total == number


def is_perfect_optimized(number: int) -> bool:
    """Check whether a number is perfect using square root optimization."""

    if number <= 1:
        return False

    total = 1
    i = 2

    while i * i <= number:

        if number % i == 0:
            total += i

            if i != number // i:
                total += number // i

        i += 1

    return total == number


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    result_basic = is_perfect_basic(number)
    result_optimized = is_perfect_optimized(number)

    print(
        f"Basic Approach: {number} is "
        f"{'a Perfect Number' if result_basic else 'not a Perfect Number'}."
    )

    print(
        f"Optimized Approach: {number} is "
        f"{'a Perfect Number' if result_optimized else 'not a Perfect Number'}."
    )
