import random


# 1. Llançament de 2 daus

print("1. Llançament de 2 daus")

dau1 = random.randint(1, 6)
dau2 = random.randint(1, 6)

print("Dau 1:", dau1)
print("Dau 2:", dau2)
print("Suma:", dau1 + dau2)


# 2. Nombres parells del 2 al 100

print("\n2. Nombres parells del 2 al 100")

numero = 2

while numero <= 100:
    print(numero)
    numero = numero + 2


# 3. Nombres parells fins a n

print("\n3. Nombres parells fins a n")

n = int(input("Introdueix un número n: "))

numero = 2

while numero <= n:
    print(numero)
    numero = numero + 2


# 4. Baraja mesclada

print("\n4. Baraja mesclada")

cartes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Abans de barrejar:")
print(cartes)

random.shuffle(cartes)

print("Després de barrejar:")
print(cartes)


# 5. Joc de daus: Anna contra Bernat

print("\n5. Joc de daus: Anna contra Bernat")

jugar = "s"

while jugar == "s":

    anna = 9
    bernat = 9

    print("\nComença una nova partida")
    print("Anna té", anna, "fitxes")
    print("Bernat té", bernat, "fitxes")

    while anna > 0 and bernat > 0:

        dau = random.randint(1, 6)

        print("\nHa sortit el dau:", dau)

        # Si surt 1, 3 o 5, guanya l'Anna
        if dau == 1 or dau == 3 or dau == 5:

            if bernat >= dau:
                bernat = bernat - dau
                anna = anna + dau
            else:
                anna = anna + bernat
                bernat = 0

            print("L'Anna agafa", dau, "fitxes")

        # Si surt 2, 4 o 6, guanya en Bernat
        else:

            if anna >= dau:
                anna = anna - dau
                bernat = bernat + dau
            else:
                bernat = bernat + anna
                anna = 0

            print("En Bernat agafa", dau, "fitxes")

        print("Anna:", anna)
        print("Bernat:", bernat)

    # Comprovar el guanyador

    if anna == 0:
        print("\nHa guanyat en Bernat!")

    if bernat == 0:
        print("\nHa guanyat l'Anna!")

    jugar = input("\nVolen jugar una altra vegada? (s/n): ")

print("\nPrograma finalitzat.")