##############################################################################################
#
# By: Dexne
# 
# Algoritmos de administracion de memoria
# 
# En esta ocacion seguimos trabajando con los algoritmos de administracion de memoria
# 
# Esta es la version mejorada del codigo de implementacion de los algoritmos
# 
# Algoritmos trabajados:
#      Primer ajuste
#      Mejor ajuste 
#      Peor ajuste 
#      Siguiente ajuste
# 
#      Cosas añadidas
# Se creo una funcion que le permite al usuario poder añadir mas espacios de memoria
# Se creo una funcion la cual te permite añadir mas archivos ya sea de manera
# Virtual (Una simulacion)
# Fisica ( Se pide la ruta de una carpeta y se agragan todos loa archivos existentes)
# 
# Además de han hecho correcciones para que si un archivo no cabe se le informe 
# al usuario que no hay espacio suficiente.
# 
##############################################################################################

# Libreria necesaria para trabajar con los archivos del sistema
import os

# Datos de los archivos y tamaños
archivos = [
    {"nombre": "hola_mundo.py", "tamano": 500},
    {"nombre": "lista_de_compras.txt", "tamano": 950},
    {"nombre": "resumen.docx", "tamano": 1200},
    {"nombre": "persona.h", "tamano": 350},
    {"nombre": "reporte.xlsx", "tamano": 2000}
]

# Vector de memoria original
memoria_original = [1000, 400, 1800, 700, 900, 1200, 1500]

# Realizamos una copia para poder ejecutar algoritmos infinitamente
memoria = memoria_original.copy()

# Lista para rastrear archivos que no caben
archivos_que_no_caben = []

# Función para reiniciar la memoria y archivos para evitar que se mantengan los archivos 
# una vez asignados por algun algoritmo
def reiniciar_memoria():
    global memoria, archivos_que_no_caben
    memoria = memoria_original.copy()
    archivos_que_no_caben = []
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
    reiniciar_memoria()  # Evitar problemas de perseverancia de datos
    for archivo in archivos:
        for i, bloque in enumerate(memoria):
            if bloque >= archivo["tamano"]:
                archivo["bloque_asignado"] = i
                memoria[i] -= archivo["tamano"]
                break
        else:
            archivos_que_no_caben.append(archivo["nombre"])

# Función para el algoritmo de Mejor Ajuste
def mejor_ajuste():
    reiniciar_memoria()  # Evitar problemas de perseverancia de datos
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
        else:
            archivos_que_no_caben.append(archivo["nombre"])

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
        else:
            archivos_que_no_caben.append(archivo["nombre"])

# Función para el algoritmo de Siguiente Ajuste
def siguiente_ajuste():
    reiniciar_memoria()
    ultimo_bloque_usado = -1
    for archivo in archivos:
        asignado = False
        for i in range(ultimo_bloque_usado + 1, len(memoria)):
            if memoria[i] >= archivo["tamano"]:
                archivo["bloque_asignado"] = i
                memoria[i] -= archivo["tamano"]
                ultimo_bloque_usado = i  # Guardamos posición donde nos quedamos
                asignado = True
                break
        if not asignado:
            archivos_que_no_caben.append(archivo["nombre"])


# Función para mostrar la asignación de archivos
def mostrar_asignacion_archivos():
    print("\nAsignación de archivos:")
    for archivo in archivos:
        if "bloque_asignado" in archivo:
            print(f"Archivo: {archivo['nombre']}, Tamaño: {archivo['tamano']} KB, Bloque asignado: {archivo['bloque_asignado'] + 1}")
        else:
            print(f"Archivo: {archivo['nombre']} no asignado")

    if archivos_que_no_caben:
        print("\nLos siguientes archivos no caben en la memoria:")
        for archivo in archivos_que_no_caben:
            print(archivo)
    print()

# Agregar nuevos espacios de memoria
def agregar_espacios_memoria():
    while True:
        tamano = int(input("Tamaño del espacio (KB): "))
        posicion = input("Posición (al inicio o al final): ").lower()
        if posicion == "al inicio":
            memoria.insert(0, tamano)
            memoria_original.insert(0, tamano)  # Actualiza memoria_original
        elif posicion == "al final":
            memoria.append(tamano)
            memoria_original.append(tamano)  # Actualiza memoria_original
        else:
            print("Posición no válida. Inténtalo de nuevo.")
        continuar = input("¿Deseas agregar otro espacio de memoria? (s/n): ").lower()
        if continuar != 's':
            break


# Función para agregar nuevos archivos
def agregar_archivos():
    while True:
        print("Selecciona una opción para agregar archivos:")
        print("[ 1 ] Archivos físicos (carpeta de referencia)")
        print("[ 2 ] Archivos virtuales (tamaño y peso)")
        print("[ 3 ] No agregar archivos")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            carpeta_referencia = input("Ruta de la carpeta de referencia: ")
            agregar_archivos_fisicos(carpeta_referencia)
        elif opcion == "2":
            agregar_archivos_virtuales()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Función para agregar archivos físicos desde una carpeta de referencia
def agregar_archivos_fisicos(carpeta_referencia):
    archivos_carpeta = os.listdir(carpeta_referencia)
    for archivo in archivos_carpeta:
        ruta_archivo = os.path.join(carpeta_referencia, archivo)
        if os.path.isfile(ruta_archivo):
            tamano = os.path.getsize(ruta_archivo) // 1024
            archivos.append({"nombre": archivo, "tamano": tamano}) # Extraer datos de interes

# Función para agregar archivos virtuales
def agregar_archivos_virtuales():
    while True:
        nombre = input("Nombre del archivo (o 'q' para salir): ")
        if nombre == 'q':
            break
        tamano = int(input("Tamaño del archivo (KB): "))
        archivos.append({"nombre": nombre, "tamano": tamano})

# Función para el menú principal
def menu_principal():
    while True:
        print("\n<-- Selecciona una opción -->")
        print("[ 1 ] Seleccionar algoritmo de asignación de memoria")
        print("[ 2 ] Agregar nuevos espacios de memoria")
        print("[ 3 ] Agregar nuevos archivos")
        print("[ 4 ] Mostrar asignación de archivos")
        print("[ 5 ] Salir")
        
        opcion = input("Elije una opción: -> ")
        
        if opcion == "1":
            mostrar_algoritmos()
        elif opcion == "2":
            agregar_espacios_memoria()
        elif opcion == "3":
            agregar_archivos()
        elif opcion == "4":
            mostrar_asignacion_archivos()
        elif opcion == "5":
            print("\t\n<--- Hasta luego, Crack --->")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Función para mostrar los algoritmos de asignación de memoria
def mostrar_algoritmos():
    while True:
        print("\n<-- Selecciona un algoritmo de asignación de memoria -->")
        print("[ 1 ] Primer Ajuste")
        print("[ 2 ] Mejor Ajuste")
        print("[ 3 ] Peor Ajuste")
        print("[ 4 ] Siguiente Ajuste")
        print("[ 5 ] Regresar al menú principal")
        
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
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Iniciar el menú principal
menu_principal()
