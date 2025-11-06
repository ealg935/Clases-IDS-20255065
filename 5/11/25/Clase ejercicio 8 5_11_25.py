menu = []

#Branch de Productos
productos = []
producto_codigo = []
producto_nombre = []
producto_categoria = []
producto_precio = []
productos.append(producto_codigo)
productos.append(producto_nombre)
productos.append(producto_categoria)
productos.append(producto_precio)
menu.append(productos)

#Branch de cliente
cliente = []
codigo_cliente = []
nombre_cliente = []
correo_clientes = []
telefono_cliente = []
cliente.append(codigo_cliente)
cliente.append(nombre_cliente)
cliente.append(correo_clientes)
cliente.append(telefono_cliente)
menu.append(cliente)

#Branch de Pedidos
pedidos = [codigo_cliente, producto_codigo]


while True:
    print( "CAFETERIA ESEN BREW")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Registrar nuevo cliente")
    print("4. Mostrar clientes")
    print("5. Registrar pedido")
    print("6. Mostrar pedidos del día")
    print("7. Mostrar categorías disponibles")
    print("8. Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    # Mostrar productos
    if opcion == "1":
        if len(producto_codigo) == 0:
            print("No hay productos registrados.")
        else:
            print("algo")