
"""
Problem: Find HCF (Highest Common Factor) of Two Numbers.

Concepts:
- Variables
- Functions
- Recursion
- Conditional Statements
- Modulus Operator (%)
- Euclidean Algorithm

Approach 1: Using Recursive Subtraction
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m)) due to recursion stack.

Approach 2: Using Euclidean Algorithm
Time Complexity: O(log(min(n, m)))
Space Complexity: O(log(min(n, m))) due to recursion stack.
"""


def find_hcf_using_subtraction(n: int, m: int) -> int:
    """Calculate HCF using recursive subtraction."""

    n = abs(n)
    m = abs(m)

    if n == 0:
        return m

    if m == 0:
        return n

    if n > m:
        return find_hcf_using_subtraction(n - m, m)

    return find_hcf_using_subtraction(n, m - n)


def find_hcf_using_euclidean(n: int, m: int) -> int:
    """Calculate HCF using the optimized Euclidean algorithm."""

    n = abs(n)
    m = abs(m)

    if m == 0:
        return n

    return find_hcf_using_euclidean(m, n % m)


if __name__ == "__main__":

    n = int(input("Enter first number (n): "))
    m = int(input("Enter second number (m): "))

    if n == 0 and m == 0:
        print("HCF is undefined for two zeros.")

    else:
        result_subtraction = find_hcf_using_subtraction(n, m)
        result_euclidean = find_hcf_using_euclidean(n, m)

        print(f"HCF using Subtraction: {result_subtraction}")
        print(f"HCF using Euclidean Algorithm: {result_euclidean}")
