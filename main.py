import tkinter as tk
from tkinter import ttk, messagebox
from Universidades import (registraruniversidad, actualizaruniversidades, borraruniversidad, enumeraruniversidades)
from Deportistas import (registrardeportista,actualizardeportista,borrardeportista,enumerardeportistas)
from Disciplinas import (registrardisciplina,borrardisciplina,enumerardisciplinas)
AZUL="#1F4E79"

listauniversidades = []
listadeportistas= []
listainscripciones= []
listadisciplinas = []
listaresultados = []

#Funciones Universidades--------------------------------------------------------------------

def accionregistrar():
    #capturar los textos en las cajas de texto
    nombre = entry_nombre.get()
    pais = entry_pais.get()
    ciudad = entry_ciudad.get()
    tipo = entry_tipo.get()
    

    #llamar función. El booleano toma el nombre de exito, y el mensaje respectivo toma el nombre de mensaje
    exito,mensaje = registraruniversidad(nombre,pais,ciudad,tipo, listauniversidades)

    #comparar si completo la operacion o no
    if exito ==True:
        messagebox.showinfo("Éxito",mensaje)
        limpiarcampos()
        accionlistar()

    else:
        messagebox.showerror("Error", mensaje)


def accionactualizar():
    nombre = entry_nombre.get()
    pais = entry_pais.get()
    ciudad = entry_ciudad.get()
    tipo = entry_tipo.get()

    exito,mensaje = actualizaruniversidades(nombre,pais,ciudad,tipo, listauniversidades)
    
    if exito ==True:
        messagebox.showinfo("Éxito",mensaje)
        limpiarcampos()
        accionlistar()
    
    else:
        messagebox.showerror("Error", mensaje)



def accioneliminar():
    nombre = entry_nombre.get()
    
    exito,mensaje = borraruniversidad (nombre,listauniversidades,listadeportistas)
    
    if exito ==True:
        messagebox.showinfo("Éxito",mensaje)
        limpiarcampos()
        accionlistar()
    
    else:
        messagebox.showerror("Error", mensaje)



def accionlistar():
    #se borran todo el contenido anterior para evitar repeticiones o acumular
    listboxresultados.delete(0,tk.END)

    resultados=enumeraruniversidades(listauniversidades)

    #recorre los resultados y los inserta en la pantalla individualmente
    for i in range (len(resultados)):
        texto = resultados [i]
        listboxresultados.insert(tk.END,texto)
        #filas alternadas, como en el mockup
        if i % 2 == 0:
            listboxresultados.itemconfig(i, bg="white")
        else:
            listboxresultados.itemconfig(i, bg="#EEF3F8")


def limpiarcampos():
    entry_nombre.delete(0,tk.END)
    entry_pais.delete(0,tk.END)
    entry_ciudad.delete(0,tk.END)
    entry_tipo.delete(0,tk.END)

#----------------------------------
#Funciones Deportistas

def accionregistrardep():
    # Capturar datos de las cajas de texto de deportistas
    nombre = entry_dep_nombre.get()
    tipodoc = entry_dep_tipodoc.get()
    documento = entry_dep_doc.get()
    universidad = entry_dep_univ.get()

    exito, mensaje = registrardeportista(nombre, tipodoc, documento, universidad, listadeportistas, listauniversidades)

    if exito == True:
        messagebox.showinfo("Éxito", mensaje)
        limpiarcamposdep()
        accionlistardep()
    else:
        messagebox.showerror("Error", mensaje)


def accionactualizardep():
    tipodoc = entry_dep_tipodoc.get()
    documento = entry_dep_doc.get()
    nombre = entry_dep_nombre.get()
    universidad = entry_dep_univ.get()

    exito, mensaje = actualizardeportista(tipodoc, documento, nombre, universidad, listadeportistas, listauniversidades)

    if exito == True:
        messagebox.showinfo("Éxito", mensaje)
        limpiarcamposdep()
        accionlistardep()
    else:
        messagebox.showerror("Error", mensaje)


def accioneliminardep():
    tipodoc = entry_dep_tipodoc.get()
    documento = entry_dep_doc.get()

    exito, mensaje = borrardeportista(tipodoc, documento, listadeportistas, listainscripciones)

    if exito == True:
        messagebox.showinfo("Éxito", mensaje)
        limpiarcamposdep()
        accionlistardep()
    else:
        messagebox.showerror("Error", mensaje)


def accionlistardep():
    # Limpiar el Listbox de deportistas antes de actualizar
    listboxresultadosdep.delete(0, tk.END)

    resultados = enumerardeportistas(listadeportistas)

    # Recorrer la lista formateada y pintarla con filas alternadas
    for i in range(len(resultados)):
        texto = resultados[i]
        listboxresultadosdep.insert(tk.END, texto)
        
        if i % 2 == 0:
            listboxresultadosdep.itemconfig(i, bg="white")
        else:
            listboxresultadosdep.itemconfig(i, bg="#EEF3F8")


def limpiarcamposdep():
    entry_dep_nombre.delete(0, tk.END)
    entry_dep_tipodoc.delete(0, tk.END)
    entry_dep_doc.delete(0, tk.END)
    entry_dep_univ.delete(0, tk.END)

#Funciones Disciplinas-------------------------------------------------------------

# NUEVO: Funciones Disciplinas

# Botón CREAR: lee los campos, llama a registrardisciplina y muestra el resultado
def accionregistrardis():
    # .get() lee lo que hay escrito en los Entry en ese momento
    nombre = entry_dis_nombre.get()
    modalidad = entry_dis_modalidad.get()

    # La función devuelve dos cosas: True/False y un mensaje. Las guardamos en exito y mensaje
    exito, mensaje = registrardisciplina(nombre, modalidad, listadisciplinas)

    if exito == True:
        messagebox.showinfo("Éxito", mensaje)
        limpiarcamposdis()
        accionlistardis()
    else:
        messagebox.showerror("Error", mensaje)


# Botón ELIMINAR: borra la disciplina cuyo nombre está escrito en la caja
def accioneliminardis():
    nombre = entry_dis_nombre.get()

    # borrardisciplina revisa que no tenga inscripciones ni resultados antes de eliminar
    exito, mensaje = borrardisciplina(nombre, listadisciplinas, listainscripciones, listaresultados)

    if exito == True:
        messagebox.showinfo("Éxito", mensaje)
        limpiarcamposdis()
        accionlistardis()
    else:
        messagebox.showerror("Error", mensaje)


# Borra el Listbox y lo vuelve a llenar con las disciplinas registradas
def accionlistardis():
    listboxresultadosdis.delete(0, tk.END)

    # enumerardisciplinas devuelve textos tipo "1. Natación | Individual"
    resultados = enumerardisciplinas(listadisciplinas)

    # Recorremos por índice, insertamos cada texto y alternamos el color de las filas
    for i in range(len(resultados)):
        texto = resultados[i]
        listboxresultadosdis.insert(tk.END, texto)

        if i % 2 == 0:
            listboxresultadosdis.itemconfig(i, bg="white")
        else:
            listboxresultadosdis.itemconfig(i, bg="#EEF3F8")


def limpiarcamposdis():
    entry_dis_nombre.delete(0, tk.END)
    entry_dis_modalidad.delete(0, tk.END)

#-----------------------------------------------------------------------------------
#------Ventana y elementos-------
ventana = tk.Tk()
ventana.title ("Copa Loyola - Sistema de Gestión Deportiva")
ventana.geometry ("850x500")

ventana.configure(bg="white")
ventana.option_add("*Frame.Background", "white")
ventana.option_add("*Label.Background", "white")

estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("TFrame", background="white")
estilo.configure("TNotebook", background="white", borderwidth=0)
estilo.configure("TNotebook.Tab", background="#F4F6F8", foreground="#8A94A0",
                 padding=(16, 7), font=("Segoe UI", 9))
estilo.map("TNotebook.Tab", background=[("selected", "white")],
           foreground=[("selected", "#333333")])

#Pestañas------------------------------------
notebook=ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

#Pestaña de Universidades--------------------
pestañauniversidades = ttk.Frame(notebook)
notebook.add(pestañauniversidades, text=" Universidades ")

# Contenido 
framecontenido = tk.Frame(pestañauniversidades)
framecontenido.pack(fill="both", expand=True, padx=15, pady=15)


# Izq Formulario y Botones

frameizquierda = tk.Frame(framecontenido)
frameizquierda.pack(side="left", anchor="n", padx=10)

# Título de la sección dentro de la pestaña
tk.Label(frameizquierda, text="Universidades", font=("Segoe UI", 16, "bold"), fg=AZUL).pack(anchor="w", pady=(0, 10))

# Estilo común de las cajas de texto 
estiloentry = dict(width=32, relief="flat", highlightthickness=1,
highlightbackground="#9AA5B1", highlightcolor=AZUL,
font=("Segoe UI", 10))

# Campos de texto
tk.Label(frameizquierda, text="Nombre de la universidad", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_nombre = tk.Entry(frameizquierda, **estiloentry)
entry_nombre.pack(pady=(2, 8), ipady=4, fill="x")

tk.Label(frameizquierda, text="País", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_pais = tk.Entry(frameizquierda, **estiloentry)
entry_pais.pack(pady=(2, 8), ipady=4, fill="x")

tk.Label(frameizquierda, text="Ciudad", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_ciudad = tk.Entry(frameizquierda, **estiloentry)
entry_ciudad.pack(pady=(2, 8), ipady=4, fill="x")

tk.Label(frameizquierda, text="Tipo de participación", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_tipo = tk.Entry(frameizquierda, **estiloentry)
entry_tipo.pack(pady=(2, 8), ipady=4, fill="x")


# Botones debajo de las cajas (Crear, Actualizar y Borrar)
framebotones = tk.Frame(frameizquierda)
framebotones.pack(pady=15)

btncrear = tk.Button(framebotones, text="Crear", bg=AZUL, fg="white", relief="flat", width=9, command=accionregistrar)
btncrear.grid(row=0, column=0, padx=3)

btn_actualizar = tk.Button(framebotones, text="Actualizar", width=9, bg="white", relief="solid", bd=1, command=accionactualizar)
btn_actualizar.grid(row=0, column=1, padx=3)

btn_eliminar = tk.Button(framebotones, text="Eliminar", width=9, bg="white", relief="solid", bd=1, command=accioneliminar)
btn_eliminar.grid(row=0, column=2, padx=3)


# Derecha, Lista Universidades Registradas

framederecha = tk.Frame(framecontenido)
framederecha.pack(side="left", anchor="n", padx=25)

tk.Label(framederecha, text="Universidades registradas", font=("Segoe UI", 11, "bold"),
bg="#E3ECF5", fg=AZUL, anchor="w", padx=12, pady=10).pack(fill="x")

listboxresultados = tk.Listbox(framederecha, width=48, height=14, bd=0, highlightthickness=1,
highlightbackground="#C9D3DE", activestyle="none",
font=("Segoe UI", 10), selectbackground="#CFE0F1",
selectforeground=AZUL)
listboxresultados.pack(pady=5)

#------------------------------------
#Ventana Deportistas
pestañadeportistas = ttk.Frame(notebook)
notebook.add(pestañadeportistas, text=" Deportistas ")

framecontenidodep = tk.Frame(pestañadeportistas)
framecontenidodep.pack(fill="both", expand=True, padx=15, pady=15)

# Columna Izquierda: Formulario de Deportistas
frameizquierdadep = tk.Frame(framecontenidodep)
frameizquierdadep.pack(side="left", anchor="n", padx=10)

tk.Label(frameizquierdadep, text="Deportistas", font=("Segoe UI", 16, "bold"), fg=AZUL).pack(anchor="w", pady=(0, 10))

# Campos de texto para Deportistas
tk.Label(frameizquierdadep, text="Nombre completo", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_dep_nombre = tk.Entry(frameizquierdadep, **estiloentry)
entry_dep_nombre.pack(pady=(2, 8), ipady=4, fill="x")

tk.Label(frameizquierdadep, text="Tipo de documento (Ej. CC, TI)", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_dep_tipodoc = tk.Entry(frameizquierdadep, **estiloentry)
entry_dep_tipodoc.pack(pady=(2, 8), ipady=4, fill="x")

tk.Label(frameizquierdadep, text="Número de documento", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_dep_doc = tk.Entry(frameizquierdadep, **estiloentry)
entry_dep_doc.pack(pady=(2, 8), ipady=4, fill="x")

tk.Label(frameizquierdadep, text="Universidad asociada", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_dep_univ = tk.Entry(frameizquierdadep, **estiloentry)
entry_dep_univ.pack(pady=(2, 8), ipady=4, fill="x")

# Botones de Deportistas (Crear, Actualizar, Eliminar)
framebotonesdep = tk.Frame(frameizquierdadep)
framebotonesdep.pack(pady=15)

btncreardep = tk.Button(framebotonesdep, text="Crear", bg=AZUL, fg="white", relief="flat", width=9, command=accionregistrardep)
btncreardep.grid(row=0, column=0, padx=3)

btnactualizardep = tk.Button(framebotonesdep, text="Actualizar", width=9, bg="white", relief="solid", bd=1, command=accionactualizardep)
btnactualizardep.grid(row=0, column=1, padx=3)

btneliminardep = tk.Button(framebotonesdep, text="Eliminar", width=9, bg="white", relief="solid", bd=1, command=accioneliminardep)
btneliminardep.grid(row=0, column=2, padx=3)

# Columna Derecha: Listbox de Deportistas Registrados
framerederechadep = tk.Frame(framecontenidodep)
framerederechadep.pack(side="left", anchor="n", padx=25)

tk.Label(framerederechadep, text="Deportistas registrados", font=("Segoe UI", 11, "bold"),
         bg="#E3ECF5", fg=AZUL, anchor="w", padx=12, pady=10).pack(fill="x")

listboxresultadosdep = tk.Listbox(framerederechadep, width=48, height=14, bd=0, highlightthickness=1,
highlightbackground="#C9D3DE", activestyle="none",
font=("Segoe UI", 10), selectbackground="#CFE0F1",
selectforeground=AZUL)
listboxresultadosdep.pack(pady=5)

#Ventana Disciplinas------------------------------------------------------


pestañadisciplinas = ttk.Frame(notebook)
notebook.add(pestañadisciplinas, text=" Disciplinas ")

# Contenedor interno: deja un margen alrededor de todo el contenido
framecontenidodis = tk.Frame(pestañadisciplinas)
framecontenidodis.pack(fill="both", expand=True, padx=15, pady=15)

# Columna izquierda: formulario y botones 
frameizquierdadis = tk.Frame(framecontenidodis)
frameizquierdadis.pack(side="left", anchor="n", padx=10)

# Título azul de la sección
tk.Label(frameizquierdadis, text="Disciplinas", font=("Segoe UI", 16, "bold"), fg=AZUL).pack(anchor="w", pady=(0, 10))

# Nombre de la disciplina
tk.Label(frameizquierdadis, text="Nombre de la disciplina", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_dis_nombre = tk.Entry(frameizquierdadis, **estiloentry)
entry_dis_nombre.pack(pady=(2, 8), ipady=4, fill="x")

# Modalidad
tk.Label(frameizquierdadis, text="Modalidad", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_dis_modalidad = tk.Entry(frameizquierdadis, **estiloentry)
entry_dis_modalidad.pack(pady=(2, 8), ipady=4, fill="x")

# Botones
framebotonesdis = tk.Frame(frameizquierdadis)
framebotonesdis.pack(pady=15)

btncreardis = tk.Button(framebotonesdis, text="Crear", bg=AZUL, fg="white", relief="flat", width=9, command=accionregistrardis)
btncreardis.grid(row=0, column=0, padx=3)

btneliminardis = tk.Button(framebotonesdis, text="Eliminar", width=9, bg="white", relief="solid", bd=1, command=accioneliminardis)
btneliminardis.grid(row=0, column=1, padx=3)

# Columna derecha
framederechadis = tk.Frame(framecontenidodis)
framederechadis.pack(side="left", anchor="n", padx=25)

tk.Label(framederechadis, text="Disciplinas registradas", font=("Segoe UI", 11, "bold"),
         bg="#E3ECF5", fg=AZUL, anchor="w", padx=12, pady=10).pack(fill="x")

listboxresultadosdis = tk.Listbox(framederechadis, width=48, height=14, bd=0, highlightthickness=1,
highlightbackground="#C9D3DE", activestyle="none",
font=("Segoe UI", 10), selectbackground="#CFE0F1",
selectforeground=AZUL)
listboxresultadosdis.pack(pady=5)


ventana.mainloop()