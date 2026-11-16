from Universidades import tiene_punto_coma


# Entradas: disciplinas (lista de diccionarios) y nombre (texto)
# Salidas: posición (índice) de la disciplina, o -1 si no existe
# Procedimientos: se recorre la lista por índices; cuando la llave "nombre" coincide
# sin importar mayúsculas o espacios, se enciende la bandera y se guarda la posición.
def buscar_disciplina(disciplinas, nombre):
    encontrado = False
    posicion = -1
    nombre_limpio = nombre.lower().strip()
    for i in range(len(disciplinas)):
        if encontrado == False and disciplinas[i]["nombre"].lower().strip() == nombre_limpio:
            encontrado = True
            posicion = i
    return posicion


# Entradas: disciplinas (lista), nombre y modalidad (textos)
# Salidas: "OK" si se registra correctamente, o un mensaje de error (texto)
# Procedimientos: limpia espacios, valida campos obligatorios y sin punto y coma,
# verifica que la modalidad sea "individual" o "por equipos", comprueba duplicados
# y agrega el diccionario a disciplinas.
def registrar_disciplina(disciplinas, nombre, modalidad):
    nombre = nombre.strip()
    modalidad = modalidad.strip().lower()

    if len(nombre) == 0 or len(modalidad) == 0:
        return "Todos los campos son obligatorios."

    if tiene_punto_coma(nombre) or tiene_punto_coma(modalidad):
        return "Ningún campo puede contener punto y coma (;)."

    if modalidad != "individual" and modalidad != "por equipos":
        return "La modalidad debe ser individual o por equipos."

    if buscar_disciplina(disciplinas, nombre) != -1:
        return "Ya existe una disciplina registrada con ese nombre."

    nueva_disciplina = {
        "nombre": nombre,
        "modalidad": modalidad
    }
    disciplinas.append(nueva_disciplina)
    return "OK"


# Entradas: disciplinas (lista de diccionarios)
# Salidas: lista de textos formateados para mostrar en el Listbox
# Procedimientos: crea una lista vacía, recorre disciplinas por índice y arma cada
# línea con el consecutivo, el nombre de la disciplina y su modalidad.
def listar_disciplinas(disciplinas):
    resultado = []
    for i in range(len(disciplinas)):
        disc_actual = disciplinas[i]
        texto = str(i + 1) + ". " + disc_actual["nombre"] + " | " + disc_actual["modalidad"]
        resultado.append(texto)
    return resultado


# Entradas: disciplinas (lista), inscripciones (matriz), resultados (matriz) y nombre (texto)
# Salidas: "OK" si se elimina correctamente, o un mensaje de error (texto)
# Procedimientos: verifica que el nombre no esté vacío, busca la disciplina, comprueba
# por índices que no esté en la columna 1 de inscripciones ni en la columna 0 de resultados,
# y la elimina con pop().
def eliminar_disciplina(disciplinas, inscripciones, resultados, nombre):
    nombre = nombre.strip()
    if len(nombre) == 0:
        return "El nombre de la disciplina es obligatorio para eliminar."

    pos_disc = buscar_disciplina(disciplinas, nombre)
    if pos_disc == -1:
        return "La disciplina no está registrada."

    nombre_exacto = disciplinas[pos_disc]["nombre"].lower().strip()

    tiene_inscripciones = False
    for i in range(len(inscripciones)):
        if tiene_inscripciones == False and inscripciones[i][1].lower().strip() == nombre_exacto:
            tiene_inscripciones = True

    if tiene_inscripciones == True:
        return "No se puede eliminar: la disciplina tiene inscripciones registradas."

    tiene_resultados = False
    for i in range(len(resultados)):
        if tiene_resultados == False and resultados[i][0].lower().strip() == nombre_exacto:
            tiene_resultados = True

    if tiene_resultados == True:
        return "No se puede eliminar: la disciplina tiene resultados registrados."

    disciplinas.pop(pos_disc)
    return "OK"