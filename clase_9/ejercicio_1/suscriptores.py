# Newsletter & Suscriptores: Marketing necesita administrar suscriptores de un boletín.
# Objetivo técnico: modelar dos objetos que interactúan. 

# Entidades sugeridas:
# ● Suscriptor: nombre, email.
# ● Newsletter: nombre, lista de suscriptores.

# Requerimientos (métodos mínimos):
# ● suscribir(suscriptor) (no permitir emails repetidos).
# ● desuscribir(email) (si no existe, informar).
# ● totalSuscriptores().   

# Criterios de aceptación:
# ● No se agregan duplicados por email.
# ● Desuscribir elimina solo si existe.
# ● Mostrar el total correctamente tras altas/bajas. 

# Escenarios de prueba:
# 1. Suscribir 3 personas (una repetida) ⇒ total = 2.
# 2. Desuscribir un email existente ⇒ total decrece.
# 3. Desuscribir un email inexistente ⇒ mensaje claro.

class Suscriptor:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Newsletter:
    def __init__(self, nombre):
        self.nombre = nombre
        self.suscriptores = []

    def suscribir(self, suscriptor):
        # No permitir emails repetidos
        for s in self.suscriptores:
            if s.email == suscriptor.email:
                print(f"El email {suscriptor.email} ya está suscrito.")
                return
        self.suscriptores.append(suscriptor)
        print(f"{suscriptor.nombre} fue suscrito exitosamente.")

    def desuscribir(self, email):
        # Si no existe, informar
        for s in self.suscriptores:
            if s.email == email:
                self.suscriptores.remove(s)
                print(f"{s.nombre} fue desuscrito exitosamente.")
                return
        print(f"El email {email} no se encuentra en la lista de suscriptores.")

    def totalSuscriptores(self):
        return len(self.suscriptores)


if __name__ == "__main__":
    boletin = Newsletter("Novedades Tech")
    print('----------------------------------------------------------------')

    # Escenario 1: Suscribir 3 personas (una repetida) => total = 2
    print("--- Escenario 1 ---")
    s1 = Suscriptor("noe", "noe@gmail.com")
    s2 = Suscriptor("cuentafantasma", "cuentafantasma@gmail.com")
    s3 = Suscriptor("Noe repetida", "noe@gmail.com")  # email repetido, no debe cargarse
    print('----------------------------------------------------------------')

    boletin.suscribir(s1)
    boletin.suscribir(s2)
    boletin.suscribir(s3)
    print(f"Total de suscriptores: {boletin.totalSuscriptores()}")
    
    # Escenario 2: Desuscribir un email existente => total decrece
    print('----------------------------------------------------------------')
    print("--- Escenario 2 ---")
    boletin.desuscribir("cuentafantasma@gmail.com")
    print(f"Total de suscriptores: {boletin.totalSuscriptores()}")
    print('----------------------------------------------------------------')

    # Escenario 3: Desuscribir un email inexistente => mensaje claro
    print("--- Escenario 3 ---")
    boletin.desuscribir("noexiste@gmail.com")
    print(f"Total de suscriptores: {boletin.totalSuscriptores()}")