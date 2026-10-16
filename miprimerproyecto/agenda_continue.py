cabecera = ("lista de la compra".center(40, "*") + "\n" +
            "{:<10}{:<15}{:>5}{:>10}".format("Nombre", "Edad", "DNI", "telefono") + "\n" +
            "*" * 40 + "\n")
print(cabecera)
continuar = "s"
while continuar == "s":
    nombre = input("Dame un nombre: ")
    Edad = input("Dame la Edad: ")
    DNI = input("Dame el DNI: ")
    telefono = input("Dame el telefono: ")
    datos = "{:<10}{:<15}{:>5}{:>10}".format(nombre, Edad, DNI, telefono)
    print(datos)
    continuar = input("¿Quieres continuar? (s/n): ")
print("Programa terminado.")
