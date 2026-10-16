ancho1= 25
ancho2= 15
ancho3= 10
anchototal= ancho1 + ancho2 + ancho3
print("*" * anchototal)
print("CARTA DEL RESTAURANTE".center(anchototal))
print("*" * anchototal)
print("Categoría".ljust(ancho1) + "Plato".ljust(ancho2) + "Precio".rjust(ancho3) + "\n" +
    "Entrantes".ljust(ancho1) + "Croquetas".ljust(ancho2) + "8€".rjust(ancho3) + "\n" +
    "Carnes".ljust(ancho1) + "Entrecot".ljust(ancho2) + "18€".rjust(ancho3) + "\n" +
    "Pescados".ljust(ancho1) + "Salmón".ljust(ancho2) + "15€".rjust(ancho3) + "\n" +
    "Postres".ljust(ancho1) + "Tarta".ljust(ancho2) + "6€".rjust(ancho3))
