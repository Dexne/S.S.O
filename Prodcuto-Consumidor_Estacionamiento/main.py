# By: Dexne
# Producto-Consumidor
# Simulacion de un estacionamiento

# Librerías necesarias
import random
import threading
import time
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import askfloat


# Definicion de la clase estacionamiento
class Estacionamiento:
    def __init__(self, tamano=12): # Establecer un espacio de 12
        self.tamano = tamano
        self.espacios = [None] * tamano
        self.entrada_activa = False
        self.salida_activa = False
        self.frecuencia_entrada = 2  # Frecuencia inicial de entrada en segundos
        self.frecuencia_salida = 2   # Frecuencia inicial de salida en segundos
        self.frecuencia_lock = threading.Lock()
        self.espacios_ocupados = 0 # Comenzar con el estacionamiento vacio

    def ingresar_auto(self, placa):
        if self.espacios_ocupados < self.tamano: # Espacios disponibles ?
            for i in range(self.tamano):
                if self.espacios[i] is None:
                    self.espacios[i] = placa # Asignamos espacio
                    self.espacios_ocupados += 1 # Reducimos capacidad
                    print(f"El auto con la placa {placa} ha ingresado al estacionamiento en el espacio {i + 1}.")
                    break
        else: # Full
            print("Estacionamiento lleno. No se pueden ingresar más autos.")

    def salir_auto(self, placa):
        if self.espacios_ocupados > 0: # Hay autos por sacar ?
            if placa in self.espacios:
                espacio = self.espacios.index(placa)
                self.espacios[espacio] = None
                self.espacios_ocupados -= 1 # Incrementar capacidad
                print(f"El auto con la placa {placa} ha salido del estacionamiento desde el espacio {espacio + 1}.")
            else:
                print(f"El auto con la placa {placa} no se encuentra en el estacionamiento.")
        else: # Empty
            print("Estacionamiento vacío. No se pueden retirar más autos.")

def auto_entrada(estacionamiento, gui):
    while estacionamiento.entrada_activa:
        with estacionamiento.frecuencia_lock:
            if estacionamiento.espacios_ocupados < estacionamiento.tamano:
                # Generamos placa para el auto
                placa = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3)) + ''.join(random.choice('0123456789') for _ in range(3))
                estacionamiento.ingresar_auto(placa)
                gui.actualizar_interfaz()
            else:
                print("Estacionamiento lleno. No se pueden ingresar más autos.")
        time.sleep(estacionamiento.frecuencia_entrada)

def auto_salida(estacionamiento, gui):
    while estacionamiento.salida_activa:
        with estacionamiento.frecuencia_lock:
            if estacionamiento.espacios_ocupados > 0:
                autos_en_estacionamiento = [auto for auto in estacionamiento.espacios if auto is not None]
                if autos_en_estacionamiento:
                    placa = random.choice(autos_en_estacionamiento)
                    estacionamiento.salir_auto(placa)
                    gui.actualizar_interfaz()
                else:
                    print("Estacionamiento vacío. No se pueden retirar más autos.")
        time.sleep(estacionamiento.frecuencia_salida)

class EstacionamientoGUI:
    def __init__(self, root, estacionamiento):
        self.root = root
        self.root.title("<--- Estacionamiento --->")
        self.estacionamiento = estacionamiento
        self.botones = []
        for i in range(estacionamiento.tamano):
            fila = i // 6 # Defincion de la matriz del estacionamiento
            columna = i % 6
            boton = tk.Button(root, text=f"Espacio {i + 1}", width=10, height=2)
            boton.grid(row=fila, column=columna)
            self.botones.append(boton)
        
        # Botón "Detener programa"
        self.detener_programa_button = tk.Button(root, text="Detener programa", command=self.detener_programa)
        self.detener_programa_button.grid(row=3, column=0, columnspan=2)
        
        # Botón "Actualizar entrada"
        self.actualizar_entrada_button = tk.Button(root, text="Actualizar entrada", command=self.actualizar_frecuencia_entrada)
        self.actualizar_entrada_button.grid(row=3, column=2, columnspan=2)

        # Botón "Actualizar salida"
        self.actualizar_salida_button = tk.Button(root, text="Actualizar salida", command=self.actualizar_frecuencia_salida)
        self.actualizar_salida_button.grid(row=3, column=4, columnspan=2)

        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        for i in range(self.estacionamiento.tamano):
            if self.estacionamiento.espacios[i] is not None:
                self.botones[i].config(bg="red") # Ocupado
            else:
                self.botones[i].config(bg="green") # Disponible

    def detener_programa(self):
        self.estacionamiento.entrada_activa = False
        self.estacionamiento.salida_activa = False
        self.root.destroy()

    def actualizar_frecuencia_entrada(self):
        with self.estacionamiento.frecuencia_lock:
            nueva_frecuencia = askfloat("Nueva entrada", "Ingrese la nueva frecuencia de entrada (segundos):", initialvalue=self.estacionamiento.frecuencia_entrada)
            if nueva_frecuencia is not None:
                self.estacionamiento.frecuencia_entrada = nueva_frecuencia

    def actualizar_frecuencia_salida(self):
        with self.estacionamiento.frecuencia_lock:
            nueva_frecuencia = askfloat("Nueva salida", "Ingrese la nueva frecuencia de salida (segundos):", initialvalue=self.estacionamiento.frecuencia_salida)
            if nueva_frecuencia is not None:
                self.estacionamiento.frecuencia_salida = nueva_frecuencia

def main():
    estacionamiento = Estacionamiento(12) # Espacio
    root = tk.Tk()
    gui = EstacionamientoGUI(root, estacionamiento)
    # Manejo por separado con hilos
    hilo_entrada = threading.Thread(target=auto_entrada, args=(estacionamiento, gui))
    hilo_salida = threading.Thread(target=auto_salida, args=(estacionamiento, gui))
    
    estacionamiento.entrada_activa = True
    estacionamiento.salida_activa = True
    
    hilo_entrada.start()
    hilo_salida.start()
    
    root.mainloop()
    
    estacionamiento.entrada_activa = False
    estacionamiento.salida_activa = False
    hilo_entrada.join()
    hilo_salida.join()

if __name__ == "__main__":
    main()
