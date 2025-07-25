#  Delcaramos esto para mostrar el menú jeje
def mostrar_menu():
    print("\nElige una opción del (1-5)")
    print("1. AGREGAR un nuevo elemento")
    print("2. MOSTRAR el contenido de la cesta de la compra")
    print("3. ELIMINAR un elemento")
    print("4. CALCULAR el total de la compra")
    print("5. RENUNCIAR para salir del programa")


#  que compraremos? >< 
def agregar_elemento(cesta):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))

    cesta[nombre] = precio
    print(f"{nombre} se agregó a la cesta.")


#  Para verificar cuántos productos tenemos en nuestra cesta
def mostrar_cesta(cesta):
    if len(cesta) == 0:
        print("La cesta está vacía.")

    else:
        print("\nContenido de la cesta:")
        for producto, precio in cesta.items():
            print(f"{producto}: ${precio:.2f}")  # esto lo vi en sus apuntes, para dos decimales(?


#  Para eliminar un producto que ya no deseemos
def eliminar_elemento(cesta):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in cesta:
        del cesta[nombre]

        print(f"{nombre} ha sido eliminado de la cesta.")
    else:
        print(f"No se encontró el producto {nombre} en la cesta.")


#  A ver si quedamos en quiebra o no jaja
def calcular_total(cesta):
    total = sum(cesta.values())
    print(f"El total de la compra es: ${total:.2f}")


#  abrimos la app jeje
def abrir_app_compras():
    cesta = {}  # sus apuntes sobre el diccionario

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            agregar_elemento(cesta)
        elif opcion == '2':
            mostrar_cesta(cesta)
        elif opcion == '3':
            eliminar_elemento(cesta)
        elif opcion == '4':
            calcular_total(cesta)
        elif opcion == '5':
            print("bye bye amix, gracias")
            break
        else:
            print("si dice del 1 al 5 pa que eliges otra? TT")

abrir_app_compras()