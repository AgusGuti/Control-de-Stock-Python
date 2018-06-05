# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez

# Estructura de producto (idProducto, nombre, stockCritico, cajas, cantidadPorCaja, precioXUnidad):


from ClaseProducto import *


producto = Producto(1, "Empanadas", 0, 0, 8, 24)
dicStock = {'empanada' : producto}

producto = Producto(2, "Chipa", 0, 0, 252, 8)
dicStock['chipa'] = producto

producto = Producto(3, "Medialuna", 0, 0, 288, 8)
dicStock['medialuna'] = producto

producto = Producto(4, "Panales", 0, 0, 288, 8)
dicStock['panales'] = producto

producto = Producto(5, "Pastelito", 0, 0, 40, 25)
dicStock['pastelito'] = producto

producto = Producto(6, "Panini", 0, 0, 24, 50)
dicStock['panini'] = producto

producto = Producto(7, "Tarta", 0, 0, 8, 85)
dicStock['tarta'] = producto

producto = Producto(8, "Mini-Tarta", 0, 0, 0, 40)
dicStock['mini'] = producto

producto = Producto(9, "Pizzeta rellena", 0, 0, 0, 35)
dicStock['pizzeta'] = producto

producto = Producto(10, "Bocaditos de pollo", 0, 0, 0, 8.5)
dicStock['bocaditos'] = producto

producto = Producto(11, "Tostable", 0, 0, 40, 29)
dicStock['tostable'] = producto

producto = Producto(12, "Brownie", 0, 0, 40, 25)
dicStock['brownie'] = producto

producto = Producto(13, "Torta", 0, 0, 40, 25)
dicStock['torta'] = producto

producto = Producto(14, "Churro", 0, 0, 40, 10)
dicStock['churro'] = producto

producto = Producto(15, "Criollito", 0, 0, 0, 10)
dicStock['criollito'] = producto

producto = Producto(16, "Bebida 220", 0, 0, 0, 17)
dicStock['220'] = producto

producto = Producto(17, "Bebida 237", 0, 0, 0, 17)
dicStock['237'] = producto

producto = Producto(18, "Bebida 250", 0, 0, 0, 17)
dicStock['250'] = producto

producto = Producto(19, "Bebida Cepita", 0, 0, 0, 17)
dicStock['cepita'] = producto

producto = Producto(20, "Bebida 600", 0, 0, 0, 40)
dicStock['600'] = producto

producto = Producto(21, "Cafe clasico chico", 0, 0, 0, 30)
dicStock['clasico'] = producto

producto = Producto(22, "Cafe especial chico", 0, 0, 0, 50)
dicStock['especial'] = producto
