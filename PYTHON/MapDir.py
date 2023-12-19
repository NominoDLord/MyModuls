########################################################################################################################
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
########################################################################################################################

"""
    Nombre: MapDir
    Tipo: Script

    Info:

        Crea un archivo de texto que contendrá la información (nombre + extensión) de los elementos que existan
        dentro del directorio a ingresar ordenados de forma estructurada.

        El archivo de texto generado tomará como referencia el nombre del directorio raíz.

    Ejemplo:

        >>> Mapa[Nombre].txt

            Nombre
            |-- archivo1.ext
            |-- archivo2.ext
            | > Carpeta1/
            |   |-- archivo3.ext
            |   |-- archivo4.ext
            |   | > Carpeta2/
            |   |   |-- archivo5.ext
            |   |   |-- archivo6.ext
            |   | > Carpeta3/
            |   |   |-- archivo7.ext
            |   | > Carpeta4/
            |   |   |-- archivo8.ext
            |   |   |-- archivo9.ext
"""

import os

def generar_estructura_directorio(directorio, archivo_salida, directorio_salida="."):
    if not os.path.exists(directorio_salida):
        print(f"La ruta del directorio de salida '{directorio_salida}' no existe. Utilizando el directorio actual.")
        directorio_salida = "."

    with open(os.path.join(directorio_salida, archivo_salida), 'w') as archivo:
        # Abre/Crea el 'archivo de salida' en modo escritura (w).
        nombre_carpeta = os.path.basename(directorio)  # Obtiene el "nombre base" del directorio (carpeta).
        archivo.write(nombre_carpeta + '\n')  # Escribe el nombre de la carpeta principal en el archivo.

        procesar_directorio(directorio, archivo, 0, directorio_salida)  # Llamar a la función recursiva.

    return None


def procesar_directorio(directorio, archivo, nivel, directorio_salida):
    for item in os.listdir(directorio):
        if not item.startswith('.'):
            ruta_item = os.path.join(directorio, item)

            prefijo_dir = "|   " * nivel + "\\ > "
            prefijo_file = "|   " * nivel + "|-- "

            if os.path.isfile(ruta_item):
                archivo.write(f"{prefijo_file}{item}\n")  # Verifica si el elemento es un archivo.
            elif os.path.isdir(ruta_item):
                archivo.write(f"{prefijo_dir}{item}/\n")  # Verifica si el elemento es un directorio.
                procesar_directorio(ruta_item, archivo, nivel + 1, directorio_salida)

    return None


def procesar_archivo(nombre):
    """

    @param nombre:
    @return:
    """
    # Lista para almacenar líneas que inician con "|--"
    lineas_guardadas = []

    # Leer el archivo
    with open(nombre, 'r') as archivo:
        lineas = archivo.readlines()

    # Filtrar líneas que inician con "|--"
    lineas_filtradas = [linea for linea in lineas if linea.startswith("|--")]

    # Guardar las líneas filtradas y eliminarlas del archivo original
    for linea in lineas_filtradas:
        lineas_guardadas.append(linea)
        lineas.remove(linea)

    # Volver a introducir las líneas guardadas en el archivo
    with open(nombre, 'w') as archivo:
        # Escribir la primera línea (sin cambios)
        archivo.write(lineas[0])

        # Escribir las líneas guardadas a partir de la segunda línea
        for linea_guardada in lineas_guardadas:
            archivo.write(linea_guardada)

        # Escribir las líneas restantes del archivo original
        for linea in lineas[1:]:
            archivo.write(linea)

    return None


ruta_de_entrada = input("Ruta del directorio a mapear: ")
carpeta = os.path.basename(ruta_de_entrada)
nombre_archivo = f"Mapa[{carpeta}].txt"

ruta_de_salida = input("Ruta para el archivo generado (opcional): ") or "."  # presiona Enter para usar el actual

generar_estructura_directorio(ruta_de_entrada, nombre_archivo, ruta_de_salida)
procesar_archivo(nombre_archivo)

# C:/Users/Ferran/Documents/GitHub/MyModuls
