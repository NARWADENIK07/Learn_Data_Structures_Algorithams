
"""
Problem: Add Two Fractions and Simplify the Result.

Concepts:
- Variables
- Functions
- Arithmetic Operators
- Recursion
- HCF / GCD
- Fraction Simplification
- Conditional Statements

Approach: Cross Multiplication + HCF

Time Complexity: O(log(min(|numerator|, denominator)))
Space Complexity: O(log(min(|numerator|, denominator)))
Due to recursive GCD calls.
"""


def find_hcf(n: int, m: int) -> int:
    """Calculate HCF using the Euclidean algorithm."""

    if m == 0:
        return abs(n)

    return find_hcf(m, n % m)


def add_fractions(n1: int, m1: int, n2: int, m2: int) -> tuple[int, int]:
    """Add two fractions and return the simplified numerator and denominator."""

    if m1 == 0 or m2 == 0:
        raise ValueError("Denominator cannot be zero.")

    # Calculate numerator and denominator
    numerator = n1 * m2 + n2 * m1
    denominator = m1 * m2

    # Keep denominator positive
    if denominator < 0:
        numerator = -numerator
        denominator = -denominator

    # Find HCF
    hcf = find_hcf(numerator, denominator)

    # Simplify the fraction
    numerator //= hcf
    denominator //= hcf

    return numerator, denominator


if __name__ == "__main__":

    n1 = int(input("Enter first numerator: "))
    m1 = int(input("Enter first denominator: "))

    n2 = int(input("Enter second numerator: "))
    m2 = int(input("Enter second denominator: "))

    try:
        numerator, denominator = add_fractions(n1, m1, n2, m2)

        print(f"Sum of fractions: {numerator}/{denominator}")

    except ValueError as error:
        print(error)
