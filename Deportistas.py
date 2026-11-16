#entradas: por parametro nombre documento universidad disciplina y lista de deportistas
#salidas: true o false con mensaje de exito o error respectivamente
#procedimiento: Primero validar que los campos esten llenos, cuenta cuantas letras hay en cada uno, si es igual a 0 retorna false y un 
#mensaje de error. Luego valida que no hayan duplicados. 
#si duplicado es igual a true entonces retorna false y el mensaje de error
#Si todo sale bien llega al final del codigo y guarda cada dato en la lista. 

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

    #Validar que no hayan duplicados (mismo tipo y número de documento)
    for i in range(len(listadeportistas)):
        if listadeportistas[i]["tipodoc"] == tipodoc and listadeportistas[i]["documento"] == documento:
            return False, "Ya existe un deportista registrado con ese documento."

    #Registro deportista nuevo
    nuevodeportista = {"nombre": nombre, "tipodoc": tipodoc, "documento": documento, "universidad": nombreuniversidad}
    listadeportistas.append(nuevodeportista)
    return True, "Deportista registrado con éxito"

#---------------------------------------------
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


#----------------------------------------------
#entradas: nombre a buscar, datos a cambiar (pais, ciudad,tipo)
 #salidas: true o false mensaje respectivo de exito o error
 #proceedimiento: pasar por parametro entradas, al igual que el registro validar espacios para que no cuenten y pasen como si hubiera algo escrito
 #en los campos, evitar que queden campos vacios, si sucede lanzar error, luego validar que se escriba uno de los dos tipos. 
 #Pasar a buscar si existe el nombre de la universidad que se quiere actualizar, si nombre en lista es igual a nombre buscar entonces actualizar datos.
 #Si se logra actualizar retornar true, mensaje de exito. De lo contrario False, Mensaje error.

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

#-----------------------------------------------------
#entradas:tipo de documento a buscar y documento a buscar
#salidas: true/false mensaje respectivo
#procedimiento: Verificar que no falten campos, no admitir espacios. Dentro del rango de la lista de deportistas si tipo de doc y 
# documento son iguales que los valores que se buscan, entonces verificar que el deportista no tenga iinscripciones, retornar false 
#si tiene y si no eliminar diccionario. Devolver true o false y mensaje.

#Diagrama de flujo D2.4
def borrardeportista(tipodocbuscar, documentobuscar, listadeportistas, listainscripciones):

    tipodocbuscar = tipodocbuscar.strip()
    documentobuscar = documentobuscar.strip()

    if len(tipodocbuscar)==0 or len(documentobuscar)==0:
        return False, "El campo de búsqueda no puede estar vacío."

    eliminado = False
    for i in range(len(listadeportistas)):
        if listadeportistas[i]["tipodoc"] == tipodocbuscar and listadeportistas[i]["documento"] == documentobuscar:
            #Validar que no tenga inscripciones
            for j in range(len(listainscripciones)):
                if listainscripciones[j]["tipodoc"] == tipodocbuscar and listainscripciones[j]["documento"] == documentobuscar:
                    return False, "No se puede eliminar: el deportista tiene inscripciones."
            listadeportistas.pop(i)
            eliminado = True
            break

    if eliminado == True:
        return True, "Deportista eliminado con éxito."
    else:
        return False, "El deportista no está registrado."


   