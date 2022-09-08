import random
dice = int(input("Number of dice:"))
dice2 = []
summa = 0
while dice > 0:
    dice2.append(1)
    dice -= 1
for n in dice2:
    summa += random.randint(1,6)
print(summa)

















