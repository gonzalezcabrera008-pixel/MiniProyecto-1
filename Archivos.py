#entradas: listas de universidades
#salidas: el set con los nombres unicos y una lista con los nombres que se repitieron
#procedimiento: Recorrer la lista de universidades, parar en cada indice, extraer de la llave nombre, asegurar que haya
#algo, si hay algo quitar espacios y mayusculas, verificar si el nombre esta en el set si esta en el set agregar a la lista de repetidos,
#antes verificando que no este en la lista de repetidos. Si no estaba en el set agregar al set.

def contruirsetuniversidades(listauniversidades):
    #crear un set para los nombres unicos y una lista para los que se repetieron, asi poder mostrarle al usuario cual se repitio
    setuni=set()
    repetidos= []
    #verificar que lo que se ingrese sea una lista, no un texto, ni numeros, etc, porque lanzaria resultados no deseados o error
    #para preveerlo se retorna simplemente.
    if type(listauniversidades) != list:
        return setuni, repetidos
    
    for i in range (len(listauniversidades)):
        universidadactual=listauniversidades[i]
        #Variable original es para mostrar y nombre cambiado es para comparar por eso a uno solo se aplica sstrip y a otro se le aplica
        #minisculas.
        nombrecambiado=""
        nombreoriginal=""

        #verificar que sea un diccionario para evitar que muestre error
        if type (universidadactual)==dict:
            #si es un dict buscar en la llave nombre y guardarla en nombre
            nombre = universidadactual.get ("nombre")
            #mientras haya algo en la llave:
            if nombre!= None:
                nombreoriginal=str(nombre).strip()
                nombrecambiado=nombreoriginal.lower()
                #si hay aunque sea espacios:
                if nombrecambiado != "":
                    if nombrecambiado in setuni:
                        #marcador para agregarlo o no a lista de repetidos sin repetirlo
                        agregar=True

                        for j in range (len(repetidos)):
                            if repetidos [j].lower()== nombrecambiado:
                                agregar=False
                        if agregar== True: 
                            repetidos.append(nombreoriginal)
                    else:
                        setuni.add(nombrecambiado)
    return setuni, repetidos                        

#------------------------------------
# Entradas: listadisciplinas
# Salidas: el set con los nombres únicos de disciplinas y una lista con los nombres que se repitieron
# Procedimientos: Recorrer la lista de disciplinas por índices, extraer la llave nombre, asegurar que haya algo, quitar espacios
# y mayúsculas, verificar si el nombre ya está en el set: si está, agregarlo a repetidos (antes verificando que no esté ya en
# la lista de repetidos) si no estaba, agregarlo al set.

def construirsetdisciplinas(listadisciplinas):
    # Set para los nombres únicos y lista para los repetidos, así se le puede mostrar al usuario cuáles se repitieron
    setdis = set()
    repetidos = []

    # Si lo que llega no es una lista (texto, número, None) se retorna vacío para evitar errores
    if type(listadisciplinas) != list:
        return setdis, repetidos

    for i in range(len(listadisciplinas)):
        disciplinaactual = listadisciplinas[i]
        # nombreoriginal sirve para mostrar, nombrecambiado (sin espacios y en minúscula) sirve para comparar
        nombrecambiado = ""
        nombreoriginal = ""

        # Verificar que sea un diccionario para evitar errores
        if type(disciplinaactual) == dict:
            nombre = disciplinaactual.get("nombre")
            if nombre != None:
                nombreoriginal = str(nombre).strip()
                nombrecambiado = nombreoriginal.lower()
                # Si después de quitar espacios no quedó vacío
                if nombrecambiado != "":
                    if nombrecambiado in setdis:
                        # Bandera para no agregar dos veces el mismo repetido
                        agregar = True
                        for j in range(len(repetidos)):
                            if repetidos[j].lower() == nombrecambiado:
                                agregar = False
                        if agregar == True:
                            repetidos.append(nombreoriginal)
                    else:
                        setdis.add(nombrecambiado)
    return setdis, repetidos

#----------------------------------------------
# Entradas: listadeportistas
# Salidas: el set con los números de documento únicos y una lista con los documentos que se repitieron
# Procedimientos: Recorrer la lista de deportistas por índices, extraer la llave documento, asegurar que haya algo, convertirlo a
# texto y quitar espacios, verificar si el documento ya está en el set: si está, agregarlo a repetidos (antes verificando que no
# esté ya en la lista de repetidos) si no estaba, agregarlo al set.

def construirsetdeportistas(listadeportistas):
    # Set para los documentos únicos y lista para los repetidos, así se le puede mostrar al usuario cuáles se repitieron
    setdep = set()
    repetidos = []

    # Si lo que llega no es una lista (texto, número, None) se retorna vacío para evitar errores
    if type(listadeportistas) != list:
        return setdep, repetidos

    for i in range(len(listadeportistas)):
        deportistaactual = listadeportistas[i]
        documentotexto = ""

        # Verificar que sea un diccionario para evitar errores
        if type(deportistaactual) == dict:
            documento = deportistaactual.get("documento")
            if documento != None:
                # str() por si el documento llega como número, strip()
                documentotexto = str(documento).strip()
                # Si después de quitar espacios no quedó vacío
                if documentotexto != "":
                    if documentotexto in setdep:
                        # Bandera para no agregar dos veces el mismo repetido
                        agregar = True
                        for j in range(len(repetidos)):
                            if repetidos[j] == documentotexto:
                                agregar = False
                        if agregar == True:
                            repetidos.append(documentotexto)
                    else:
                        setdep.add(documentotexto)
    return setdep, repetidos

#---------------------------------------------
 # Entradas: listauniversidades, listadisciplinas y listadeportistas (listas de diccionarios)
# Salidas: True/False según si se encontró algún repetido, y un texto que indica cuáles son
# Procedimientos: Llamar a las tres funciones que construyen los sets para obtener las listas de repetidos. Guardarlas en una
# matriz (una fila por tipo de dato) junto a una lista de títulos. Recorrer la matriz si una fila
# tiene repetidos, se marca hayduplicados = True y se arma su mensaje de texto con los repetidos separados por coma. Al final se
# retorna el mensaje con los repetidos, o un mensaje de que no hay ninguno.

def detectarduplicados(listauniversidades, listadisciplinas, listadeportistas):
    setuni, repetidosuni = contruirsetuniversidades(listauniversidades)
    setdis, repetidosdis = construirsetdisciplinas(listadisciplinas)
    setdep, repetidosdep = construirsetdeportistas(listadeportistas)

    # cada fila es la lista de repetidos de un tipo de dato titulos[i] es el nombre de la fila i
    grupos = [repetidosuni, repetidosdis, repetidosdep]
    titulos = ["Universidades repetidas: ", "Disciplinas repetidas: ", "Deportistas repetidos (documento): "]

    hayduplicados = False
    mensaje = ""

    for i in range(len(grupos)):
        grupoactual=grupos[i]
        # Solo se arma el mensaje si esa fila tiene repetidos
        if len(grupoactual) > 0:
            hayduplicados = True

            #salto de linea para organizar mejor, solo cuando ya hay algo escrito
            if mensaje!= "":
                mensaje =mensaje+"\n"

            mensaje = mensaje+titulos[i]

            #recorre lo que hay dentro de la lista 
            for j in range(len(grupoactual)):
                # Coma despues del primer elemento
                if j > 0 :
                    mensaje = mensaje+","
                mensaje=mensaje+str(grupoactual[j])

    if hayduplicados == True:
        mensaje = "Se encontraron datos repetidos:\n\n" + mensaje
    else:
        mensaje = "No se encontraron datos repetidos."
    return hayduplicados, mensaje


#------------------------------------------------
# Entradas: universidades, deportistas, disciplinas, inscripciones y resultados
# Salidas: True/False según si la estructura es correcta, y un texto que explica el primer problema

# Procedimientos: Guardar las 5 listas en una matriz junto con sus nombres y las llaves que debe tener cada una. Recorrer con
# ciclos por índices cada lista, cada elemento y cada llave. Se verifica que cada dato sea una lista, que cada elemento sea un
# diccionario y que cada llave exista y tenga un texto no vacío. Con la bandera valido se detiene la revisión en el primer
# error y se retorna el mensaje que indica dónde está; si no hay errores se retorna True.

# Entradas: listauniversidades, listadeportistas, listadisciplinas, listainscripciones y listaresultados
# Salidas: tupla (valido, mensaje): True/False según si la estructura es correcta, y un texto que explica el primer problema

# Procedimientos: Guardar las 5 listas en una matriz junto con sus nombres y las llaves que debe tener cada una. Recorrer con
# ciclos por índices cada lista, cada elemento y cada llave. Se verifica que cada dato sea una lista, que cada elemento sea un
# diccionario y que cada llave exista y tenga un texto no vacío. Con la bandera valido se detiene la revisión en el primer
# error y se retorna el mensaje que indica dónde está; si no hay errores se retorna True.

def validarestructuradatos(listauniversidades, listadeportistas, listadisciplinas, listainscripciones, listaresultados):
    # Las 5 listas juntas. La posición i de las tres listas siguientes habla del mismo tipo de dato
    datos = [listauniversidades, listadeportistas, listadisciplinas, listainscripciones, listaresultados]
    nombres = ["Universidades", "Deportistas", "Disciplinas", "Inscripciones", "Resultados"]
    # Llaves que debe tener cada diccionario de cada lista
    llaves = [
        ["nombre", "pais", "ciudad", "tipo"],
        ["nombre", "tipodoc", "documento", "universidad"],
        ["nombre", "modalidad"],
        ["tipodoc", "documento", "disciplina"],
        ["disciplina", "universidad", "posicion"]
    ]

    #empieza en True y pasa a False al encontrar el primer error
    valido = True
    mensaje = "La estructura de los datos es válida."

    #recorre las 5 listas
    for i in range(len(datos)):
        listaactual = datos[i]
        nombrelista = nombres[i]
        llavesactuales = llaves[i]

        # revisar que sea lista
        if valido == True and type(listaactual) != list:
            valido = False
            mensaje = nombrelista + ": los datos deben ser una lista."

        # Solo si es lista se revisan sus elementos
        if valido == True and type(listaactual) == list:

            #recorre los diccionarios de la lista
            for j in range(len(listaactual)):
                elemento = listaactual[j]
                posicion = str(j + 1)

                # es un diccionario?
                if valido == True and type(elemento) != dict:
                    valido = False
                    mensaje = nombrelista + ": el elemento " + posicion + " no es un diccionario."

                # Solo si es diccionario se revisan sus llaves
                if valido == True and type(elemento) == dict:

                    # recorre las llaves que debe tener el diccionario
                    for k in range(len(llavesactuales)):
                        #pararse en cada llave dentro del conjunto de llaves que tiene el dicc.
                        llave = llavesactuales[k]
                        #si llave no esta en diccionario 
                        if valido == True and llave not in elemento:
                            valido = False
                            mensaje = nombrelista + ": al elemento " + posicion + " le falta la llave '" + llave + "'."

                        if valido == True:
                            #saca el contenido de la llave
                            valor = elemento[llave]

                            if type(valor) != str:
                                valido = False
                                mensaje = nombrelista + ": en el elemento " + posicion + " la llave '" + llave + "' debe ser texto."

                            if valido == True and valor.strip() == "":
                                valido = False
                                mensaje = nombrelista + ": en el elemento " + posicion + " la llave '" + llave + "' está vacía."
    return valido, mensaje
#----------------------------------