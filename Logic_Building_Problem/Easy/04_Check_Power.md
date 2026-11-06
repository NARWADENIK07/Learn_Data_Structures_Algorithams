# 04. Check Whether Y Is a Power of X

`<sub>`{=html}Difficulty: Easy · Topic: Programming Fundamentals ·
Language: Python`</sub>`{=html}

Learn how to check whether one positive integer can be written as a
power of another. This problem introduces conditions, loops, modulus
(`%`), floor division (`//`), and repeated division.

------------------------------------------------------------------------

## 1. Problem statement

Given two integers `x` and `y`, check whether `y` is a power of `x`.

That means checking whether there is a non-negative integer `n` such
that:

\[ y = x\^n \]

    Base (`x`)   Number (`y`) Calculation                            Output
  ------------ -------------- -------------------------------------- --------
           `2`            `8` `2 × 2 × 2`                            True
           `3`           `81` `3 × 3 × 3 × 3`                        True
           `5`           `25` `5 × 5`                                True
           `2`           `10` No whole-number power of 2 equals 10   False
           `3`           `12` No whole-number power of 3 equals 12   False
           `1`            `1` A power of 1 is 1                      True
           `1`            `5` A power of 1 is always 1               False

The supplied solution returns `False` when `x` or `y` is zero or
negative.

## 2. Concepts you will practise

  Concept                  Why it is useful here
  ------------------------ ------------------------------------------
  Variables                Store the base `x` and number `y`
  Functions                Keep the checking logic reusable
  Conditional statements   Handle invalid values and `x == 1`
  `while` loop             Repeatedly divide the number by the base
  Modulus (`%`)            Check whether division is exact
  Floor division (`//`)    Divide and keep the integer quotient

### Understand `%` and `//` first

Suppose `y = 8` and `x = 2`.

  Expression     Result Meaning
  ------------ -------- ------------------------------------
  `8 % 2`           `0` 8 is divisible by 2
  `8 // 2`          `4` Integer quotient of 8 divided by 2
  `4 % 2`           `0` 4 is divisible by 2
  `4 // 2`          `2` Integer quotient of 4 divided by 2

The algorithm keeps dividing `y` by `x` while each division is exact.

## 3. Approach --- Using repeated division

### Idea

If `y` is a power of `x`, repeatedly dividing `y` by `x` should
eventually reduce it to `1`, with no remainder at every division.

Steps:

1.  Check whether `x` and `y` are positive. If not, return `False`.
2.  Handle `x == 1` separately. A power of `1` is `1`, so return whether
    `y == 1`.
3.  While `y` is greater than `1` and divisible by `x`, divide `y` by
    `x`.
4.  If the final value of `y` is exactly `1`, return `True`; otherwise
    return `False`.

### Dry run 1: Is 8 a power of 2?

Input:

``` text
x = 2
y = 8
```

    Iteration   Current `y`       `y % x` Action          New `y`
  ----------- ------------- ------------- ------------- ---------
            1             8   `8 % 2 = 0` Divide by 2           4
            2             4   `4 % 2 = 0` Divide by 2           2
            3             2   `2 % 2 = 0` Divide by 2           1

The value reaches `1`, so the function returns `True`.

``` text
8 → 4 → 2 → 1
```

### Dry run 2: Is 10 a power of 2?

Input:

``` text
x = 2
y = 10
```

    Iteration   Current `y`        `y % x` Action                  New `y`
  ----------- ------------- -------------- --------------------- ---------
            1            10   `10 % 2 = 0` Divide by 2                   5
            2             5    `5 % 2 = 1` Not divisible; stop           5

The remaining value is `5`, not `1`, so the function returns `False`.

``` text
10 → 5
```

### Flowchart

``` mermaid
flowchart TD
    A["Start: receive x and y"] --> B{"Are x and y positive?"}
    B -- "No" --> C["Return False"]
    B -- "Yes" --> D{"Is x equal to 1?"}
    D -- "Yes" --> E["Return whether y equals 1"]
    D -- "No" --> F{"Is y > 1 and y % x == 0?"}
    F -- "Yes" --> G["y = y // x"]
    G --> F
    F -- "No" --> H{"Is y equal to 1?"}
    H -- "Yes" --> I["Return True"]
    H -- "No" --> J["Return False"]
```

### Python solution

``` python
def is_power_of_number(x: int, y: int) -> bool:
    """Check whether Y is a power of X."""

    if x <= 0 or y <= 0:
        return False

    if x == 1:
        return y == 1

    while y > 1 and y % x == 0:
        y //= x

    return y == 1
```

### Understand the important lines

-   `if x <= 0 or y <= 0:` rejects zero and negative inputs in this
    solution.
-   `if x == 1:` handles the special case where the base is `1`.
-   `y > 1` ensures repeated division continues only while the value is
    greater than `1`.
-   `y % x == 0` checks whether `y` can be divided evenly by `x`.
-   `y //= x` divides `y` by `x` and stores the integer quotient back in
    `y`.
-   `return y == 1` checks whether repeated division reached exactly
    `1`.

## 4. Why does repeated division work?

Consider powers of `3`:

``` text
3⁴ = 81

81 ÷ 3 = 27
27 ÷ 3 = 9
 9 ÷ 3 = 3
 3 ÷ 3 = 1
```

Every division is exact, and the final result is `1`.

Now consider `20`:

``` text
20 % 3 = 2
```

The division is not exact. Therefore, `20` is not a power of `3`.

## 5. Complexity analysis

Let `k` be the number of successful divisions needed to reduce `y` to
`1`, when `x > 1`.

  -----------------------------------------------------------------------
  Complexity              Result                  Explanation
  ----------------------- ----------------------- -----------------------
  Time complexity         `O(logₓ y)`             Each loop iteration
                                                  divides `y` by `x`

  Auxiliary space         `O(1)`                  Only a fixed number of
  complexity                                      variables are used
  -----------------------------------------------------------------------

**Why logarithmic time?**

Every iteration reduces the current value by a factor of `x`. The number
of repeated divisions needed to reach `1` grows logarithmically with
`y`.

The special case `x == 1` is handled before the loop, so the logarithmic
expression applies when `x > 1`.

## 6. Complete program

``` python
def is_power_of_number(x: int, y: int) -> bool:
    """Check whether Y is a power of X."""

    if x <= 0 or y <= 0:
        return False

    if x == 1:
        return y == 1

    while y > 1 and y % x == 0:
        y //= x

    return y == 1


if __name__ == "__main__":

    x = int(input("Enter the base number (x): "))
    y = int(input("Enter the number to check (y): "))

    result = is_power_of_number(x, y)

    if result:
        print(f"{y} is a power of {x}.")
    else:
        print(f"{y} is not a power of {x}.")
```

[Open `04_Check_Power.py`](04_Check_Power.py)

**Note:** The function changes its local variable `y` while dividing it.
The original `y` in the main program remains unchanged, so the printed
message shows the input value.

## 7. Sample output

Example 1:

``` text
Enter the base number (x): 2
Enter the number to check (y): 8
8 is a power of 2.
```

Example 2:

``` text
Enter the base number (x): 2
Enter the number to check (y): 10
10 is not a power of 2.
```

Example 3:

``` text
Enter the base number (x): 1
Enter the number to check (y): 1
1 is a power of 1.
```

## 8. Test your understanding

Try answering these questions before checking the answers.

### Question 1: What does `y % x == 0` check?

**Answer:** It checks whether `y` is exactly divisible by `x`, with no
remainder.

### Question 2: Why do we use `y //= x`?

**Answer:** It divides `y` by `x` and stores the integer quotient back
in `y`. This lets the loop check the next division.

### Question 3: Why is `x == 1` handled separately?

**Answer:** Dividing by `1` never reduces `y`. The loop would not make
progress, so the function directly checks whether `y` is `1`.

### Question 4: What happens when `x = 2` and `y = 12`?

**Answer:** `12` is divided by `2` to get `6`, then by `2` to get `3`.
Since `3` is not divisible by `2` and is not `1`, the function returns
`False`.

### Question 5: What value indicates a successful check?

**Answer:** The repeated divisions reduce `y` to exactly `1`.

## 9. Practise it yourself

Predict whether each pair returns `True` or `False`.

-   [ ] `x = 2, y = 16` → ?
-   [ ] `x = 3, y = 27` → ?
-   [ ] `x = 5, y = 125` → ?
-   [ ] `x = 2, y = 12` → ?
-   [ ] `x = 4, y = 64` → ?
-   [ ] `x = 1, y = 7` → ?
-   [ ] `x = 0, y = 8` → ?
-   [ ] `x = 3, y = 1` → ?

**Extra challenge:** Modify the program to count how many successful
divisions are performed before the loop stops. What does that count
represent when the input is a valid power and `x > 1`?

## 10. Key takeaways

After completing this problem, you should be able to explain:

-   What it means for `y` to be a power of `x`.
-   How `%` checks whether a division is exact.
-   How `//` performs integer division.
-   How repeated division checks whether a number is a power.
-   Why the base `1` needs a separate condition.
-   Why the loop eventually stops for valid positive inputs with
    `x > 1`.
-   Why the time complexity is logarithmic and auxiliary space
    complexity is constant.

**Before moving on:** Try writing the function again without copying it.
Trace the values of `y` for `x = 2, y = 32`, and explain why the
function returns `True`.

------------------------------------------------------------------------

[← Previous: Prime Testing](03_Prime_Testing.md) · [Back to Easy
Problems](README.md) · [Next: Factorial](06_Factorial.md)
