# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez
import time
import os



formato=time.localtime()
print(time.asctime(formato))

file=open ('formato.txt','w')

file.write("\n hello agus puto")

file.close()


with open('stock.txt') as file:
    # recorre linea a linea
    for linea in file:
        # muestra la ultima leida
        print(linea)  
file.close()
os.system('cls')


file=open('formato.txt','r')
lista=file.readlines()
numlinea=0
for linea in lista:
	numlinea+=1
	print(numlinea,linea)
	pass

input ("presione enter para salir")

