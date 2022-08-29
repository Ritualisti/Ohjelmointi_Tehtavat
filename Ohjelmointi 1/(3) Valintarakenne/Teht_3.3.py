

gender = input("Sukupuolesi (nainen/mies)?")
hg_value = int(input("Hemoglobiinisi (g/l)?"))

if gender == "nainen":
    if hg_value < 117:
        print("Hemoglobiinisi on alhainen.")
    elif hg_value <= 175:
        print("Hemoglobiinisi on normaali.")
    else:
        print("Hemoglobiinisi on korkea.")
elif gender == "mies":
    if hg_value < 134:
        print("Hemoglobiinisi on alhainen.")
    elif hg_value <= 195:
        print("Hemoglobiinisi on normaali.")
    else:
        print("Hemoglobiinisi on korkea.")


