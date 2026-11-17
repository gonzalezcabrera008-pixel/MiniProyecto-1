#entradas: nombre, modalidad y lista de disciplinas
#salidas: true o false con mensaje de exito o error respectivamente
#procedimiento: Primero validar que los campos esten llenos, cuenta cuantas letras hay en cada uno, si es igual a 0 retorna false y un 
#mensaje de error. Luego valida que la modalidad sea individual o por equipos. Despues valida que no hayan duplicados,
#recorriendo la lista y comparando nombres. Si duplicado es igual a true retorna false y el mensaje de error.
#Si todo sale bien llega al final del codigo y guarda cada dato en la lista.
  
#Diagrama de flujo D3.1.

def registrardisciplina(nombre, modalidad, listadisciplinas):

    nombre = nombre.strip()
    modalidad = modalidad.strip()

    #Validar que se llenen todos los campos
    if len(nombre)==0 or len(modalidad)==0:
        return False, "Todos los campos son obligatorios."

    #Validar que la modalidad sea individual o por equipos
    if modalidad.lower()!="individual" and modalidad.lower()!="por equipos":
        return False, "La modalidad debe ser Individual o Por equipos."

    #Validar que no hayan duplicados
    duplicado = False
    for i in range(len(listadisciplinas)):
        if listadisciplinas[i]["nombre"].lower() == nombre.lower():
            duplicado = True

    if duplicado == True:
        return False, "Ya existe una disciplina registrada con ese nombre."

    #Registro disciplina nueva (si todo salio bien)
    nuevadisciplina = {"nombre": nombre, "modalidad": modalidad}
    listadisciplinas.append(nuevadisciplina)
    return True, "Disciplina registrada con éxito"

#---------------------------------------------
#entradas: lista de disciplinas
#salidas: lista de disciplinas con formato diferente para mostrar en la interfaz
#procedimiento: crear lista nueva, para i en el rango de la cantidad de disciplinas, individualmente 
#asignar a la disciplina actual el nombre de disciplinaactual.
#para crear el texto presentable, ponerle a i+1 (porque empieza en 0), un punto para que quede por ejemplo 1. 
#el nombre de la disciplina, un separador y su modalidad.
#Agregar nuevo texto al final de la lista nueva y retornar el resultado

#Diagrama de flujo D3.2

def enumerardisciplinas(listadisciplinas):
    resultado = []
    for i in range(len(listadisciplinas)):
        #Se coge una disciplina de la lista y se le asigna un nombre corto para facilidad
        disciplinaactual = listadisciplinas[i]
        #(Texto en formato presentable)
        texto = str(i+1) + ". " + disciplinaactual["nombre"] + " | " + disciplinaactual["modalidad"]
        resultado.append(texto)
    return resultado

#---------------------------------------------
#entradas: nombre de la disciplina a eliminar, lista de disciplinas, lista de inscripciones y lista de resultados
#salidas: true/false con mensaje respectivo
#procedimiento: Verificar que el campo no este vacio, quitar espacios. Recorrer la lista de disciplinas buscando el nombre y 
#guardar su posicion con una bandera. Si no se encuentra retornar false. Si se encuentra, verificar que no tenga inscripciones ni 
#resultados asociados, retornar false si tiene. Si no tiene, eliminar la disciplina por su posicion y retornar true.

#Diagrama de flujo D3.3



def borrardisciplina(nombrebuscar, listadisciplinas, listainscripciones, listaresultados):

    nombrebuscar = nombrebuscar.strip()

    if len(nombrebuscar)==0:
        return False, "El campo de búsqueda no puede estar vacío."

    #Buscar la posición de la disciplina (sin borrar todavía)
    encontrado = False
    posicion= 0
    for i in range(len(listadisciplinas)):
        if listadisciplinas[i]["nombre"].lower() == nombrebuscar.lower():
            encontrado = True
            posicion= i
            
    if encontrado == False:
        return False, "La disciplina no está registrada."

    #Validar que no tenga inscripciones
    for j in range(len(listainscripciones)):
        if listainscripciones[j]["disciplina"].lower() == nombrebuscar.lower():
            return False, "No se puede eliminar: la disciplina tiene inscripciones."

    #Validar que no tenga resultados
    for k in range(len(listaresultados)):
        if listaresultados[k]["disciplina"].lower() == nombrebuscar.lower():
            return False, "No se puede eliminar: la disciplina tiene resultados registrados."

    listadisciplinas.pop(i)
    return True, "Disciplina eliminada con éxito."
