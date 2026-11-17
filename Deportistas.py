#entradas: nombre completo, tipo de documento, número de documento, universidad, lista de deportistas y lista de universidades
#salidas: True y mensaje de éxito si registra, o False y mensaje de error
#procedimiento: validar que los campos estén llenos. Verificar que la universidad exista y que no haya otro deportista
#con el mismo número de documento. Si todo sale bien, guardar el nuevo deportista en la lista.

#Diagrama de flujo D2.1

def registrardeportista(nombre, tipodoc, documento, universidad, listadeportistas, listauniversidades):

    nombre = nombre.strip()
    tipodoc = tipodoc.strip()
    documento = documento.strip()
    universidad = universidad.strip()

    #Validar que se llenen todos los campos
    if len(nombre)==0 or len(tipodoc)==0 or len(documento)==0 or len(universidad)==0:
        return False, "Todos los campos son obligatorios."

    #Validar que la universidad esté registrada
    existe = False
    nombreuniversidad = ""
    for i in range(len(listauniversidades)):
        if listauniversidades[i]["nombre"].lower() == universidad.lower():
            existe = True
            nombreuniversidad = listauniversidades[i]["nombre"]
    if existe == False:
        return False, "La universidad no está registrada."

    #Validar que no hayan duplicados (mismo número de documento)
    for i in range(len(listadeportistas)):
        if listadeportistas[i]["documento"] == documento:
            return False, "Ya existe un deportista registrado con ese documento."

    #Registro deportista nuevo
    nuevodeportista = {"nombre": nombre, "tipodoc": tipodoc, "documento": documento, "universidad": nombreuniversidad}
    listadeportistas.append(nuevodeportista)
    return True, "Deportista registrado con éxito"

#entradas: lista de deportistas
#salidas: lista de deportistas con formato diferente para mostrar en la interfaz
#procedimiento: crear lista nueva, para i en el rango de la cantidad de deportistas, individualmente 
#asignar al deportista actual el nombre de deportistaactual.
#para crear el texto presentable, ponerle a i+1 (porque empieza en 0), un punto para que quede por ejemplo 1. 
#el nombre del deportista, un separador y su numero de documento
#Agregar nuevo texto al final de la lista nueva y retornar el resultado

#Diagrama de flujo D2.2

def enumerardeportistas(listadeportistas):
    resultado = []
    for i in range(len(listadeportistas)):
        #Se coge una persona de la lista y se le asigna un nombre corto para facilidad
        deportistaactual = listadeportistas[i]
#(Texto en formato presentable)
        texto = str(i+1) + ". " + deportistaactual["nombre"] + " | " + deportistaactual["tipodoc"] + " " + deportistaactual["documento"] + " | " + deportistaactual["universidad"]
        resultado.append(texto)
    return resultado


#entradas: tipo de documento, número de documento, nuevo nombre, nueva universidad, lista de deportistas y lista de universidades
#salidas: True y mensaje de éxito si actualiza, o False y mensaje de error
#procedimiento: validar los campos y comprobar que la nueva universidad exista. Recorrer la lista buscando el deportista
#por tipo y número de documento. Si se encuentra, actualizar el nombre y la universidad.

#Diagrama de flujo D2.3
def actualizardeportista(tipodocbuscar, documentobuscar, nnombre, nuniversidad, listadeportistas, listauniversidades):

    tipodocbuscar = tipodocbuscar.strip()
    documentobuscar = documentobuscar.strip()
    nnombre = nnombre.strip()
    nuniversidad = nuniversidad.strip()

    #Validar que se llenen todos los campos
    if len(tipodocbuscar)==0 or len(documentobuscar)==0 or len(nnombre)==0 or len(nuniversidad)==0:
        return False, "Todos los campos son obligatorios."

    #Validar que la nueva universidad esté registrada
    existe = False
    nombreuniversidad = ""
    for i in range(len(listauniversidades)):
        if listauniversidades[i]["nombre"].lower() == nuniversidad.lower():
            existe = True
            nombreuniversidad = listauniversidades[i]["nombre"]
    if existe == False:
        return False, "La universidad no está registrada."

    #Buscar al deportista por tipo y número de documento
    actualizado = False
    for i in range(len(listadeportistas)):
        if listadeportistas[i]["tipodoc"] == tipodocbuscar and listadeportistas[i]["documento"] == documentobuscar:
            depact = listadeportistas[i]
            depact["nombre"] = nnombre
            depact["universidad"] = nombreuniversidad
            actualizado = True

    if actualizado == True:
        return True, "Deportista actualizado con éxito."
    else:
        return False, "El deportista no está registrado."

#entradas:tipo de documento a buscar y documento a buscar
#salidas: true/false mensaje respectivo
#procedimiento: Verificar que no falten campos. Dentro del rango de la lista de deportistas, si tipo de documento y
#documento son iguales que los valores que se buscan, verificar que el deportista no tenga inscripciones, retornar false
#si tiene y si no eliminar diccionario. Devolver true o false y mensaje.

#Diagrama de flujo D2.4
def borrardeportista(tipodocbuscar, documentobuscar, listadeportistas, listainscripciones):

    tipodocbuscar = tipodocbuscar.strip()
    documentobuscar = documentobuscar.strip()

    if len(tipodocbuscar)==0 or len(documentobuscar)==0:
        return False, "El campo de búsqueda no puede estar vacío."

    eliminado = False
    for i in range(len(listadeportistas)):
        if eliminado == False and listadeportistas[i]["tipodoc"] == tipodocbuscar and listadeportistas[i]["documento"] == documentobuscar:
            #Validar que no tenga inscripciones
            for j in range(len(listainscripciones)):
                if listainscripciones[j]["tipodoc"] == tipodocbuscar and listainscripciones[j]["documento"] == documentobuscar:
                    return False, "No se puede eliminar: el deportista tiene inscripciones."
            listadeportistas.pop(i)
            eliminado = True

    if eliminado == True:
        return True, "Deportista eliminado con éxito."
    else:
        return False, "El deportista no está registrado."
