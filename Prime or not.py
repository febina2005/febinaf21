num = int(input("Enter a Number"))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
print("Is prime:",is_prime)
