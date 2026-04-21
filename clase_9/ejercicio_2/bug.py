# Bug Tracker Lite:
# Un equipo necesita registrar y cerrar bugs en un proyecto. 
# Objetivo técnico: múltiples objetos con estados sencillos. 
# Entidades sugeridas:
# ● Bug: id, título, severidad (“low”, “medium”, “high”), estado (“open”, “closed”).
# ● Proyecto: nombre, lista de bugs. 

# Requerimientos (métodos mínimos): 
# ● reportarBug(título, severidad) (estado inicial “open”). 
# ● cerrarBug(id) (si ya está “closed”, informar). 
# ● listarAbiertos() / contarPorSeveridad(severidad)  

# Criterios de aceptación:
# ● Severidad solo admite low/medium/high. 
# ● Un bug cerrado no cambia de estado si se intenta cerrar de nuevo. 
# ● Listar abiertos devuelve solo los “open”. 

# Escenarios de prueba: 
# 1. Reportar 3 bugs (1 high, 2 medium) ⇒ contarPorSeveridad("medium") = 2. 
# 2. Cerrar 1 bug ⇒ listarAbiertos no lo muestra. 
# 3. Cerrar un bug dos veces ⇒ mensaje claro la segunda vez.

class Bug:
    def __init__(self, id, titulo, severidad):
        self.id = id
        self.titulo = titulo
        self.severidad = severidad
        self.estado = "open"

class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bugs = []
        self.contador_id = 1

    def reportarBug(self, titulo, severidad):
        # Severidad solo admite low, medium o high
        if severidad not in ["low", "medium", "high"]:
            print(f"Severidad '{severidad}' no válida. Usar: low, medium o high.")
            return
        bug = Bug(self.contador_id, titulo, severidad)
        self.bugs.append(bug)
        print(f"Bug #{bug.id} reportado: '{titulo}' - severidad: {severidad}")
        self.contador_id += 1

    def cerrarBug(self, id):
        for bug in self.bugs:
            if bug.id == id:
                if bug.estado == "closed":
                    print(f"El bug #{id} ya está cerrado.")
                    return
                bug.estado = "closed"
                print(f"Bug #{id} cerrado exitosamente.")
                return
        print(f"No se encontró el bug con id #{id}.")

    def listarAbiertos(self):
        abiertos = [bug for bug in self.bugs if bug.estado == "open"]
        if not abiertos:
            print("No hay bugs abiertos.")
            return
        print("Bugs abiertos:")
        for bug in abiertos:
            print(f"  #{bug.id} - {bug.titulo} [{bug.severidad}]")

    def contarPorSeveridad(self, severidad):
        total = sum(1 for bug in self.bugs if bug.severidad == severidad)
        print(f"Bugs con severidad '{severidad}': {total}")
        return total


if __name__ == "__main__":
    proyecto = Proyecto("Mi Proyecto")

    # Escenario 1: Reportar 3 bugs (1 high, 2 medium) → contarPorSeveridad("medium") = 2
    print("----------------------------------------------------------------")
    print("--- Escenario 1 ---")
    proyecto.reportarBug("Error en login", "high")
    proyecto.reportarBug("Botón no responde", "medium")
    proyecto.reportarBug("Texto cortado en pantalla", "medium")
    proyecto.contarPorSeveridad("medium")
    print("----------------------------------------------------------------")

    # Escenario 2: Cerrar 1 bug → listarAbiertos no lo muestra
    print("--- Escenario 2 ---")
    proyecto.cerrarBug(1)
    proyecto.listarAbiertos()
    print("----------------------------------------------------------------")

    # Escenario 3: Cerrar un bug dos veces → mensaje claro la segunda vez
    print("--- Escenario 3 ---")
    proyecto.cerrarBug(1)
    print("----------------------------------------------------------------")