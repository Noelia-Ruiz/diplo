# Nuestra Función: Crear una función donde se deba mandar nuestro nombre, apellido y edad por parámetros,
# para poder después leerlo por terminal. Luego modificar el código para solicitar los mismos datos por terminal
# y mandarlos por parámetros.

# Pasos básicos:
# 1. Crear la estructura de la función.
# 2. Establecer las variables que va a recibir los parámetros.
# 3. Escribir el print que corresponde para mostrar la información dada.
# 4. Agregar el llamado a la función
# 5. Por último, agregar una línea donde se solicite el ingreso de datos.

def datos(nombre, apellido, edad):
    print(f"Nombre: {nombre}, apellido: {apellido}, Edad: {edad}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")

datos (nombre, apellido, edad)