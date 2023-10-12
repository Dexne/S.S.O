##################################################################################
# 
# By: Dexne
# 
# Practica - Hilos
# 
# Objetivo, mover 2 imagenes (Una vertical y otra horizonatal) con hilos
# Un hilo para cada imagen
#
# Dado que no puede ser en terminal, hacemos uso de la libreria TkInter
# Para desarrollar un entorno grafico sentillo.
# 
##################################################################################

# Librerias necesarias
import tkinter as tk
from tkinter import Canvas, Button
from PIL import Image, ImageTk
import threading
import time

# Función para mover la imagen de izquierda a derecha
def move_image_x():
    global x1, running
    while running:
        canvas.move(image1_id, 2, 0)
        x1 += 2
        if x1 > window_width:
            x1 = -100
            canvas.coords(image1_id, x1, y1)
        time.sleep(0.01)

# Función para mover la imagen de arriba hacia abajo
def move_image_y():
    global y2, running
    while running:
        canvas.move(image2_id, 0, 2)
        y2 += 2
        if y2 > window_height:
            y2 = -100
            canvas.coords(image2_id, x2, y2)
        time.sleep(0.01)

# Función para detener los hilos y cerrar la ventana
def stop_program():
    global running
    running = False
    window.destroy()

# Crear la ventana principal
window = tk.Tk()
window.title("<--- Movimiento de Imágenes --->")

# Configurar el lienzo (Canvas)
window_width = 1600
window_height = 1000
canvas = Canvas(window, width=window_width, height=window_height)
canvas.pack()

# Cargar las imágenes
image1 = Image.open("imagen1.png")
image2 = Image.open("imagen2.png")
photo1 = ImageTk.PhotoImage(image1)
photo2 = ImageTk.PhotoImage(image2)

# Mostrar las imágenes en el lienzo
image1_id = canvas.create_image(0, 100, anchor=tk.NW, image=photo1)
image2_id = canvas.create_image(100, 0, anchor=tk.NW, image=photo2)

# Inicializar las posiciones de las imágenes
x1, y1 = 0, 100
x2, y2 = 100, 0

# Variable para controlar si los hilos siguen corriendo
running = True

# Crear hilos para mover las imágenes
thread1 = threading.Thread(target=move_image_x)
thread2 = threading.Thread(target=move_image_y)

# Iniciar los hilos
thread1.start()
thread2.start()

# Botón para terminar el programa
button = Button(window, text="Terminar", command=stop_program)
button.pack()

window.mainloop()
