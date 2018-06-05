# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez

from ClaseProducto import *
from DicDatos import *
from ManejoRegistro import *
import os

os.system('cls')

print("GGGGGGG")
print("GG       UU  UU  TTTTTT  LL      OOOOOO  PPPPPP")
print("GG       UU  UU    TT    LL      OO  OO  PP  PP")
print("GG  GGG  UU  UU    TT    LL      OO  OO  PPPPPP")
print("GG   GG  UU  UU    TT    LL      OO  OO  PP    ")
print("GGGGGGG  UUUUUU    TT    LLLLLL  OOOOOO  PP    ")

print ("\n")

print ("Desarrollado por GUTLOP SA")
print ("\n")

print ("Menu:")
print ("1- Agregar stock")
print ("2- Quitar stock")
print ("3- Modificar stock critico")
print ("4- Modificar cantidad por caja")
print ("5- Modificar precio por unidad")
print ()
print ("0- Salir")
print ()

opcion = int(input("Ingrese una de las opciones descritas: "))

os.system('cls')

# Agregar stock

if (opcion == 1):
	print("Agregar stock: \n")

	for key in dicStock:
		print(key, "\t")
		pass

	opcion = input("\nSeleccione un elemento: ")
	print("\n")
	dicStock[opcion].mostrarProducto()
	print()
	dato = int(input("Indique la cantidad de cajas agregadas: "))
	dicStock[opcion].agregarStock(dato)

	# Registrar en el archivo

	pass


# Remover stock

if (opcion == 2):
	print("Quitar stock: \n")

	for key in dicStock:
		print(key, "\t")
		pass

	opcion = input("\nSeleccione un elemento: ")
	print("\n")
	dicStock[opcion].mostrarProducto()
	print()
	dato = int(input("Indique la cantidad elementos vendidos: "))
	dicStock[opcion].descontarStock(dato)

	# Registrar en el archivo

	pass


# Modificar stock critico

if (opcion == 3):
	print("Modificar stock critico: \n")

	for key in dicStock:
		print(key, "\t")
		pass

	opcion = input("\nSeleccione un elemento: ")
	print("\n")
	dicStock[opcion].mostrarProducto()
	print()
	dato = int(input("Indique el nuevo stock critico: "))
	dicStock[opcion].modificarStockCritico(dato)

	# Registrar en el archivo

	pass


# Modificar cantidad por caja

if (opcion == 4):
	print("Modificar cantidad por caja: \n")

	for key in dicStock:
		print(key, "\t")
		pass

	opcion = input("\nSeleccione un elemento: ")
	print("\n")
	dicStock[opcion].mostrarProducto()
	print()
	dato = int(input("Indique la nueva cantidad por caja: "))
	dicStock[opcion].modificarStockCritico(dato)

	# Registrar en el archivo

	pass


# Modificar precio por unidad

if (opcion == 5):
	print("Modificar precio por unidad: \n")

	for key in dicStock:
		print(key, "\t")
		pass

	opcion = input("\nSeleccione un elemento: ")
	print("\n")
	dicStock[opcion].mostrarProducto()
	print()
	dato = int(input("Indique el nuevo precio por unidad: "))
	dicStock[opcion].modificarPrecioXUnidad(dato)

	# Registrar en el archivo

	pass


# Salida

if (opcion == 0):
	exit()
	pass