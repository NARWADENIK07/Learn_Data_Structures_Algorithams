
"""
Problem: Check Whether a Number Is Prime.

Concepts:
- Variables
- Functions
- Conditional Statements
- For Loop
- Break Statement
- For-Else Statement
- Modulus Operator (%)
- Square Root

Approach 1: Basic Approach
Time Complexity: O(n)
Space Complexity: O(1)

Approach 2: Optimized Approach (Square Root)
Time Complexity: O(sqrt(n))
Space Complexity: O(1)
"""


def is_prime_basic(number: int) -> bool:
    """Check whether a number is prime using the basic approach."""

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def is_prime_optimized(number: int) -> bool:
    """Check whether a number is prime using the square root approach."""

    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    result_basic = is_prime_basic(number)
    result_optimized = is_prime_optimized(number)

    print(
        f"Basic Approach: "
        f"{number} is {'Prime' if result_basic else 'Not Prime'}."
    )

    print(
        f"Optimized Approach: "
        f"{number} is {'Prime' if result_optimized else 'Not Prime'}."
    )
