ancho1 = 10
ancho2 = 20
ancho3 = 15
ancho4 = 15
ancho5 = 12
ancho6 = 12
ancho7 = 15
anchototal = ancho1 + ancho2 + ancho3 + ancho4 + ancho5 + ancho6 + ancho7
print("*" * anchototal)
print("PLANTILLA DE EMPLEADOS".center(anchototal))
print("*" * anchototal)
print("ID".ljust(ancho1) +
      "Nombre".ljust(ancho2) +
      "Puesto".ljust(ancho3) +
      "Turno".ljust(ancho4) +
      "Salario".ljust(ancho5) +
      "Antigüedad".ljust(ancho6) +
      "Teléfono".rjust(ancho7))
print("001".ljust(ancho1) +
      "Ana García López".ljust(ancho2) +
      "Camarera".ljust(ancho3) +
      "Mañana".ljust(ancho4) +
      "1.200€".ljust(ancho5) +
      "2 años".ljust(ancho6) +
      "611223344".rjust(ancho7))
print("002".ljust(ancho1) +
      "Carlos Martín".ljust(ancho2) +
      "Chef".ljust(ancho3) +
      "Tarde".ljust(ancho4) +
      "2.500€".ljust(ancho5) +
      "5 años".ljust(ancho6) +
      "622334455".rjust(ancho7))
print("003".ljust(ancho1) +
      "Elena Ruiz".ljust(ancho2) +
      "Gerente".ljust(ancho3) +
      "Completo".ljust(ancho4) +
      "3.800€".ljust(ancho5) +
      "8 años".ljust(ancho6) +
      "633445566".rjust(ancho7))
print("004".ljust(ancho1) +
      "Miguel Ángel".ljust(ancho2) +
      "Barman".ljust(ancho3) +
      "Noche".ljust(ancho4) +
      "1.500€".ljust(ancho5) +
      "3 años".ljust(ancho6) +
      "644556677".rjust(ancho7))
print("005".ljust(ancho1) +
      "Sofía Hernández".ljust(ancho2) +
      "Ayudante".ljust(ancho3) +
      "Mañana".ljust(ancho4) +
      "950€".ljust(ancho5) +
      "1 año".ljust(ancho6) +
      "655667788".rjust(ancho7))
