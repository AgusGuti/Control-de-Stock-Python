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

#Metdodo que descuenta el stock considerando que fue vendido y muestra el nuevo estado
#Verifica que el stock descontado no sea mayor al existente. 
	def descontarStock(self, cantidadVendidos):
		if (self.stockActual >= cantidadVendidos):
			self.stockActual = (self.stockActual - cantidadVendidos)
			
			if (self.stockActual <= self.stockCritico):
				print("Stock actual: ", self.stockActual)
				print("Se requiere reposicion.")
				pass

			pass
		else:
			print("ERROR la cantidad vendida no puede ser mayor al stock disponible.")


#Metdodo que agrega stock por cantidad de cajas. El valor de cada caja es atributo de cada producto.
	def agregarStock(self, cajas):
		self.stockActual = self.stockActual + (cajas * self.cantidadPorCaja)
		pass

#Metdodo que permite modificar el stock critico.
	def modificarStockCritico(self, stockCritico):
		self.stockCritico = stockCritico
		pass

#Metdodo que permite modificar la cantidad que se agrega por cada caja.
	def modificarCantidadPorCaja(self, cantidadPorCaja):
		self.cantidadPorCaja = cantidadPorCaja
		pass

#Metdodo que permite modificar el precion por unidad del producto.
	def modificarPrecioXUnidad(self, precioXUnidad):
		self.precioXUnidad = precioXUnidad
		pass

#Metdodo que muestra los atributos del producto de forma ordenada.
	def mostrarProducto(self):
		print("ID: ", self.idProducto)
		print("Nombre: ", self.nombre)
		print("Stock: ", self.stockActual)
		print("Stock critico: ", self.stockCritico)
		print("Cantidad por caja: ", self.cantidadPorCaja)
		print("Precio x unidad: ", self.precioXUnidad)