nombreVendedor = None
productos = []   #lista
producto = {}   #diccionario


opcion = 100

print("Mercado")
print("***************")
print("1. Crear lista mercado")
print("2. Ver lista de mercado")
print("3. Editar producto de la lista")
print("4. Eliminar producto de la lista")
print("Presiona 5 para salir")
while opcion != 5:
    opcion = int(input("Elija una opción: "))
    if opcion == 1:
        print("Bienvenido a la creacion de tu lista de mercado")
        
        #creando claves y valores de un dicionario o objeto
        producto["id"]=5
        producto["nombre"]=input("Digita el nombre del producto:")
        producto["precio"]=int(input("Precio del producto: "))
        producto["cantidad"]=int(input("cuantos elementos de este producto vas a llevar: "))
        producto["presentacion"]=input("Cual presentacion llevaras? ")
        
        #mostrando mi diccionario
        #print(producto)
        
        #Poblando una lista (Agregando elementos a una lista)
        productos.append(producto)
        print(productos)
        
        
        
    elif opcion == 2:
        print("Estoy en la 2")
    elif opcion == 3:
        print("Estoy en la 3")
    elif opcion == 4:
        print("Estoy en la 4")
    else:
        print("Opción no válida")
