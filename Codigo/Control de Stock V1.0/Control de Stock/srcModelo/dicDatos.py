# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez

# Estructura de producto (idProducto, nombre, stockCritico, cajas, cantidadPorCaja, precioXUnidad):


from srcModelo.ClaseProducto import *
from srcModelo.dicEmpanadas import *
from srcModelo.ElementoDiccionario import *
from srcModelo import dicPanales


producto = Producto(1, "Chipa", 0, 0, 252, 0)
dicStock = {'chipa' : producto}

producto = Producto(3, "Empanadas", 0, 0, 8, 0)
dicStock['empanada'] = producto

producto = Producto(3, "Tarta", 0, 0, 8, 0)
dicStock['tarta'] = producto

producto = Producto(4, "Mini-Tarta", 0, 0, 0, 0)
dicStock['mini'] = producto

producto = Producto(5, "Panini", 0, 0, 24, 0)
dicStock['panini'] = producto

producto = Producto(6, "Tostable", 0, 0, 40, 0)
dicStock['tostable'] = producto

producto = Producto(7, "Medialuna", 0, 0, 288, 0)
dicStock['medialuna'] = producto

producto = Producto(8, "Churro", 0, 0, 40, 0)
dicStock['churro'] = producto

producto = Producto(3, "Panales", 0, 0, 8, 0)
dicStock['panal'] = producto

producto = Producto(10, "Criollito", 0, 0, 0, 0)
dicStock['criollito'] = producto
