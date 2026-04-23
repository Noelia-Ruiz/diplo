# Alumno - Crear una clase Alumno.
# Atributos: nombre, notas (lista vacía al inicio).
# Métodos: agregar_nota(nota) (solo acepta entre 0 y 10), promedio() → devuelve el promedio, estado() → imprime "Aprobado" si el promedio ≥ 6, sino "Desaprobado".
# Prueba: crear un alumno, agregarle 3 notas, mostrar promedio y estado.
# Pasos básicos:
# 1. Crear el objeto Alumno.
# 2. Crear cada uno de los métodos y sus respectivos parámetros.
# 3. Crear las llamadas correspondientes.

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = [] # lista vacía al inicio

    def agregar_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
        else:
            print("La nota debe estar entre 0 y 10")

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return round(sum(self.notas) / len(self.notas), 2) # se redondean los decimales a dos dígitos

    def estado(self):
        if self.promedio() >= 6:
            print(f"Alumno {self.nombre}: aprobado")
        else:
            print(f"Alumno {self.nombre}: desaprobado")


alumno1 = Alumno("Noelia Ruiz")
alumno1.agregar_nota(8)
alumno1.agregar_nota(6)
alumno1.agregar_nota(9)

print(alumno1.promedio())
alumno1.estado()

print('-----------------------------')

alumno2 = Alumno("Carlos Pérez")
alumno2.agregar_nota(7)
alumno2.agregar_nota(6)
alumno2.agregar_nota(4)

print(alumno2.promedio())
alumno2.estado()
