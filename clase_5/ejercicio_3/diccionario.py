# Nuestro Diccionario:
# Armar un diccionario con información sobre ustedes.
# Ingresar al menos 8 elementos sobre su persona. Luego,
# mostrar todos los elementos en la terminal.

persona = {
    "nombre": "Noelia",
    "apellido": "Ruiz",
    "edad": 36,
    "email": "ruiz.noeliaromina@gmail.com",
    "ciudad": "Rosario",
    "cp": 2000,
    "matriculado": True,
    "sucursales": ["Rosario", "Carcarañá", "Roldán"]
}

print(persona["nombre"])  # Noelia
print(persona["sucursales"][0])  # Rosario
print(persona["apellido"], persona["edad"], persona["ciudad"])  # Ruiz 36 Rosario

print(persona)