hores = float(input("Introduce las horas trabajadas: "))
preu_hora = float(input("Introduce el precio por hora: "))

if hores <= 35:
    import_total = hores * preu_hora
else:
    hores_extres = hores - 35
    import_total = (35 * preu_hora) + (hores_extres * preu_hora * 1.5)

print("El importe final es:", import_total, "euros")
