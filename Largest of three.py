a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a > c:
    print("The largest number is:", a)
elif b > c and b > a:
    print("The largest number is:", b)
else:
    print("The largest number is:",c)
