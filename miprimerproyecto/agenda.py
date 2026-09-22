cabecera = ("Agenda".center(40, "*") + "\n" +
            "Nombre".ljust(10) +
            "Edad".ljust(15) +
            "DNI".rjust(5) +
            "telefono".rjust(10) + "\n" +
            "*" * 40 + "\n")
nombre = input("dame un nombre: ")
Edad = input("dame la Edad: ")
DNI = input("dame el DNI: ")
telefono = input("dame el telefono: ")
datos = (nombre.ljust(10) +
         Edad.ljust(15) +
         DNI.rjust(5) +
         telefono.rjust(10))
nombre2 = input("dame un nombre: ")
Edad2 = input("dame la Edad: ")
DNI2 = input("dame el DNI: ")
telefono2 = input("dame el telefono: ")
datos2 = (nombre2.ljust(10) +
          Edad2.ljust(15) +
          DNI2.rjust(5) +
          telefono2.rjust(10))
print(cabecera + datos + "\n" + datos2)
