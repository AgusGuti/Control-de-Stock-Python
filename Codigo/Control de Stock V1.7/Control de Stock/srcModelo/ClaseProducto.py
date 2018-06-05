# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez

class Producto(object):
	"""docstring for Producto"""
	
	def __init__(self, idProducto, nombre, stockCritico, cajas, cantidadPorCaja, precioXUnidad):
		super(Producto, self).__init__()
		self.idProducto = idProducto
		self.nombre = nombre
		self.stockCritico = stockCritico
		self.cajas = cajas
		self.cantidadPorCaja = cantidadPorCaja
		self.precioXUnidad = precioXUnidad
		self.stockActual = (cajas * cantidadPorCaja)
		self.ventas = 0
		self.merma = 0

	def descontarStock(self, cantRestado):
		if (self.stockActual >= cantRestado):
			self.stockActual = (self.stockActual - cantRestado)
			
			if (self.stockActual <= self.stockCritico):
				print("Stock actual: ", self.stockActual)
				print("Se requiere reposicion.")
				pass

			pass
		else:
			print("ERROR la cantidad vendida no puede ser mayor al stock disponible.")

	def agregarStock(self, cajas):
		self.stockActual = self.stockActual + (cajas * self.cantidadPorCaja)
		pass

	def modificarStockCritico(self, stockCritico):
		self.stockCritico = stockCritico
		pass

	def modificarCantidadPorCaja(self, cantidadPorCaja):
		self.cantidadPorCaja = cantidadPorCaja
		pass

	def modificarPrecioXUnidad(self, precioXUnidad):
		self.precioXUnidad = precioXUnidad
		pass

	def mostrarProducto(self):
		print("Stock: ", self.stockActual, end=" ; ")
		print("Stock critico: ", self.stockCritico, end=" ; ")
		print("Cantidad por caja: ", self.cantidadPorCaja, end=" ; ")
		print("Precio por unidad: ", self.precioXUnidad)
		
	def calcularPrecio(self):
		return(self.stockActual * self.precioXUnidad)
		pass
