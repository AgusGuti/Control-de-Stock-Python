# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez

from funciones import *
from menu import *
from dicPromo import *

class Promo(object):
    
    def __init__(self, idPromo, nombre, cntVentas, precio):
        self.idPromo = idPromo
        self.nombre = nombre
        self.cntVentas = cntVentas
        self.precio = precio
        
        
    def mostrarPromo(self):
        print(self.nombre)
        print("Cantidad vendidas: ", self.cntVentas, end=" ; ")
        print("Precio: ", self.precio)
        