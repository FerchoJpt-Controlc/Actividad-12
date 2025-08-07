def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    mayores = [x for x in lista[1:] if x[1] > pivote[1]]
    iguales = [x for x in lista if x[1] == pivote[1]]
    menores = [x for x in lista[1:] if x[1] < pivote[1]]
    return quick_sort(mayores) + iguales + quick_sort(menores)


def Ingresar():
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

        repartidores[nombre] = {
            "paquetes": paquetes,
            "zona": zona
        }

    print("\nrepartidores reguistrados")

    return repartidores

def mostrar(repartidores):
    lista = [(nombre, info["paquetes"], info["zona"]) for nombre, info in repartidores.items()]
    ordenados = quick_sort(lista)

    print("\nLista de repartidores con mas paquetes entregados")
    for nombre, paquetes, zona in ordenados:
        print(f"{nombre} = {paquetes} paquetes entregados")


def buscar(repartidores):
    nombre_buscar = input("\nBuscar repartidor: ").strip()

    encontrado = False
    for nombre in repartidores:
        if nombre.lower() == nombre_buscar.lower():
            datos = repartidores[nombre]
            print(f"\n{nombre} entregó {datos['paquetes']} paquetes en la zona {datos['zona']}.")
            encontrado = True
            break

    if not encontrado:
        print(f"\nRepartidor '{nombre_buscar}' no encontrado.")

def estadisticas(repartidores):
    print("\nEstadisticas de los repartidores")

    if not repartidores:
        print("No hay datos para mostrar.")
        return

    total = 0
    cantidades = []

    for datos in repartidores.values():
        total += datos["paquetes"]
        cantidades.append(datos["paquetes"])

    promedio = total / len(repartidores)
    max_entregas = max(cantidades)
    min_entregas = min(cantidades)


    repartidores_max = [nombre for nombre, datos in repartidores.items() if datos["paquetes"] == max_entregas]
    repartidores_min = [nombre for nombre, datos in repartidores.items() if datos["paquetes"] == min_entregas]

    print(f"Total de paquetes entregados: {total}")
    print(f"Promedio de entregas: {promedio:.2f}")
    print(f"Mayor número de entregas: {', '.join(repartidores_max)} ({max_entregas})")
    print(f"Menor número de entregas: {', '.join(repartidores_min)} ({min_entregas})")

repartidores =Ingresar()
mostrar(repartidores)
estadisticas(repartidores)
buscar(repartidores)



