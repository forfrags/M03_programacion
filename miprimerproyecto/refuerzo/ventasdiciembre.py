ancho1 = 20
ancho2 = 15
ancho3 = 15
ancho4 = 20
ancho5 = 10
anchototal = ancho1 + ancho2 + ancho3 + ancho4 + ancho5
print("*" * anchototal)
print("ESTADÍSTICAS DE VENTAS - DICIEMBRE".center(anchototal))
print("*" * anchototal)
print("Producto".ljust(ancho1) +
      "Unidades".ljust(ancho2) +
      "Ingresos".ljust(ancho3) +
      "Tendencia".ljust(ancho4) +
      "Crecimiento".rjust(ancho5))
print("Entrecot".ljust(ancho1) +
      "156".ljust(ancho2) +
      "3.654,60€".ljust(ancho3) +
      "Ascendente".ljust(ancho4) +
      "+15%".rjust(ancho5))
print("Paella Valenciana".ljust(ancho1) +
      "89".ljust(ancho2) +
      "1.687,55€".ljust(ancho3) +
      "Estable".ljust(ancho4) +
      "+2%".rjust(ancho5))
print("Ensalada César".ljust(ancho1) +
      "203".ljust(ancho2) +
      "1.727,50€".ljust(ancho3) +
      "Ascendente".ljust(ancho4) +
      "+22%".rjust(ancho5))
print("Cocido Madrileño".ljust(ancho1) +
      "67".ljust(ancho2) +
      "971,50€".ljust(ancho3) +
      "Descendente".ljust(ancho4) +
      "-8%".rjust(ancho5))
print("Tarta de Queso".ljust(ancho1) +
      "178".ljust(ancho2) +
      "1.237,10€".ljust(ancho3) +
      "Ascendente".ljust(ancho4) +
      "+18%".rjust(ancho5))
