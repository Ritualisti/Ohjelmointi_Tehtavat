numbers = []
readingNumbers = True
while readingNumbers:
    strInput = input("Anna luku: ")
    if strInput == "":
        readingNumbers = False
    else:
        numbers.append(int(strInput))

print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(numbers[0:5])













