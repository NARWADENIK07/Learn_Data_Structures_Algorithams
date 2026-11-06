# 01. Sum of Digits of a Number

`<sub>`{=html}Difficulty: Easy · Topic: Programming Fundamentals ·
Language: Python`</sub>`{=html}

Learn how to extract the digits of a number and add them together. This
problem introduces loops, functions, string conversion, and the `%` and
`//` operators.

------------------------------------------------------------------------

## 1. Problem statement

Given an integer, calculate the sum of all its digits.

     Input Calculation         Output
  -------- ----------------- --------
    `1234` `1 + 2 + 3 + 4`       `10`
     `508` `5 + 0 + 8`           `13`
       `7` `7`                    `7`
       `0` `0`                    `0`
    `-246` `2 + 4 + 6`           `12`

For a negative number, these solutions add the digits of its absolute
value. The minus sign is not treated as a digit.

## 2. Concepts you will practise

  Concept                 Why it is useful here
  ----------------------- -------------------------------------------
  Variables               Store the number and running total
  Functions               Keep each solution reusable
  `for` loop              Visit each character in the number string
  `while` loop            Extract digits until no digits remain
  Type conversion         Convert between integers and strings
  Modulus (`%`)           Get the last digit
  Floor division (`//`)   Remove the last digit
  `abs()`                 Handle negative input

### Two operators to understand first

For `number = 123`:

  Expression      Result Meaning
  ------------- -------- -----------------------
  `123 % 10`         `3` Get the last digit
  `123 // 10`       `12` Remove the last digit

Remember: - `% 10` gives the last digit. - `// 10` removes the last
digit.

## 3. Approach 1 --- Using a `for` loop

### Idea

Convert the number into a string, visit each digit one by one, convert
each character back into an integer, and add it to the total.

### Step-by-step example

Suppose the input is `1234`.

1.  Convert `1234` into the string `"1234"`.
2.  Start with `total = 0`.
3.  Read each character and convert it into an integer.
4.  Add each digit to `total`.

    Loop iteration   Digit read Calculation     Total
  ---------------- ------------ ------------- -------
                 1          `1` `0 + 1`             1
                 2          `2` `1 + 2`             3
                 3          `3` `3 + 3`             6
                 4          `4` `6 + 4`            10

### Flowchart

``` mermaid
flowchart TD
    A["Start"] --> B["Receive number"]
    B --> C["Convert abs(number) to string"]
    C --> D["Set total = 0"]
    D --> E["Get next digit character"]
    E --> F{"More digits?"}
    F -- "Yes" --> G["Convert character to integer"]
    G --> H["Add digit to total"]
    H --> E
    F -- "No" --> I["Return total"]
    I --> J["End"]
```

### Python solution

``` python
def sum_of_digits_using_for(number: int) -> int:
    """Calculate the sum of digits using a for loop."""

    total = 0

    for digit in str(abs(number)):
        total += int(digit)

    return total
```

### Understand the important lines

-   `abs(number)` makes a negative input positive.
-   `str(...)` converts the integer into a string so we can visit its
    digits.
-   `int(digit)` converts one digit character back into an integer.
-   `total += int(digit)` adds that digit to the running sum.
-   `return total` sends the final answer back.

## 4. Approach 2 --- Using a `while` loop and mathematical operations

### Idea

Instead of converting the number into a string, extract its last digit
using `% 10`. Add that digit to the total, then remove it using `// 10`.

Repeat until the number becomes `0`.

### Step-by-step dry run

Input: `number = 1234`

Initial values:

``` text
number = 1234
total  = 0
```

  -----------------------------------------------------------------------
          Iteration     `number % 10`       Total after    `number // 10`
                              (digit)          addition 
  ----------------- ----------------- ----------------- -----------------
                  1                 4                 4               123

                  2                 3                 7                12

                  3                 2                 9                 1

                  4                 1                10                 0
  -----------------------------------------------------------------------

When `number` becomes `0`, the loop stops.

Final answer: **10**

### Flowchart

``` mermaid
flowchart TD
    A["Start: number = 1234, total = 0"] --> B["digit = number % 10"]
    B --> C["Add digit to total"]
    C --> D["number = number // 10"]
    D --> E{"Is number greater than 0?"}
    E -- "Yes" --> B
    E -- "No" --> F["Return total"]
```

### Python solution

``` python
def sum_of_digits_using_while(number: int) -> int:
    """Calculate the sum of digits using a while loop."""

    number = abs(number)
    total = 0

    while number != 0:
        digit = number % 10
        total += digit
        number //= 10

    return total
```

### Understand the important lines

-   `number = abs(number)` handles negative numbers.
-   `number % 10` extracts the last digit.
-   `total += digit` adds that digit to the sum.
-   `number //= 10` removes the last digit.
-   `while number != 0` repeats until all digits have been processed.

**Why does the loop work?**

Every time the loop runs, `number //= 10` removes one decimal digit. A
positive integer therefore gets smaller until it reaches `0`.

## 5. Compare both approaches

  -----------------------------------------------------------------------
  Comparison              `for` loop              `while` loop
  ----------------------- ----------------------- -----------------------
  Main idea               Visit characters in a   Extract digits
                          string                  mathematically

  String conversion       Yes                     No

  Uses `%` and `//`       No                      Yes

  Time complexity         `O(d)`                  `O(d)`

  Auxiliary space         `O(d)`                  `O(1)`
  -----------------------------------------------------------------------

Here, `d` means the number of digits in the input.

### What does the complexity mean?

-   **Time complexity `O(d)`:** The algorithm processes each digit once.
-   **Space complexity `O(d)` for the string approach:** Converting the
    number to a string requires storage proportional to the number of
    digits.
-   **Space complexity `O(1)` for the mathematical approach:** It uses a
    fixed number of extra variables.

Both approaches are useful. The string approach is straightforward to
read, while the mathematical approach teaches a number-processing
technique used in many programming problems.

## 6. Complete program

The following program runs both approaches and displays their results.

``` python
def sum_of_digits_using_for(number: int) -> int:
    """Calculate the sum of digits using a for loop."""

    total = 0

    for digit in str(abs(number)):
        total += int(digit)

    return total


def sum_of_digits_using_while(number: int) -> int:
    """Calculate the sum of digits using a while loop."""

    number = abs(number)
    total = 0

    while number != 0:
        digit = number % 10
        total += digit
        number //= 10

    return total


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    result_for = sum_of_digits_using_for(number)
    result_while = sum_of_digits_using_while(number)

    print(f"Sum of Digits using For Loop: {result_for}")
    print(f"Sum of Digits using While Loop: {result_while}")
```

[Open `01_Sum_of_Digits.py`](01_Sum_of_Digits.py)

## 7. Sample output

``` text
Enter a number: 1234
Sum of Digits using For Loop: 10
Sum of Digits using While Loop: 10
```

Another example:

``` text
Enter a number: -508
Sum of Digits using For Loop: 13
Sum of Digits using While Loop: 13
```

## 8. Test your understanding

Try to answer these questions before opening the hints.

```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}Question 1: What does 456 % 10
return?`</strong>`{=html}
```{=html}
</summary>
```
**Answer:** `6`, because `% 10` gives the last digit.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}Question 2: What does 456 // 10
return?`</strong>`{=html}
```{=html}
</summary>
```
**Answer:** `45`, because `// 10` removes the last digit.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}Question 3: What is the sum of the digits of
9021?`</strong>`{=html}
```{=html}
</summary>
```
**Answer:** `9 + 0 + 2 + 1 = 12`.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}Question 4: Why does the while loop
stop?`</strong>`{=html}
```{=html}
</summary>
```
**Answer:** Each iteration removes one digit using floor division by 10.
Eventually, `number` becomes `0`, so `number != 0` is false.

```{=html}
</details>
```
## 9. Practise it yourself

Try these inputs without running the program first. Write down your
predicted output, then run your code to check.

-   [ ] `123` → ?
-   [ ] `9005` → ?
-   [ ] `777` → ?
-   [ ] `0` → ?
-   [ ] `-321` → ?

**Extra challenge:** Modify the program to count how many digits a
number contains. Think about how you could use the same `% 10` and
`// 10` operations.

## 10. Key takeaways

After completing this problem, you should be able to explain:

-   How to visit digits using string conversion and a `for` loop.
-   How `% 10` extracts the last digit.
-   How `// 10` removes the last digit.
-   How to maintain a running total inside a loop.
-   Why the two approaches have different auxiliary space complexity.

**Before moving on:** Try to write both functions again without copying
the code. If you can explain each step and get the correct result, you
have understood the problem.

------------------------------------------------------------------------

[← Back to Easy Problems](README.md) · [Next: Reverse Digits
→](02_Reverse_Digits.md)
