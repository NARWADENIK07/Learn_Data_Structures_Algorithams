# 03. Check Whether a Number Is Prime

`<sub>`{=html}Difficulty: Easy · Topic: Programming Fundamentals ·
Language: Python`</sub>`{=html}

Learn how to determine whether a number is prime. This problem
introduces divisibility, conditional statements, loops, the `break`
statement, the `for-else` structure, and an important optimization using
the square root of a number.

------------------------------------------------------------------------

## 1. Problem statement

Given an integer, check whether it is a prime number.

A **prime number** is a natural number greater than `1` that has exactly
two positive factors:

-   `1`
-   The number itself

**Examples**

    Input Factors                                       Output
  ------- --------------------------------------------- -----------
      `2` `1, 2`                                        Prime
      `7` `1, 7`                                        Prime
      `9` `1, 3, 9`                                     Not Prime
      `1` `1`                                           Not Prime
      `0` No positive prime-factor definition applies   Not Prime
     `-5` Negative number                               Not Prime

**Important:** `0`, `1`, and negative integers are not prime numbers.

## 2. Concepts you will practise

  -----------------------------------------------------------------------
  Concept                             Why it is useful here
  ----------------------------------- -----------------------------------
  Variables                           Store the number and candidate
                                      divisors

  Functions                           Keep the prime-checking logic
                                      reusable

  Conditional statements              Handle numbers less than or equal
                                      to `1`

  `for` loop                          Test possible divisors

  `break`                             Stop when a divisor is found

  `for-else`                          Identify whether the loop finished
                                      without finding a divisor

  Modulus (`%`)                       Check whether a number divides
                                      evenly

  Square root                         Reduce the number of divisors that
                                      need checking
  -----------------------------------------------------------------------

### Understand divisibility first

The modulus operator `%` gives the remainder after division.

  Expression     Result Meaning
  ------------ -------- -------------------------
  `7 % 2`           `1` 7 is not divisible by 2
  `8 % 2`           `0` 8 is divisible by 2
  `9 % 3`           `0` 9 is divisible by 3

A number is divisible by another number when the remainder is `0`.

## 3. Approach 1 --- Basic approach

### Idea

To check whether a number is prime, try dividing it by every integer
from `2` up to `number - 1`.

-   If any divisor divides the number evenly, it is **not prime**.
-   If no divisor divides it evenly, it is **prime**.

First, handle numbers less than or equal to `1`, because they are not
prime.

### Step-by-step example: Is 7 prime?

Test possible divisors from `2` to `6`.

    Divisor Calculation     Remainder Divisible?
  --------- ------------- ----------- ------------
          2 `7 % 2`                 1 No
          3 `7 % 3`                 1 No
          4 `7 % 4`                 3 No
          5 `7 % 5`                 2 No
          6 `7 % 6`                 1 No

No divisor is found, so `7` is prime.

Now consider `9`:

    Divisor Calculation     Remainder Divisible?
  --------- ------------- ----------- ------------
          2 `9 % 2`                 1 No
          3 `9 % 3`                 0 Yes

A divisor is found, so `9` is not prime. There is no need to test
further divisors.

### Flowchart

``` mermaid
flowchart TD
    A["Start: receive number"] --> B{"Is number <= 1?"}
    B -- "Yes" --> C["Return False: not prime"]
    B -- "No" --> D["Try divisors from 2 to number - 1"]
    D --> E{"Is number divisible by divisor?"}
    E -- "Yes" --> F["Return False: not prime"]
    E -- "No" --> G["Try next divisor"]
    G --> H{"More divisors?"}
    H -- "Yes" --> E
    H -- "No" --> I["Return True: prime"]
```

### Python solution

``` python
def is_prime_basic(number: int) -> bool:
    """Check whether a number is prime using the basic approach."""

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True
```

### Understand the important lines

-   `if number <= 1:` handles values that cannot be prime.
-   `range(2, number)` checks possible divisors from `2` to
    `number - 1`.
-   `number % i == 0` checks whether the current divisor divides the
    number evenly.
-   `return False` stops the function as soon as a divisor is found.
-   `return True` runs if the loop finishes without finding a divisor.

### What is the `for-else` statement?

Your solution uses `return` to finish the function. Python also supports
a `for-else` structure:

``` python
for i in range(2, number):
    if number % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
```

The `else` block runs only when the loop finishes normally, without
encountering `break`.

## 4. Approach 2 --- Optimized approach using square root

### Idea

The basic approach checks every possible divisor up to `number - 1`. We
can reduce this work by checking only up to the square root of the
number.

**Why is this possible?**

If a number can be written as a product of two factors, at least one of
those factors must be less than or equal to its square root.

For example:

``` text
36 = 4 × 9
36 = 6 × 6
36 = 9 × 4
```

The factor pairs meet around `√36 = 6`. If a divisor exists, at least
one factor in a pair is at most `6`.

Therefore, if no integer from `2` through `√number` divides the number,
it is prime.

### Visual explanation

For `36`, the factor pairs are:

``` text
1 × 36
2 × 18
3 × 12
4 × 9
6 × 6
```

After reaching `6`, the pairs repeat in reverse order.

### Step-by-step example: Is 29 prime?

Calculate:

``` text
√29 ≈ 5.38
```

We only need to test integer divisors from `2` through `5`.

    Divisor Calculation     Remainder Divisible?
  --------- ------------- ----------- ------------
          2 `29 % 2`                1 No
          3 `29 % 3`                2 No
          4 `29 % 4`                1 No
          5 `29 % 5`                4 No

No divisor is found, so `29` is prime.

Now consider `49`:

``` text
√49 = 7
```

    Divisor Calculation     Remainder Divisible?
  --------- ------------- ----------- ------------
          2 `49 % 2`                1 No
          3 `49 % 3`                1 No
          4 `49 % 4`                1 No
          5 `49 % 5`                4 No
          6 `49 % 6`                1 No
          7 `49 % 7`                0 Yes

A divisor is found, so `49` is not prime.

### Flowchart

``` mermaid
flowchart TD
    A["Start: receive number"] --> B{"Is number <= 1?"}
    B -- "Yes" --> C["Return False"]
    B -- "No" --> D["Set limit = floor(sqrt(number))"]
    D --> E["Try divisor i starting at 2"]
    E --> F{"Is i <= limit?"}
    F -- "No" --> G["Return True: prime"]
    F -- "Yes" --> H{"Is number % i == 0?"}
    H -- "Yes" --> I["Return False: not prime"]
    H -- "No" --> J["Increase i by 1"]
    J --> F
```

### Python solution

``` python
def is_prime_optimized(number: int) -> bool:
    """Check whether a number is prime using the square root approach."""

    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
```

### Understand the important line

``` python
range(2, int(number ** 0.5) + 1)
```

-   `number ** 0.5` calculates the square root.
-   `int(...)` converts it to an integer.
-   `+ 1` is needed because the ending value in `range()` is excluded.

For example, if `number = 49`:

``` python
int(49 ** 0.5) + 1
# 7 + 1 = 8

range(2, 8)
# 2, 3, 4, 5, 6, 7
```

This includes `7`, which is an important divisor of `49`.

## 5. Compare both approaches

  Comparison                   Basic approach             Square root approach
  ---------------------------- -------------------------- -------------------------------
  Divisors checked             Up to `number - 1`         Up to `√number`
  Time complexity              `O(n)`                     `O(√n)`
  Auxiliary space complexity   `O(1)`                     `O(1)`
  Best use                     Learning the basic logic   More efficient prime checking

Here, `n` represents the input number.

### What does the complexity mean?

-   **Basic `O(n)`:** The number of possible divisors grows
    approximately with the input number.
-   **Optimized `O(√n)`:** The number of possible divisors grows with
    the square root of the input number.
-   **Space `O(1)`:** Both approaches use a fixed number of extra
    variables.

The optimized approach performs fewer checks for large numbers.

## 6. Complete program

The following program runs both approaches and displays their results.

``` python
def is_prime_basic(number: int) -> bool:
    """Check whether a number is prime using the basic approach."""

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def is_prime_optimized(number: int) -> bool:
    """Check whether a number is prime using the square root approach."""

    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":

    number = int(input("Enter a number: "))

    result_basic = is_prime_basic(number)
    result_optimized = is_prime_optimized(number)

    print(
        f"Basic Approach: "
        f"{number} is {'Prime' if result_basic else 'Not Prime'}."
    )

    print(
        f"Optimized Approach: "
        f"{number} is {'Prime' if result_optimized else 'Not Prime'}."
    )
```

[Open `03_Prime_Testing.py`](03_Prime_Testing.py)

## 7. Sample output

For a prime number:

``` text
Enter a number: 29
Basic Approach: 29 is Prime.
Optimized Approach: 29 is Prime.
```

For a non-prime number:

``` text
Enter a number: 49
Basic Approach: 49 is Not Prime.
Optimized Approach: 49 is Not Prime.
```

For a number less than or equal to `1`:

``` text
Enter a number: 1
Basic Approach: 1 is Not Prime.
Optimized Approach: 1 is Not Prime.
```

## 8. Test your understanding

Try answering these questions before checking the answers.

### Question 1: Is `1` a prime number?

**Answer:** No. A prime number must have exactly two positive factors.
The number `1` has only one.

### Question 2: What does `number % i == 0` check?

**Answer:** It checks whether `number` is exactly divisible by `i`, with
no remainder.

### Question 3: Why do we check only up to the square root?

**Answer:** If a number has a factor greater than its square root, its
matching factor must be smaller than the square root. Checking up to the
square root is enough to find a factor if one exists.

### Question 4: Why is `+ 1` used in the optimized `range()`?

**Answer:** Python's `range()` excludes its ending value. Adding `1`
ensures the integer square root is included when it is a possible
divisor.

### Question 5: What does `break` do in a loop?

**Answer:** It immediately exits the loop.

## 9. Practise it yourself

Predict whether each number is prime before running your program.

-   [ ] `2` → ?
-   [ ] `11` → ?
-   [ ] `15` → ?
-   [ ] `23` → ?
-   [ ] `49` → ?
-   [ ] `97` → ?
-   [ ] `100` → ?
-   [ ] `1` → ?

**Extra challenge:** Modify the optimized function so that it also
counts how many divisibility checks it performs. Compare the count for
the basic and optimized approaches using the same input.

## 10. Key takeaways

After completing this problem, you should be able to explain:

-   What makes a number prime.
-   How `%` helps check divisibility.
-   Why `0`, `1`, and negative numbers are not prime.
-   How a loop can test possible divisors.
-   How `break` can stop a loop early.
-   How the square root optimization reduces the number of checks.
-   Why the optimized approach has `O(√n)` time complexity.

**Before moving on:** Try writing both functions again without copying.
Explain why checking divisors only up to the square root is sufficient.

------------------------------------------------------------------------

[← Previous: Reverse Digits](02_Reverse_Digits.md) · [Back to Easy
Problems](README.md) · [Next: Check Power →](04_Check_Power.md)
