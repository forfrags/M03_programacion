print("Jugador   Dado1   Dado2   Dado3   Puntos")
print("*" * 60)

atacante_dado1 = int(input("Dado 1 atacante: "))
atacante_dado2 = int(input("Dado 2 atacante: "))
atacante_dado3 = int(input("Dado 3 atacante: "))

defensor_dado1 = int(input("Dado 1 defensor: "))
defensor_dado2 = int(input("Dado 2 defensor: "))

atacante_puntos = 0
defensor_puntos = 2

print("{:<15} {:<10} {:<10} {:<10} {:<10}".format(
    "Atacante", atacante_dado1, atacante_dado2, atacante_dado3, atacante_puntos))

print("{:<15} {:<10} {:<10} {:<10} {:<10}".format(
    "Defensor", defensor_dado1, defensor_dado2, "", defensor_puntos))
