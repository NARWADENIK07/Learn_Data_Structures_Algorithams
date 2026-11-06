# 02. Reverse a Number

`<sub>`{=html}Difficulty: Easy · Topic: Programming Fundamentals ·
Language: Python`</sub>`{=html}

Learn how to reverse the digits of an integer. In this problem, you will
practise string slicing, loops, modulus (`%`), floor division (`//`),
and handling negative numbers.

------------------------------------------------------------------------

## 1. Problem statement

Given an integer, reverse the order of its digits and return the
reversed number.

     Input   Reversed output
  -------- -----------------
    `1234`            `4321`
     `560`              `65`
       `7`               `7`
       `0`               `0`
    `-246`            `-642`

**Important:** The solutions return an integer. Therefore, leading
zeroes in the reversed result are not displayed. For example, reversing
`560` produces the integer `65`, not `065`.

For negative numbers, the minus sign stays at the beginning. Only the
digits are reversed.

## 2. Concepts you will practise

  Concept                 Why it is useful here
  ----------------------- ------------------------------------------
  Variables               Store the input and reversed number
  Functions               Keep each solution reusable
  String conversion       Convert a number into text
  String slicing          Reverse the characters in a string
  `while` loop            Process digits one at a time
  Modulus (`%`)           Extract the last digit
  Floor division (`//`)   Remove the last digit
  Arithmetic              Build the reversed number digit by digit

### Two operators to understand first

For `number = 123`:

  Expression      Result Meaning
  ------------- -------- ------------------------
  `123 % 10`         `3` Extract the last digit
  `123 // 10`       `12` Remove the last digit

The mathematical approach uses these operations to take digits from
right to left.

## 3. Approach 1 --- Using string slicing

### Idea

Convert the number to a string, reverse the string using slicing, and
convert the result back into an integer.

Python's `[::-1]` slicing syntax reads a sequence backwards.

### Step-by-step example

Suppose the input is `1234`.

1.  Convert the number to a string: `"1234"`.
2.  Reverse the string using `[::-1]`: `"4321"`.
3.  Convert the reversed string into an integer: `4321`.
4.  If the original number was negative, put the negative sign back.

    Step Operation          Result
  ------ ------------------ ----------
       1 `str(abs(1234))`   `"1234"`
       2 `"1234"[::-1]`     `"4321"`
       3 `int("4321")`      `4321`

### Visual flow

``` mermaid
flowchart TD
    A["Start: receive number"] --> B["Remember whether number is negative"]
    B --> C["Convert absolute value to string"]
    C --> D["Reverse string using [::-1]"]
    D --> E["Convert reversed string to integer"]
    E --> F{"Was original number negative?"}
    F -- "Yes" --> G["Return negative result"]
    F -- "No" --> H["Return positive result"]
    G --> I["End"]
    H --> I
```

### Python solution

``` python
def reverse_using_string(number: int) -> int:
    """Reverse a number using string slicing."""

    reversed_number = str(abs(number))[::-1]

    result = int(reversed_number)

    return -result if number < 0 else result
```

### Understand the important lines

-   `abs(number)` gets the non-negative magnitude of the number.
-   `str(...)` converts the number into a string.
-   `[::-1]` reverses the string.
-   `int(reversed_number)` converts the reversed digits back into an
    integer.
-   `return -result if number < 0 else result` restores the negative
    sign when needed.

## 4. Approach 2 --- Using a `while` loop and mathematical operations

### Idea

Build the reversed number one digit at a time.

1.  Extract the last digit using `% 10`.
2.  Move the existing reversed number one decimal place to the left by
    multiplying it by `10`.
3.  Add the extracted digit.
4.  Remove the last digit from the original number using `// 10`.
5.  Repeat until the original number becomes `0`.

### The key formula

``` python
reversed_number = reversed_number * 10 + digit
```

For example, if `reversed_number` is `43` and the next digit is `2`:

``` text
43 * 10 + 2
= 430 + 2
= 432
```

### Step-by-step dry run

Input: `number = 1234`

Initial values:

``` text
number = 1234
reversed_number = 0
```

  ----------------------------------------------------------------------------
       Iteration      Extracted Calculation        New reversed      Remaining
                          digit                          number         number
  -------------- -------------- ---------------- -------------- --------------
               1              4 `0 * 10 + 4`                  4            123

               2              3 `4 * 10 + 3`                 43             12

               3              2 `43 * 10 + 2`               432              1

               4              1 `432 * 10 + 1`             4321              0
  ----------------------------------------------------------------------------

When the original number becomes `0`, the loop stops.

Final answer: **4321**

### Visualise the digit extraction

``` mermaid
flowchart TD
    A["Start: number = 1234, reversed = 0"] --> B["digit = number % 10"]
    B --> C["reversed = reversed * 10 + digit"]
    C --> D["number = number // 10"]
    D --> E{"Is number greater than 0?"}
    E -- "Yes" --> B
    E -- "No" --> F["Apply original sign"]
    F --> G["Return reversed number"]
```

### Python solution

``` python
def reverse_using_loop(number: int) -> int:
    """Reverse a number using mathematical operations."""

    sign = -1 if number < 0 else 1
    number = abs(number)

    reversed_number = 0

    while number > 0:
        digit = number % 10

        reversed_number = reversed_number * 10 + digit

        number //= 10

    return sign * reversed_number
```

### Understand the important lines

-   `sign = -1 if number < 0 else 1` remembers whether the input is
    negative.
-   `number = abs(number)` lets the loop process only the digits.
-   `number % 10` extracts the last digit.
-   `reversed_number * 10 + digit` appends that digit to the reversed
    number.
-   `number //= 10` removes the digit that was just processed.
-   `return sign * reversed_number` restores the original sign.

## 5. Compare both approaches

  Comparison                   String slicing       Mathematical operations
  ---------------------------- -------------------- ----------------------------
  Main idea                    Reverse the string   Extract and rebuild digits
  Uses string conversion       Yes                  No
  Uses a loop explicitly       No                   Yes
  Time complexity              `O(d)`               `O(d)`
  Auxiliary space complexity   `O(d)`               `O(1)`

Here, `d` is the number of digits in the input.

### What does the complexity mean?

-   **Time complexity `O(d)`:** Each approach processes a number of
    characters or digits proportional to the number of digits.
-   **Space complexity `O(d)` for string slicing:** The string
    representation and reversed string require storage proportional to
    the number of digits.
-   **Space complexity `O(1)` for the mathematical approach:** It uses a
    fixed number of extra variables, regardless of the number of digits.

The string approach is concise and easy to understand. The mathematical
approach is useful for learning how to process digits without converting
the number into a string.

## 6. Complete program

The following program runs both approaches and displays their results.

``` python
def reverse_using_string(number: int) -> int:
    """Reverse a number using string slicing."""

    reversed_number = str(abs(number))[::-1]

    result = int(reversed_number)

    return -result if number < 0 else result


def reverse_using_loop(number: int) -> int:
    """Reverse a number using mathematical operations."""

    sign = -1 if number < 0 else 1
    number = abs(number)

    reversed_number = 0

    while number > 0:
        digit = number % 10

        reversed_number = reversed_number * 10 + digit

        number //= 10

    return sign * reversed_number


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    result_string = reverse_using_string(number)
    result_loop = reverse_using_loop(number)

    print(f"Reversed Number using String Slicing: {result_string}")
    print(f"Reversed Number using While Loop: {result_loop}")
```

[Open `02_Reverse_Digits.py`](02_Reverse_Digits.py)

## 7. Sample output

``` text
Enter a number: 1234
Reversed Number using String Slicing: 4321
Reversed Number using While Loop: 4321
```

Another example:

``` text
Enter a number: -560
Reversed Number using String Slicing: -65
Reversed Number using While Loop: -65
```

## 8. Test your understanding

Try answering these questions before checking the answers.

### Question 1: What does `[::-1]` do?

**Answer:** It creates a reversed version of a sequence, such as a
string.

### Question 2: What does `123 % 10` return?

**Answer:** `3`, because `% 10` extracts the last digit.

### Question 3: Why do we multiply `reversed_number` by `10`?

**Answer:** Multiplying by `10` shifts its digits one decimal place to
the left, making room for the next digit.

### Question 4: What happens when we reverse `560`?

**Answer:** The reversed digits are `065`, but converting that string to
an integer gives `65`. Leading zeroes are not retained in an integer.

### Question 5: How does the code handle a negative number?

**Answer:** It reverses the absolute value and then restores the
negative sign.

## 9. Practise it yourself

Predict the output before running your program.

-   [ ] `123` → ?
-   [ ] `9005` → ?
-   [ ] `777` → ?
-   [ ] `0` → ?
-   [ ] `-321` → ?

**Extra challenge:** Try writing a solution that reverses the digits
without using string conversion or string slicing. Use only mathematical
operations.

## 10. Key takeaways

After completing this problem, you should be able to explain:

-   How string slicing with `[::-1]` reverses a string.
-   How `% 10` extracts the last digit.
-   How `// 10` removes the last digit.
-   How multiplying by `10` helps build a reversed number.
-   How to preserve the sign of a negative number.
-   Why the two approaches have different auxiliary space complexity.

**Before moving on:** Try to write both functions again without copying
the code. Explain how each approach works using the input `2468`.

------------------------------------------------------------------------

[← Previous: Sum of Digits](01_Sum_of_Digits.md) · [Back to Easy
Problems](README.md) · [Next: Prime Testing →](03_Prime_Testing.md)
