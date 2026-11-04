
"""
Problem: Find the Opposite Face of a Dice.

Concepts:
- Variables
- Functions
- Conditional Statements
- Arithmetic Operators

Approach: Using Mathematical Formula

Formula:
Opposite Face = 7 - Given Face

Time Complexity: O(1)
Space Complexity: O(1)
"""


def opposite_face(number: int) -> int:
    """Return the opposite face of a standard six-sided dice."""

    if number < 1 or number > 6:
        raise ValueError("Please enter a valid number between 1 and 6.")

    return 7 - number


if __name__ == "__main__":

    number = int(input("Enter a dice facing number (1-6): "))

    try:
        result = opposite_face(number)

        print(
            f"For dice facing number {number}, "
            f"the opposite face will have the number {result}."
        )

    except ValueError as error:
        print(error)
