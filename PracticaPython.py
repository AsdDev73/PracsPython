#Lista de la compra

# Añadir elemento a la lista de la compra
def añadir_a_lista(lista_compra):
    elemento = input("\nIngrese el artículo que desea añadir a la lista de la compra: ")
    lista_compra.append(elemento)
    print( elemento," añadido a la lista de la compra.")

# Borrar elemento de la lista de la compra
def borrar_de_lista(lista_compra):
    elemento = input("\nIngrese el artículo que desea borrar de la lista de la compra: ")
    if elemento in lista_compra:
        lista_compra.remove(elemento)
        print(elemento," borrado de la lista de la compra.")
    else:
        print(elemento," no está en la lista de la compra.")

# Ver toda la lista de la compra
def ver_lista(lista_compra):
    if not lista_compra:
        print("\nLa lista de la compra está vacía.")
    else:
        print("\nLista de la compra:")
        for i, elemento in enumerate(lista_compra):
            print(f"{i + 1}. {elemento}")

# Función para ver el número de elementos en la lista de la compra
def numero_elementos(lista_compra):
    print("\nNúmero de elementos en la lista de la compra: ", {len(lista_compra)})

# Función principal para ejecutar el programa

lista_compra = []
Control=True
while Control:
    print("\nMenú:")
    print("1. Añadir elemento a la lista")
    print("2. Borrar elemento de la lista")
    print("3. Ver lista de la compra")
    print("4. Ver número de elementos en la lista")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        añadir_a_lista(lista_compra)
    elif opcion == "2":
        borrar_de_lista(lista_compra)
    elif opcion == "3":
        ver_lista(lista_compra)
    elif opcion == "4":
        numero_elementos(lista_compra)
    elif opcion == "5":
        print("\n ¡Hasta luego!")
        Control=False
    else:
        print("\nOpción inválida. Por favor, seleccione una opción válida.")
