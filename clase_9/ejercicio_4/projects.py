# Inventario & Valorización: Logística necesita controlar stock y valor de inventario. 

# Objetivo técnico: dos clases que interactúan con reglas de negocio simples. 

# Entidades sugeridas: 
# ● Producto: nombre, precio (mayor que 0). 
# ● Inventario: ítems (producto + cantidad). 

# Requerimientos (métodos mínimos): 
# ● agregar(producto, cantidad) 
# ● Si el producto ya existe, sumar cantidad. 
# ● No permitir cantidad ≤ 0 ni precio ≤ 0. 
# ● remover(nombre, cantidad) 
# ● No permitir stock negativo ni remover inexistentes. 
# ● stockDe(nombre) 
# ● valorTotal() (suma de precio * cantidad de todos los productos). 

# Criterios de aceptación: 
# ● No se agregan productos con precio ≤ 0. 
# ● No se aceptan cantidades ≤ 0 en altas ni bajas. 
# ● valorTotal() calcula correctamente tras varias operaciones  

# Escenarios de prueba: 
# 1. Agregar Producto A(10$, 3u) y Producto B(25$, 2u) ⇒ valorTotal = (10 * 3) + (25 * 2) = 80. 
# 2. Agregar más de Producto A (2u) ⇒ stockDe(Producto A) actualizado. 
# 3. Remover más de lo existente ⇒ mensaje y sin cambios. 
# 4. Intentar agregar C con precio 0 ⇒ rechazo y valorTotal sin cambios (= 100).


class Producto:
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio = precio


class Inventario:
	def __init__(self):
		self.items = {}

	def agregar(self, producto, cantidad):
		if producto.precio <= 0:
			print(f"No se puede agregar '{producto.nombre}': el precio debe ser mayor a 0.")
			return

		if cantidad <= 0:
			print("No se puede agregar una cantidad menor o igual a 0.")
			return

		if producto.nombre in self.items:
			self.items[producto.nombre]["cantidad"] += cantidad
			print(f"Se sumaron {cantidad} unidades de '{producto.nombre}'.")
			return

		self.items[producto.nombre] = {
			"producto": producto,
			"cantidad": cantidad,
		}
		print(f"Se agregó '{producto.nombre}' con {cantidad} unidades.")

	def remover(self, nombre, cantidad):
		if cantidad <= 0:
			print("No se puede remover una cantidad menor o igual a 0.")
			return

		if nombre not in self.items:
			print(f"El producto '{nombre}' no existe en el inventario.")
			return

		stock_actual = self.items[nombre]["cantidad"]
		if cantidad > stock_actual:
			print(f"No hay stock suficiente de '{nombre}'. Stock actual: {stock_actual}.")
			return

		self.items[nombre]["cantidad"] -= cantidad
		print(f"Se removieron {cantidad} unidades de '{nombre}'.")

		if self.items[nombre]["cantidad"] == 0:
			del self.items[nombre]
			print(f"'{nombre}' quedó sin stock y fue eliminado del inventario.")

	def stockDe(self, nombre):
		if nombre not in self.items:
			return 0
		return self.items[nombre]["cantidad"]

	def valorTotal(self):
		total = 0
		for item in self.items.values():
			total += item["producto"].precio * item["cantidad"]
		return total


if __name__ == "__main__":
	inventario = Inventario()

	producto_a = Producto("Producto A", 10)
	producto_b = Producto("Producto B", 25)
	producto_c = Producto("C", 0)

	print("----------------------------------------------------------------")
	print("--- Escenario 1 ---")
	inventario.agregar(producto_a, 3)
	inventario.agregar(producto_b, 2)
	print(f"Valor total: ${inventario.valorTotal()}")

	print("----------------------------------------------------------------")
	print("--- Escenario 2 ---")
	inventario.agregar(producto_a, 2)
	print(f"Stock de Producto A: {inventario.stockDe('Producto A')} unidades")

	print("----------------------------------------------------------------")
	print("--- Escenario 3 ---")
	inventario.remover("Producto A", 10)
	print(f"Stock de Producto A luego del intento: {inventario.stockDe('Producto A')} unidades")

	print("----------------------------------------------------------------")
	print("--- Escenario 4 ---")
	inventario.agregar(producto_c, 1)
	print(f"Valor total final: ${inventario.valorTotal()}")
	print("----------------------------------------------------------------")