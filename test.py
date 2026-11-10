n = int(input("Enter a value of n : "))
r = int(input("Enter a value of r : "))

Numerator = 1
Denominator = 1
d = n-r

while n >= 1 :

    Numerator *= n

    n -=1


while d >= 1 :

    Denominator *= d

    d -= 1


print(Numerator//Denominator)