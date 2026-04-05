# Usando los retornos: 
# Crear una función en la que, al ingresar 5 valores por terminal, retornará el valor más alto y luego lo mostrará en terminal.

# Pasos básicos: 
# 1. Armar una función vacía con un return al final.
# 2. Crear un algoritmo para encontrar el valor más alto.
# 3. Instanciar la variable que recibirá el valor.
# 4. Instanciar la función.
# 5. Escribir un print con la variable retornada.

def valor_mas_alto():
    valores = []
    for i in range(5):
        valor = int(input(f"Ingrese el valor {i+1}: "))
        valores.append(valor)
    return max(valores)

resultado = valor_mas_alto()
print(f"El valor más alto ingresado es: {resultado}")

