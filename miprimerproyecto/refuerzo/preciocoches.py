ancho1 = 20
ancho2 = 15
ancho3 = 18
ancho4 = 25
anchototal = ancho1 + ancho2 + ancho3 + ancho4
modelo = input("Introduce el modelo: ")
precio = float(input("Introduce el precio: "))
descuento = float(input("Introduce el descuento (%): "))
preciodescuento = precio - (precio * descuento / 100)
print("*" * anchototal)
print("PRECIO DEL COCHE".center(anchototal))
print("*" * anchototal)
print(f"{'Modelo':<{ancho1}}"
      f"{'Precio':<{ancho2}}"
      f"{'Descuento (%)':<{ancho3}}"
      f"{'Precio con descuento':<{ancho4}}")
print(f"{modelo:<{ancho1}}"
      f"{precio:<{ancho2}.2f}"
      f"{descuento:<{ancho3}.2f}"
      f"{preciodescuento:<{ancho4}.2f}")
print("*" * anchototal)
