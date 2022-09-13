def vuodenaika(syote):
    talvi = ("12", "1", "2")
    kevat = ("3", "4", "5")
    kesa = ("6", "7", "8")
    syksy = ("9", "10", "11")
    for n in talvi:
        if syote in n:
            print("talvi")
    for n in kevat:
        if syote in n:
            print("kevat")
    for n in kesa:
        if syote in n:
            print("kesa")
    for n in syksy:
        if syote in n:
            print("syksy")
    return
syote = (input("Anna kuukautta vastaava numero (1-12): "))
vuodenaika(syote)
