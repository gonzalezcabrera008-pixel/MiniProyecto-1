#entradas: lista de deportistas y documento que se desea buscar
#salidas: posición del deportista o -1 si no está registrado
#procedimiento: recorrer la lista de deportistas por índices y comparar la llave "documento".
def buscar_deportista(listadeportistas, documento):
    encontrado = False
    posicion = -1
    documento = documento.strip()

    for i in range(len(listadeportistas)):
        if encontrado == False and listadeportistas[i]["documento"].strip() == documento:
            encontrado = True
            posicion = i

    return posicion


#entradas: lista de disciplinas y nombre de la disciplina a buscar
#salidas: posición de la disciplina o -1 si no está registrada
#procedimiento: recorrer la lista por índices y comparar la llave "nombre" sin importar mayúsculas.
def buscar_disciplina(listadisciplinas, nombre):
    encontrado = False
    posicion = -1
    nombre = nombre.lower().strip()

    for i in range(len(listadisciplinas)):
        if encontrado == False and listadisciplinas[i]["nombre"].lower().strip() == nombre:
            encontrado = True
            posicion = i

    return posicion


#entradas: lista de inscripciones, documento y disciplina a buscar
#salidas: posición de la inscripción o -1 si no existe
#procedimiento: recorrer la lista de inscripciones por índices y comparar las llaves "documento" y "disciplina".
def buscar_inscripcion(listainscripciones, documento, disciplina):
    encontrado = False
    posicion = -1
    documento = documento.strip()
    disciplina = disciplina.lower().strip()

    for i in range(len(listainscripciones)):
        if encontrado == False:
            if listainscripciones[i]["documento"].strip() == documento and listainscripciones[i]["disciplina"].lower().strip() == disciplina:
                encontrado = True
                posicion = i

    return posicion


#entradas: listas de inscripciones, deportistas y disciplinas, número de documento y nombre de disciplina
#salidas: True y mensaje de éxito, o False y mensaje de error
#procedimiento: validar los campos, buscar el deportista y la disciplina, evitar inscripciones repetidas y guardar un diccionario con sus datos.
def inscribir_deportista(listainscripciones, listadeportistas, listadisciplinas, documento, disciplina):
    documento = documento.strip()
    disciplina = disciplina.strip()

    if len(documento) == 0 or len(disciplina) == 0:
        return False, "Todos los campos son obligatorios."

    posicion_deportista = buscar_deportista(listadeportistas, documento)
    if posicion_deportista == -1:
        return False, "El deportista no está registrado."

    posicion_disciplina = buscar_disciplina(listadisciplinas, disciplina)
    if posicion_disciplina == -1:
        return False, "La disciplina no está registrada."

    nombre_disciplina = listadisciplinas[posicion_disciplina]["nombre"]
    if buscar_inscripcion(listainscripciones, documento, nombre_disciplina) != -1:
        return False, "El deportista ya está inscrito en esa disciplina."

    deportista = listadeportistas[posicion_deportista]
    nueva_inscripcion = {
        "tipodoc": deportista["tipodoc"],
        "documento": deportista["documento"],
        "disciplina": nombre_disciplina
    }
    listainscripciones.append(nueva_inscripcion)
    return True, "Inscripción registrada con éxito."


#entradas: lista de inscripciones, documento y disciplina que se desea eliminar
#salidas: True y mensaje de éxito, o False y mensaje de error
#procedimiento: validar los datos, buscar la inscripción por documento y disciplina y eliminar el diccionario encontrado.
def eliminar_inscripcion(listainscripciones, documento, disciplina):
    documento = documento.strip()
    disciplina = disciplina.strip()

    if len(documento) == 0 or len(disciplina) == 0:
        return False, "Debe ingresar el documento y la disciplina."

    posicion = buscar_inscripcion(listainscripciones, documento, disciplina)
    if posicion == -1:
        return False, "No existe una inscripción con ese documento y disciplina."

    listainscripciones.pop(posicion)
    return True, "Inscripción eliminada con éxito."


#entradas: listas de inscripciones y deportistas, y disciplina opcional para filtrar
#salidas: lista de textos con nombre, documento, universidad y disciplina
#procedimiento: recorrer las inscripciones, buscar los datos del deportista y agregar una línea formateada al resultado.
def listar_inscripciones_por_disciplina(listainscripciones, listadeportistas, disciplina):
    resultado = []
    filtro = disciplina.lower().strip()
    contador = 0

    for i in range(len(listainscripciones)):
        inscripcion_actual = listainscripciones[i]
        if len(filtro) == 0 or inscripcion_actual["disciplina"].lower().strip() == filtro:
            contador = contador + 1
            posicion_deportista = buscar_deportista(listadeportistas, inscripcion_actual["documento"])
            if posicion_deportista != -1:
                deportista = listadeportistas[posicion_deportista]
                texto = str(contador) + ". " + deportista["nombre"] + " (" + inscripcion_actual["documento"] + ") | " + deportista["universidad"] + " | " + inscripcion_actual["disciplina"]
            else:
                texto = str(contador) + ". Doc: " + inscripcion_actual["documento"] + " | " + inscripcion_actual["disciplina"]
            resultado.append(texto)

    return resultado
