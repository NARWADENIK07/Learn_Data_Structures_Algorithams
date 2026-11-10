
"""
Problem: Convert a Fraction into a Decimal String

Description:
Convert a fraction a/b into its decimal representation.
If the fractional part repeats, enclose the repeating
digits in parentheses.

Concepts Used:
- Integer Division (//)
- Modulo Operator (%)
- Dictionary
- While Loop
- String Slicing
- XOR Operator (^)

Time Complexity: O(b)
Auxiliary Space: O(b)

Where:
b = Absolute value of the denominator
"""


def fraction_to_decimal(a: int, b: int) -> str:
    """Convert a fraction into a decimal string."""

    if b == 0:
        raise ValueError("Denominator cannot be zero.")

    if a == 0:
        return "0"

    result = "-" if (a < 0) ^ (b < 0) else ""

    a = abs(a)
    b = abs(b)

    result += str(a // b)

    remainder = a % b

    if remainder == 0:
        return result

    result += "."

    remainder_map = {}

    while remainder > 0:

        if remainder in remainder_map:
            position = remainder_map[remainder]

            result = (
                result[:position]
                + "("
                + result[position:]
                + ")"
            )
            break

        remainder_map[remainder] = len(result)

        remainder *= 10

        result += str(remainder // b)

        remainder %= b

    return result


if __name__ == "__main__":

    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    try:
        result = fraction_to_decimal(a, b)
        print("Decimal representation:", result)

    except ValueError as error:
        print(error)
