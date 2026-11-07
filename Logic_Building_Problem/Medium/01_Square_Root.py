
"""
Problem: Find the Integer Square Root of a Number.

Concepts:
- Variables
- Functions
- While Loop
- Conditional Statements
- Binary Search
- Integer Division

Approach 1: Using Linear Search
Time Complexity: O(sqrt(n))
Space Complexity: O(1)

Approach 2: Using Binary Search
Time Complexity: O(log n)
Space Complexity: O(1)

Note:
Return the floor value of the square root.
"""


def square_root_using_loop(number: int) -> int:
    """Find the integer square root using a while loop."""

    if number < 2:
        return number

    result = 1

    while result * result <= number:
        result += 1

    return result - 1


def square_root_using_binary_search(number: int) -> int:
    """Find the integer square root using binary search."""

    if number < 2:
        return number

    low = 1
    high = number
    result = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= number:
            result = mid
            low = mid + 1

        else:
            high = mid - 1

    return result


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    if number < 0:
        print("Please enter a non-negative number.")

    else:
        result_loop = square_root_using_loop(number)
        result_binary = square_root_using_binary_search(number)

        print(f"Square Root using Loop: {result_loop}")
        print(f"Square Root using Binary Search: {result_binary}")
