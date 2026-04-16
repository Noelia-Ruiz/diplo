# Una clase para todos:
# Con lo visto durante la clase, deberán armar una clase tipo
# vehículo, con toda la información que crean necesaria.

class vehiculo:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def mostrar_info(self):
        return f"Vehículo: {self.marca} {self.modelo} ({self.año}), Color: {self.color}"

auto = vehiculo("Toyota", "Corolla", 2020, "Rojo")
print(auto.mostrar_info())