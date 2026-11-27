# pruebas_reportes.py
# Pruebas de generar_medallero_csv (Reportes.py). Incluye casos "de ataque":
# entradas vacías, mal formadas, rutas inválidas y nombres con caracteres raros.
# Ejecutar con:  python pruebas_reportes.py
import csv
import csv
import pandas as pd
from Reportes import (
    generar_medallero_csv,
    crear_dataframe_resultados,
    calcular_medallas_por_universidad,
    calcular_puntos,
    identificar_universidad_ganadora,
)

# Entradas: ruta (texto con la ruta de un archivo de texto)
# Salidas: lista con las líneas del archivo, sin el salto de línea final
# Procedimientos: se abre el archivo, se leen todas las líneas y se recorren por
# índices quitando los caracteres de salto de línea de cada una.
def leer_lineas(ruta):
    with open(ruta, "r", encoding="utf-8-sig") as archivo:
        crudas = archivo.readlines()
    lineas = []
    for i in range(len(crudas)):
        lineas.append(crudas[i].rstrip("\r\n"))
    return lineas


# Entradas: ruta (texto con la ruta de un archivo csv)
# Salidas: matriz (lista de filas) con el contenido leído con el módulo csv
# Procedimientos: se abre el archivo y el lector csv separa cada línea en sus
# columnas, respetando las comillas de los textos con comas.
def leer_filas_csv(ruta):
    with open(ruta, "r", newline="", encoding="utf-8-sig") as archivo:
        filas = list(csv.reader(archivo))
    return filas


# Entradas: ninguna
# Salidas: un texto que dice si todas las pruebas pasaron o cuáles fallaron
# Procedimientos: se ejecuta la función con datos normales y con datos hechos
# para romperla; cada caso que no da lo esperado agrega su nombre a la lista
# "fallos", y al final se arma el texto con el resultado.
def probar_generar_medallero_csv():
    fallos = []
    encabezado = "Universidad,Oro,Plata,Bronce,Puntos"

    universidades = [
        {"nombre": "Javeriana Cali", "pais": "Colombia", "ciudad": "Cali", "tipo": "nacional"},
        {"nombre": "Universidad de los Andes", "pais": "Colombia", "ciudad": "Bogotá", "tipo": "nacional"},
        {"nombre": "Universidad de Lima", "pais": "Perú", "ciudad": "Lima", "tipo": "internacional"},
        {"nombre": "Universidad de Chile", "pais": "Chile", "ciudad": "Santiago", "tipo": "internacional"},
    ]
    resultados = [
        {"disciplina": "Natación", "universidad": "Javeriana Cali", "posicion": "Oro"},
        {"disciplina": "Natación", "universidad": "Universidad de Lima", "posicion": "Plata"},
        {"disciplina": "Natación", "universidad": "Universidad de los Andes", "posicion": "Bronce"},
        {"disciplina": "Atletismo", "universidad": "Universidad de Lima", "posicion": "Oro"},
        {"disciplina": "Atletismo", "universidad": "Javeriana Cali", "posicion": "Plata"},
    ]

    # Caso 1: datos normales (la universidad sin medallas también aparece)
    respuesta = generar_medallero_csv(universidades, resultados, "prueba_normal.csv")
    lineas = leer_lineas("prueba_normal.csv")
    if respuesta[0] != True or len(lineas) != 5:
        fallos.append("caso 1: datos normales")
    elif lineas[0] != encabezado or lineas[1] != "Javeriana Cali,1,1,0,5" or lineas[2] != "Universidad de los Andes,0,0,1,1":
        fallos.append("caso 1: contenido de las filas")
    elif lineas[3] != "Universidad de Lima,1,1,0,5" or lineas[4] != "Universidad de Chile,0,0,0,0":
        fallos.append("caso 1: filas finales o universidad con 0 medallas")

    # Caso 2: las dos listas vacías -> archivo solo con encabezados, sin romperse
    respuesta = generar_medallero_csv([], [], "prueba_vacio.csv")
    lineas = leer_lineas("prueba_vacio.csv")
    if respuesta[0] != True or len(lineas) != 1 or lineas[0] != encabezado:
        fallos.append("caso 2: listas vacías")

    # Caso 3: resultados sin universidades registradas -> solo encabezados
    respuesta = generar_medallero_csv([], resultados, "prueba_sin_universidades.csv")
    lineas = leer_lineas("prueba_sin_universidades.csv")
    if respuesta[0] != True or len(lineas) != 1:
        fallos.append("caso 3: resultados sin universidades")

    # Caso 4: mayúsculas y espacios distintos entre universidad y resultado
    uni_raras = [{"nombre": "  javeriana CALI "}]
    res_raros = [
        {"disciplina": "X", "universidad": "Javeriana Cali", "posicion": "  ORO "},
        {"disciplina": "Y", "universidad": "JAVERIANA cali  ", "posicion": "plata"},
    ]
    respuesta = generar_medallero_csv(uni_raras, res_raros, "prueba_espacios.csv")
    lineas = leer_lineas("prueba_espacios.csv")
    if respuesta[0] != True or len(lineas) != 2 or lineas[1] != "  javeriana CALI ,1,1,0,5":
        fallos.append("caso 4: mayúsculas y espacios")

    # Caso 5: una posición que no es oro, plata ni bronce se ignora
    res_cobre = [{"disciplina": "X", "universidad": "Javeriana Cali", "posicion": "Cobre"}]
    respuesta = generar_medallero_csv(universidades, res_cobre, "prueba_cobre.csv")
    lineas = leer_lineas("prueba_cobre.csv")
    if respuesta[0] != True or lineas[1] != "Javeriana Cali,0,0,0,0":
        fallos.append("caso 5: posición desconocida")

    # Caso 6: entradas que no son listas
    if generar_medallero_csv(None, [], "prueba_x.csv") != (False, "Los datos del medallero deben ser listas."):
        fallos.append("caso 6a: universidades None")
    if generar_medallero_csv([], "texto", "prueba_x.csv") != (False, "Los datos del medallero deben ser listas."):
        fallos.append("caso 6b: resultados es un texto")
    if generar_medallero_csv(None, None, "prueba_x.csv")[0] != False:
        fallos.append("caso 6c: las dos son None")

    # Caso 7: un registro que no es diccionario
    respuesta = generar_medallero_csv(["texto"], resultados, "prueba_x.csv")
    if respuesta[0] != False or respuesta[1] != "Estructura inválida: algún registro no es un diccionario o tiene un valor que no es texto.":
        fallos.append("caso 7a: universidad que es un texto")
    respuesta = generar_medallero_csv(universidades, [5], "prueba_x.csv")
    if respuesta[0] != False:
        fallos.append("caso 7b: resultado que es un número")

    # Caso 8: falta una llave
    respuesta = generar_medallero_csv([{"pais": "Perú"}], [], "prueba_x.csv")
    if respuesta != (False, "Estructura inválida: falta la llave 'nombre' en algún registro."):
        fallos.append("caso 8a: falta la llave nombre")
    respuesta = generar_medallero_csv(universidades, [{"universidad": "Javeriana Cali"}], "prueba_x.csv")
    if respuesta != (False, "Estructura inválida: falta la llave 'posicion' en algún registro."):
        fallos.append("caso 8b: falta la llave posicion")

    # Caso 9: un valor que no es texto
    respuesta = generar_medallero_csv(universidades, [{"universidad": "Javeriana Cali", "posicion": None}], "prueba_x.csv")
    if respuesta[0] != False:
        fallos.append("caso 9: posicion es None")

    # Caso 10: rutas inválidas (carpeta que no existe, ruta que es una carpeta, ruta None)
    respuesta = generar_medallero_csv(universidades, resultados, "carpeta_que_no_existe/prueba.csv")
    if respuesta[0] != False:
        fallos.append("caso 10a: carpeta inexistente")
    respuesta = generar_medallero_csv(universidades, resultados, ".")
    if respuesta[0] != False:
        fallos.append("caso 10b: la ruta es una carpeta")
    respuesta = generar_medallero_csv(universidades, resultados, None)
    if respuesta != (False, "La ruta del archivo no es válida."):
        fallos.append("caso 10c: ruta None")

    # Caso 11: nombre con coma, comillas y salto de línea (el módulo csv debe entrecomillarlos)
    uni_csv = [
        {"nombre": 'Universidad, "Lima"'},
        {"nombre": "Uni\nversidad"},
    ]
    respuesta = generar_medallero_csv(uni_csv, [], "prueba_caracteres.csv")
    filas = leer_filas_csv("prueba_caracteres.csv")
    if respuesta[0] != True or len(filas) != 3:
        fallos.append("caso 11: cantidad de filas con caracteres raros")
    elif filas[1][0] != 'Universidad, "Lima"' or filas[2][0] != "Uni\nversidad" or len(filas[1]) != 5:
        fallos.append("caso 11: el nombre no se recuperó igual")

    # Caso 12: tildes y eñes, y que el archivo lleve la marca BOM para que Excel las muestre bien
    uni_tildes = [{"nombre": "Universidad Católica del Perú"}, {"nombre": "Pontificia Universidad Javeriana – Bogotá"}]
    respuesta = generar_medallero_csv(uni_tildes, [], "prueba_tildes.csv")
    lineas = leer_lineas("prueba_tildes.csv")
    with open("prueba_tildes.csv", "rb") as archivo:
        primeros_bytes = archivo.read(3)
    if respuesta[0] != True or lineas[1] != "Universidad Católica del Perú,0,0,0,0":
        fallos.append("caso 12: tildes")
    if primeros_bytes != b"\xef\xbb\xbf":
        fallos.append("caso 12: falta la marca BOM utf-8-sig")

    # Caso 13: la función se llama como la usará la interfaz (solo 2 parámetros) y crea medallero.csv
    respuesta = generar_medallero_csv(universidades, resultados)
    if respuesta != (True, "Medallero exportado a medallero.csv con 4 universidades."):
        fallos.append("caso 13: llamada con 2 parámetros")

    if len(fallos) == 0:
        return "Todas las pruebas pasaron"
    texto = "Fallaron:"
    for i in range(len(fallos)):
        texto = texto + " | " + fallos[i]
    return texto


# Entradas: ninguna
# Salidas: un texto que dice si todas las pruebas de crear_dataframe_resultados
# pasaron o cuáles fallaron
# Procedimientos: se ejecuta la función con resultados normales y con datos hechos
# para romperla (vacíos, mal formados, medallas raras, textos con espacios); cada
# caso que no da lo esperado agrega su nombre a la lista "fallos".
def probar_crear_dataframe_resultados():
    fallos = []
    columnas = ["Universidad", "Disciplina", "Medalla"]
    mensaje_estructura = "Estructura inválida: algún resultado no es un diccionario o tiene un valor que no es texto."
    resultados = [
        {"disciplina": "Natación", "universidad": "Javeriana Cali", "posicion": "Oro"},
        {"disciplina": "Natación", "universidad": "Universidad de Lima", "posicion": "Plata"},
        {"disciplina": "Natación", "universidad": "Universidad de los Andes", "posicion": "Bronce"},
        {"disciplina": "Atletismo", "universidad": "Universidad de Lima", "posicion": "Oro"},
        {"disciplina": "Atletismo", "universidad": "Javeriana Cali", "posicion": "Plata"},
    ]

    # Caso 1: datos normales
    respuesta = crear_dataframe_resultados(resultados)
    if respuesta[0] != True:
        fallos.append("caso 1: datos normales")
    else:
        df = respuesta[1]
        if list(df.columns) != columnas or len(df) != 5:
            fallos.append("caso 1: columnas o cantidad de filas")
        elif df.iloc[0, 0] != "Javeriana Cali" or df.iloc[0, 1] != "Natación" or df.iloc[0, 2] != "Oro":
            fallos.append("caso 1: valores de la primera fila")
        elif df.iloc[4, 0] != "Javeriana Cali" or df.iloc[4, 1] != "Atletismo" or df.iloc[4, 2] != "Plata":
            fallos.append("caso 1: valores de la última fila")

    # Caso 2: lista vacía
    if crear_dataframe_resultados([]) != (False, "No hay resultados registrados para generar el reporte."):
        fallos.append("caso 2: lista vacía")

    # Caso 3: lo recibido no es una lista
    if crear_dataframe_resultados(None) != (False, "Los resultados deben ser una lista."):
        fallos.append("caso 3a: None")
    if crear_dataframe_resultados("texto") != (False, "Los resultados deben ser una lista."):
        fallos.append("caso 3b: un texto")
    if crear_dataframe_resultados({"universidad": "A"}) != (False, "Los resultados deben ser una lista."):
        fallos.append("caso 3c: un diccionario")

    # Caso 4: espacios y mayúsculas; además la lista original no se debe modificar
    raros = [{"disciplina": " X ", "universidad": " Javeriana Cali ", "posicion": "  ORO "}]
    respuesta = crear_dataframe_resultados(raros)
    if respuesta[0] != True:
        fallos.append("caso 4: espacios y mayúsculas")
    elif respuesta[1].iloc[0, 0] != "Javeriana Cali" or respuesta[1].iloc[0, 1] != "X" or respuesta[1].iloc[0, 2] != "Oro":
        fallos.append("caso 4: no limpió los textos")
    if raros[0]["posicion"] != "  ORO " or raros[0]["universidad"] != " Javeriana Cali ":
        fallos.append("caso 4: modificó la lista original")

    # Caso 5: una medalla inválida se ignora y la válida se conserva
    mezcla = [
        {"disciplina": "X", "universidad": "Javeriana Cali", "posicion": "Oro"},
        {"disciplina": "X", "universidad": "Universidad de Lima", "posicion": "Cobre"},
    ]
    respuesta = crear_dataframe_resultados(mezcla)
    if respuesta[0] != True or len(respuesta[1]) != 1:
        fallos.append("caso 5: medalla inválida mezclada con una válida")

    # Caso 6: ninguna medalla válida
    solo_cobre = [{"disciplina": "X", "universidad": "Javeriana Cali", "posicion": "Cobre"}]
    if crear_dataframe_resultados(solo_cobre) != (False, "Ningún resultado tiene una medalla válida (Oro, Plata o Bronce)."):
        fallos.append("caso 6: ninguna medalla válida")

    # Caso 7: registros que no son diccionarios
    if crear_dataframe_resultados([5]) != (False, mensaje_estructura):
        fallos.append("caso 7a: un número")
    if crear_dataframe_resultados(["texto"]) != (False, mensaje_estructura):
        fallos.append("caso 7b: un texto")
    if crear_dataframe_resultados([None]) != (False, mensaje_estructura):
        fallos.append("caso 7c: None")

    # Caso 8: falta una llave
    sin_disciplina = [{"universidad": "A", "posicion": "Oro"}]
    if crear_dataframe_resultados(sin_disciplina) != (False, "Estructura inválida: falta la llave 'disciplina' en algún resultado."):
        fallos.append("caso 8a: falta la llave disciplina")
    sin_posicion = [{"universidad": "A", "disciplina": "X"}]
    if crear_dataframe_resultados(sin_posicion) != (False, "Estructura inválida: falta la llave 'posicion' en algún resultado."):
        fallos.append("caso 8b: falta la llave posicion")

    # Caso 9: un valor que no es texto
    posicion_none = [{"universidad": "A", "disciplina": "X", "posicion": None}]
    if crear_dataframe_resultados(posicion_none) != (False, mensaje_estructura):
        fallos.append("caso 9a: posicion es None")
    posicion_numero = [{"universidad": "A", "disciplina": "X", "posicion": 1}]
    if crear_dataframe_resultados(posicion_numero) != (False, mensaje_estructura):
        fallos.append("caso 9b: posicion es un número")

    # Caso 10: muchos resultados (2000) no rompen la función
    grande = []
    for i in range(2000):
        grande.append({"disciplina": "D" + str(i), "universidad": "U" + str(i), "posicion": "Bronce"})
    respuesta = crear_dataframe_resultados(grande)
    if respuesta[0] != True or len(respuesta[1]) != 2000:
        fallos.append("caso 10: 2000 resultados")

    if len(fallos) == 0:
        return "Todas las pruebas pasaron"
    texto = "Fallaron:"
    for i in range(len(fallos)):
        texto = texto + " | " + fallos[i]
    return texto

# Entradas: ninguna
# Salidas: texto indicando si todas las pruebas pasaron o cuáles fallaron
# Procedimientos: ejecuta calcular_medallas_por_universidad con casos normales y
# casos límite (sin plata/bronce, un solo dato, DataFrame vacío, None, tipos
# erróneos, columnas faltantes, tildes/comas y celdas corruptas) acumulando fallos.
def probar_calcular_medallas_por_universidad():
    fallos = []

    # Caso 1: datos normales
    df_normal = pd.DataFrame([
        {"Universidad": "Javeriana Cali", "Disciplina": "Natación", "Medalla": "Oro"},
        {"Universidad": "Javeriana Cali", "Disciplina": "Atletismo", "Medalla": "Plata"},
        {"Universidad": "Universidad de Lima", "Disciplina": "Natación", "Medalla": "Bronce"},
    ])
    ok, res = calcular_medallas_por_universidad(df_normal)
    if ok != True or list(res.columns) != ["Universidad", "Oro", "Plata", "Bronce"] or len(res) != 2:
        fallos.append("caso 1: estructura o columnas normales")
    else:
        fila_jav = res[res["Universidad"] == "Javeriana Cali"].iloc[0]
        if int(fila_jav["Oro"]) != 1 or int(fila_jav["Plata"]) != 1 or int(fila_jav["Bronce"]) != 0:
            fallos.append("caso 1: conteo Javeriana")

    # Caso 2: universidad solo con Oro (no existen filas de Plata ni Bronce)
    df_solo_oro = pd.DataFrame([
        {"Universidad": "Javeriana Cali", "Disciplina": "Natación", "Medalla": "Oro"},
    ])
    ok, res = calcular_medallas_por_universidad(df_solo_oro)
    if ok != True or list(res.columns) != ["Universidad", "Oro", "Plata", "Bronce"]:
        fallos.append("caso 2: reindex sin Plata ni Bronce")
    elif int(res.iloc[0]["Oro"]) != 1 or int(res.iloc[0]["Plata"]) != 0 or int(res.iloc[0]["Bronce"]) != 0:
        fallos.append("caso 2: relleno con 0 o tipo int")

    # Caso 3: DataFrame vacío
    df_vacio = pd.DataFrame(columns=["Universidad", "Disciplina", "Medalla"])
    ok, msg = calcular_medallas_por_universidad(df_vacio)
    if ok != False or msg != "No hay resultados para calcular el medallero.":
        fallos.append("caso 3: DataFrame vacío")

    # Caso 4: None y tipos incorrectos
    if calcular_medallas_por_universidad(None)[0] != False:
        fallos.append("caso 4a: entrada None")
    if calcular_medallas_por_universidad([{"Universidad": "X", "Medalla": "Oro"}])[0] != False:
        fallos.append("caso 4b: entrada lista en vez de DataFrame")
    if calcular_medallas_por_universidad("texto")[0] != False:
        fallos.append("caso 4c: entrada texto")

    # Caso 5: columnas faltantes
    df_sin_medalla = pd.DataFrame([{"Universidad": "Javeriana Cali", "Disciplina": "Natación"}])
    ok, msg = calcular_medallas_por_universidad(df_sin_medalla)
    if ok != False or msg != "Estructura inválida: falta la columna 'Medalla'.":
        fallos.append("caso 5a: falta columna Medalla")

    df_sin_univ = pd.DataFrame([{"Disciplina": "Natación", "Medalla": "Oro"}])
    ok, msg = calcular_medallas_por_universidad(df_sin_univ)
    if ok != False or msg != "Estructura inválida: falta la columna 'Universidad'.":
        fallos.append("caso 5b: falta columna Universidad")

    # Caso 6: nombres con tildes, eñes y comas
    df_raros = pd.DataFrame([
        {"Universidad": 'Universidad, "Lima"', "Disciplina": "Fútbol", "Medalla": "Oro"},
        {"Universidad": "Universidad Católica del Perú", "Disciplina": "Natación", "Medalla": "Plata"},
    ])
    ok, res = calcular_medallas_por_universidad(df_raros)
    if ok != True or len(res) != 2:
        fallos.append("caso 6: nombres con tildes y comas")

    # Caso 7: celdas con valores nulos o corruptos
    df_nulos = pd.DataFrame([{"Universidad": None, "Disciplina": "Natación", "Medalla": None}])
    if calcular_medallas_por_universidad(df_nulos)[0] != False:
        fallos.append("caso 7a: filas con None")

    df_corrupto = pd.DataFrame([{"Universidad": ["lista"], "Disciplina": "Natación", "Medalla": "Oro"}])
    if calcular_medallas_por_universidad(df_corrupto)[0] != False:
        fallos.append("caso 7b: celda con objeto no hashable")

    if len(fallos) == 0:
        return "Todas las pruebas de calcular_medallas_por_universidad pasaron"
    texto = "Fallaron:"
    for i in range(len(fallos)):
        texto = texto + " | " + fallos[i]
    return texto

# Entradas: ninguna
# Salidas: texto indicando si todas las pruebas de calcular_puntos pasaron
# Procedimientos: ejecuta calcular_puntos con datos normales, una sola fila,
# DataFrame vacío, None, tipos incorrectos, columnas faltantes y datos no
# numéricos en las medallas, acumulando cualquier fallo encontrado.
def probar_calcular_puntos():
    fallos = []

    # Caso 1: datos normales
    df_medallas = pd.DataFrame([
        {"Universidad": "Javeriana Cali", "Oro": 1, "Plata": 1, "Bronce": 0},
        {"Universidad": "Universidad de los Andes", "Oro": 0, "Plata": 0, "Bronce": 1},
        {"Universidad": "Universidad de Chile", "Oro": 0, "Plata": 0, "Bronce": 0},
    ])
    ok, res = calcular_puntos(df_medallas)
    if ok != True or list(res.columns) != ["Universidad", "Oro", "Plata", "Bronce", "Puntos"]:
        fallos.append("caso 1: columnas de salida")
    elif int(res.iloc[0]["Puntos"]) != 5 or int(res.iloc[1]["Puntos"]) != 1 or int(res.iloc[2]["Puntos"]) != 0:
        fallos.append("caso 1: cálculo de puntos")

    # Caso 2: un solo registro y nombres con tildes/comas
    df_uno = pd.DataFrame([
        {"Universidad": 'Universidad, "Católica del Perú"', "Oro": 2, "Plata": 1, "Bronce": 3},
    ])
    ok, res = calcular_puntos(df_uno)
    if ok != True or int(res.iloc[0]["Puntos"]) != 11:
        fallos.append("caso 2: un solo registro o fórmula 2*3 + 1*2 + 3*1")

    # Caso 3: DataFrame vacío
    df_vacio = pd.DataFrame(columns=["Universidad", "Oro", "Plata", "Bronce"])
    ok, msg = calcular_puntos(df_vacio)
    if ok != False or msg != "No hay datos para calcular los puntos.":
        fallos.append("caso 3: DataFrame vacío")

    # Caso 4: None y tipos incorrectos
    if calcular_puntos(None)[0] != False:
        fallos.append("caso 4a: entrada None")
    if calcular_puntos([{"Universidad": "X", "Oro": 1}])[0] != False:
        fallos.append("caso 4b: entrada lista")
    if calcular_puntos("texto")[0] != False:
        fallos.append("caso 4c: entrada texto")

    # Caso 5: columnas faltantes
    df_sin_bronce = pd.DataFrame([{"Universidad": "Javeriana Cali", "Oro": 1, "Plata": 0}])
    ok, msg = calcular_puntos(df_sin_bronce)
    if ok != False or msg != "Estructura inválida: falta la columna 'Bronce'.":
        fallos.append("caso 5a: falta columna Bronce")

    df_sin_univ = pd.DataFrame([{"Oro": 1, "Plata": 0, "Bronce": 0}])
    ok, msg = calcular_puntos(df_sin_univ)
    if ok != False or msg != "Estructura inválida: falta la columna 'Universidad'.":
        fallos.append("caso 5b: falta columna Universidad")

    # Caso 6: medallas corruptas (texto no numérico o None)
    df_texto = pd.DataFrame([{"Universidad": "Javeriana Cali", "Oro": "tres", "Plata": 1, "Bronce": 0}])
    if calcular_puntos(df_texto)[0] != False:
        fallos.append("caso 6a: medalla con texto")

    df_nulo = pd.DataFrame([{"Universidad": "Javeriana Cali", "Oro": None, "Plata": 1, "Bronce": 0}])
    if calcular_puntos(df_nulo)[0] != False:
        fallos.append("caso 6b: medalla con None")

    if len(fallos) == 0:
        return "Todas las pruebas de calcular_puntos pasaron"
    texto = "Fallaron:"
    for i in range(len(fallos)):
        texto = texto + " | " + fallos[i]
    return texto

# Entradas: ninguna
# Salidas: texto indicando si todas las pruebas de identificar_universidad_ganadora pasaron
# Procedimientos: prueba ganador claro, desempate por oro, desempate por plata,
# desempate por bronce, empate total persistente, una sola universidad, DataFrame
# vacío, None, columnas faltantes y datos corruptos, acumulando cualquier fallo.
def probar_identificar_universidad_ganadora():
    fallos = []

    # Caso 1: ganador claro por puntos
    df_claro = pd.DataFrame([
        {"Universidad": "Universidad de los Andes", "Oro": 0, "Plata": 1, "Bronce": 1, "Puntos": 3},
        {"Universidad": "Javeriana Cali", "Oro": 2, "Plata": 0, "Bronce": 0, "Puntos": 6},
    ])
    ok, res = identificar_universidad_ganadora(df_claro)
    if ok != True or res != "Javeriana Cali (6 puntos)":
        fallos.append("caso 1: ganador claro")

    # Caso 2: empate en puntos desempatado por Oro (ambas con 6 puntos)
    df_empate_oro = pd.DataFrame([
        {"Universidad": "Universidad de Lima", "Oro": 0, "Plata": 3, "Bronce": 0, "Puntos": 6},
        {"Universidad": "Javeriana Cali", "Oro": 2, "Plata": 0, "Bronce": 0, "Puntos": 6},
    ])
    ok, res = identificar_universidad_ganadora(df_empate_oro)
    if ok != True or res != "Javeriana Cali (6 puntos)":
        fallos.append("caso 2: desempate por Oro")

    # Caso 3: empate en puntos y oro, desempatado por Plata (ambas con 5 puntos y 1 oro)
    df_empate_plata = pd.DataFrame([
        {"Universidad": "Universidad de Chile", "Oro": 1, "Plata": 0, "Bronce": 2, "Puntos": 5},
        {"Universidad": "Universidad de Lima", "Oro": 1, "Plata": 1, "Bronce": 0, "Puntos": 5},
    ])
    ok, res = identificar_universidad_ganadora(df_empate_plata)
    if ok != True or res != "Universidad de Lima (5 puntos)":
        fallos.append("caso 3: desempate por Plata")

    # Caso 4: empate total persistente (mismos puntos, oros, platas y bronces)
    df_empate_total = pd.DataFrame([
        {"Universidad": "Javeriana Cali", "Oro": 1, "Plata": 1, "Bronce": 0, "Puntos": 5},
        {"Universidad": "Universidad de Lima", "Oro": 1, "Plata": 1, "Bronce": 0, "Puntos": 5},
        {"Universidad": "Universidad de Chile", "Oro": 0, "Plata": 0, "Bronce": 1, "Puntos": 1},
    ])
    ok, res = identificar_universidad_ganadora(df_empate_total)
    if ok != True or res != "Empate entre: Javeriana Cali, Universidad de Lima (5 puntos)":
        fallos.append("caso 4: empate total persistente")

    # Caso 5: una sola universidad con tildes y comas
    df_una = pd.DataFrame([
        {"Universidad": 'Universidad, "Católica del Perú"', "Oro": 1, "Plata": 0, "Bronce": 0, "Puntos": 3},
    ])
    ok, res = identificar_universidad_ganadora(df_una)
    if ok != True or res != 'Universidad, "Católica del Perú" (3 puntos)':
        fallos.append("caso 5: una sola universidad con caracteres especiales")

    # Caso 6: DataFrame vacío
    df_vacio = pd.DataFrame(columns=["Universidad", "Oro", "Plata", "Bronce", "Puntos"])
    ok, msg = identificar_universidad_ganadora(df_vacio)
    if ok != False or msg != "No hay datos para identificar la universidad ganadora.":
        fallos.append("caso 6: DataFrame vacío")

    # Caso 7: None y tipos incorrectos
    if identificar_universidad_ganadora(None)[0] != False:
        fallos.append("caso 7a: entrada None")
    if identificar_universidad_ganadora([{"Universidad": "X", "Puntos": 3}])[0] != False:
        fallos.append("caso 7b: entrada lista")
    if identificar_universidad_ganadora("texto")[0] != False:
        fallos.append("caso 7c: entrada texto")

    # Caso 8: falta columna Puntos
    df_sin_puntos = pd.DataFrame([{"Universidad": "Javeriana Cali", "Oro": 1, "Plata": 0, "Bronce": 0}])
    ok, msg = identificar_universidad_ganadora(df_sin_puntos)
    if ok != False or msg != "Estructura inválida: falta la columna 'Puntos'.":
        fallos.append("caso 8: falta columna Puntos")

    # Caso 9: datos corruptos (texto en puntos o universidad None)
    df_corrupto = pd.DataFrame([{"Universidad": "Javeriana Cali", "Oro": 1, "Plata": 0, "Bronce": 0, "Puntos": "seis"}])
    if identificar_universidad_ganadora(df_corrupto)[0] != False:
        fallos.append("caso 9a: puntos no numéricos")

    df_uni_none = pd.DataFrame([{"Universidad": None, "Oro": 1, "Plata": 0, "Bronce": 0, "Puntos": 3}])
    if identificar_universidad_ganadora(df_uni_none)[0] != False:
        fallos.append("caso 9b: universidad None")

    if len(fallos) == 0:
        return "Todas las pruebas de identificar_universidad_ganadora pasaron"
    texto = "Fallaron:"
    for i in range(len(fallos)):
        texto = texto + " | " + fallos[i]
    return texto

if __name__ == "__main__":
    print(probar_generar_medallero_csv())
    print(probar_crear_dataframe_resultados())
    print(probar_calcular_medallas_por_universidad())
    print(probar_calcular_puntos())
    print(probar_identificar_universidad_ganadora())