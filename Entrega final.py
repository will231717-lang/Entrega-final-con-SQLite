import dataset
inventario = dataset.connect("sqlite:///inventarios.db")
tabla = inventario["productos"]

while True:

    opciones = input("*-* Bienvenido al inventario de los 76 Sixer *-* \n\nL - Lista de productos\nB - Busqueda de producto\nI - Ingresar producto\nE - Eliminacion de producto\nS - Salir\n===========================\n\n").upper()

    match opciones:

         case "S":
             break

         case "L":
             for producto in tabla:
                 print(f"ID: {producto['id']} nombre: {producto['nombre']} precio: {producto ['precio']} categoria: {producto['categoria']}\n")

         case "B":
             busqueda = input("Ingrese el producto que desea buscar: ").strip()
             producto = tabla.find_one(nombre=busqueda).strip()
             if producto:
                 print(f"Producto encontrado:\n{producto['nombre']}\nEn la categoria: {producto['categoria']}\nCon el precio de: ${producto['precio']}\n")
             else:
                 print("El producto no se encuentra en inventario\n")

         case "I":
             agregarProducto = input("Ingrese el producto que desee agregar al invetario: ")
             agregarPrecio = float(input("Ingrese el precio del producto:  $ ").strip())
             agregarCategoria = input("Ingrese la categoria del producto: ").strip()
             productosIngresados = {'nombre': agregarProducto, 'precio': agregarPrecio, 'categoria': agregarCategoria}
             tabla.insert(productosIngresados)
             print(f"AGREGADO CON EXITO!!!\n")
    
         case "E":
             eliminar = input("Ingrese el producto que desee eliminar del inventario: ").strip()
             tabla.delete(nombre=eliminar)
             print(f"{eliminar} ELIMINADO CON EXITO!!!\n")