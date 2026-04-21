# Consigna - Control de Saldo: Un cajero automático tiene que decidir si entrega el dinero o no.
# Los datos que tiene son: saldo_disponible y monto_a_retirar.
# Explicar con palabras el paso a paso de la lógica que debería seguir el cajero para aprobar la operación,
# rechazarla si el monto es mayor al saldo y rechazarla si el monto es igual a 0. 

# Paso a paso de la lógica:
# 1. Recibir el saldo disponible y el monto que se quiere retirar.
# 2. Verificar si el monto a retirar es igual a 0. Si es así, rechazar la operación porque no tiene sentido retirar $0.
# 3. Verificar si el monto a retirar es mayor al saldo disponible. Si es así, rechazar la operación por saldo insuficiente.
# 4. Si el monto es mayor a 0 y menor o igual al saldo disponible, aprobar la operación y entregar el dinero.

saldo_disponible = 10000
print(f"Su saldo disponible es: ${saldo_disponible}")
monto_a_retirar = int(input("Ingrese el monto a retirar: "))

if monto_a_retirar == 0:
    print("Operación rechazada: el monto a retirar no puede ser $0.")
elif monto_a_retirar > saldo_disponible:
    print(f"Operación rechazada: saldo insuficiente. Su saldo es ${saldo_disponible}.")
else:
    saldo_disponible -= monto_a_retirar
    print(f"Operación aprobada. Se retiraron ${monto_a_retirar}. Saldo restante: ${saldo_disponible}.")