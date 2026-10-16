numero = int(input("Introduce un número: "))
factor = 2
while numero > 1:
    if numero % factor == 0:
        print(factor)
        numero = numero // factor
    else:
        factor = factor + 1