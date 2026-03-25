# Nuestra lista:
# Tendrán que armar una lista de 5 nombres, y mostrarlos a
# todos en terminal. Luego remover el nombre en la posición 3
# y poner un nuevo nombre al final de la lista. Mostrar en
# terminal cómo quedaría después. 


# Pasos básicos: 
# 1. Crear una lista. 
# 2. Agregar los 5 nombres y mostrarlos en terminal.
# 3. Utilizar remove para quitar el nombre de la posición 3. 
# 4. Usar un push para agregar un nuevo nombre al final de la lista. 
# 5. Mostrar en terminal cómo quedó la lista.

nombres = ["Tatiana", "Rodrigo", "Sofia", "Noelia", "Juan"]  # Paso 1 y 2
print("Lista original:", nombres) # se la muestra en pantalla

# Paso 3: Remover el nombre en la posición 3 (índice 2)
nombre_removido = nombres.pop(2) # se saca a Sofia de la lista

# Paso 4: Agregar un nuevo nombre al final
nombres.append("María")

# Paso 5: Mostrar la lista final
print("Lista modificada:", nombres)
# se muestra la lista modificada en pantalla, con el nuevo nombre y sin el nombre removido.
