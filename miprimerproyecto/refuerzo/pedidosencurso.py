ancho1 = 10
ancho2 = 20
ancho3 = 10
ancho4 = 15
ancho5 = 10
ancho6 = 15
ancho7 = 20
anchototal = ancho1 + ancho2 + ancho3 + ancho4 + ancho5 + ancho6 + ancho7
print("*" * anchototal)
print("PEDIDOS EN CURSO - COCINA".center(anchototal))
print("*" * anchototal)
print("Mesa".ljust(ancho1) + "Pedido".ljust(ancho2) + "Cant".ljust(ancho3) +
      "Estado".ljust(ancho4) + "Tiempo".ljust(ancho5) + "Chef".ljust(ancho6) +
      "Notas".rjust(ancho7) + "\n" +
      "A5".ljust(ancho1) + "Entrecot".ljust(ancho2) + "2".ljust(ancho3) +
      "En Cocina".ljust(ancho4) + "15 min".ljust(ancho5) + "Chef Carlos".ljust(ancho6) +
      "Poco hecho".rjust(ancho7) + "\n" +
      "B2".ljust(ancho1) + "Paella Valenciana".ljust(ancho2) + "4".ljust(ancho3) +
      "Preparando".ljust(ancho4) + "25 min".ljust(ancho5) + "Chef Ana".ljust(ancho6) +
      "Sin marisco".rjust(ancho7) + "\n" +
      "C8".ljust(ancho1) + "Ensalada César".ljust(ancho2) + "3".ljust(ancho3) +
      "Listo".ljust(ancho4) + "0 min".ljust(ancho5) + "Chef Luis".ljust(ancho6) +
      "Sin crutones".rjust(ancho7) + "\n" +
      "D1".ljust(ancho1) + "Cocido Madrileño".ljust(ancho2) + "6".ljust(ancho3) +
      "Servido".ljust(ancho4) + "-5 min".ljust(ancho5) + "Chef Marta".ljust(ancho6) +
      "Extra garbanzos".rjust(ancho7))
