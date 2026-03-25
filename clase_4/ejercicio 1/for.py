# Uniendo Conceptos:
# Creamos una estructura for para ingresar diferentes edades,
# y posteriormente una segunda estructura for para mostrar
# en terminal los valores mayores a 30. 

# Pasos básicos: 
# 1. Armamos dos estructuras for, con la misma cantidad de ciclos que queremos. 
# 2. En la primera, programamos para que se ingresen números. 
# 3. En el segundo, creamos una estructura de decisión para comparar si los
# valores son mayores a 30.
# 4. Agregamos un print en la estructura de decisión que cumpla con la condición dada

edades = []
cantidad = 5  # vamos a repetir el ciclo 5 veces para ingresar 5 edades

# Primer for: ingresar las edades
for i in range(cantidad):
	edad = int(input(f"Ingrese la edad nº{i+1} : "))
	edades.append(edad)

# Segundo for: mostrar edades mayores a 30
print("Edades mayores a 30:")
for edad in edades:
	if edad > 30:
		print(edad)