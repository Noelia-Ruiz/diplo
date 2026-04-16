# Una clase para todos:
# Con lo visto durante la clase, deberán armar una clase tipo
# vehículo, con toda la información que crean necesaria.

class vehiculo:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

# Un método para todos:
# Con lo visto durante la clase, deberán armar un método como acelerar, con toda la información que crean necesaria. 
# Luego, traten de generar dos métodos extras que crean que se puedan aplicar a vehículos.
    
    def mostrar_info(self):
        return f"Vehículo: {self.marca} {self.modelo} ({self.año}), Color: {self.color}"

    def acelerar(self, velocidad): # método principal de la consigna
        self.velocidad = velocidad
        return f"El {self.marca} {self.modelo} está acelerando a {self.velocidad} km/h."

    def frenar(self): # primer método extra
        self.velocidad = 0
        return f"El {self.marca} {self.modelo} ha frenado."

    def repintar(self, nuevo_color): # segundo método extra
        self.color = nuevo_color
        return f"El {self.marca} {self.modelo} ahora es de color {self.color}."

auto = vehiculo("Citroën", "C3", 2015, "Violeta mauve") # se cambian datos para el ejercicio
print(auto.mostrar_info())
print(auto.acelerar(120))
print(auto.repintar("Rosa malva")) # nuevo color
print(auto.frenar())
