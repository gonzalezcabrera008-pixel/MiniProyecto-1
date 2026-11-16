#entradas: lista de universidades y resultados
#salidas: lista con medallas de oro, plata y bronce de cada universidad
#procedimiento: recorrer universidades y resultados por índices para contar las medallas de cada una.
def consultar_medallero(listauniversidades, listaresultados):
    textos = []

    for i in range(len(listauniversidades)):
        nombre_universidad = listauniversidades[i]["nombre"]
        oros = 0
        platas = 0
        bronces = 0

        for j in range(len(listaresultados)):
            resultado_actual = listaresultados[j]
            if resultado_actual["universidad"].lower().strip() == nombre_universidad.lower().strip():
                posicion = resultado_actual["posicion"].lower().strip()
                if posicion == "oro":
                    oros = oros + 1
                elif posicion == "plata":
                    platas = platas + 1
                elif posicion == "bronce":
                    bronces = bronces + 1

        texto = nombre_universidad + " | Oro: " + str(oros) + " | Plata: " + str(platas) + " | Bronce: " + str(bronces)
        textos.append(texto)

    return textos


#entradas: lista de universidades y resultados
#salidas: clasificación general y nombre de la universidad o universidades ganadoras
#procedimiento: contar puntos y medallas, ordenar manualmente por puntos, oros, platas y bronces, e informar los empates del primer puesto.
def consultar_universidad_ganadora(listauniversidades, listaresultados):
    nombres = []
    puntos = []
    oros_lista = []
    platas_lista = []
    bronces_lista = []

    for i in range(len(listauniversidades)):
        nombre_universidad = listauniversidades[i]["nombre"]
        oros = 0
        platas = 0
        bronces = 0

        for j in range(len(listaresultados)):
            resultado_actual = listaresultados[j]
            if resultado_actual["universidad"].lower().strip() == nombre_universidad.lower().strip():
                posicion = resultado_actual["posicion"].lower().strip()
                if posicion == "oro":
                    oros = oros + 1
                elif posicion == "plata":
                    platas = platas + 1
                elif posicion == "bronce":
                    bronces = bronces + 1

        nombres.append(nombre_universidad)
        puntos.append(oros * 3 + platas * 2 + bronces)
        oros_lista.append(oros)
        platas_lista.append(platas)
        bronces_lista.append(bronces)

    for i in range(len(nombres)):
        for j in range(len(nombres) - 1 - i):
            intercambiar = False
            if puntos[j] < puntos[j + 1]:
                intercambiar = True
            elif puntos[j] == puntos[j + 1] and oros_lista[j] < oros_lista[j + 1]:
                intercambiar = True
            elif puntos[j] == puntos[j + 1] and oros_lista[j] == oros_lista[j + 1] and platas_lista[j] < platas_lista[j + 1]:
                intercambiar = True
            elif puntos[j] == puntos[j + 1] and oros_lista[j] == oros_lista[j + 1] and platas_lista[j] == platas_lista[j + 1] and bronces_lista[j] < bronces_lista[j + 1]:
                intercambiar = True

            if intercambiar == True:
                temporal = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = temporal

                temporal = puntos[j]
                puntos[j] = puntos[j + 1]
                puntos[j + 1] = temporal

                temporal = oros_lista[j]
                oros_lista[j] = oros_lista[j + 1]
                oros_lista[j + 1] = temporal

                temporal = platas_lista[j]
                platas_lista[j] = platas_lista[j + 1]
                platas_lista[j + 1] = temporal

                temporal = bronces_lista[j]
                bronces_lista[j] = bronces_lista[j + 1]
                bronces_lista[j + 1] = temporal

    textos = []
    for i in range(len(nombres)):
        texto = str(i + 1) + ". " + nombres[i] + " | " + str(puntos[i]) + " puntos"
        textos.append(texto)

    if len(nombres) == 0:
        textos.append("No hay universidades registradas.")
    else:
        ganadoras = ""
        for i in range(len(nombres)):
            if puntos[i] == puntos[0] and oros_lista[i] == oros_lista[0] and platas_lista[i] == platas_lista[0] and bronces_lista[i] == bronces_lista[0]:
                if len(ganadoras) > 0:
                    ganadoras = ganadoras + ", "
                ganadoras = ganadoras + nombres[i]
        textos.append("Universidad ganadora: " + ganadoras)

    return textos


#entradas: listas de deportistas, universidades e inscripciones
#salidas: textos con nombre del deportista, universidad, país y disciplinas en las que participa
#procedimiento: recorrer deportistas, buscar el país de su universidad y unir las disciplinas de sus inscripciones.
def consultar_deportistas_participantes(listadeportistas, listauniversidades, listainscripciones):
    textos = []

    for i in range(len(listadeportistas)):
        deportista = listadeportistas[i]
        nombre_universidad = deportista["universidad"]
        pais = "Sin país"

        for j in range(len(listauniversidades)):
            if listauniversidades[j]["nombre"].lower().strip() == nombre_universidad.lower().strip():
                pais = listauniversidades[j]["pais"]

        disciplinas_texto = ""
        for j in range(len(listainscripciones)):
            inscripcion = listainscripciones[j]
            if inscripcion["tipodoc"].strip() == deportista["tipodoc"].strip() and inscripcion["documento"].strip() == deportista["documento"].strip():
                if len(disciplinas_texto) > 0:
                    disciplinas_texto = disciplinas_texto + ", "
                disciplinas_texto = disciplinas_texto + inscripcion["disciplina"]

        if len(disciplinas_texto) == 0:
            disciplinas_texto = "Sin disciplinas"

        texto = deportista["nombre"] + " | " + nombre_universidad + " | " + pais + " | " + disciplinas_texto
        textos.append(texto)

    return textos


#entradas: listas de universidades, deportistas, disciplinas, inscripciones y resultados
#salidas: estadísticas generales de la Copa Loyola
#procedimiento: contar universidades nacionales e internacionales y mostrar el total de registros de cada lista.
def consultar_estadisticas_generales(listauniversidades, listadeportistas, listadisciplinas, listainscripciones, listaresultados):
    nacionales = 0
    internacionales = 0

    for i in range(len(listauniversidades)):
        tipo = listauniversidades[i]["tipo"].lower().strip()
        if tipo == "nacional":
            nacionales = nacionales + 1
        elif tipo == "internacional":
            internacionales = internacionales + 1

    textos = []
    textos.append("Universidades: " + str(len(listauniversidades)))
    textos.append("Nacionales: " + str(nacionales) + " | Internacionales: " + str(internacionales))
    textos.append("Deportistas: " + str(len(listadeportistas)) + " | Disciplinas: " + str(len(listadisciplinas)))
    textos.append("Inscripciones: " + str(len(listainscripciones)) + " | Medallas: " + str(len(listaresultados)))
    return textos
