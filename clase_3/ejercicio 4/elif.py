# Pedirle al usuario que ingrese su edad. Luego:

# 1. Si es menor de 13, imprimir "Niño"
# 2. Si tiene entre 13 y 17 inclusive, imprimir "Adolescente"
# 3. Si tiene entre 18 y 64 inclusive, imprimir "Adulto"
# 4. Si tiene 65 o más, imprimir "Jubilado"

# Pasos básicos:
# 1. Crear variable edad con input() y convertirla a entero.
# 2. Usar if, elif y else para controlar los rangos.
# 3. Usar solo comparadores simples (>=, <=, <, >).
# 4. Escribir un print con la variable retornada.

edad = int(input("Ingrese su edad: "))

if edad < 13:
    print("sos un niño")
elif 13 <= edad <= 17:
    print("sos adolescente")
elif 18 <= edad <= 64:
    print("sos un adulto")
else:
    print("sos jubilado")

