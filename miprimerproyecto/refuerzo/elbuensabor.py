ancho1 = 20
ancho2 = 15
ancho3 = 10
ancho4 = 10
ancho5 = 10
ancho6 = 10
anchototal = ancho1 + ancho2 + ancho3 + ancho4 + ancho5 + ancho6
print("*" * anchototal)
print("RESERVAS - RESTAURANTE EL BUEN SABOR".center(anchototal))
print("*" * anchototal)
print("Nombre".ljust(ancho1) + "Fecha".ljust(ancho2) + "Hora".ljust(ancho3) +
      "Personas".ljust(ancho4) + "Mesa".ljust(ancho5) + "Teléfono".rjust(ancho6) + "\n" +
      "María González".ljust(ancho1) + "15/12/2024".ljust(ancho2) + "14:30".ljust(ancho3) +
      "4".ljust(ancho4) + "A12".ljust(ancho5) + "612345678".rjust(ancho6) + "\n" +
      "Juan Pérez".ljust(ancho1) + "16/12/2024".ljust(ancho2) + "21:00".ljust(ancho3) +
      "2".ljust(ancho4) + "B5".ljust(ancho5) + "698765432".rjust(ancho6) + "\n" +
      "Ana Rodríguez".ljust(ancho1) + "17/12/2024".ljust(ancho2) + "13:15".ljust(ancho3) +
      "6".ljust(ancho4) + "C8".ljust(ancho5) + "655443322".rjust(ancho6) + "\n" +
      "Carlos López".ljust(ancho1) + "18/12/2024".ljust(ancho2) + "20:45".ljust(ancho3) +
      "8".ljust(ancho4) + "D3".ljust(ancho5) + "677889900".rjust(ancho6))
