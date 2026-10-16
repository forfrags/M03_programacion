cabecera = ("{:^30}\n{:10}{:>10}{:>10}\n{}\n".format(
    "lista de la compra", "Articulo", "Cantidad", "precio", "*" * 30))
articulo = input("dame un articulo")
cantidad = input("dame la cantidad")
precio = float(input("dame el precio"))
datos = "{:10}{:>10}{:>10.2f}\n".format(articulo, cantidad, precio)
print(cabecera + datos)
