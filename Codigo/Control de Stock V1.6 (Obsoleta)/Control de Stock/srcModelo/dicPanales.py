# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez

# Estructura de producto (idProducto, nombre, stockCritico, cajas, cantidadPorCaja, precioXUnidad):


from srcModelo.ClaseProducto import Producto


producto = Producto(1, "Membrillo", 0, 0, 0, 0)
dicPanales = {'membrillo' : producto}

producto = Producto(2, "Batata", 0, 0, 0, 0)
dicPanales['batata'] = producto