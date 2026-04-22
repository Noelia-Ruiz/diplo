# Suite de Pruebas & Casos: QA necesita un resumen de ejecucion de casos.
# Objetivo tecnico: objetos que se componen y resumen estados.

# Entidades sugeridas: 
# ● TestCase: id, nombre, pasos, estado (“PENDING”, “PASS”, “FAIL”). 
# ● TestSuite: nombre, lista de test cases. 

# Requerimientos (métodos mínimos): 
# ● agregarCaso(caso) (estado inicial “PENDING”). 
# ● marcarPass(id) / marcarFail(id). 
# ● resumen() → devuelve cantidades por estado.   

Suite de Pruebas & Casos (cont.): 

# Criterios de aceptación: 
# ● Solo permite estados PENDING/PASS/FAIL. 
# ● resumen() refleja el conteo real. 

# Escenarios de prueba: 
# 1. Agregar 4 casos (2 PASS, 1 FAIL, 1 PENDING) ⇒ resumen correcto. 
# 2. Marcar FAIL sobre un id inexistente ⇒ mensaje claro. 
# 3. Cambiar un FAIL a PASS ⇒ el resumen se actualiza.

class TestCase:
	ESTADOS_VALIDOS = ["PENDING", "PASS", "FAIL"]

	def __init__(self, id, nombre, pasos, estado="PENDING"):
		if estado not in self.ESTADOS_VALIDOS:
			raise ValueError(
				f"Estado '{estado}' no valido. Usar: PENDING, PASS o FAIL."
			)
		self.id = id
		self.nombre = nombre
		self.pasos = pasos
		self.estado = estado

	def cambiarEstado(self, nuevo_estado):
		if nuevo_estado not in self.ESTADOS_VALIDOS:
			print(
				f"Estado '{nuevo_estado}' no valido. Usar: PENDING, PASS o FAIL."
			)
			return
		self.estado = nuevo_estado


class TestSuite:
	def __init__(self, nombre):
		self.nombre = nombre
		self.casos = []

	def agregarCaso(self, caso):
		caso.cambiarEstado("PENDING")
		self.casos.append(caso)
		print(f"Caso #{caso.id} agregado: {caso.nombre}")

	def marcarPass(self, id):
		for caso in self.casos:
			if caso.id == id:
				caso.cambiarEstado("PASS")
				print(f"Caso #{id} marcado como PASS.")
				return
		print(f"No se encontro el caso con id #{id}.")

	def marcarFail(self, id):
		for caso in self.casos:
			if caso.id == id:
				caso.cambiarEstado("FAIL")
				print(f"Caso #{id} marcado como FAIL.")
				return
		print(f"No se encontro el caso con id #{id}.")

	def resumen(self):
		resumen_estados = {"PENDING": 0, "PASS": 0, "FAIL": 0}
		for caso in self.casos:
			resumen_estados[caso.estado] += 1
		return resumen_estados


if __name__ == "__main__":
	suite = TestSuite("Regresion Login")

	caso_1 = TestCase(1, "Login valido", ["Abrir app", "Ingresar credenciales"])
	caso_2 = TestCase(2, "Login invalido", ["Abrir app", "Ingresar clave invalida"])
	caso_3 = TestCase(3, "Recuperar clave", ["Abrir app", "Ir a Olvide mi clave"])
	caso_4 = TestCase(4, "Cerrar sesion", ["Iniciar sesion", "Presionar salir"])

	print("----------------------------------------------------------------")
	print("--- Escenario 1 ---")
	suite.agregarCaso(caso_1)
	suite.agregarCaso(caso_2)
	suite.agregarCaso(caso_3)
	suite.agregarCaso(caso_4)
	suite.marcarPass(1)
	suite.marcarPass(2)
	suite.marcarFail(3)
    
	print(f"Resumen: {suite.resumen()}")

	print("----------------------------------------------------------------")
	print("--- Escenario 2 ---")
	suite.marcarFail(99)
	print(f"Resumen: {suite.resumen()}")

	print("----------------------------------------------------------------")
	print("--- Escenario 3 ---")
	suite.marcarPass(3)
	print(f"Resumen: {suite.resumen()}")
	print("----------------------------------------------------------------")