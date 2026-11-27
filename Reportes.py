import csv
import pandas as pd


# Entradas: listauniversidades (lista de diccionarios con la llave "nombre"),
# listaresultados (lista de diccionarios con las llaves "universidad" y "posicion")
# y ruta (texto, opcional; por defecto "medallero.csv")
# Salidas: una tupla (True, mensaje) si el archivo se creó, o (False, mensaje)
# con la descripción del error encontrado
# Procedimientos: 1) Verificar que las dos entradas sean listas. 2) Crear en
# memoria una matriz "filas" cuya primera fila son los encabezados. 3) Por cada
# universidad (ciclo por índices) recorrer los resultados por índices, contar
# oros, platas y bronces con acumuladores y calcular los puntos (3, 2 y 1).
# Cada universidad queda como una fila de la matriz, incluso con 0 medallas.
# 4) Si algún registro tiene una estructura inválida se retorna el error sin
# haber creado ningún archivo. 5) Abrir el archivo y escribir la matriz fila
# por fila con el módulo csv, controlando los errores de escritura.
def generar_medallero_csv(listauniversidades, listaresultados, ruta="medallero.csv"):
    if type(listauniversidades) != list or type(listaresultados) != list:
        return False, "Los datos del medallero deben ser listas."

    filas = []
    filas.append(["Universidad", "Oro", "Plata", "Bronce", "Puntos"])

    try:
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

            puntos = oros * 3 + platas * 2 + bronces
            filas.append([nombre_universidad, oros, platas, bronces, puntos])
    except KeyError as error:
        return False, "Estructura inválida: falta la llave " + str(error) + " en algún registro."
    except (TypeError, AttributeError):
        return False, "Estructura inválida: algún registro no es un diccionario o tiene un valor que no es texto."

    try:
        with open(ruta, "w", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.writer(archivo)
            for i in range(len(filas)):
                escritor.writerow(filas[i])
    except PermissionError:
        return False, "No se pudo escribir " + str(ruta) + ". Si está abierto en Excel u otro programa, ciérralo e inténtalo de nuevo."
    except TypeError:
        return False, "La ruta del archivo no es válida."
    except OSError:
        return False, "No se pudo crear " + str(ruta) + ". Revisa que la carpeta exista y que haya espacio en el disco."

    cantidad = len(filas) - 1
    if cantidad == 0:
        return True, "Medallero exportado a " + ruta + " (no hay universidades registradas; solo se escribieron los encabezados)."
    return True, "Medallero exportado a " + ruta + " con " + str(cantidad) + " universidades."


# Entradas: listaresultados (lista de diccionarios con las llaves "universidad",
# "disciplina" y "posicion")
# Salidas: una tupla. (True, df) donde df es el DataFrame con las columnas
# Universidad, Disciplina y Medalla; o (False, mensaje) con la descripción del problema
# Procedimientos: 1) Verificar que la entrada sea una lista y que no esté vacía.
# 2) Crear tres listas vacías, una por cada columna. 3) Recorrer los resultados por
# índices, quitar los espacios de los textos y conservar solo las medallas válidas
# (Oro, Plata o Bronce); si un registro tiene una estructura inválida se retorna un
# mensaje sin romper el programa. 4) Si no quedó ninguna fila válida, retornar el
# error. 5) Armar el DataFrame con las tres columnas y retornarlo.
def crear_dataframe_resultados(listaresultados):
    if type(listaresultados) != list:
        return False, "Los resultados deben ser una lista."

    if len(listaresultados) == 0:
        return False, "No hay resultados registrados para generar el reporte."

    universidades = []
    disciplinas = []
    medallas = []

    try:
        for i in range(len(listaresultados)):
            resultado_actual = listaresultados[i]
            universidad = resultado_actual["universidad"].strip()
            disciplina = resultado_actual["disciplina"].strip()
            medalla = resultado_actual["posicion"].strip().capitalize()

            if medalla == "Oro" or medalla == "Plata" or medalla == "Bronce":
                universidades.append(universidad)
                disciplinas.append(disciplina)
                medallas.append(medalla)
    except KeyError as error:
        return False, "Estructura inválida: falta la llave " + str(error) + " en algún resultado."
    except (TypeError, AttributeError):
        return False, "Estructura inválida: algún resultado no es un diccionario o tiene un valor que no es texto."

    if len(medallas) == 0:
        return False, "Ningún resultado tiene una medalla válida (Oro, Plata o Bronce)."

    df = pd.DataFrame({"Universidad": universidades, "Disciplina": disciplinas, "Medalla": medallas})
    return True, df

# Entradas: df (DataFrame de Pandas con al menos las columnas "Universidad" y "Medalla")
# Salidas: una tupla (True, df_medallas) con el conteo de Oro, Plata y Bronce por
# universidad como enteros, o (False, mensaje) si hay algún error de estructura
# Procedimientos: 1) Verificar que la entrada sea un DataFrame y no esté vacío.
# 2) Comprobar mediante ciclos por índices y banderas que existan las columnas
# "Universidad" y "Medalla". 3) Agrupar por "Universidad" y "Medalla", contar
# ocurrencias y reorganizar columnas con reindex para garantizar Oro, Plata y
# Bronce en entero (rellenando con 0 las faltantes). 4) Controlar errores con try/except.
def calcular_medallas_por_universidad(df):
    if type(df) != pd.DataFrame:
        return False, "Estructura inválida: se esperaba un DataFrame de Pandas."

    if len(df) == 0:
        return False, "No hay resultados para calcular el medallero."

    columnas_actuales = list(df.columns)
    requeridas = ["Universidad", "Medalla"]
    for i in range(len(requeridas)):
        encontrada = False
        for j in range(len(columnas_actuales)):
            if columnas_actuales[j] == requeridas[i]:
                encontrada = True
        if encontrada == False:
            return False, "Estructura inválida: falta la columna '" + requeridas[i] + "'."

    try:
        tabla = df.groupby(["Universidad", "Medalla"]).size().unstack(fill_value=0)
        if len(tabla) == 0:
            return False, "No hay resultados válidos para calcular el medallero."
        tabla = tabla.reindex(columns=["Oro", "Plata", "Bronce"], fill_value=0)
        tabla = tabla.astype(int).reset_index()
        tabla.columns.name = None
    except (KeyError, TypeError, ValueError, AttributeError):
        return False, "Estructura inválida: los datos del DataFrame no tienen el formato esperado."

    return True, tabla

# Entradas: df_medallas (DataFrame de Pandas con las columnas "Universidad",
# "Oro", "Plata" y "Bronce")
# Salidas: una tupla (True, df_puntos) con la nueva columna "Puntos" calculada
# como Oro*3 + Plata*2 + Bronce*1, o (False, mensaje) si hay error de estructura
# Procedimientos: 1) Verificar que la entrada sea un DataFrame y no esté vacío.
# 2) Validar mediante ciclos por índices y banderas que existan las columnas
# "Universidad", "Oro", "Plata" y "Bronce". 3) Copiar la tabla, asegurar que
# las columnas de medallas sean enteros y calcular la columna "Puntos" con
# operaciones vectorizadas de Pandas. 4) Controlar errores con try/except.
def calcular_puntos(df_medallas):
    if type(df_medallas) != pd.DataFrame:
        return False, "Estructura inválida: se esperaba un DataFrame de Pandas."

    if len(df_medallas) == 0:
        return False, "No hay datos para calcular los puntos."

    columnas_actuales = list(df_medallas.columns)
    requeridas = ["Universidad", "Oro", "Plata", "Bronce"]
    for i in range(len(requeridas)):
        encontrada = False
        for j in range(len(columnas_actuales)):
            if columnas_actuales[j] == requeridas[i]:
                encontrada = True
        if encontrada == False:
            return False, "Estructura inválida: falta la columna '" + requeridas[i] + "'."

    try:
        tabla = df_medallas.copy()
        tabla["Oro"] = tabla["Oro"].astype(int)
        tabla["Plata"] = tabla["Plata"].astype(int)
        tabla["Bronce"] = tabla["Bronce"].astype(int)
        tabla["Puntos"] = tabla["Oro"] * 3 + tabla["Plata"] * 2 + tabla["Bronce"]
        tabla["Puntos"] = tabla["Puntos"].astype(int)
    except (KeyError, TypeError, ValueError, AttributeError):
        return False, "Estructura inválida: las columnas de medallas deben contener números enteros."

    return True, tabla

# Entradas: df_puntos (DataFrame de Pandas con las columnas "Universidad",
# "Oro", "Plata", "Bronce" y "Puntos")
# Salidas: una tupla (True, texto_ganadora) indicando la universidad ganadora
# o el aviso de empate persistente con todas las empatadas, o (False, mensaje)
# si ocurre un error de estructura
# Procedimientos: 1) Validar que la entrada sea un DataFrame no vacío y tenga
# las 5 columnas requeridas mediante ciclos por índices y banderas. 2) Copiar
# la tabla, verificar que no haya universidades nulas y convertir las columnas
# numéricas a entero. 3) Ordenar descendentemente por Puntos, Oro, Plata y
# Bronce con sort_values. 4) Recorrer las filas por índices para recolectar
# todas las universidades empatadas en el primer puesto y armar el texto final.
def identificar_universidad_ganadora(df_puntos):
    if type(df_puntos) != pd.DataFrame:
        return False, "Estructura inválida: se esperaba un DataFrame de Pandas."

    if len(df_puntos) == 0:
        return False, "No hay datos para identificar la universidad ganadora."

    columnas_actuales = list(df_puntos.columns)
    requeridas = ["Universidad", "Oro", "Plata", "Bronce", "Puntos"]
    for i in range(len(requeridas)):
        encontrada = False
        for j in range(len(columnas_actuales)):
            if columnas_actuales[j] == requeridas[i]:
                encontrada = True
        if encontrada == False:
            return False, "Estructura inválida: falta la columna '" + requeridas[i] + "'."

    try:
        tabla = df_puntos.copy()
        if tabla["Universidad"].isnull().any():
            return False, "Estructura inválida: hay registros sin nombre de universidad."

        tabla["Oro"] = tabla["Oro"].astype(int)
        tabla["Plata"] = tabla["Plata"].astype(int)
        tabla["Bronce"] = tabla["Bronce"].astype(int)
        tabla["Puntos"] = tabla["Puntos"].astype(int)

        tabla = tabla.sort_values(
            by=["Puntos", "Oro", "Plata", "Bronce"],
            ascending=False
        ).reset_index(drop=True)

        max_puntos = int(tabla.iloc[0]["Puntos"])
        max_oro = int(tabla.iloc[0]["Oro"])
        max_plata = int(tabla.iloc[0]["Plata"])
        max_bronce = int(tabla.iloc[0]["Bronce"])

        ganadoras = []
        for i in range(len(tabla)):
            fila = tabla.iloc[i]
            mismos_puntos = int(fila["Puntos"]) == max_puntos
            mismos_oros = int(fila["Oro"]) == max_oro
            mismas_platas = int(fila["Plata"]) == max_plata
            mismos_bronces = int(fila["Bronce"]) == max_bronce

            if mismos_puntos and mismos_oros and mismas_platas and mismos_bronces:
                ganadoras.append(str(fila["Universidad"]))

        if len(ganadoras) == 1:
            return True, ganadoras[0] + " (" + str(max_puntos) + " puntos)"

        nombres_empatados = ""
        for i in range(len(ganadoras)):
            if i > 0:
                nombres_empatados = nombres_empatados + ", "
            nombres_empatados = nombres_empatados + ganadoras[i]

        return True, "Empate entre: " + nombres_empatados + " (" + str(max_puntos) + " puntos)"
    except (KeyError, TypeError, ValueError, AttributeError):
        return False, "Estructura inválida: los datos del DataFrame no tienen el formato esperado."

if __name__ == "__main__":
    universidades_demo = [
        {"nombre": "Javeriana Cali", "pais": "Colombia", "ciudad": "Cali", "tipo": "nacional"},
        {"nombre": "Universidad de Lima", "pais": "Perú", "ciudad": "Lima", "tipo": "internacional"},
        {"nombre": "Universidad de Chile", "pais": "Chile", "ciudad": "Santiago", "tipo": "internacional"},
    ]
    resultados_demo = [
        {"disciplina": "Natación", "universidad": "Javeriana Cali", "posicion": "Oro"},
        {"disciplina": "Natación", "universidad": "Universidad de Lima", "posicion": "Plata"},
    ]
    print(generar_medallero_csv(universidades_demo, resultados_demo))
    respuesta_demo = crear_dataframe_resultados(resultados_demo)
    print(respuesta_demo[0])
    print(respuesta_demo[1])
    ok_df, df_demo = crear_dataframe_resultados(resultados_demo)
    if ok_df == True:
        print(calcular_medallas_por_universidad(df_demo))
    if ok_df == True:
        ok_med, df_med_demo = calcular_medallas_por_universidad(df_demo)
        if ok_med == True:
            print(calcular_puntos(df_med_demo))
    if ok_df == True and ok_med == True:
        ok_pts, df_pts_demo = calcular_puntos(df_med_demo)
        if ok_pts == True:
            print(identificar_universidad_ganadora(df_pts_demo))

