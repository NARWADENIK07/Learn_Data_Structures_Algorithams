
"""
Problem: Find the Day of the Week for a Given Date.

Concepts:
- Variables
- Functions
- For Loops
- Lists
- Conditional Statements
- Leap Year
- Modulus Operator (%)
- Date Calculation

Approach: Counting Total Days from 01-01-0001

Time Complexity: O(year + month)
Space Complexity: O(1)

Note:
01-01-0001 was Monday in the Gregorian calendar.
"""


def is_leap_year(year: int) -> bool:
    """Check whether a year is a leap year."""

    return (year % 400 == 0) or (
        year % 4 == 0 and year % 100 != 0
    )


def get_day_of_week(date: list[int]) -> str:
    """Find the weekday for a given date [day, month, year]."""

    day, month, year = date

    days_in_month = [
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]

    weekdays = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    # Validate year and month
    if year < 1 or month < 1 or month > 12:
        raise ValueError("Please enter a valid date.")

    # Handle leap year
    if is_leap_year(year):
        days_in_month[1] = 29

    # Validate day
    if day < 1 or day > days_in_month[month - 1]:
        raise ValueError("Invalid day for the given month.")

    total_days = 0

    # Count complete years before the given year
    for y in range(1, year):
        total_days += 366 if is_leap_year(y) else 365

    # Count complete months before the given month
    for m in range(month - 1):
        total_days += days_in_month[m]

    # Count days before the given date
    total_days += day - 1

    # Calculate weekday
    return weekdays[total_days % 7]


if __name__ == "__main__":

    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    try:
        result = get_day_of_week([day, month, year])

        print(f"Day of the week: {result}")

    except ValueError as error:
        print(error)
