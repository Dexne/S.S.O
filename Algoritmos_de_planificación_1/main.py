#########################################################################################################
#
# Made of by Dexne
#
# Codigo elaborado en Python con ayuda del modulo csv para el cargado del archvivo
#
# En este pequeño script se hace la implementacion de los algoritmos de planificacion
# de planificacion como:
# Round Robin
# SJF
# FIFO
# Prioridades
# 
# Para el caso de Round Robin se establece un quantum de 3
# Como ejecutar el codigo
# Basta con descargar o clonar el codigo fuente
# Descargar o poner el archivo "procesos.txt" en
# la misma ruta que el archivo "main.py"
# 
# Si cuentas con un IDE completo de desarrollo de python puedes valerte de la opcion de "Ejecutar"
# Si te encuentras en un sistema operativo Linux abriremos una nueva terminal y nos dirijimos al 
# directorio.
# Seguido de eso ejecutamos el siguiente comando "python3 main.py"
# En ese momento el código comenzará a ejecutarse.
#
#########################################################################################################

import csv # Modulo para poder tomar el txt como un csv

# Algoritmo Round Robin
def round_robin( procesos, quantum ):
    resultado = []
    cola = procesos.copy()
    tiempo_actual = 0
    
    while cola:
        proceso_actual = cola.pop(0)
        nombre, tiempo, prioridad = proceso_actual
        
        if tiempo > quantum:
            tiempo_actual += quantum
            resultado.append((tiempo_actual, nombre))
            tiempo -= quantum
            cola.append((nombre, tiempo, prioridad))  # Vuelve a poner el proceso al final de la cola
        else:
            tiempo_actual += tiempo
            resultado.append((tiempo_actual, nombre))
    
    return resultado


# Algoritmo SJF
def sjf( procesos ):
    procesos.sort(key=lambda x: x[1]) # Ordenar en torno al tiempo
    resultado = []
    tiempo_actual = 0
    
    for proceso in procesos:
        nombre, tiempo, prioridad = proceso
        tiempo_actual += tiempo
        resultado.append((tiempo_actual, nombre))
    
    return resultado

# Algoritmo FIFO
def fifo( procesos ):
    resultado = []
    tiempo_actual = 0
    
    for proceso in procesos:
        nombre, tiempo, prioridad = proceso
        tiempo_actual += tiempo
        resultado.append((tiempo_actual, nombre))
    
    return resultado

# Algoritmo por Prioridades
def prioridades( procesos ):
    procesos.sort(key=lambda x: x[2]) # Ordenar en torno a la prioridad
    resultado = []
    tiempo_actual = 0
    
    for proceso in procesos:
        nombre, tiempo, prioridad = proceso
        tiempo_actual += tiempo
        resultado.append((tiempo_actual, nombre))
    
    return resultado

# Función para cargar los procesos desde el archivo
def cargar_procesos(archivo):
    procesos = []
    with open(archivo, 'r') as file: # Apertura del archivo en modo lectura
        reader = csv.reader(file) # Leemos el txt de procesos en forma de csv
        for row in reader:
            nombre, tiempo, prioridad = row # Definicion de las cabeceras 
            procesos.append((nombre, int(tiempo), int(prioridad))) # Coversion a enteros
    return procesos

# Función principal
def main():
    archivo_procesos = "procesos.txt" # Path de procesos.txt
    procesos = cargar_procesos(archivo_procesos)
    
    while True:
        print("\t<-- Algoritmos de Planificación -->")
        print("[ 1 ] Round Robin (lapso)")
        print("[ 2 ] SJF (el más corto primero)")
        print("[ 3 ] FIFO (el primero en llegar, el primero en salir)")
        print("[ 4 ] Prioridades (establece prioridades)")
        print("[ 0 ] Salir")
        
        opcion = input("Seleccione un algoritmo (0-4): ")
        
        if opcion == '0': break

        elif opcion == '1':
            quantum = 3
            resultados = round_robin(procesos, quantum)
            print("\nResultados del Algoritmo Round Robin:")
        elif opcion == '2':
            resultados = sjf(procesos)
            print("\nResultados del Algoritmo SJF (Shortest Job First):")
        elif opcion == '3':
            resultados = fifo(procesos)
            print("\nResultados del Algoritmo FIFO (First-In, First-Out):")
        elif opcion == '4':
            resultados = prioridades(procesos)
            print("\nResultados del Algoritmo de Prioridades:")
        else:
            print("Opción no válida. Intente de nuevo.") # Validacion
            continue
        
        for tiempo, proceso in resultados: # Mostrar los resultados de los algoritmos
            print(f"Servicio: {proceso}, Tiempo de Finalización: {tiempo}")
        
        probar_otro = input("\n¿Quieres probar otro algoritmo? [ 1 ] Si, [ 0 ] No: ")
        if probar_otro != '1': # Terminar el ciclo
            break

if __name__ == "__main__":
    main()