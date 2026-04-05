# Análisis de notas:
# Pedir al usuario que ingrese 5 notas (entre 1 y 10) y almacenarlas en una lista. Luego, crear una función que
# reciba esa lista como parámetro, calcule el promedio de las notas y lo devuelva. 
# Finalmente, mostrar el promedio por pantalla.

notas = []
for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1} (entre 1 y 10): "))
    notas.append(nota)

def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

promedio = calcular_promedio(notas)
print(f"El promedio de las notas ingresadas es: {promedio}")