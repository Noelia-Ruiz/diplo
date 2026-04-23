# Cuenta Bancaria

# Crear una clase CuentaBancaria.
# Atributos: titular, saldo.
# Métodos: depositar(monto), retirar(monto), mostrar_saldo()
# Prueba: crear una cuenta con 1000 iniciales, depositar 500, intentar retirar 2000 y luego 700.
# Pasos básicos:
# 1. Crear el objeto CuentaBancaria.
# 2. Crear los 3 métodos y sus respectivos parámetros.
# 3. Realizar la prueba solicitada.


class CuentaBancaria:
	def __init__(self, titular, saldo):
		self.titular = titular
		self.saldo = saldo

	def depositar(self, monto):
		if monto > 0:
			self.saldo += monto
			print(f"Se depositaron ${monto}")
		else:
			print("El monto tiene que ser mayor a 0") # tampoco puede ser 0

	def retirar(self, monto):
		if monto <= 0:
			print("El monto tiene que ser mayor a 0") # mayor o igual a 0 en este caso
		elif monto > self.saldo:
			print("No alcanza el saldo")
		else:
			self.saldo -= monto
			print(f"Se retiraron ${monto}")

	def mostrar_saldo(self):
		print("------------------------------------------------")
		print(f"Saldo actual de {self.titular}: ${self.saldo}")
		print("------------------------------------------------")

cuenta = CuentaBancaria("Noelia Ruiz", 100000)

cuenta.mostrar_saldo()
cuenta.depositar(50000)
cuenta.mostrar_saldo()
cuenta.retirar(20000)
cuenta.retirar(7000)
cuenta.mostrar_saldo()