# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez


from funciones import *
from operator import invert
from _overlapped import NULL
from menu import *
from dicPromo import dicPromo

salir =False


while(salir == False):
	limpia()
	
	mostrarMenuPromo()

	opcion = leerEntero("Ingrese el item de cafe/promo: ")
	
	if (opcion == 0):
		salir == True
		pass
	else:
		print()
		cantidad = leerEntero("Ingrese la cantidad vendida: ")
		print()
		dicPromo["promo" + opcion].cntVentas += 1
		pass		
 
	pass


