#1 carta restaurante
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
#2 reservas restaurante el buen sabor
ancho1 = 20
ancho2 = 15
ancho3 = 10
ancho4 = 10
ancho5 = 10
ancho6 = 10
anchototal = ancho1 + ancho2 + ancho3 + ancho4 + ancho5 + ancho6
print("*" * anchototal)
print("RESERVAS - RESTAURANTE EL BUEN SABOR".center(anchototal))
print("*" * anchototal)
print("Nombre".ljust(ancho1) + "Fecha".ljust(ancho2) + "Hora".ljust(ancho3) +
      "Personas".ljust(ancho4) + "Mesa".ljust(ancho5) + "Teléfono".rjust(ancho6) + "\n" +
      "María González".ljust(ancho1) + "15/12/2024".ljust(ancho2) + "14:30".ljust(ancho3) +
      "4".ljust(ancho4) + "A12".ljust(ancho5) + "612345678".rjust(ancho6) + "\n" +
      "Juan Pérez".ljust(ancho1) + "16/12/2024".ljust(ancho2) + "21:00".ljust(ancho3) +
      "2".ljust(ancho4) + "B5".ljust(ancho5) + "698765432".rjust(ancho6) + "\n" +
      "Ana Rodríguez".ljust(ancho1) + "17/12/2024".ljust(ancho2) + "13:15".ljust(ancho3) +
      "6".ljust(ancho4) + "C8".ljust(ancho5) + "655443322".rjust(ancho6) + "\n" +
      "Carlos López".ljust(ancho1) + "18/12/2024".ljust(ancho2) + "20:45".ljust(ancho3) +
      "8".ljust(ancho4) + "D3".ljust(ancho5) + "677889900".rjust(ancho6))
#3 Pedidos en curso cocina
ancho1 = 10
ancho2 = 20
ancho3 = 10
ancho4 = 15
ancho5 = 10
ancho6 = 15
ancho7 = 20
anchototal = ancho1 + ancho2 + ancho3 + ancho4 + ancho5 + ancho6 + ancho7
print("*" * anchototal)
print("PEDIDOS EN CURSO - COCINA".center(anchototal))
print("*" * anchototal)
print("Mesa".ljust(ancho1) + "Pedido".ljust(ancho2) + "Cant".ljust(ancho3) +
      "Estado".ljust(ancho4) + "Tiempo".ljust(ancho5) + "Chef".ljust(ancho6) +
      "Notas".rjust(ancho7) + "\n" +
      "A5".ljust(ancho1) + "Entrecot".ljust(ancho2) + "2".ljust(ancho3) +
      "En Cocina".ljust(ancho4) + "15 min".ljust(ancho5) + "Chef Carlos".ljust(ancho6) +
      "Poco hecho".rjust(ancho7) + "\n" +
      "B2".ljust(ancho1) + "Paella Valenciana".ljust(ancho2) + "4".ljust(ancho3) +
      "Preparando".ljust(ancho4) + "25 min".ljust(ancho5) + "Chef Ana".ljust(ancho6) +
      "Sin marisco".rjust(ancho7) + "\n" +
      "C8".ljust(ancho1) + "Ensalada César".ljust(ancho2) + "3".ljust(ancho3) +
      "Listo".ljust(ancho4) + "0 min".ljust(ancho5) + "Chef Luis".ljust(ancho6) +
      "Sin crutones".rjust(ancho7) + "\n" +
      "D1".ljust(ancho1) + "Cocido Madrileño".ljust(ancho2) + "6".ljust(ancho3) +
      "Servido".ljust(ancho4) + "-5 min".ljust(ancho5) + "Chef Marta".ljust(ancho6) +
      "Extra garbanzos".rjust(ancho7))
#4 plantilla de empleados
ancho1 = 10
ancho2 = 20
ancho3 = 15
ancho4 = 15
ancho5 = 12
ancho6 = 12
ancho7 = 15
anchototal = ancho1 + ancho2 + ancho3 + ancho4 + ancho5 + ancho6 + ancho7
print("*" * anchototal)
print("PLANTILLA DE EMPLEADOS".center(anchototal))
print("*" * anchototal)
print("ID".ljust(ancho1) +
      "Nombre".ljust(ancho2) +
      "Puesto".ljust(ancho3) +
      "Turno".ljust(ancho4) +
      "Salario".ljust(ancho5) +
      "Antigüedad".ljust(ancho6) +
      "Teléfono".rjust(ancho7))
print("001".ljust(ancho1) +
      "Ana García López".ljust(ancho2) +
      "Camarera".ljust(ancho3) +
      "Mañana".ljust(ancho4) +
      "1.200€".ljust(ancho5) +
      "2 años".ljust(ancho6) +
      "611223344".rjust(ancho7))
print("002".ljust(ancho1) +
      "Carlos Martín".ljust(ancho2) +
      "Chef".ljust(ancho3) +
      "Tarde".ljust(ancho4) +
      "2.500€".ljust(ancho5) +
      "5 años".ljust(ancho6) +
      "622334455".rjust(ancho7))
print("003".ljust(ancho1) +
      "Elena Ruiz".ljust(ancho2) +
      "Gerente".ljust(ancho3) +
      "Completo".ljust(ancho4) +
      "3.800€".ljust(ancho5) +
      "8 años".ljust(ancho6) +
      "633445566".rjust(ancho7))
print("004".ljust(ancho1) +
      "Miguel Ángel".ljust(ancho2) +
      "Barman".ljust(ancho3) +
      "Noche".ljust(ancho4) +
      "1.500€".ljust(ancho5) +
      "3 años".ljust(ancho6) +
      "644556677".rjust(ancho7))
print("005".ljust(ancho1) +
      "Sofía Hernández".ljust(ancho2) +
      "Ayudante".ljust(ancho3) +
      "Mañana".ljust(ancho4) +
      "950€".ljust(ancho5) +
      "1 año".ljust(ancho6) +
      "655667788".rjust(ancho7))
#5 Menu semanal
ancho1 = 15
ancho2 = 25
ancho3 = 25
ancho4 = 20
ancho5 = 10
anchototal = ancho1 + ancho2 + ancho3 + ancho4 + ancho5
print("*" * anchototal)
print("MENÚ SEMANAL - DEL 16 AL 22 DE DICIEMBRE".center(anchototal))
print("*" * anchototal)
print("Día".ljust(ancho1) +
      "Primeros".ljust(ancho2) +
      "Segundos".ljust(ancho3) +
      "Postres".ljust(ancho4) +
      "Precio".rjust(ancho5))
print("Lunes".ljust(ancho1) +
      "Sopa de Verduras".ljust(ancho2) +
      "Pollo Asado".ljust(ancho3) +
      "Fruta del Tiempo".ljust(ancho4) +
      "18,50€".rjust(ancho5))
print("Martes".ljust(ancho1) +
      "Ensalada Mixta".ljust(ancho2) +
      "Merluza al Horno".ljust(ancho3) +
      "Flan Casero".ljust(ancho4) +
      "20,75€".rjust(ancho5))
print("Miércoles".ljust(ancho1) +
      "Lentejas".ljust(ancho2) +
      "Entrecot".ljust(ancho3) +
      "Tarta de Queso".ljust(ancho4) +
      "25,90€".rjust(ancho5))
print("Jueves".ljust(ancho1) +
      "Crema de Calabacín".ljust(ancho2) +
      "Pescado a la Plancha".ljust(ancho3) +
      "Helado".ljust(ancho4) +
      "19,80€".rjust(ancho5))
print("Viernes".ljust(ancho1) +
      "Paella Valenciana".ljust(ancho2) +
      "Mariscada".ljust(ancho3) +
      "Brownie".ljust(ancho4) +
      "32,50€".rjust(ancho5))
print("Sábado".ljust(ancho1) +
      "Cocido Madrileño".ljust(ancho2) +
      "Cordero Asado".ljust(ancho3) +
      "Natillas".ljust(ancho4) +
      "28,75€".rjust(ancho5))
print("Domingo".ljust(ancho1) +
      "Menú Especial".ljust(ancho2) +
      "Menú Especial".ljust(ancho3) +
      "Menú Especial".ljust(ancho4) +
      "35,00€".rjust(ancho5))
#6 estadistica de ventas
ancho1 = 20
ancho2 = 15
ancho3 = 15
ancho4 = 20
ancho5 = 10
anchototal = ancho1 + ancho2 + ancho3 + ancho4 + ancho5
print("*" * anchototal)
print("ESTADÍSTICAS DE VENTAS - DICIEMBRE".center(anchototal))
print("*" * anchototal)
print("Producto".ljust(ancho1) +
      "Unidades".ljust(ancho2) +
      "Ingresos".ljust(ancho3) +
      "Tendencia".ljust(ancho4) +
      "Crecimiento".rjust(ancho5))
print("Entrecot".ljust(ancho1) +
      "156".ljust(ancho2) +
      "3.654,60€".ljust(ancho3) +
      "Ascendente".ljust(ancho4) +
      "+15%".rjust(ancho5))
print("Paella Valenciana".ljust(ancho1) +
      "89".ljust(ancho2) +
      "1.687,55€".ljust(ancho3) +
      "Estable".ljust(ancho4) +
      "+2%".rjust(ancho5))
print("Ensalada César".ljust(ancho1) +
      "203".ljust(ancho2) +
      "1.727,50€".ljust(ancho3) +
      "Ascendente".ljust(ancho4) +
      "+22%".rjust(ancho5))
print("Cocido Madrileño".ljust(ancho1) +
      "67".ljust(ancho2) +
      "971,50€".ljust(ancho3) +
      "Descendente".ljust(ancho4) +
      "-8%".rjust(ancho5))
print("Tarta de Queso".ljust(ancho1) +
      "178".ljust(ancho2) +
      "1.237,10€".ljust(ancho3) +
      "Ascendente".ljust(ancho4) +
      "+18%".rjust(ancho5))