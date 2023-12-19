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
    INFO:
    Se realiza una lectura del archivo de texto (~.txt) que contiene valores booleanos y los almacena en una lista.
"""

# Introducir la localización del Archivo
nombre_archivo = input("Dirección Archivo TXT: ")

# Lista para almacenar los valores
valores = []

# Intentar abrir y leer el archivo
try:
    with open(nombre_archivo, 'r') as archivo:
        # Leer cada línea del archivo
        for linea in archivo:
            # Convertir el valor a booleano y agregarlo a la lista
            valor = linea.strip().lower() == 'true'
            valores.append(valor)

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")


""" Ejemplo:
    
    .../valores.txt
        
        True
        True
        False
        False
        True
        False
        True
    
    .../LecturaTXT [Bools].py
    
        print(valores)
    
    .../CMD
    
    >>> [True, True, False, False, True, False, True]
"""

