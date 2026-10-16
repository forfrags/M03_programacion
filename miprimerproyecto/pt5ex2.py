preuhora = 30
preumetre = 0.5
IVA = 0.21

hores = float(input("Introdueix les hores treballades: "))
metres = float(input("Introdueix els metres de cable instalats: "))

preubrut = (hores * preuhora) + (metres * preumetre)
preufinal = preubrut * (1 + IVA)

print("El preu brut es", preubrut, "€")
print("El preu amb IVA es", preufinal, "€")
