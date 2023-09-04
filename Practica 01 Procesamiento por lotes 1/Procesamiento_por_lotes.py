# Made of by Dexne

import socket


# Convertir valor hexa a decimal
# caso exitoso convierte el numero
# caso de falla, devuelve null
def hex_to_decimal(hex_string):
    try:
        decimal_value = int(hex_string, 16)
        return decimal_value
    except ValueError:
        return None

# Convertir direccion IPv4 a hexa
# caso de exito, hace la convercion
# caso de falla, devuelve null
def convert_ipv4_to_hex(ipv4_address):
    try:
        # socket.inet_aton(ipv4_address) toma una dirección IPv4 en formato
        #  de cadena (por ejemplo, "192.168.1.1") y la convierte en una 
        # representación binaria de 32 bits.
        hex_value = socket.inet_aton(ipv4_address).hex() # .hex() toma la representación binaria y la convierte en una cadena hexadecimal.
        return hex_value
    except OSError:
        return None

# Nombre del archivo de entrada y salida
archivo_entrada = "prueba2.txt" 
archivo_salida = "resultados.txt"

# Abre el archivo de salida en modo escritura
with open(archivo_salida, 'w') as output_file:
    # Leer el archivo de entrada
    with open(archivo_entrada, 'r') as input_file:
        lines = input_file.readlines()

    # Procesar cada línea del archivo
    for line in lines:
        # Indicar que los elementos esta separados por comas
        elementos = line.strip().split(',')
        
        if len(elementos) >= 6:
            # Separar la primera posición por la diagonal y convertir valores hexadecimales a decimales
            valores_hex = elementos[0].split('/')[0].split(':')
            valores_decimales = [str(hex_to_decimal(hex_val)) for hex_val in valores_hex]

            # Convertir números en la sexta posición a hexadecimal con la división de puntos
            numeros_sexta_posicion = elementos[5].split('.')
            hex_numeros = [hex(int(num)).replace('0x', '') for num in numeros_sexta_posicion]
            hex_sexta_posicion = '.'.join(hex_numeros)

            # Guardar los datos en un mismo renglón con la división de puntos
            datos_renglon = f"{elementos[2]}, " \
                            f"{', '.join(valores_decimales)}, " \
                            f"{hex_sexta_posicion}\n"
            output_file.write(datos_renglon)

# Cierra los archivos
input_file.close()
output_file.close()
