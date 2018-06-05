# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez

from ClaseProducto import *
from dicDatos import *
from manejoDeArchivos import *
from funciones import *
from operator import invert
from _overlapped import NULL
from menu import *

# Restauro datos anteriores
if(levantarStock(dicStock)):
 	print("Restauracion de datos exitosa!")
else:
 	print("No se encontro archivo de restauracion")
 	pass
 
input()

salir = False

print ("\n")
usuario = leerCadena("Ingrese el nombre del usuario: ")
print ("\n")
print ("Bienvenido " + usuario + "!")
print()
input()

while(salir == False):
	limpia()
	print ("\t\tDesarrollado por GUTLOP")
	print ("\n")
	
	mostrarMenuPrincipal()

	opcion = leerEntero("Ingrese una de las opciones descritas: ")

	limpia()
	print ()

# Agregar stock
	if (opcion == 1):
		print("Agregar stock: \n")
	
		for key in dicStock:
			print(key, "\t")
			pass
		
		elemento = buscarElemento()		
		print()
		
		# Opcion de volver al menu principal
		if(elemento != '0'):
			dato = leerEntero("Indique la cantidad de cajas agregadas: ")
			dicStock[elemento].agregarStock(dato)
			
			print()
			print("Nuevo estado del producto: ")
			dicStock[elemento].mostrarProducto()
			print()
		
			# Registrar en el archivo
			crearArchivoConfig(dicStock)
			
			print("Presione una tecla para continuar...")
			input()
			pass
		pass

# Remover stock
	if (opcion == 2):
		print("Venta/Quita de stock: \n")
	
	# Se pregunta si fue una venta o una merma (o salir)
		while(True):
			opc = leerEntero("\nEs:\n1- Venta particular\n2- Venta de promocion\n3- Merma\n\n0- Volver al menu principal")
			
			if(opc == 1 or opc == 2 or opc == 3 or opc == 0):
				break
				pass
			else:
				print("\nERROR No existe esa opcion\n")
				pass
		pass
				
		# Opcion de volver al menu principal
		if(opc != 0 and (opc == 1 or opc == 3)):
			for key in dicStock:
				print(key, "\t")
				pass
			
			elemento = buscarElemento()
			print()		
			
			# Opcion de volver al menu principal
			if(elemento != '0'):
				dato = leerEntero("Indique la cantidad elementos quitados: ")				
				
				# Se registra en base a lo elegido previamente
				if(opc == 1):								
					dicStock[elemento].descontarStock(dato, 1)
					dicStock[elemento].ventas += dato
					pass
				else:
					dicStock[elemento].descontarStock(dato, 2)
					dicStock[elemento].merma += dato
					pass	
				pass
			
			pass
			
		# Caso de una promo
		if(opc != 0 and opc == 2):
			salida = False

	        while(salida == False):
	            limpia()
	            mostrarMenuPromo()
	        
	            option = leerEntero("Ingrese el numero de promo: ")
	            
	            if (option == 0):
	                salida == True
	            else:	
	                print()
	                cantidad = leerEntero("Ingrese la cantidad vendida: ")
	                print()
	                dicPromo["promo" + opcion].cntVentas += 1
	                pass         
	        pass
	    	pass      
				
		# Registrar en el archivo
		crearArchivoConfig(dicStock)
		
		print()
		print("Nuevo estado del producto: ")
		dicStock[elemento].mostrarProducto()
		print()
		
		print("Presione una tecla para continuar...")
		input()
		pass

# Modificar stock critico
	if (opcion == 3):
		print("Modificar stock critico: \n")
	
		for key in dicStock:
			print(key, "\t")
			pass
	
		elemento = buscarElemento()
		print()
		
		# Opcion de volver al menu principal
		if(elemento != '0'):
			dato = leerEntero("Indique el nuevo stock critico: ")	
			
			# Opcion de volver al menu principal
			if(dato != 0):
				dicStock[elemento.lower()].modificarStockCritico(dato)
			
				print()
				print("Nuevo estado del producto: ")
				dicStock[elemento].mostrarProducto()
				print()
			
				# Registrar en el archivo
				crearArchivoConfig(dicStock)
				
				print("Presione una tecla para continuar...")
				input()
				pass
			pass
		pass

# Modificar cantidad por caja
	if (opcion == 4):
		print("Modificar cantidad por caja: \n")
	
		for key in dicStock:
			print(key, "\t")
			pass
	
		elemento = buscarElemento()
		print()
		
		# Opcion de volver al menu principal
		if(elemento != '0'):
			dato = leerEntero("Indique la nueva cantidad por caja: ")
			
			# Opcion de volver al menu principal
			if(dato != 0):
				dicStock[elemento.lower()].modificarCantidadPorCaja(dato)
				
				print()
				print("Nuevo estado del producto: ")
				dicStock[elemento].mostrarProducto()
				print()
			
				# Registrar en el archivo
				crearArchivoConfig(dicStock)
				
				print("Presione una tecla para continuar...")
				input()
				pass
			pass
		pass

# Modificar precio por unidad
	if (opcion == 5):
		print("Modificar precio por unidad: \n")
	
		for key in dicStock:
			print(key, "\t")
			pass
	
		elemento = buscarElemento()
		print()
		
		# Opcion de volver al menu principal
		if(elemento != '0'):			
			dato = leerEntero("Indique el nuevo precio por unidad: ")
			
			# Opcion de volver al menu principal
			if(dato != 0):
				dicStock[elemento].modificarPrecioXUnidad(dato)
				
				print()
				print("Nuevo estado del producto: ")
				dicStock[elemento].mostrarProducto()
				print()
			
				# Registrar en el archivo
				crearArchivoConfig(dicStock)
				
				print("Presione una tecla para continuar...")
				input()
				pass
			pass
		pass

# Mostrar un producto
	if (opcion == 6):
		print("Mostrar un producto: \n")
	
		for key in dicStock:
			print(key, "\t")
			pass
	
		elemento = buscarElemento()
		print()
		
		# Opcion de volver al menu principal
		if(elemento != '0'):
			print("Presione una tecla para continuar...")
			input()
			pass
		
		pass

# Mostrar todos los productos
	if (opcion == 7):
		print("Lista de productos: \n")
	
		for key in dicStock:
				print(dicStock[key].nombre)
				dicStock[key].mostrarProducto()
				print("\n")
		pass			
		print()
		
		print("Presione una tecla para continuar...")
		input()
		
	pass
		
# Genera el registro diario
	if (opcion == 9):
		print("Generando registro diario... \n")
	
		error = crearArchivo(dicStock, usuario)
		print()
		
		if(error == False):
			print("Archivo generado con exito!!")
			print()
			pass
	
		print("Presione una tecla para continuar...")
		input()
					
	pass
		
# Salida

	if (opcion == 0):
		salir = True;
		print()
		
		mostrarLogo()
		
		print("Saliendo del programa. Muchas gracias.")
		input()
		
		exit()
		pass

pass
