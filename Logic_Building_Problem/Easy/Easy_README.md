# Easy Problems --- Python Programming Before DSA

Welcome to the **Easy** section of this repository! This section is
designed for learners who want to strengthen their Python programming
and problem-solving skills before starting Data Structures and
Algorithms (DSA).

You do not need advanced programming knowledge to begin. Start with the
first problem, understand the idea, trace the examples, and then try
writing the solution yourself.

> **Learning principle:** Do not just copy the code. Understand the
> problem, explain the logic in your own words, and practise changing
> the input.

------------------------------------------------------------------------

## Table of Contents

-   [What you will learn](#what-you-will-learn)
-   [How to use this section](#how-to-use-this-section)
-   [Your learning path](#your-learning-path)
-   [Easy problem list](#easy-problem-list)
-   [Core concepts visual guide](#core-concepts-visual-guide)
-   [How to approach a problem](#how-to-approach-a-problem)
-   [Practice checklist](#practice-checklist)
-   [When are you ready for the next
    level?](#when-are-you-ready-for-the-next-level)
-   [Tips for beginners](#tips-for-beginners)

------------------------------------------------------------------------

## What you will learn

By completing these problems, you will practise:

  -----------------------------------------------------------------------
  Skill                               What it means
  ----------------------------------- -----------------------------------
  Variables and data types            Store numbers and other values

  Operators                           Perform calculations and
                                      comparisons

  Conditional statements              Make decisions using `if`, `elif`,
                                      and `else`

  Loops                               Repeat instructions using `for` and
                                      `while`

  Functions                           Divide a program into reusable
                                      blocks

  Strings                             Work with text and convert values

  Number logic                        Solve problems involving digits and
                                      divisors

  Basic recursion                     Understand a function calling
                                      itself

  Problem-solving                     Turn a question into a clear
                                      sequence of steps

  Complexity basics                   Get an introduction to time and
                                      space complexity
  -----------------------------------------------------------------------

You will also see different ways to solve the same problem. Comparing
approaches helps you understand why one solution may be simpler or more
efficient than another.

## How to use this section

Each problem has a Python solution file. Open the file, read the problem
description and concepts, run the program, and experiment with different
inputs.

### Recommended workflow

``` mermaid
flowchart TD
    A["Read the problem"] --> B["Understand the input and output"]
    B --> C["Try a small example manually"]
    C --> D["Write the steps in plain language"]
    D --> E["Implement the solution in Python"]
    E --> F["Run and test different inputs"]
    F --> G{"Does it work?"}
    G -- "No" --> H["Find the mistake and revise"]
    H --> E
    G -- "Yes" --> I["Explain the logic and analyse complexity"]
    I --> J["Move to the next problem"]
```

**A good habit:** Before opening the solution, spend 10--15 minutes
trying the problem yourself. If you get stuck, look at the relevant
concept and then return to the problem.

## Your learning path

The problems are numbered to give you a suggested order. Follow that
order when you are starting out. If a concept is unfamiliar, revise it
before moving ahead.

``` mermaid
flowchart TD
    A["Start: Python basics"] --> B["Basic number operations"]
    B --> C["Conditions and loops"]
    C --> D["Digit-based problems"]
    D --> E["Divisors, factors and number properties"]
    E --> F["Functions and recursion"]
    F --> G["Series and mathematical patterns"]
    G --> H["Ready to begin DSA fundamentals"]
```

This is a learning guide, not a strict rule. You can revisit earlier
problems whenever you need more practice.

## Easy problem list

The following problems are currently included in the Easy folder. Select
a Python file to view its implementation.

  ----------------------------------------------------------------------------------------------------------------------
                    No. Problem          Main concepts    Solution
  --------------------- ---------------- ---------------- --------------------------------------------------------------
                     01 Sum of Digits    Loops, strings,  [01_Sum_of_Digits.py](01_Sum_of_Digits.py)
                                         `%`, `//`        

                     02 Reverse Digits   Strings,         [02_Reverse_Digits.py](02_Reverse_Digits.py)
                                         slicing, loops,  
                                         `%`, `//`        

                     03 Prime Testing    Conditions,      [03_Prime_Testing.py](03_Prime_Testing.py)
                                         loops,           
                                         divisibility,    
                                         square root      

                     04 Check Power      Conditions,      [04_Check_Power.py](04_Check_Power.py)
                                         repeated         
                                         division, `%`,   
                                         `//`             

                     05 Overlapping      Geometry,        [05_Overlapping_Rectangles.py](05_Overlapping_Rectangles.py)
                        Rectangles       conditions,      
                                         comparisons      

                     06 Factorial        Loops,           [06_Factorial.py](06_Factorial.py)
                                         functions,       
                                         recursion        

                     07 Pair Cube Count  Nested loops,    [07_Pair_Cube_Count.py](07_Pair_Cube_Count.py)
                                         conditions,      
                                         exponentiation   

                     08 GCD or HCF       Divisibility,    [08_GCD_or_HCF.py](08_GCD_or_HCF.py)
                                         recursion,       
                                         Euclidean        
                                         algorithm        

                     09 LCM              Loops, GCD,      [09_LCM.py](09_LCM.py)
                                         mathematical     
                                         formula          

                     10 Perfect Number   Divisors, loops, [10_Perfect_Number.py](10_Perfect_Number.py)
                                         square root      

                     11 Add Two          Arithmetic, GCD, [11_Add_Two_Fractions.py](11_Add_Two_Fractions.py)
                        Fractions        simplification   

                     12 Day of the Week  Conditions,      [12_Day_of_the_Week.py](12_Day_of_the_Week.py)
                                         arithmetic, date 
                                         logic            

                     13 Nth Fibonacci    Loops,           [13_Nth_Fibonacci.py](13_Nth_Fibonacci.py)
                                         recursion,       
                                         series           

                     14 Decimal to       Number systems,  [14_Decimal_to_Binary.py](14_Decimal_to_Binary.py)
                        Binary           division,        
                                         remainders       

                     15 Nth Term of a    Loops,           [15_n-th_term_of_series.py](15_n-th_term_of_series.py)
                        Series           arithmetic,      
                                         formulas         

                     16 Armstrong Number Digits, loops,   [16_Armstrong_Number.py](16_Armstrong_Number.py)
                                         strings, powers  

                     17 Palindrome       Strings,         [17_Palindrome_Number.py](17_Palindrome_Number.py)
                        Number           slicing, loops,  
                                         digit reversal   

                     18 Digit Root       Repeated digit   [18_Digit_Root.py](18_Digit_Root.py)
                                         sum, arithmetic  
  ----------------------------------------------------------------------------------------------------------------------

> **Note:** The table links to the Python solution files. Detailed,
> step-by-step Markdown explanations can be added alongside each
> solution as the tutorials are written.

## Core concepts visual guide

These diagrams introduce a few ideas that appear repeatedly in the
problems.

### 1. How a `for` loop works

A `for` loop repeats a block of code for each item in a sequence.

``` mermaid
flowchart TD
    A["Start"] --> B["Get next item"]
    B --> C{"Is an item available?"}
    C -- "Yes" --> D["Execute loop body"]
    D --> B
    C -- "No" --> E["Continue after the loop"]
```

Example:

``` python
for number in range(1, 4):
    print(number)
```

Output:

``` text
1
2
3
```

### 2. How a `while` loop works

A `while` loop continues as long as its condition is `True`.

``` mermaid
flowchart TD
    A["Start"] --> B["Check condition"]
    B --> C{"Condition is True?"}
    C -- "Yes" --> D["Run loop body"]
    D --> E["Update a value"]
    E --> B
    C -- "No" --> F["Exit the loop"]
```

Example:

``` python
number = 3

while number > 0:
    print(number)
    number -= 1
```

Output:

``` text
3
2
1
```

Make sure that the loop can eventually reach a condition that is
`False`. Otherwise, you may create an infinite loop.

### 3. Understanding `%` and `//`

These two operators are especially useful in number and digit problems.

For example, when `number = 123`:

  Expression      Result Meaning
  ------------- -------- -----------------------
  `123 % 10`         `3` Get the last digit
  `123 // 10`       `12` Remove the last digit

``` mermaid
flowchart TD
    A["number = 123"] --> B["digit = number % 10"]
    B --> C["digit = 3"]
    C --> D["number = number // 10"]
    D --> E["number = 12"]
    E --> F["Repeat until number becomes 0"]
```

Try changing `123` to another number and predict the results before
running the code.

### 4. How a function works

A function is a reusable block of code. It can receive input, perform a
task, and return a result.

``` mermaid
flowchart LR
    A["Input"] --> B["Function"]
    B --> C["Process"]
    C --> D["Return result"]
    D --> E["Use the result"]
```

Example:

``` python
def add(a: int, b: int) -> int:
    return a + b

answer = add(10, 20)
print(answer)
```

Output:

``` text
30
```

### 5. Understanding recursion

Recursion happens when a function calls itself. A recursive solution
needs a **base case** so that it can stop.

``` mermaid
flowchart TD
    A["Call factorial(4)"] --> B["4 × factorial(3)"]
    B --> C["3 × factorial(2)"]
    C --> D["2 × factorial(1)"]
    D --> E["Base case: factorial(1) = 1"]
    E --> F["Return results back through the calls"]
```

For example:

``` python
def factorial(number: int) -> int:
    if number == 1:
        return 1

    return number * factorial(number - 1)
```

This example demonstrates the idea for positive integers. The base case
and input validation must be designed carefully in a complete program.

## How to approach a problem

When you see a new question, use this simple five-step method:

1.  **Understand:** What exactly is the question asking?
2.  **Identify:** What input will you receive, and what output is
    expected?
3.  **Plan:** Write the solution steps in plain English.
4.  **Code and test:** Convert the steps into Python and test normal and
    edge cases.
5.  **Review:** Explain why your solution works and consider its time
    and space complexity.

### Example: Sum of digits

Suppose the input is `246`.

``` text
246 → take 6 → remaining number 24
 24 → take 4 → remaining number 2
  2 → take 2 → remaining number 0

Sum = 6 + 4 + 2 = 12
```

The key operations are:

``` python
digit = number % 10
number = number // 10
```

Try tracing the same process with `1357`.

## Practice checklist

Use this checklist to track your learning. GitHub displays these as
checkboxes, so you can tick them as you complete each topic.

### Before solving

-   [ ] I can explain the problem in my own words.
-   [ ] I understand the expected input and output.
-   [ ] I have tried at least one example manually.

### While solving

-   [ ] I attempted the problem before checking the solution.
-   [ ] I can explain each important line of code.
-   [ ] I tested more than one input.
-   [ ] I checked edge cases where relevant.

### After solving

-   [ ] I can explain the approach without reading the code.
-   [ ] I understand the time complexity.
-   [ ] I understand the space complexity.
-   [ ] I can solve the problem again without copying.

## When are you ready for the next level?

You do not need to memorise every solution. You should be comfortable
with the ideas behind them.

You are ready to move towards the next section when you can:

-   Use conditions and loops without confusion.
-   Write and call simple functions.
-   Work with strings and basic number operations.
-   Trace a program using sample inputs.
-   Explain the logic of a solution in simple language.
-   Recognise when a loop or recursive call stops.
-   Understand basic Big O time and space complexity.

If some of these are still difficult, that is completely normal.
Practise the relevant problems again.

## Tips for beginners

-   **Understand before memorising:** Learn why the code works.
-   **Type the code yourself:** Avoid only copying and pasting.
-   **Predict the output:** Make a guess before running the program.
-   **Test edge cases:** Try zero, one, negative values, repeated
    digits, or other boundary inputs when relevant.
-   **Compare approaches:** A solution that is easy to write is not
    always the most efficient.
-   **Be consistent:** A little practice every day is better than
    rushing through many problems once.
-   **Explain your solution:** If you can teach the logic to someone
    else, you probably understand it.

------------------------------------------------------------------------

## Keep learning

After completing the Easy section, continue to the [Medium](../Medium/)
and [Hard](../Hard/) folders when you are ready.

Return to the [main repository README](../../README.md) to see the
complete learning roadmap.

**Remember:** The goal is not to finish all the questions quickly. The
goal is to build the problem-solving foundation that will make learning
DSA easier.
