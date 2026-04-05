# Integrando el código: Armar un programa que permita registrar usuarios.
# Cada usuario debe tener un nombre, apellido, edad y ciudad. Al finalizar la carga de 3 usuarios, el programa debe: 
# Mostrar cuántos viven en “Buenos Aires” 
# Calcular el promedio de edad 
# Mostrar los nombres completos (nombre + apellido) de todos los usuarios
# Los usuarios deben almacenarse como diccionarios dentro de una lista. Se
# pueden hacer funciones para organizar el código.

def registrar_usuario():
    usuarios = []
    for i in range(3):
        nombre = input("Ingresá tu nombre: ")
        apellido = input("Ingresá tu apellido: ")
        edad = int(input("Ingresá tu edad: "))
        ciudad = input("Ingresá tu ciudad: ")
        usuario = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "ciudad": ciudad
        }
        print('----------------------------------------------------------------')
        usuarios.append(usuario)
    return usuarios

def mostrar_resultados(usuarios):
    cantidad_buenos_aires = sum(1 for usuario in usuarios if usuario["ciudad"].lower() == "buenos aires") # por si lo escriben con mayusculas
    promedio_edad = sum(usuario["edad"] for usuario in usuarios) / len(usuarios) # usuarios / cant de usuario con ciudad bs as
    nombres_completos = [f"{usuario['nombre']} {usuario['apellido']}" for usuario in usuarios]

    print(f"Cantidad de usuarios que viven en Buenos Aires: {cantidad_buenos_aires}")
    print('----------------------------------------------------------------')

    print(f"Promedio de edad: {promedio_edad:.2f}") # el :.2f es para mostrar solo 2 decimales, sino se muestra con muchos decimales
    print('----------------------------------------------------------------')

    print("Nombres completos de los usuarios:")
    for i, nombre in enumerate(nombres_completos, start=1):
        print(f"Usuario nº {i}: {nombre}")
    print('----------------------------------------------------------------')

# El programa principal ejecutandosé en la función main, que llama a las funciones de registro y muestra de resultados.    
def main():
    usuarios = registrar_usuario()
    mostrar_resultados(usuarios)

if __name__ == "__main__":
    main()