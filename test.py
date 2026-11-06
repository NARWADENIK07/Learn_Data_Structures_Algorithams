number = int(input("Enter a number : "))

binary = []

while number :
    
    binary.append(str(number % 2))

    number //= 2

print("".join(binary[::-1]))