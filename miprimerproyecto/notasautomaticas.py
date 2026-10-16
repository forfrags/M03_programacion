cabecera = ("{:^40}\n{:10}{:>10}{:>10}{:>10}\n{}\n".format(
    "lista de alumnos", "Nombre", "DNI", "Nota", "Resultado", "*" * 40))
nombre = input("Dame el nombre: ")
dni = input("Dame el DNI: ")
nota = float(input("Dame la nota: "))
if nota < 4:
    resultado = "Suspendido"
elif nota < 6:
    resultado = "Aprobado"
elif nota < 9:
    resultado = "Notable"
elif nota <= 10:
    resultado = "Excelente"
else:
    resultado = "Nota no válida"
datos = "{:10}{:>10}{:>10.2f}{:>10}\n".format(
    nombre, dni, nota, resultado)
print(cabecera + datos)
