
"""
Problem: Count Numbers Having Exactly 3 Divisors

Description:
For every query number, count how many numbers
less than or equal to it have exactly 3 divisors.

Concepts Used:
- Prime Numbers
- Prime Squares
- Sieve of Eratosthenes
- Binary Search

Time Complexity:
O(M log log M + Q log P)

Auxiliary Space:
O(M)

Where:
M = square root of the maximum query
Q = number of queries
P = number of primes up to M
"""

from math import isqrt
from bisect import bisect_right


def sieve_of_eratosthenes(limit: int) -> list[int]:
    """Return all prime numbers up to the given limit."""

    is_prime = [True] * (limit + 1)

    if limit >= 0:
        is_prime[0] = False

    if limit >= 1:
        is_prime[1] = False

    for i in range(2, isqrt(limit) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [
        i for i in range(2, limit + 1)
        if is_prime[i]
    ]


def three_divisors(queries: list[int]) -> list[int]:
    """Count numbers with exactly 3 divisors for each query."""

    if not queries:
        return []

    max_limit = isqrt(max(queries))

    primes = sieve_of_eratosthenes(max_limit)

    ans = []

    for num in queries:
        if num < 0:
            ans.append(0)
            continue

        count = bisect_right(primes, isqrt(num))
        ans.append(count)

    return ans


if __name__ == "__main__":

    numbers = list(map(int, input(
        "Enter query numbers separated by spaces: "
    ).split()))

    result = three_divisors(numbers)

    print("Output:", result)
