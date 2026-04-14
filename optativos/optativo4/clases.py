# Clase de Clases:
# Diseñar un “FormularioContacto” con nombre, email y mensaje. 
# El método enviar() solo debería ‘permitir’ el envío si los tres campos tienen contenido; si no, debe
# ‘responder’ con un mensaje claro por campo faltante.
# Pensar 3 casos de prueba (completo, un campo vacío, todos vacíos).

class FormularioContacto:
	def __init__(self, nombre, email, mensaje):
		self.nombre = nombre
		self.email = email
		self.mensaje = mensaje

	def enviar(self):
		faltantes = []

		if not self.nombre.strip():
			faltantes.append("nombre")
		if not self.email.strip():
			faltantes.append("email")
		if not self.mensaje.strip():
			faltantes.append("mensaje")

		if not faltantes:
			return "Enviado con éxito."

		mensajes_error = [f"Falta completar el campo: {campo}." for campo in faltantes]
		return "\n".join(mensajes_error)


def probar_formulario(nombre_caso, formulario):
	print(f"{nombre_caso}:")
	print(formulario.enviar())
	print("-" * 50)


if __name__ == "__main__":
	# Caso 1: completo
	formulario_completo = FormularioContacto(
		"Ana Pérez",
		"ana@email.com",
		"Quiero recibir más información."
	)

	# Caso 2: un campo vacío (mensaje)
	formulario_un_campo_vacio = FormularioContacto(
		"Juan Gómez",
		"juan@email.com",
		""
	)

	# Caso 3: todos vacíos
	formulario_todos_vacios = FormularioContacto("", "", "")

	probar_formulario("Caso 1 - Formulario completo", formulario_completo)
	probar_formulario("Caso 2 - Un campo vacío", formulario_un_campo_vacio)
	probar_formulario("Caso 3 - Todos los campos vacíos", formulario_todos_vacios)
