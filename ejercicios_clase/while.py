# Creando nuestro while:
# Para poner en práctica lo que acabamos de aprender,
# crearemos un ciclo while donde el ciclo deberá hacer loop
# cinco veces, mostrando en pantalla los números del 1 al 5. 

# Pasos básicos: 
# 1. Creamos una variable y le asignamos un valor. 
# 2. Creamos la estructura while. 
# 3. Colocamos un agregador de valor en la variable. 
# 4. Ponemos un print para ver los valores

contador = 1  # Paso 1: creamos una variable y le asignamos el valor de 1
while contador <= 5:  # Paso 2: mientras contador sea menor o igual a 5
	print(contador)   # Paso 4: vamos mostrando los valores en consola
	contador += 1     # Paso 3: incrementamos en cada vuelta el valor en la variable para evitar un bucle infinito

