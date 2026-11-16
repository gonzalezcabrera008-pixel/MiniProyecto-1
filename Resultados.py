#entradas: lista de disciplinas y nombre a buscar
#salidas: posición de la disciplina o -1 si no se encuentra
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


#entradas: lista de universidades y nombre a buscar
#salidas: posición de la universidad o -1 si no se encuentra
#procedimiento: recorrer la lista por índices y comparar la llave "nombre" sin importar mayúsculas.
def buscar_universidad(listauniversidades, nombre):
    encontrado = False
    posicion = -1
    nombre = nombre.lower().strip()

    for i in range(len(listauniversidades)):
        if encontrado == False and listauniversidades[i]["nombre"].lower().strip() == nombre:
            encontrado = True
            posicion = i

    return posicion


#entradas: lista de resultados, disciplina y universidad a buscar
#salidas: posición del resultado o -1 si no existe
#procedimiento: recorrer la lista por índices y comparar las llaves "disciplina" y "universidad".
def buscar_resultado(listaresultados, disciplina, universidad):
    encontrado = False
    posicion = -1
    disciplina = disciplina.lower().strip()
    universidad = universidad.lower().strip()

    for i in range(len(listaresultados)):
        if encontrado == False:
            if listaresultados[i]["disciplina"].lower().strip() == disciplina and listaresultados[i]["universidad"].lower().strip() == universidad:
                encontrado = True
                posicion = i

    return posicion


#entradas: listas de resultados, disciplinas y universidades, disciplina, universidad y posición obtenida
#salidas: True y mensaje de éxito, o False y mensaje de error
#procedimiento: validar los campos, verificar que existan la disciplina y la universidad, validar la medalla y evitar posiciones repetidas por disciplina.
def registrar_resultado(listaresultados, listadisciplinas, listauniversidades, disciplina, universidad, posicion):
    disciplina = disciplina.strip()
    universidad = universidad.strip()
    posicion = posicion.strip().lower()

    if len(disciplina) == 0 or len(universidad) == 0 or len(posicion) == 0:
        return False, "Todos los campos son obligatorios."

    if posicion != "oro" and posicion != "plata" and posicion != "bronce":
        return False, "La posición debe ser Oro, Plata o Bronce."

    posicion_disciplina = buscar_disciplina(listadisciplinas, disciplina)
    if posicion_disciplina == -1:
        return False, "La disciplina no está registrada."

    posicion_universidad = buscar_universidad(listauniversidades, universidad)
    if posicion_universidad == -1:
        return False, "La universidad no está registrada."

    nombre_disciplina = listadisciplinas[posicion_disciplina]["nombre"]
    nombre_universidad = listauniversidades[posicion_universidad]["nombre"]

    for i in range(len(listaresultados)):
        if listaresultados[i]["disciplina"].lower().strip() == nombre_disciplina.lower().strip() and listaresultados[i]["posicion"].lower().strip() == posicion:
            return False, "Ya existe una universidad con esa posición en la disciplina."
        if listaresultados[i]["disciplina"].lower().strip() == nombre_disciplina.lower().strip() and listaresultados[i]["universidad"].lower().strip() == nombre_universidad.lower().strip():
            return False, "La universidad ya tiene un resultado registrado en esa disciplina."

    nuevo_resultado = {
        "disciplina": nombre_disciplina,
        "universidad": nombre_universidad,
        "posicion": posicion.capitalize()
    }
    listaresultados.append(nuevo_resultado)
    return True, "Resultado registrado con éxito."


#entradas: lista de resultados, disciplina y universidad que se desea eliminar
#salidas: True y mensaje de éxito, o False y mensaje de error
#procedimiento: validar los datos, buscar el resultado por disciplina y universidad y eliminar el diccionario encontrado.
def eliminar_resultado(listaresultados, disciplina, universidad):
    disciplina = disciplina.strip()
    universidad = universidad.strip()

    if len(disciplina) == 0 or len(universidad) == 0:
        return False, "Debe ingresar la disciplina y la universidad."

    posicion = buscar_resultado(listaresultados, disciplina, universidad)
    if posicion == -1:
        return False, "No existe un resultado con esa disciplina y universidad."

    listaresultados.pop(posicion)
    return True, "Resultado eliminado con éxito."


#entradas: lista de resultados y disciplina opcional para filtrar
#salidas: lista de textos con disciplina, universidad y medalla
#procedimiento: recorrer los resultados por índices y agregar cada registro que coincida con el filtro.
def listar_resultados(listaresultados, disciplina):
    resultado = []
    filtro = disciplina.lower().strip()
    contador = 0

    for i in range(len(listaresultados)):
        resultado_actual = listaresultados[i]
        if len(filtro) == 0 or resultado_actual["disciplina"].lower().strip() == filtro:
            contador = contador + 1
            texto = str(contador) + ". " + resultado_actual["disciplina"] + " | " + resultado_actual["universidad"] + " | " + resultado_actual["posicion"]
            resultado.append(texto)

    return resultado