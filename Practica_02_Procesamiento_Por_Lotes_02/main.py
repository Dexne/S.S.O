# Made of by: Dexne
# 
# Practica 02: Procesamiento por lotes 2
# 
# Codigo realizado en el lenguaje de programación python
# Este codigo se apoya de las librerias OS, random, string y shutil para su ejecucion
# El objetivo del presente script es el de, dada una ruta en especifico, revisa
# todos los archivos dentro de el, incluso los que estan dentro de carpetas anidados
# y comienza a iterar dentro de su contenido cambiando las letras por numeros y viceversa
# en el mismo directorio de la carpeta origen.

# Pasos para la correcta ejecucion:
#     Descargar o copiar el archivo main.py
#     Si se cuenta con un IDE completo de desarrollo de python dar click en ejecutar
#     Si se encuentra en un sistema operativo linux como yo:
#         Abra una nueva terminal
#         Navege hasta la ruta donde tiene su archivo main.py
#         Ejecutar el siguiente comando: python3 main.py
# 
#     El programa le pedirá la ruta de la carpeta donde trabajará
# 
#     Asegurese de ingresarla tal cual es, de ser posible, copia la ruta desde
#     el explorador de archivos.

# Libreríias necesarias
import os
import random
import string
import shutil

# Función para cambiar caracteres en un archivo
def cambiar_caracteres_en_archivo(archivo):
    try:
        with open(archivo, 'r') as f: # Apertura en modo lectura
            contenido = f.read()
        
        nuevo_contenido = []
        for caracter in contenido: # Iterar en el documento
            if caracter.isalpha():
                nuevo_caracter = random.choice(string.digits)
            elif caracter.isdigit():
                nuevo_caracter = random.choice(string.ascii_uppercase)
            else:
                nuevo_caracter = caracter
            nuevo_contenido.append(nuevo_caracter)

        with open(archivo, 'w') as f: # Apertura en modo escritura
            f.write(''.join(nuevo_contenido))
    except Exception as e: # Manejo de excepciones
        print(f"Error al cambiar caracteres en el archivo {archivo}: {e}")

# Pedir la ubicación de la carpeta de origen
carpeta_origen = input("Ingrese la ubicación de la carpeta de origen: ")

# Crear una copia de la carpeta de origen en el mismo directorio
carpeta_copia = os.path.join(os.path.dirname(carpeta_origen), "copia")
# copiará todos los archivos y subcarpetas de carpeta_origen a carpeta_copia
shutil.copytree(carpeta_origen, carpeta_copia)

# Procesar archivos en la carpeta de copia
for root, _, files in os.walk(carpeta_copia):
    for file in files:
        archivo = os.path.join(root, file)
        cambiar_caracteres_en_archivo(archivo)

print("Proceso completado. Los archivos han sido modificados en la carpeta de copia.")
