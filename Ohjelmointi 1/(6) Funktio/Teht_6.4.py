def number(luvut):
    for n in luvut:
        summa += n
        return
syote = (input("Anna luku:"))
lista = []
while syote != "":
    intsyote = int(syote)
    lista.append(intsyote)
    syote = input("Anna luku:")
lista = number(lista)
print(lista)


















