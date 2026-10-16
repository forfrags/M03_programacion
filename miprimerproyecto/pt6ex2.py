num = int(input("Introdueix un número múltiple de 10: "))
while num % 10 != 0:
    num = int(input("No és múltiple de 10. Torna-ho a introduir: "))
base = num
exponent = 0
while base % 10 == 0:
    base = base // 10
    exponent += 1
print(base, "per 10 elevat a", exponent)
