from re import I


n = int(input("Please Enter any Positive Number: "))

if n < 0:
    print("Error: Number must be Positive.")
else:
    sum = 0
    i = n
    while i > 0:
        sum += i
        i -= 1
    print("Sum of all Positive numbers till", n,"is", sum)    