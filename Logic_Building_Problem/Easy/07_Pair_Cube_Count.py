
"""
Problem: Count Pairs Whose Cube Sum Equals a Given Number.

Concepts:
- Variables
- Functions
- Nested Loops
- Conditional Statements
- Exponentiation Operator (**)

Approach 1: Using Nested Loops

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def count_cube_sum_pairs(number: int) -> int:
    """Count pairs (i, j) satisfying i^3 + j^3 = number."""

    count = 0

    for i in range(1, number + 1):
        for j in range(1, number):
            if i**3 + j**3 == number:
                count += 1

    return count


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    if number <= 0:
        print("Please enter a positive number.")

    else:
        result = count_cube_sum_pairs(number)

        print(f"Number of valid pairs: {result}")
