def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

def ingresar():
    repartidores = {}

    while True:
        cantidad_input = input("\nCantidad de repartidores que partidores que hoy: ").strip()
        if not cantidad_input.isdigit():
            print("Ingrese un número válido.")
            continue
        cantidad = int(cantidad_input)
        if cantidad <= 0:
            print("Debe ingresar un número mayor que cero.")
            continue
        break

    for _ in range(cantidad):
        while True:
            nombre = input("\nNombre: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.")
            elif nombre in repartidores:
                print("Este nombre ya fue ingresado.")
            else:
                break

        while True:
            paquetes_input = input("Paquetes: ").strip()
            if not paquetes_input.isdigit():
                print("Ingrese un número válido.")
                continue
            paquetes = int(paquetes_input)
            if paquetes < 0:
                print("La cantidad de paquetes no puede ser negativa.")
            else:
                break

        while True:
            zona = input("Zona: ").strip()
            if zona == "":
                print("La zona no puede estar vacía.")
            else:
                break

        repartidores[nombre] = {"paquetes": paquetes, "zona": zona}

    print("\nRegistro original")
    print(repartidores)

    return repartidores


ingresar()

