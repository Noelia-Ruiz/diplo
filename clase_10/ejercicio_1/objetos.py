# Objetos: Crear 5 clases que hereden de su clase padre. Luego, invocar dichos objetos y utilizar sus métodos.

# Pasos básicos:
# 1. Crear el objeto padre. 
# 2. Crear 5 nuevos objetos, cada uno con métodos y sus respectivos parámetros.
# 3. Crear la llamada para cada objeto.

class Animal:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def presentarse(self):
		return f"Hola, soy {self.nombre} y tengo {self.edad} años."


class Perro(Animal):
	def emitir_sonido(self):
		return "estoy ladrando: Guau"


class Gato(Animal):
	def emitir_sonido(self):
		return "estoy maullando: Miau"


class Pajaro(Animal):
	def emitir_sonido(self):
		return "estoy piando: Pio pio"


class Vaca(Animal):
	def emitir_sonido(self):
		return "estoy mugiendo: Muuu"


class Caballo(Animal):
	def emitir_sonido(self):
		return "estoy relinchando: Jiii"


# Invocacion de objetos y uso de metodos
perro = Perro("El Facu", 13)
gato = Gato("Nino minino", 8)
pajaro = Pajaro("Tuckson", 1)
vaca = Vaca("Lola", 5)
caballo = Caballo("Rocinante", 12)

animales = [perro, gato, pajaro, vaca, caballo]

for animal in animales:
	print(animal.presentarse())
	print(f"como soy un {animal.__class__.__name__}, {animal.emitir_sonido()}") # para hilar el tipo de animal con el sonido que hace
	print("------------------------------------------------")