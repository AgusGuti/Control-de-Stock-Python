# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez

import time
import os


# Metodo que crea el archivo con el nombre de la fecha y carga los datos SOLO si no existe.
def crearArchivo(diccionario):
    
    nombre = time.asctime(time.localtime()) + ".txt"
    nombre = nombre[0:10] + " - " + nombre[20:]
    
    if (os.path.isfile(nombre) == False):
        with open(nombre, 'w') as fileStock:
            escribirArchivo(fileStock, diccionario)
            fileStock.close()
        pass
    else:
        print("ERROR el archivo ya existe.")    
        pass   
    
    pass


# Metodo que escribe el archivo seleccionado
def escribirArchivo(archivo, diccionario):
    total = 0
    
    archivo.write("Producto\tStock\tPrecio p/u\n\n")
        
    for key in diccionario:
        aEscribir = []
        aEscribir.append(diccionario[key].nombre + "    ")
        aEscribir.append(str(diccionario[key].stockActual))
        aEscribir.append(str(diccionario[key].precioXUnidad))
        archivo.write('\t'.join(aEscribir) + "\n")
        
        total += diccionario[key].calcularPrecio()
        pass
    
    archivo.write("\n\t\t\tTotal: " + str(total))                
    pass


# Metodo que permite modificar el archivo seleccionado.
def modificarArchivo(archivo, diccionario):
    
    pass
