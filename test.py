
"""
Problem: Find the K-th Digit of a Raised-to-Power Number

Description:
Calculate a^b and find the K-th digit from the right.
If K is invalid, display an appropriate message.

Concepts Used:
- Exponentiation
- While Loop
- Integer Division (//)
- Modulo Operator (%)
- Conditional Statements

Time Complexity: O(b log a + d)
Auxiliary Space: O(d)

Where:
d = Number of digits in a^b
"""


def find_kth_digit(a: int, b: int, k: int) -> int | None:
    """Return the K-th digit from the right in a^b."""

    if k <= 0:
        return None

    number = a ** b

    if k > len(str(number)):
        return None

    while k > 1:
        number //= 10
        k -= 1

    return number % 10


if __name__ == "__main__":

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    k = int(input("Enter k: "))

    result = find_kth_digit(a, b, k)

    if result is None:
        print("Digit does not exist.")
    else:
        print("K-th digit:", result)
