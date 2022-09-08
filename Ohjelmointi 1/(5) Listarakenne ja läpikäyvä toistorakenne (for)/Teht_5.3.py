num = int(input("Enter a number: "))
variable = False

if num > 1:
    for n in range(2, num):
        if num % n == 0:
            variable = True
            break

if variable:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")

















