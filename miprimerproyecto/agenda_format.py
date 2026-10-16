cabecera = ("lista de la compra".center(40,"*") + "\n" +
            "{:<10}{:<15}{:>5}{:>10}".format("Nombre", "Edad", "DNI", "telefono") + "\n" +
            "*" * 40 + "\n")
nombre = input("dame un nombre")
Edad = input("dame la Edad")
DNI = input("dame el DNI")
telefono = input("dame el telefono")
datos = "{:<10}{:<15}{:>5}{:>10}".format(nombre, Edad, DNI, telefono)
print(cabecera + datos)
nombre = input("dame un nombre")
Edad = input("dame la Edad")
DNI = input("dame el DNI")
telefono = input("dame el telefono")
datos = "{:<10}{:<15}{:>5}{:>10}".format(nombre, Edad, DNI, telefono)
print(datos)

nombre = input("dame un nombre")
Edad = input("dame la Edad")
DNI = input("dame el DNI")
telefono = input("dame el telefono")
datos = "{:<10}{:<15}{:>5}{:>10}".format(nombre, Edad, DNI, telefono)
print(datos)

