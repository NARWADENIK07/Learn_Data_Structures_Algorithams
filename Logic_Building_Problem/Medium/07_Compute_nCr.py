
"""
Problem: Calculate nCr (Combination)

Description:
Calculate the number of ways to select r items
from n items without considering their order.

Formula:
nCr = n! / (r! * (n-r)!)

Concepts Used:
- Factorial
- While Loop
- Multiplication
- Integer Division
- Conditional Statements

Time Complexity: O(n)
Auxiliary Space: O(1)
"""


def factorial(number: int) -> int:
    """Calculate the factorial of a non-negative integer."""

    result = 1

    while number >= 1:
        result *= number
        number -= 1

    return result


def calculate_ncr(n: int, r: int) -> int:
    """Calculate the combination nCr."""

    if n < 0 or r < 0 or r > n:
        raise ValueError("Invalid values: n must be >= r >= 0.")

    numerator = factorial(n)

    denominator = factorial(r) * factorial(n - r)

    return numerator // denominator


if __name__ == "__main__":

    n = int(input("Enter a value of n: "))
    r = int(input("Enter a value of r: "))

    try:
        result = calculate_ncr(n, r)
        print(f"{n}C{r} =", result)

    except ValueError as error:
        print(error)
