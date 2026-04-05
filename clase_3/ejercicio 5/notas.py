# Pedirle al usuario que ingrese su nota (del 1 al 10). Luego:
# Si la nota es menor a 4, imprimir "Desaprobado"
# Si es igual a 4 o 5, imprimir "Regular"
# Si es igual a 6, 7 u 8, imprimir "Bueno"
# Si es igual a 9, imprimir "Muy Bueno"
# Si es igual a 10, imprimir "Excelente"

# Pasos básicos:
# 1. Crear variable nota con input() y convertirla a entero.
# 2. Validar que la nota esté entre 1 y 10 (extra opcional).
# 3. Usar if y elif para evaluar igualdad o rangos.

nota = int(input("Ingrese su nota (1-10): "))

if nota < 4:
    print("Desaprobado")
elif nota == 4 or nota == 5:
    print("Regular")
elif nota == 6 or nota == 7 or nota == 8:
    print("Bueno")
elif nota == 9:
    print("Muy Bueno")
elif nota == 10:
    print("Excelente")
else:
    print("Nota inválida")