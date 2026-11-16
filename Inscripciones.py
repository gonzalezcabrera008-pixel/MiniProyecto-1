from Deportistas import buscar_deportista
from Disciplinas import buscar_disciplina


# Entradas: inscripciones (matriz), num_doc (texto) y disciplina (texto)
# Salidas: posición (índice) de la inscripción en la matriz, o -1 si no existe
# Procedimientos: recorre la matriz inscripciones por índices comparando la columna 0
# (num_doc) y la columna 1 (disciplina); si coinciden, enciende la bandera y guarda el índice.
def buscar_inscripcion(inscripciones, num_doc, disciplina):
    encontrado = False
    posicion = -1
    doc_limpio = num_doc.strip()
    disc_limpia = disciplina.lower().strip()
    for i in range(len(inscripciones)):
        if encontrado == False:
            if inscripciones[i][0].strip() == doc_limpio and inscripciones[i][1].lower().strip() == disc_limpia:
                encontrado = True
                posicion = i
    return posicion


# Entradas: inscripciones (matriz), deportistas (lista), disciplinas (lista), num_doc y disciplina (textos)
# Salidas: "OK" si se inscribe correctamente, o un mensaje de error (texto)
# Procedimientos: valida campos obligatorios, comprueba que el deportista y la disciplina
# existan en sus listas, verifica que no esté ya inscrito en esa disciplina
# y agrega la fila [num_doc, nombre_disciplina] a la matriz inscripciones.
def inscribir_deportista(inscripciones, deportistas, disciplinas, num_doc, disciplina):
    num_doc = num_doc.strip()
    disciplina = disciplina.strip()

    if len(num_doc) == 0 or len(disciplina) == 0:
        return "Todos los campos son obligatorios."

    pos_dep = buscar_deportista(deportistas, num_doc)
    if pos_dep == -1:
        return "El deportista no está registrado."

    pos_disc = buscar_disciplina(disciplinas, disciplina)
    if pos_disc == -1:
        return "La disciplina no está registrada."

    nombre_disc_exacto = disciplinas[pos_disc]["nombre"]

    if buscar_inscripcion(inscripciones, num_doc, nombre_disc_exacto) != -1:
        return "El deportista ya está inscrito en esa disciplina."

    nueva_fila = [num_doc, nombre_disc_exacto]
    inscripciones.append(nueva_fila)
    return "OK"


# Entradas: inscripciones (matriz), num_doc (texto) y disciplina (texto)
# Salidas: "OK" si se elimina correctamente, o un mensaje de error (texto)
# Procedimientos: valida que los campos no estén vacíos, busca la fila correspondiente
# en la matriz inscripciones y la elimina usando pop().
def eliminar_inscripcion(inscripciones, num_doc, disciplina):
    num_doc = num_doc.strip()
    disciplina = disciplina.strip()

    if len(num_doc) == 0 or len(disciplina) == 0:
        return "Debe ingresar el documento y la disciplina para eliminar la inscripción."

    pos_insc = buscar_inscripcion(inscripciones, num_doc, disciplina)
    if pos_insc == -1:
        return "No existe una inscripción con ese documento y disciplina."

    inscripciones.pop(pos_insc)
    return "OK"


# Entradas: inscripciones (matriz), deportistas (lista) y disciplina (texto)
# Salidas: lista de textos formateados con los deportistas inscritos
# Procedimientos: recorre la matriz inscripciones por índices; si disciplina está vacía
# muestra todas las inscripciones, y si tiene texto filtra por esa disciplina cruzando
# el nombre y universidad desde la lista deportistas.
def listar_inscripciones_por_disciplina(inscripciones, deportistas, disciplina):
    resultado = []
    filtro = disciplina.lower().strip()
    contador = 0

    for i in range(len(inscripciones)):
        doc_actual = inscripciones[i][0]
        disc_actual = inscripciones[i][1]

        if len(filtro) == 0 or disc_actual.lower().strip() == filtro:
            contador = contador + 1
            pos_dep = buscar_deportista(deportistas, doc_actual)
            if pos_dep != -1:
                nombre_dep = deportistas[pos_dep]["nombre"]
                univ_dep = deportistas[pos_dep]["universidad"]
                texto = str(contador) + ". " + nombre_dep + " (" + doc_actual + ") | " + univ_dep + " | " + disc_actual
            else:
                texto = str(contador) + ". Doc: " + doc_actual + " | " + disc_actual
            resultado.append(texto)

    return resultado