agenda = ""
salir = False
while salir == False:
    print("\n" + "1) Nuevo Telefono")
    print("2) Mostrar agenda")
    print("3) Salir")
    opcion = input("Opcion: ")
    if opcion == "1":
        nombre = input("Introduce el nombre: ")
        telefono = input("Introduce el telefono: ")
        print("\n" + "Nombre: {}".format(nombre))
        print("Telefono: {}".format(telefono))
        confirmar = input("¿Quieres guardar el contacto? (s/n): ")
        if confirmar == "s":
            agenda = agenda + "{:<25} {}\n".format(nombre, telefono)
            print("Contacto guardado correctamente.")
        else:
            print("Contacto no guardado.")
    elif opcion == "2":
        print("\n" + ("*") * 30)
        print("          AGENDA")
        print(("*") * 30)
        print("{:<25} {}".format("Nombre", "Tfn"))
        print(("-") * 30)
        print(agenda)
        input("\n" + "Enter to continue...")
    elif opcion == "3":
        print("\n" + "Saliendo del programa...")
        input("Enter to continue...")
        salir = True
    else:
        print("\n" + "Opcion incorrecta.")