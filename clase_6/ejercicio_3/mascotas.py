# Censo de mascotas:
# Armar un pequeño programa que permita cargar información de 3 mascotas. Para cada una, pedirle al usuario que ingrese
# el nombre, especie y edad. Guardar cada mascota como un diccionario y agregala a una lista general.
# Luego, crear una función que recorra la lista y muestre los nombres de las mascotas que tengan más de 5 años.

mascotas = []
for i in range(3):
    nombre = input(f"Ingrese el nombre de la mascota {i+1}: ")
    especie = input(f"Ingrese la especie de la mascota {i+1}: ")
    edad = int(input(f"Ingrese la edad de la mascota {i+1} (en años): "))
    print('----------------------------------------------------------------')
    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad
    }
    
    mascotas.append(mascota)

def mostrar_mascotas_mayores_5(mascotas):
    # Recorremos todas las mascotas y mostramos el nombre si tiene más de 5 años
    print("Mascotas con más de 5 años:")
    hay_mayores = False
    for mascota in mascotas:
        if mascota["edad"] > 5:
            print(mascota ["nombre"])
            hay_mayores = True
    if not hay_mayores:
        print("Ninguna mascota tiene más de 5 años.")

mostrar_mascotas_mayores_5(mascotas)  