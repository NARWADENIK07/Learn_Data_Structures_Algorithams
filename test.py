a = int(input("Enter a value of Numerator : "))
b = int(input("Enter a value of Denominator : "))


if a == 0 :

    print("0")

res  = "-" if (a < 0) ^ (b < 0) else ""

a = abs(a)
b = abs(b)

res += str(a // b)

rem = a%b

if rem == 0:
    print(rem)

res += "."
mp =  {}

while rem > 0 :

    if rem in mp:
        res = res[:mp[rem]] + "(" + res[mp[rem]:] + ")"
        break

    mp[rem] = len(res)

    rem = rem*10

    res += str(rem //b)
    rem = rem%b

print(res)