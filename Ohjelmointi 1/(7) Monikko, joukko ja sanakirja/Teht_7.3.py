lentoasemat = {}
syote = 3

while syote != 0:
    print("2 = Syötä uusi")
    print("1 = Hae")
    print("0 = Lopeta")
    syote = int(input("Valitse toiminto: "))
    if syote == 2:
        icao = print(input("Syötä ICAO-koodi: "))
        asema = print(input("Syötä lentoasema: "))
        lentoasemat["icao"] = asema
    if syote == 1:
        haku = input("Syötä ICAO-koodi: ")
        if haku in lentoasemat:
            print(lentoasemat[icao])



















