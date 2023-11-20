########################################################################################################################
# By: Dexne
# 
# Version modificada y mejorada de la practica 04 - Algoritmos de planificacion
# En esta version se ha modificado para que ahora funcione con hilos, esto gracias a la liberia de threading
# Ademass, se ha implementado una pequenia y simple interfaz de usuario para hacerlo un poco mas amigable y facil
# de usar.
# 
# Los algoritmos trabajados son:
# Round Robin
# SJF
# FIFO
# Prioridades
#
########################################################################################################################

import csv
import sys
import threading
import tkinter as tk


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
        resultado.append( (tiempo_actual, nombre) )
    
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

# Función para agregar un servicio y actualizar el archivo
def agregar_servicio(nombre_entry, tiempo_entry, prioridad_entry, procesos, resultados_text):
    nombre = nombre_entry.get()
    tiempo = int(tiempo_entry.get())
    prioridad = int(prioridad_entry.get())

    nuevo_servicio = (nombre, tiempo, prioridad)
    procesos.append(nuevo_servicio)

    with open("procesos.txt", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(nuevo_servicio)

    mensaje = f"Servicio '{nombre}' agregado con éxito y actualizado en procesos.txt.\n"
    resultados_text.insert(tk.END, mensaje)

# Función principal para ejecutar algoritmos en un hilo
def execute_algorithm(procesos, opcion, resultados_text):
    archivo_procesos = "procesos.txt"
    resultados_text.delete(1.0, tk.END)  # Limpiar el contenido anterior

    if opcion == '1':
        quantum = 3
        resultados = round_robin(procesos, quantum)
        resultados_text.insert(tk.END, "\n\tResultados del Algoritmo Round Robin:\n")
    elif opcion == '2':
        resultados = sjf(procesos)
        resultados_text.insert(tk.END, "\n\tResultados del Algoritmo SJF (Shortest Job First):\n")
    elif opcion == '3':
        resultados = fifo(procesos)
        resultados_text.insert(tk.END, "\n\tResultados del Algoritmo FIFO (First-In, First-Out):\n")
    elif opcion == '4':
        resultados = prioridades(procesos)
        resultados_text.insert(tk.END, "\n\tResultados del Algoritmo de Prioridades:\n")
    
    for tiempo, proceso in resultados:
        resultado = f"Servicio: {proceso}, Tiempo de Finalización: {tiempo}\n"
        resultados_text.insert(tk.END, resultado)

# Función principal
def main():

    def cerrar_programa():
        ventana.destroy()
        sys.exit(0)
    
    ventana = tk.Tk()
    ventana.title("Algoritmos de Planificación")

    # Establecer el tamaño de la ventana
    ventana.geometry("600x700")

    # Etiqueta de bienvenida
    bienvenida_label = tk.Label(ventana, text="Planificador de procesos", font=("Arial", 18))
    bienvenida_label.pack()

    # Botón para cargar procesos al programa
    cargar_procesos_button = tk.Button(ventana, text="Cargar procesos", command=lambda: cargar_procesos("procesos.txt"))
    cargar_procesos_button.pack()

    # Entradas para agregar un servicio
    nombre_label = tk.Label(ventana, text="Nombre del proceso:")
    nombre_label.pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    tiempo_label = tk.Label(ventana, text="Tiempo de duración:")
    tiempo_label.pack()
    tiempo_entry = tk.Entry(ventana)
    tiempo_entry.pack()

    prioridad_label = tk.Label(ventana, text="Prioridad:")
    prioridad_label.pack()
    prioridad_entry = tk.Entry(ventana)
    prioridad_entry.pack()

    # Botón para agregar un servicio
    agregar_servicio_button = tk.Button(ventana, text="Agregar servicio", command=lambda: agregar_servicio(nombre_entry, tiempo_entry, prioridad_entry, procesos, resultados_text))
    agregar_servicio_button.pack()

    # Botones para ejecutar algoritmos
    round_robin_button = tk.Button(ventana, text="[Round Robin]", command=lambda: threading.Thread(target=execute_algorithm, args=(procesos, '1', resultados_text)).start())
    round_robin_button.pack()

    sjf_button = tk.Button(ventana, text="[    SJF    ]", command=lambda: threading.Thread(target=execute_algorithm, args=(procesos, '2', resultados_text)).start())
    sjf_button.pack()

    fifo_button = tk.Button(ventana, text="[    FIFO   ]", command=lambda: threading.Thread(target=execute_algorithm, args=(procesos, '3', resultados_text)).start())
    fifo_button.pack()

    prioridades_button = tk.Button(ventana, text="[Prioridades]", command=lambda: threading.Thread(target=execute_algorithm, args=(procesos, '4', resultados_text)).start())
    prioridades_button.pack()

    # Crear un widget Text para mostrar los resultados
    resultados_text = tk.Text(ventana, height=15, width=60)
    resultados_text.pack()

    # Botón para cerrar el programa
    cerrar_programa_button = tk.Button(ventana, text="Cerrar programa", command=cerrar_programa)
    cerrar_programa_button.pack()

    ventana.mainloop()

if __name__ == "__main__":
    procesos = cargar_procesos("procesos.txt")
    main()
