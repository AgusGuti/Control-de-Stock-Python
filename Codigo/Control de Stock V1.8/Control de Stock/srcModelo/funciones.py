# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez

import subprocess as sp
from dicDatos import *
import sys
from builtins import str

#Funcion que limpia la pantalla

def limpia():
    plataforma = sys.platform
    if plataforma.startswith('linux'):
        sp.call('clear')
    elif plataforma.startswith('win'):
        sp.call('cls', shell=True)
        
        
#Funcion que valida que lo ingresado sea un numero entero
#Emite mensaje de error al no cumplirse
#Se pasa mensaje a mostrar previo al ingreso como parametro        

def leerEntero(mensaje):

    while(True):
        dato = input(mensaje)
        try:
            dato = int(dato)
            break
        except ValueError:
                print("ERROR El elemento ingresado no es un entero")
        pass
    
    return dato

#Funcion que valida que lo ingresado sea una cadena
#Emite mensaje de error al no cumplirse
#Se pasa mensaje a mostrar previo al ingreso como parametro

#(INCOMPLETA)
def leerCadena(mensaje):

    while(True):
        dato = str(input(mensaje))
        
        if(dato.isalpha() == True):
            break
            pass
        else:
            print("ERROR Lo ingresado no es un nombre")
            pass
                        
        pass
    
    return dato

#Funcion que busca un elemento en el diccionario de Stock
#Emite mensaje de error al no existir el elemento
#Se convierte lo ingresado a minuscula para evitar discrepancias

def buscarElemento():

    while(True):
        opcion = input("\nSeleccione un elemento: (0- Para volver al menu principal)\n")
        if(opcion != '0'):
            try:
                opcion = opcion.lower()
                dicStock[opcion].mostrarProducto()
                break
            except KeyError:
                print("ERROR El producto no existe en la lista")
            pass
            pass
        else:
            break
            pass
    
    return opcion


#Funcion que muestra el logo del grupo de trabajo

def mostrarLogo():
    
    print("\tGGGGGGG")
    print("\tGG       UU  UU  TTTTTT  LL      OOOOOO  PPPPPP")
    print("\tGG       UU  UU    TT    LL      OO  OO  PP  PP")
    print("\tGG  GGG  UU  UU    TT    LL      OO  OO  PPPPPP")
    print("\tGG   GG  UU  UU    TT    LL      OO  OO  PP    ")
    print("\tGGGGGGG  UUUUUU    TT    LLLLLL  OOOOOO  PP    ")
    
    print ("\n")
    print ("\t\tDesarrollado por GUTLOP")
    print ("\n")