

#entradas: para cada universidad nombre, país, ciudad y tipo de participación (nacional o internacional)
#salidas: True si todo salio bien, de lo contrario False junto con mensaje especificando el error

#Procedimiento: Primero validar que los campos esten llenos, cuenta cuantas letras hay en cada uno, si es igual a 0 retorna false y un 
#mensaje de error. Luego valida que no hayan duplicados. Comienza contando cuantas universidades hay y en ese rango entra en cada 
#diccionario con la llave "nombre" compara si es igual o no al nuevo nombre a registrar y guarda true en duplicado si esta duplicado, 
#si duplicado es igual a true entonces retorna false y el mensaje de error
#Si todo sale bien llega al final del codigo y guarda cada dato en la lista. 

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
        if listauniversidades[i]["nombre"].lower().strip() == nombre.lower().strip:
            duplicado=True

    if duplicado==True:
        return False, "Ya existe una universidad registrada con ese nombre"
    
    #Registro universidad nueva (si todo salio bien)
    nuevauniversidad={"nombre": nombre, "pais": pais, "ciudad": ciudad, "tipo": tipo}
    listauniversidades.append(nuevauniversidad)
    return True, "Universidad registrada con éxito"

#-------------------------------------------------------------------------------
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
 
 #----------------------------------------------------------------------------------
 #entradas: nombre a buscar, datos a cambiar (pais, ciudad,tipo)
 #salidas: true o false mensaje respectivo de exito o error
 #proceedimiento: pasar por parametro entradas, al igual que el registro validar espacios para que no cuenten y pasen como si hubiera algo escrito
 #en los campos, evitar que queden campos vacios, si sucede lanzar error, luego validar que se escriba uno de los dos tipos. 
 #Pasar a buscar si existe el nombre de la universidad que se quiere actualizar, si nombre en lista es igual a nombre buscar entonces actualizar datos.
 #Si se logra actualizar retornar true, mensaje de exito. De lo contrario False, Mensaje error.

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
        if listauniversidades[i]["nombre"].lower().strip()==nombrebuscar.lower().strip():
            #Actualizamos campos dentro de la posicion
            univact=listauniversidades[i]
            univact["pais"]=npais
            univact["ciudad"]=nciudad
            univact["tipo"]=ntipo
            actualizado=True
            break

    if actualizado == True:
        return True, "Universidad actualizada con éxito."
    else:
        return False, "La universidad no esta registrada."
    

#---------------------------------------------------------------------------
#entradas: nombre de la universidad que se desea eliminar
#salidas: true y mensaje de exito, false y mensaje de error
#procedimiento: pedir nombre de la universidad a buscar, quitar espacios y mayusculas, verificar que la busqueda no este vacia, recorrer 
# lista de universidades comparando el nombre a buscar con los registros, si el nombre coincide eliminar, retornar true o false dependiendo
#del resultado.

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
        if listauniversidades[i]["nombre"].strip().lower()==nombrebuscar.strip().lower():
            for j in range(len(listadeportistas)):
                if listadeportistas[j]["universidad"].lower() == nombrebuscar:
                    return False, "No se puede eliminar: la universidad tiene deportistas"
            #Borrar diccionario en el que estamos parados (i)
            listauniversidades.pop(i)
            eliminado=True
            break
    if eliminado==True:
            return True, "La universidad fue elimninada con éxito."
    else:
            return False, "No se pudo completar la operación."
        
