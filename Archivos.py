#entradas: listas de universidades
#salidas: el set con los nombres unicos y una lista con los nombres que se repitieron
#procedimiento:

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

