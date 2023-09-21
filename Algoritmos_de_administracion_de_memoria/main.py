# Datos de los archivos y tamaños
archivos = [
    {"nombre": "hola_mundo.py", "tamano": 500},
    {"nombre": "lista_de_compras.txt", "tamano": 950},
    {"nombre": "resumen.docx", "tamano": 1200},
    {"nombre": "persona.h", "tamano": 350},
    {"nombre": "reporte.xlsx", "tamano": 2000}
]

# Vector de memoria original
memoria_original = [1000, 400, 2000, 700, 900, 1200, 2000]

# Vector de memoria actual
# Realizamos una copia para poder ejecutar algoritmos infinitamente
memoria = memoria_original.copy()

# Función para reiniciar la memoria y archivos
def reiniciar_memoria():
    global memoria
    memoria = memoria_original.copy()
    for archivo in archivos:
        archivo.pop("bloque_asignado", None)

# Función para mostrar el estado de la memoria
def mostrar_estado_memoria():
    print("\nEstado de la memoria:")
    for i, bloque in enumerate(memoria):
        print(f"Bloque {i + 1}: {bloque} KB")
    print()

# Función para el algoritmo de Primer Ajuste
def primer_ajuste():
    reiniciar_memoria() # Evitar problemas de perseverancia de datos
    for archivo in archivos:
        for i, bloque in enumerate(memoria):
            if bloque >= archivo["tamano"]:
                archivo["bloque_asignado"] = i
                memoria[i] -= archivo["tamano"]
                break

# Función para el algoritmo de Mejor Ajuste
def mejor_ajuste():
    reiniciar_memoria() # Evitar problemas de perseverancia de datos
    for archivo in archivos:
        mejor_ajuste_idx = -1
        mejor_ajuste_tamano = float('inf')
        for i, bloque in enumerate(memoria):
            if bloque >= archivo["tamano"] and bloque - archivo["tamano"] < mejor_ajuste_tamano:
                mejor_ajuste_idx = i
                mejor_ajuste_tamano = bloque - archivo["tamano"]
        if mejor_ajuste_idx != -1:
            archivo["bloque_asignado"] = mejor_ajuste_idx
            memoria[mejor_ajuste_idx] -= archivo["tamano"]

# Función para el algoritmo de Peor Ajuste
def peor_ajuste():
    reiniciar_memoria()
    for archivo in archivos:
        peor_ajuste_idx = -1
        peor_ajuste_tamano = -1
        for i, bloque in enumerate(memoria):
            if bloque >= archivo["tamano"] and bloque > peor_ajuste_tamano:
                peor_ajuste_idx = i
                peor_ajuste_tamano = bloque
        if peor_ajuste_idx != -1:
            archivo["bloque_asignado"] = peor_ajuste_idx
            memoria[peor_ajuste_idx] -= archivo["tamano"]

# Función para el algoritmo de Siguiente Ajuste
def siguiente_ajuste():
    reiniciar_memoria()
    ultimo_bloque_usado = -1
    for archivo in archivos:
        for i in range(ultimo_bloque_usado + 1, len(memoria)):  
            if memoria[i] >= archivo["tamano"]:
                archivo["bloque_asignado"] = i
                memoria[i] -= archivo["tamano"]
                ultimo_bloque_usado = i # Guardamos posicion donde nos quedamos
                break
        if "bloque_asignado" not in archivo:
            for i in range(ultimo_bloque_usado + 1):
                if memoria[i] >= archivo["tamano"]:
                    archivo["bloque_asignado"] = i
                    memoria[i] -= archivo["tamano"]
                    ultimo_bloque_usado = i
                    break

# Función para mostrar la asignación de archivos
def mostrar_asignacion_archivos():
    print("\nAsignación de archivos:")
    for archivo in archivos:
        if "bloque_asignado" in archivo:
            print(f"Archivo: {archivo['nombre']}, Tamaño: {archivo['tamano']} KB, Bloque asignado: {archivo['bloque_asignado'] + 1}")
        else:
            print(f"Archivo: {archivo['nombre']} no asignado")
    print()

# Función para el menú principal
def menu_principal():
    while True:
        print("\n<-- Selecciona un algoritmo de asignación de memoria --->")
        print("[ 1 ] Primer Ajuste")
        print("[ 2 ] Mejor Ajuste")
        print("[ 3 ] Peor Ajuste")
        print("[ 4 ] Siguiente Ajuste")
        print("[ 5 ] Salir")
        
        opcion = input("Elije una opción: -> ")
        
        if opcion == "1":
            primer_ajuste()
            mostrar_estado_memoria()
            mostrar_asignacion_archivos()
        elif opcion == "2":
            mejor_ajuste()
            mostrar_estado_memoria()
            mostrar_asignacion_archivos()
        elif opcion == "3":
            peor_ajuste()
            mostrar_estado_memoria()
            mostrar_asignacion_archivos()
        elif opcion == "4":
            siguiente_ajuste()
            mostrar_estado_memoria()
            mostrar_asignacion_archivos()
        elif opcion == "5":
            print("\t\n<--- Hasta luego, Crack --->")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Iniciar el menú principal
menu_principal()