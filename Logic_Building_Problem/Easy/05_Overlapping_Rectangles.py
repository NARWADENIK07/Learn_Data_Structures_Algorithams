
"""
Problem: Check Whether Two Rectangles Overlap.

Concepts:
- Variables
- Functions
- Lists
- Conditional Statements
- Coordinate Geometry
- Logical Operators (and, or)

Approach: Using Rectangle Coordinates

Coordinate Representation:
- l1: Top-left coordinate of Rectangle 1
- r1: Bottom-right coordinate of Rectangle 1
- l2: Top-left coordinate of Rectangle 2
- r2: Bottom-right coordinate of Rectangle 2

Time Complexity: O(1)
Space Complexity: O(1)
"""


def do_overlap(
    l1: list[int],
    r1: list[int],
    l2: list[int],
    r2: list[int]
) -> bool:
    """Check whether two rectangles overlap."""

    # Check if one rectangle is completely left of the other
    if l1[0] > r2[0] or l2[0] > r1[0]:
        return False

    # Check if one rectangle is completely above the other
    if l1[1] < r2[1] or l2[1] < r1[1]:
        return False

    return True


if __name__ == "__main__":

    # Test Case 1: Overlapping rectangles
    l1, r1 = [0, 10], [10, 0]
    l2, r2 = [5, 5], [15, 0]

    result1 = do_overlap(l1, r1, l2, r2)

    print(f"Test Case 1: {str(result1).lower()}")

    # Test Case 2: Non-overlapping rectangles
    l3, r3 = [0, 2], [1, 1]
    l4, r4 = [-2, 0], [0, -3]

    result2 = do_overlap(l3, r3, l4, r4)

    print(f"Test Case 2: {str(result2).lower()}")
