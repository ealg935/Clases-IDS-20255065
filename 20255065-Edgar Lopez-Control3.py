agente = "encargado"
platillo = []
precios = []
while True:
    nombre = input("Nombre del agente: ")
    if nombre == agente:
        print("Bienvenido", agente)
        break
    else: 
        print("usuario no exitente")
        print("Nombre del agente: ")
while True:
    opcion = input("Seleccione una de las siguientes opciones (1-Crear un platillo, 2- Consultar platillos y precios, 3-Colocar un pedido, 4-Salir): ")
    if opcion == "1":
        nomplatillo = input("Ingrese el nombre del platillo a crear: ")
        while True:
            precio = input("Ingrese el precio del platillo a crear: ")
            if precio.replace(".","",1).isdigit():
                precio2 = float(precio)
                break
            else:
                print("Precio no valido")
        platillo.append(nomplatillo)
        precios.append(precio2)
        print(f"Platillo '{nomplatillo}' agregado con precio ${precio2:.2f}")
    elif opcion == "2":
        if len(platillo) == 0:
                print("Actualmente no hay platillos ingresados")
        else:
            for i in range(len(platillo)):
                print(f"{platillo[i]}: ${precios[i]:.2f}")
    elif opcion == "3":
        if len(platillo) == 0:
            print("No hay platillos disponibles")
        else:
            pedido = input("Indique el nombre del platillo para su orden: ")
            encontrado = False
            for i in range(len(platillo)):
                if platillo[i] == pedido:
                    print(f"Usted ha elegido {platillo[i]} con un precio de ${precios[i]:.2f}")
                    encontrado = True
                    break
                if not encontrado:
                    print("El platillo ingresado no existe.")
    elif opcion == "4":
        print("Terminar ejecucion")
        break
    else:
        print("Opción no válida, intente nuevamente.") 