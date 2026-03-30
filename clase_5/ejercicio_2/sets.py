# Sets sin duplicados:
# Crear un set con los nombres de tres frutas. Luego,
# intentar agregar una fruta que ya esté en el set.
# Finalmente, mostrar el set completo usando print() y
# observar que no se repite ningún elemento.

set_ejemplo = {"manzana", "banana", "naranja"}

print(set_ejemplo)  # {'manzana', 'banana', 'naranja'}
set_ejemplo.remove("naranja")  # se saca naranja

set_ejemplo.add("manzana")  # Intentamos agregar "manzana" nuevamente
print(set_ejemplo)  # {'manzana', 'banana'}