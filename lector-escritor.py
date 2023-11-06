#####################################################################
#
# By: Dexne
# 
# Lector-Escritor
#
# Durante la edición (Editar), no se permita la lectura (Leer) 
# para mantener la consistencia de los datos.
# Durante la escritura (Guardar), no se permita ni la lectura ni la 
# edición para evitar interferencias.
#
#####################################################################
import tkinter as tk
import threading
import time

archivo_mutex = threading.Semaphore(1)
lectores_mutex = threading.Semaphore(1)
lectores_count = 0
archivo_contenido = "Este es el contenido del archivo para lectura en tiempo real."

def leer():
    global lectores_count
    lectores_mutex.acquire()
    lectores_count += 1
    if lectores_count == 1:
        archivo_mutex.acquire()
    lectores_mutex.release()

    text.delete(1.0, tk.END)
    mostrar_contenido_en_tiempo_real(archivo_contenido)

    lectores_mutex.acquire()
    lectores_count -= 1
    if lectores_count == 0:
        archivo_mutex.release()
    lectores_mutex.release()

def mostrar_contenido_en_tiempo_real(contenido):
    for palabra in contenido.split():
        text.insert(tk.END, palabra + ' ')
        root.update_idletasks()
        time.sleep(0.1)  # Ajusta el tiempo de espera aquí para controlar la velocidad

def editar():
    global archivo_contenido
    # Habilita la edición en la ventana de visualización
    text.config(state=tk.NORMAL)

def guardar():
    global archivo_contenido
    archivo_contenido = text.get("1.0", tk.END)

    archivo_mutex.acquire()
    with open("archivo.txt", "w") as file:
        file.write(archivo_contenido)
    archivo_mutex.release()

    # Deshabilita la edición en la ventana de visualización
    text.config(state=tk.DISABLED)

def main():
    global root, text
    root = tk.Tk()
    root.title("Simulación de Lector-Escritor")
    ventana_lectura = tk.Frame(root)
    ventana_lectura.pack(side=tk.LEFT)
    label_lectura = tk.Label(ventana_lectura, text="Ventana de Lectura")
    label_lectura.pack()
    btn_leer = tk.Button(ventana_lectura, text="Leer", command=leer)
    btn_leer.pack()
    ventana_edicion = tk.Frame(root)
    ventana_edicion.pack(side=tk.LEFT)
    label_edicion = tk.Label(ventana_edicion, text="Ventana de Edición")
    label_edicion.pack()

    # Agrega un campo de edición de texto en modo deshabilitado
    text = tk.Text(ventana_edicion, height=5, width=30, state=tk.DISABLED)
    text.pack()

    btn_editar = tk.Button(ventana_edicion, text="Editar", command=editar)
    btn_editar.pack()
    ventana_guardado = tk.Frame(root)
    ventana_guardado.pack(side=tk.LEFT)
    label_guardado = tk.Label(ventana_guardado, text="Ventana de Guardado")
    label_guardado.pack()
    btn_guardar = tk.Button(ventana_guardado, text="Guardar", command=guardar)
    btn_guardar.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
