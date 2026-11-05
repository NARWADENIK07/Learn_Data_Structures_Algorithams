
"""
Problem: Find LCM (Least Common Multiple) of Two Numbers.

Concepts:
- Variables
- Functions
- For Loop
- Conditional Statements
- Modulus Operator (%)
- max() and min()
- GCD / HCF

Approach 1: Using Multiples and Loop
Time Complexity: O(n) upper bound
Space Complexity: O(1)

Approach 2: Using GCD Formula
Time Complexity: O(log(min(n, m)))
Space Complexity: O(1)

Formula:
LCM(a, b) = abs(a * b) // GCD(a, b)
"""


def find_lcm_using_loop(n: int, m: int) -> int:
    """Calculate LCM by checking multiples of the larger number."""

    n = abs(n)
    m = abs(m)

    if n == 0 or m == 0:
        return 0

    greater = max(n, m)
    smaller = min(n, m)

    for i in range(greater, n * m + 1, greater):
        if i % smaller == 0:
            return i

    return 0


def find_gcd(n: int, m: int) -> int:
    """Calculate GCD using the Euclidean algorithm."""

    while m != 0:
        n, m = m, n % m

    return n


def find_lcm_using_gcd(n: int, m: int) -> int:
    """Calculate LCM using the GCD formula."""

    if n == 0 or m == 0:
        return 0

    return abs(n * m) // find_gcd(abs(n), abs(m))


if __name__ == "__main__":

    n = int(input("Enter first number (n): "))
    m = int(input("Enter second number (m): "))

    result_loop = find_lcm_using_loop(n, m)
    result_gcd = find_lcm_using_gcd(n, m)

    print(f"LCM using Loop: {result_loop}")
    print(f"LCM using GCD: {result_gcd}")
