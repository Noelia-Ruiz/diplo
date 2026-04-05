# Control de acceso con función:
# Pedirle al usuario que ingrese su nombre y edad. 
# Crear una función llamada verificar_acceso() que reciba ambos valores por parámetro. 
# Si la edad es mayor o igual a 18, la función debe imprimir:-"Bienvenido/a, [nombre]. Tenés acceso autorizado."
# Caso contrario, debe imprimir:-"Lo siento, [nombre]. El acceso no está permitido."

def verificar_acceso(nombre, edad):
    if edad >= 18:
        print(f"Bienvenido/a, {nombre}. Tenés acceso autorizado.")
    else:
        print(f"Lo siento, {nombre}. El acceso no está permitido.")

nombre = input("Ingresá tu nombre: ")
edad = int(input("Ingresá tu edad: "))
verificar_acceso(nombre, edad)

