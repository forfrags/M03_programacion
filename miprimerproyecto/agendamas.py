menu = "Delete Contact".center(40, "*") + "\n"
for j in range(agenda.count(";")):
    if j == 0:
        inicio = 0
        final = agenda.find(";")
    else:
        inicio = final + 1
        final = agenda.find(";", inicio)
    contacto = agenda[inicio:final]
    primer_separador = contacto.find("*")
    segundo_separador = contacto.find("*", primer_separador + 1)

    nombre = contacto[:primer_separador]
    direccion = contacto[primer_separador + 1:segundo_separador]
    menu = menu + str(j + 1) + ")" + "{:20}{:20}\n".format(nombre, direccion)
menu = menu + str(agenda.count(";") + 1) + ")Go Back"
print(menu)
opc = input("Option:\n")
if not opc.isdigit():
    print("Non-Numeric Option ")
    input("Enter to continue")
elif not int(opc) in range(1, agenda.count(";") + 2):
    print("Option Out Of Range")
    input("Enter to continue")
else:
    opc = int(opc)
    if opc == agenda.count(";") + 1:
        flg_00 = True
        flg_04 = False
    else:

        inicio = 0
        final = 0
        for j in range(opc):
            if j == 0:
                inicio = 0
                final = agenda.find(";")
            else:
                inicio = final + 1
                final = agenda.find(";", inicio)
            contacto = agenda[inicio:final]
        # print(contacto)
        agenda = agenda[:inicio] + agenda[final + 1:]