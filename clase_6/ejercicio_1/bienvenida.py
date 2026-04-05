# Bienvenida personalizada:
# Pedir al usuario que ingrese su nombre, edad y ciudad.
# Guardar esta información en un diccionario.

# Luego, imprimir un mensaje personalizado como el siguiente:
# "Hola Juan, tenés 25 años y vivís en Rosario."

info_usuario = {}
info_usuario["nombre"] = input("Ingrese su nombre: ")
info_usuario["edad"] = int(input("Ingrese su edad: "))
info_usuario["ciudad"] = input("Ingrese su ciudad: ")

print(f"Hola {info_usuario['nombre']}, tenés {info_usuario['edad']} años y vivís en {info_usuario['ciudad']}.")