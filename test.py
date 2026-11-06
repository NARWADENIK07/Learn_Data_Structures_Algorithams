number = int(input("Enter a number : "))

new_number = int(str(number)[::-1])

if new_number == number :
    print("Given number is palindrome")

else :

    print("Given number is not palindrome")
