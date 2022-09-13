
lista = {}
nimi = input("Anna nimi: ")
while nimi != "":
    if nimi in lista:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    lista.add(nimi)
print(lista)