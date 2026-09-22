cabezera = ("lista de la compra".center(30,"*") + "\n" + "Articulo".ljust(10)
            + "Cantidad".rjust(10) + "precio".rjust(10) + "\n" + "*"* 30 + "\n")
articulo = input("dame un articulo")
cantidad = input("dame la cantidad")
precio = input("dame el precio")
datos = articulo.ljust(10) + cantidad.rjust(10) + precio.rjust(10) + "\n"
print(cabezera + datos)
articulo2 = input("dame un articulo")
cantidad2 = input("dame la cantidad")
precio2 = input("dame el precio")
datos2 = articulo2.ljust(10) + cantidad2.rjust(10) + precio2.rjust(10) + "\n"
print(cabezera + datos + datos2 )
articulo3 = input("dame un articulo")
cantidad3 = input("dame la cantidad")
precio3 = input("dame el precio")
datos3 = articulo3.ljust(10) + cantidad3.rjust(10) + precio3.rjust(10) + "\n"
print(cabezera + datos + datos2 + datos3)