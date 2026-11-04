n = int(input("Enter n: "))
m = int(input("Enter m: "))

# Find quotient
abs_div = n // m

# Find two nearby multiples
first_multiple = abs_div * m
second_multiple = (abs_div + 1) * m

# Compare distances
if abs(n - first_multiple) < abs(n - second_multiple):
    closest_multiple = first_multiple

elif abs(n - first_multiple) == abs(n - second_multiple):
    closest_multiple = max(
        [first_multiple, second_multiple],
        key=abs
    )

else:
    closest_multiple = second_multiple

print(f"The closest multiple of {m} to {n} is: {closest_multiple}")