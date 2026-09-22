cabecera = ("{}\n{:30}{:>10}{:>10}{:>10}\n{}\n".format(
    "Magatzem Logistic".center(60),
    "Producte", "Quantitat", "Preu", "Total",
    "*" * 60))
articulo = input("Dame un artículo: ")
cantidad = int(input("Dame la cantidad: "))
precio = float(input("Dame el precio: "))
total = cantidad * precio
datos = "{:30}{:>10}{:>10.2f}{:>10.2f}\n".format(
    articulo, cantidad, precio, total)
print("*" * 60)
print(cabecera + datos)
print("{:>60}\n{:>60.2f}".format("Total Inventari", total))
articulo = input("Dame un artículo: ")
cantidad = int(input("Dame la cantidad: "))
precio = float(input("Dame el precio: "))
total = cantidad * precio
datos = "{:30}{:>10}{:>10.2f}{:>10.2f}\n".format(
    articulo, cantidad, precio, total)
print("*" * 60)
print(cabecera + datos)
print("{:>60}\n{:>60.2f}".format("Total Inventari", total))
articulo = input("Dame un artículo: ")
cantidad = int(input("Dame la cantidad: "))
precio = float(input("Dame el precio: "))
total = cantidad * precio
datos = "{:30}{:>10}{:>10.2f}{:>10.2f}\n".format(
    articulo, cantidad, precio, total)
print("*" * 60)
print(cabecera + datos)
print("{:>60}\n{:>60.2f}".format("Total Inventari", total))
