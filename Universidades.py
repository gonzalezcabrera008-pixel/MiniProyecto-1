

#entradas: para cada universidad nombre, país, ciudad y tipo de participación (nacional o internacional)
#salidas: True si todo salio bien, de lo contrario False junto con mensaje especificando el error

#procedimiento: Primero validar que los campos estén llenos y que el tipo de participación sea nacional o internacional.
#Luego recorrer la lista de universidades y comparar el nombre para evitar duplicados. Si todo sale bien, guardar los datos
#de la nueva universidad en la lista y retornar True con el mensaje de éxito.

#Diagrama de flujo, D1.1

def registraruniversidad(nombre, pais, ciudad, tipo, listauniversidades):

    #Eliminar espacios para que no cuenten como un campo llenado en caso de llenar el campo con espacios. 
    nombre = nombre.strip()
    pais = pais.strip()
    ciudad = ciudad.strip()
    tipo = tipo.strip()

    #Validar que se llenen todos los campos
    if len(nombre)==0 or len(pais)==0 or len(ciudad)==0 or len(tipo)==0:
        return False, "Todos los campos son obligatorios."

    #Validar que en tipo se escriba nacional o internacional, de lo contrario es un error
    if tipo.lower()!="nacional" and tipo.lower()!= "internacional":
        return False, "El tipo de participación debe ser Internacional o Nacional."

    #Validar que no hayan duplicados
    duplicado=False
    for i in range (len(listauniversidades)):
        if listauniversidades[i]["nombre"].lower().strip() == nombre.lower().strip():
            duplicado=True

    if duplicado==True:
        return False, "Ya existe una universidad registrada con ese nombre"
    
    #Registro universidad nueva (si todo salio bien)
    nuevauniversidad={"nombre": nombre, "pais": pais, "ciudad": ciudad, "tipo": tipo}
    listauniversidades.append(nuevauniversidad)
    return True, "Universidad registrada con éxito"

#entradas: lista universidades
#salidas: lista de universidades con formato diferente para mostrar en la interfaz
#procedimiento: crear lista nueva, para i en el rango de la cantidad de universidades, coger universidad por universidad, individualmente 
#asignar a la universidad actual el nombre de universidadactual.
#para crear el texto presentable, ponerle a i+1 (porque empieza en 0), un punto para que quede por ejemplo 1. 
#el nombre de la universidad, un separador y su pais.
#Agregar nuevo texto al final de la lista nueva y retornar el resultado

#Diagrama de flujo D1.2

def enumeraruniversidades(listauniversidades):
    resultado=[]
    for i in range (len(listauniversidades)):
        #Se coge una universidad de la lista y se le asigna un nombre corto para facilidad
        universidadactual= listauniversidades[i]
        #Para cada universidad se hace el siguiente procedimiento (Texto en formato presentable)
        Texto= str(i+1) + ". " + universidadactual["nombre"] + " | " + universidadactual["pais"]
        resultado.append(Texto)
    return resultado

lista=[{"nombre": "Javeriana","pais": "Colombia","ciudad": "Cali","tipo" : "Nacional"}]
#print (enumeraruniversidades(lista))
 
#entradas: nombre de la universidad a buscar, nuevo país, nueva ciudad, nuevo tipo y lista de universidades
#salidas: True y mensaje de éxito si actualiza, o False y mensaje de error
#procedimiento: validar los campos y el tipo de participación. Recorrer la lista buscando el nombre de la universidad.
#Si se encuentra, actualizar país, ciudad y tipo. Si no se encuentra, retornar False con el mensaje de error.

#Diagrama de flujo D1.3
def actualizaruniversidades(nombrebuscar, npais, nciudad, ntipo, listauniversidades):
    #Eliminar espacios para que no cuenten como un campo llenado en caso de llenar el campo con espacios. 
    nombrebuscar = nombrebuscar.strip()
    npais = npais.strip()
    nciudad = nciudad.strip()
    ntipo = ntipo.strip()

    #Validar que se llenen todos los campos
    if len(nombrebuscar)==0 or len(npais)==0 or len(nciudad)==0 or len(ntipo)==0:
        return False, "Todos los campos son obligatorios."

    #Validar que en tipo se escriba nacional o internacional, de lo contrario es un error
    if ntipo.lower()!="nacional" and ntipo.lower()!= "internacional":
        return False, "El tipo de participación debe ser Internacional o Nacional."

    #Ciclo para encontrar la universidad
    actualizado=False
    for i in range(len(listauniversidades)):
        #comparar nombre actual con el que buscamos
        if actualizado == False and listauniversidades[i]["nombre"].lower().strip()==nombrebuscar.lower().strip():
            #Actualizamos campos dentro de la posicion
            univact=listauniversidades[i]
            univact["pais"]=npais
            univact["ciudad"]=nciudad
            univact["tipo"]=ntipo
            actualizado=True

    if actualizado == True:
        return True, "Universidad actualizada con éxito."
    else:
        return False, "La universidad no esta registrada."
    

#entradas: nombre de la universidad que se desea eliminar
#salidas: true y mensaje de exito, false y mensaje de error
#procedimiento: validar el nombre, recorrer la lista de universidades y buscar la coincidencia. Si se encuentra,
#revisar que no tenga deportistas asociados. Si no tiene deportistas, eliminarla y retornar True.

#Diagrama de flujo D1.4

def borraruniversidad(nombrebuscar, listauniversidades,listadeportistas):
    #limpiar espacios y mayusculas para facilitar busqueda.
    nombrebuscar=nombrebuscar.lower().strip()
    #Verificar que campo de busqueda no este vacio
    if len(nombrebuscar)==0:
        return False, "El campo de busqueda no puede estar vacio."

    #Recorrer lista para encontrar la universidad
    eliminado=False
    for i in range (len(listauniversidades)):
        #buscar si nombre actual es igual a nombre a buscar, quitando mayusculas y espacios para evitar errores
        if eliminado == False and listauniversidades[i]["nombre"].strip().lower()==nombrebuscar.strip().lower():
            for j in range(len(listadeportistas)):
                if listadeportistas[j]["universidad"].lower() == nombrebuscar:
                    return False, "No se puede eliminar: la universidad tiene deportistas"
            #Borrar diccionario en el que estamos parados (i)
            listauniversidades.pop(i)
            eliminado=True
    if eliminado==True:
            return True, "La universidad fue elimninada con éxito."
    else:
            return False, "No se pudo completar la operación."
