# PASO 1: Crear la lista y pedir las 7 temperaturas
# Creamos una lista vacía donde se van a guardar las temperaturas.
# Luego, con un for que va del 1 al 7, le pedimos al usuario que ingrese
# la temperatura de cada día y la agregamos a la lista con append().

temperaturas = []

for dia in range(1, 8):
    temp = int(input(f"Ingrese la temperatura del día {dia}: "))
    temperaturas.append(temp)

print("\nTemperaturas ingresadas:", temperaturas)

# PASO 2: Ciclo FOR - Contar días con temperatura mayor a 30°
# Recorrer la lista con un for. Por cada temperatura, preguntamos
# si es mayor a 30. Si lo es, sumamos 1 al contador.
# Al final mostramos cuántos días superaron los 30 grados.

dias_calurosos = 0

for temp in temperaturas:
    if temp > 30:
        dias_calurosos += 1

print(f"\nCantidad de días con temperatura mayor a 30°: {dias_calurosos}")

# PASO 3: Ciclo WHILE - Mostrar temperaturas menores a 10°
# Usamos un while con un índice que arranca en 0 y avanza de a 1
# hasta recorrer toda la lista. En cada vuelta, si la temperatura
# es menor a 10, la mostramos junto con el número de día, esto se consigue haciendo (índice + 1).

print("\nDías con temperatura menor a 10°:")

i = 0

while i < len(temperaturas): # el iterador recorre todas las temperaturas
    if temperaturas[i] < 10: # si la temperatura del día i es menor a 10
        print(f"  Día {i + 1}: {temperaturas[i]}°") # se muestra el día y la temperatura
    i += 1
