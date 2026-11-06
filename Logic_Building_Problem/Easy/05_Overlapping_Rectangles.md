# 05. Check Whether Two Rectangles Overlap

`<sub>`{=html}Difficulty: Easy · Topic: Programming Fundamentals ·
Language: Python`</sub>`{=html}

Learn how to determine whether two rectangles overlap using their corner
coordinates. This problem introduces coordinate geometry, lists,
conditional statements, logical operators (`and`, `or`), and
constant-time checking.

------------------------------------------------------------------------

## 1. Problem statement

You are given the coordinates of two rectangles. Each rectangle is
represented by two points:

-   `l`: Top-left coordinate
-   `r`: Bottom-right coordinate

Check whether the two rectangles overlap.

In this problem, each point is represented as `[x, y]`:

``` text
[x-coordinate, y-coordinate]
```

For example:

``` python
l1 = [0, 10]   # Top-left of Rectangle 1
r1 = [10, 0]   # Bottom-right of Rectangle 1

l2 = [5, 5]    # Top-left of Rectangle 2
r2 = [15, 0]   # Bottom-right of Rectangle 2
```

The function returns: - `True` if the rectangles overlap. - `False` if
they do not overlap.

**Important:** The supplied solution treats rectangles that only touch
at an edge or corner as overlapping. It uses strict separation checks
(`>` and `<`), so equality at a boundary does not count as being
separated.

## 2. Concepts you will practise

  -----------------------------------------------------------------------
  Concept                             Why it is useful here
  ----------------------------------- -----------------------------------
  Variables                           Store the four rectangle
                                      coordinates

  Functions                           Keep the overlap check reusable

  Lists                               Represent each coordinate as
                                      `[x, y]`

  Conditional statements              Check whether the rectangles are
                                      separated

  Coordinate geometry                 Understand positions on the x-axis
                                      and y-axis

  Logical `or`                        Check whether any separation
                                      condition is true

  Logical `and`                       Understand that overlap requires no
                                      separation in either direction
  -----------------------------------------------------------------------

### Understand a coordinate

A coordinate such as `[5, 8]` means:

-   `5` is the x-coordinate (horizontal position).
-   `8` is the y-coordinate (vertical position).

``` text
             y-axis
               ↑
          8    |       ● (5, 8)
               |
          0    +----------------→ x-axis
               0       5
```

In the code, `l1[0]` means the x-coordinate of the top-left point of
Rectangle 1, and `l1[1]` means its y-coordinate.

## 3. Understand the rectangle representation

The solution assumes axis-aligned rectangles: their sides are parallel
to the x-axis and y-axis.

Each rectangle is represented by its top-left and bottom-right corners.

``` text
Top-left (l)                    x increases →
     ┌─────────────────────┐
     │                     │
     │       Rectangle     │
     │                     │
     └─────────────────────┘
                         Bottom-right (r)

y increases upward ↑
```

For example, Rectangle 1:

``` python
l1 = [0, 10]
r1 = [10, 0]
```

This means: - Left x-coordinate = `0` - Right x-coordinate = `10` - Top
y-coordinate = `10` - Bottom y-coordinate = `0`

## 4. Approach --- Check whether rectangles are separated

### Idea

Instead of directly trying to calculate the overlapping area, check
whether the rectangles are completely separated.

Two rectangles do **not** overlap if at least one of these conditions is
true:

1.  Rectangle 1 is completely to the left of Rectangle 2.
2.  Rectangle 2 is completely to the left of Rectangle 1.
3.  Rectangle 1 is completely above Rectangle 2.
4.  Rectangle 2 is completely above Rectangle 1.

If none of these conditions is true, the rectangles overlap according to
the boundary rule used in this solution.

### The four separation conditions

  -----------------------------------------------------------------------
  Condition                           Meaning
  ----------------------------------- -----------------------------------
  `l1[0] > r2[0]`                     Rectangle 1 is completely to the
                                      right of Rectangle 2

  `l2[0] > r1[0]`                     Rectangle 2 is completely to the
                                      right of Rectangle 1

  `l1[1] < r2[1]`                     Rectangle 1 is completely below
                                      Rectangle 2

  `l2[1] < r1[1]`                     Rectangle 2 is completely below
                                      Rectangle 1
  -----------------------------------------------------------------------

If any one condition is true, the function returns `False`.

### Visual example 1 --- Overlapping rectangles

Rectangle 1:

``` text
Top-left:     [0, 10]
Bottom-right: [10, 0]
```

Rectangle 2:

``` text
Top-left:     [5, 5]
Bottom-right: [15, 0]
```

The rectangles share some area:

``` text
y
↑
10  ┌───────────────┐
    │ Rectangle 1   │
 5  │       ┌───────┼──────────┐
    │       │Overlap│ Rect. 2  │
 0  └───────┴───────┴──────────┘
    0       5       10         15  → x
```

None of the four separation conditions is true. Therefore, the result is
`True`.

### Visual example 2 --- Non-overlapping rectangles

Rectangle 1:

``` python
l1 = [0, 2]
r1 = [1, 1]
```

Rectangle 2:

``` python
l2 = [-2, 0]
r2 = [0, -3]
```

Rectangle 2 is below Rectangle 1, so the rectangles are separated
vertically.

``` text
y
↑
 2  ┌───────┐
    │ Rect.1│
 1  └───────┘

 0  ┌────────────┐
    │  Rect. 2   │
-3  └────────────┘
    -2      0    1  → x
```

The condition `l1[1] < r2[1]` is:

``` python
2 < -3
```

This is `False`, so that is not the vertical separation test for these
particular coordinates. The other vertical separation condition is:

``` python
l2[1] < r1[1]
0 < 1
```

This is `True`. Therefore, the function returns `False`.

### Flowchart

``` mermaid
flowchart TD
    A["Start: receive four corner points"] --> B{"Rectangle 1 left of Rectangle 2 OR Rectangle 2 left of Rectangle 1?"}
    B -- "Yes" --> F["Return False: no overlap"]
    B -- "No" --> C{"Rectangle 1 below Rectangle 2 OR Rectangle 2 below Rectangle 1?"}
    C -- "Yes" --> F
    C -- "No" --> D["Return True: rectangles overlap"]
```

### Python solution

``` python
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
```

### Understand the important lines

**Horizontal separation:**

``` python
if l1[0] > r2[0] or l2[0] > r1[0]:
    return False
```

-   `l1[0]` is the left x-coordinate of Rectangle 1.
-   `r2[0]` is the right x-coordinate of Rectangle 2.
-   `l1[0] > r2[0]` means Rectangle 1 starts to the right of Rectangle
    2.
-   `l2[0] > r1[0]` checks the opposite direction.
-   `or` means either condition is enough to prove horizontal
    separation.

**Vertical separation:**

``` python
if l1[1] < r2[1] or l2[1] < r1[1]:
    return False
```

-   `l1[1]` is the top y-coordinate of Rectangle 1.
-   `r2[1]` is the bottom y-coordinate of Rectangle 2.
-   `l1[1] < r2[1]` means Rectangle 1 is completely below Rectangle 2.
-   `l2[1] < r1[1]` checks the opposite direction.

If neither horizontal nor vertical separation exists, the function
returns `True`.

## 5. Dry run

Use the overlapping example:

``` python
l1 = [0, 10]
r1 = [10, 0]
l2 = [5, 5]
r2 = [15, 0]
```

  Check             Substitution   Result
  ----------------- -------------- --------
  `l1[0] > r2[0]`   `0 > 15`       False
  `l2[0] > r1[0]`   `5 > 10`       False
  `l1[1] < r2[1]`   `10 < 0`       False
  `l2[1] < r1[1]`   `5 < 0`        False

No separation condition is true. The function reaches:

``` python
return True
```

So the rectangles overlap.

## 6. Important note --- What if rectangles only touch?

The supplied code uses `>` and `<` to detect separation. Because of
this, rectangles that touch at an edge or corner are treated as
overlapping.

For example, if one rectangle ends at x-coordinate `5` and another
begins at x-coordinate `5`, neither is strictly to the left of the
other.

This is a boundary convention. If a problem defines overlap as requiring
a shared positive area, touching edges or corners should instead be
treated as non-overlapping. Always follow the definition in the
question.

## 7. Complexity analysis

  -----------------------------------------------------------------------
  Complexity              Result                  Explanation
  ----------------------- ----------------------- -----------------------
  Time complexity         `O(1)`                  Only a fixed number of
                                                  coordinate comparisons
                                                  are performed

  Auxiliary space         `O(1)`                  Only a fixed number of
  complexity                                      extra variables are
                                                  used
  -----------------------------------------------------------------------

**Why constant time?**

The function always checks at most four separation conditions,
regardless of the rectangles' sizes or coordinate values. It does not
loop over the points inside the rectangles.

## 8. Complete program

The following program runs the two test cases from your Python solution.

``` python
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
```

[Open `05_Overlapping_Rectangles.py`](05_Overlapping_Rectangles.py)

## 9. Sample output

``` text
Test Case 1: true
Test Case 2: false
```

The program converts Python's `True` and `False` values to lowercase
text using `.lower()` before printing.

## 10. Test your understanding

Try answering these questions before checking the answers.

### Question 1: What does a coordinate such as `[5, 8]` represent?

**Answer:** The x-coordinate is `5` and the y-coordinate is `8`.

### Question 2: When are two rectangles definitely not overlapping?

**Answer:** When one rectangle is completely to the left, right, above,
or below the other.

### Question 3: What does the `or` operator mean in the separation condition?

**Answer:** If either separation condition is true, the rectangles are
considered non-overlapping.

### Question 4: Why does the function return `True` at the end?

**Answer:** If none of the four separation conditions is true, the
rectangles are not separated horizontally or vertically, so they overlap
according to this solution's boundary convention.

### Question 5: Does this implementation count rectangles that only touch at an edge as overlapping?

**Answer:** Yes. The strict comparisons (`>` and `<`) mean equality at a
boundary is not considered separation.

## 11. Practise it yourself

Try to predict the result for each pair. Use the same coordinate format:
top-left point followed by bottom-right point.

-   [ ] Rectangle 1: `l1 = [0, 10]`, `r1 = [10, 0]`; Rectangle 2:
    `l2 = [5, 5]`, `r2 = [15, 0]` → ?
-   [ ] Rectangle 1: `l1 = [0, 5]`, `r1 = [5, 0]`; Rectangle 2:
    `l2 = [10, 5]`, `r2 = [15, 0]` → ?
-   [ ] Rectangle 1: `l1 = [0, 10]`, `r1 = [10, 0]`; Rectangle 2:
    `l2 = [2, 8]`, `r2 = [4, 6]` → ?
-   [ ] Rectangle 1: `l1 = [0, 5]`, `r1 = [5, 0]`; Rectangle 2:
    `l2 = [5, 5]`, `r2 = [10, 0]` → ?

**Extra challenge:** Draw two rectangles on paper and write their
top-left and bottom-right coordinates. Try to identify which of the four
separation conditions applies before running the function.

## 12. Key takeaways

After completing this problem, you should be able to explain:

-   How rectangles can be represented using top-left and bottom-right
    coordinates.
-   How x-coordinates describe horizontal position and y-coordinates
    describe vertical position.
-   How to detect horizontal and vertical separation.
-   How `or` combines separation conditions.
-   Why checking for separation can be simpler than calculating the
    overlapping area.
-   Why the algorithm takes `O(1)` time and `O(1)` auxiliary space.
-   How the chosen boundary rule affects rectangles that only touch.

**Before moving on:** Try to explain the four separation conditions
without looking at the code. Then test a pair of rectangles that overlap
and a pair that are separated.

------------------------------------------------------------------------

[← Previous: Check Power](04_Check_Power.md) · [Back to Easy
Problems](README.md) · [Next: Factorial](06_Factorial.md)
