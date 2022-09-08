def gas(x):
    return x * 3.785

bensa = float(input("Gallona määrä: "))
while bensa >= 0:
    bensa = gas(bensa)
    print(bensa)
    bensa = float(input("Gallona määrä: "))


















