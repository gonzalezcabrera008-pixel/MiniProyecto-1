import tkinter as tk
from tkinter import ttk, messagebox
from Universidades import (registraruniversidad, actualizaruniversidades, borraruniversidad, enumeraruniversidades)
from Deportistas import (registrardeportista,actualizardeportista,borrardeportista,enumerardeportistas)
from Disciplinas import (registrardisciplina,borrardisciplina,enumerardisciplinas)
from Inscripciones import (inscribir_deportista, eliminar_inscripcion, listar_inscripciones_por_disciplina)
from Resultados import (registrar_resultado, eliminar_resultado, listar_resultados)
from Consultas import (consultar_medallero, consultar_universidad_ganadora, consultar_deportistas_participantes, consultar_estadisticas_generales)
from Reportes import (generar_reporte_pandas, exportar_reporte_csv)
from Archivos import (validarantesdeguardar, guardardatosjson, cargardatosjson, contarregistros)
from Reportes import generar_medallero_csv

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

#Funciones Inscripciones------------------------------------------------------------

def accioninscribir():
    documento = entry_insc_doc.get()
    disciplina = entry_insc_disc.get()
    exito, mensaje = inscribir_deportista(listainscripciones, listadeportistas, listadisciplinas, documento, disciplina)
    if exito == True:
        messagebox.showinfo("Éxito", mensaje)
        accionlistarinscripciones()
    else:
        messagebox.showerror("Error", mensaje)


def accioneliminarinscripcion():
    documento = entry_insc_doc.get()
    disciplina = entry_insc_disc.get()
    exito, mensaje = eliminar_inscripcion(listainscripciones, documento, disciplina)
    if exito == True:
        messagebox.showinfo("Éxito", mensaje)
        accionlistarinscripciones()
    else:
        messagebox.showerror("Error", mensaje)


def accionlistarinscripciones():
    listboxresultadosinsc.delete(0, tk.END)
    resultados = listar_inscripciones_por_disciplina(listainscripciones, listadeportistas, entry_insc_disc.get())
    for i in range(len(resultados)):
        listboxresultadosinsc.insert(tk.END, resultados[i])
        if i % 2 == 0:
            listboxresultadosinsc.itemconfig(i, bg="white")
        else:
            listboxresultadosinsc.itemconfig(i, bg="#EEF3F8")


def accionregistrarresultado():
    exito, mensaje = registrar_resultado(listaresultados, listadisciplinas, listauniversidades, entry_res_disc.get(), entry_res_univ.get(), entry_res_pos.get())
    if exito == True:
        messagebox.showinfo("Éxito", mensaje)
        accionlistarresultados()
    else:
        messagebox.showerror("Error", mensaje)


def accioneliminarresultado():
    exito, mensaje = eliminar_resultado(listaresultados, entry_res_disc.get(), entry_res_univ.get())
    if exito == True:
        messagebox.showinfo("Éxito", mensaje)
        accionlistarresultados()
    else:
        messagebox.showerror("Error", mensaje)


def accionlistarresultados():
    listboxresultadosres.delete(0, tk.END)
    resultados = listar_resultados(listaresultados, entry_res_disc.get())
    for i in range(len(resultados)):
        listboxresultadosres.insert(tk.END, resultados[i])
        if i % 2 == 0:
            listboxresultadosres.itemconfig(i, bg="white")
        else:
            listboxresultadosres.itemconfig(i, bg="#EEF3F8")


def mostrarresultadosconsulta(resultados):
    listboxconsultas.delete(0, tk.END)
    for i in range(len(resultados)):
        listboxconsultas.insert(tk.END, resultados[i])
        if i % 2 == 0:
            listboxconsultas.itemconfig(i, bg="white")
        else:
            listboxconsultas.itemconfig(i, bg="#EEF3F8")


def accionconsultarmedallero():
    mostrarresultadosconsulta(consultar_medallero(listauniversidades, listaresultados))


def accionconsultarganadora():
    mostrarresultadosconsulta(consultar_universidad_ganadora(listauniversidades, listaresultados))


def accionconsultardeportistas():
    mostrarresultadosconsulta(consultar_deportistas_participantes(listadeportistas, listauniversidades, listainscripciones))


def accionconsultarestadisticas():
    mostrarresultadosconsulta(consultar_estadisticas_generales(listauniversidades, listadeportistas, listadisciplinas, listainscripciones, listaresultados))

#Zona Reporte Pandas
# Entradas: ninguna (lee listaresultados en memoria desde main)
# Salidas: ninguna (abre una ventana Toplevel con la tabla de resultados,
# la universidad ganadora y botones de acción, o muestra error con messagebox)
# Procedimientos: 1) Llamar a generar_reporte_pandas(listaresultados).
# 2) Si retorna False, mostrar el error con messagebox.showerror.
# 3) Si retorna True, abrir una ventana Toplevel con los títulos, botones
# "Generar Reporte con Pandas" y "Exportar CSV", una tabla ttk.Treeview
# llenada por índices desde df_puntos y la línea de universidad ganadora.
# 4) Confirmar la generación con messagebox.showinfo.
def accionreportepandas():
    ok, mensaje, df_puntos, ganadora = generar_reporte_pandas(listaresultados)
    if ok == False:
        messagebox.showerror("Error", mensaje)
        return

    ventana_reporte = tk.Toplevel(ventana)
    ventana_reporte.title("Reporte: resultados de la Copa Loyola")
    ventana_reporte.geometry("680x430")
    ventana_reporte.configure(bg="white")

    contenedor = tk.Frame(ventana_reporte, bg="white")
    contenedor.pack(fill="both", expand=True, padx=20, pady=15)

    tk.Label(
        contenedor,
        text="Reporte: resultados de la Copa Loyola",
        font=("Segoe UI", 15, "bold"),
        fg=AZUL,
        bg="white"
    ).pack(anchor="w")

    tk.Label(
        contenedor,
        text="Agrupación: universidad",
        font=("Segoe UI", 10),
        fg="#555555",
        bg="white"
    ).pack(anchor="w", pady=(2, 10))

    frame_botones_rep = tk.Frame(contenedor, bg="white")
    frame_botones_rep.pack(anchor="w", pady=(0, 10))

    # Entradas: ninguna
    # Salidas: ninguna
    # Procedimientos: cierra la ventana actual del reporte y vuelve a ejecutar accionreportepandas para refrescar los datos.
    def accion_actualizar_reporte():
        ventana_reporte.destroy()
        accionreportepandas()

    # Entradas: ninguna
    # Salidas: ninguna
    # Procedimientos: llama a exportar_reporte_csv(df_puntos) y muestra el resultado con messagebox.
    def accion_exportar_desde_ventana():
        ok_csv, msg_csv = exportar_reporte_csv(df_puntos)
        if ok_csv == True:
            messagebox.showinfo("Éxito", msg_csv, parent=ventana_reporte)
        else:
            messagebox.showerror("Error", msg_csv, parent=ventana_reporte)

    tk.Button(
        frame_botones_rep,
        text="Generar Reporte con Pandas",
        bg=AZUL,
        fg="white",
        relief="flat",
        padx=12,
        pady=4,
        command=accion_actualizar_reporte
    ).grid(row=0, column=0, padx=(0, 8))

    tk.Button(
        frame_botones_rep,
        text="Exportar CSV",
        bg="white",
        relief="solid",
        bd=1,
        padx=12,
        pady=4,
        command=accion_exportar_desde_ventana
    ).grid(row=0, column=1)

    columnas = ("Universidad", "Oro", "Plata", "Bronce", "Puntos")
    tabla_tree = ttk.Treeview(contenedor, columns=columnas, show="headings", height=10)
    tabla_tree.heading("Universidad", text="Universidad")
    tabla_tree.heading("Oro", text="Oro")
    tabla_tree.heading("Plata", text="Plata")
    tabla_tree.heading("Bronce", text="Bronce")
    tabla_tree.heading("Puntos", text="Puntos")

    tabla_tree.column("Universidad", width=250, anchor="w")
    tabla_tree.column("Oro", width=85, anchor="center")
    tabla_tree.column("Plata", width=85, anchor="center")
    tabla_tree.column("Bronce", width=85, anchor="center")
    tabla_tree.column("Puntos", width=95, anchor="center")

    tabla_tree.tag_configure("par", background="white")
    tabla_tree.tag_configure("impar", background="#EEF3F8")

    for i in range(len(df_puntos)):
        fila = df_puntos.iloc[i]
        valores = (
            str(fila["Universidad"]),
            int(fila["Oro"]),
            int(fila["Plata"]),
            int(fila["Bronce"]),
            int(fila["Puntos"])
        )
        if i % 2 == 0:
            tabla_tree.insert("", tk.END, values=valores, tags=("par",))
        else:
            tabla_tree.insert("", tk.END, values=valores, tags=("impar",))

    tabla_tree.pack(fill="both", expand=True, pady=(0, 12))

    tk.Label(
        contenedor,
        text="Universidad ganadora: " + ganadora,
        font=("Segoe UI", 11, "bold"),
        bg="#E3ECF5",
        fg=AZUL,
        anchor="w",
        padx=12,
        pady=8
    ).pack(fill="x")

    messagebox.showinfo("Éxito", mensaje, parent=ventana_reporte)
#Fin Zona Reporte Pandas (Santiago)

#Archivos (Karol)
def actualizarareainformacion(mensaje):
    cu, cd, cs, cn, cr = contarregistros(listauniversidades, listadeportistas, listadisciplinas, listainscripciones, listaresultados)
    lblinfomensaje.config(text=mensaje)
    lblinfoconteo.config(text="Universidades: " + str(cu) + " | Deportistas: " + str(cd) + "\nDisciplinas: " + str(cs) + " | Inscripciones: " + str(cn) + "\nResultados: " + str(cr))


def accionguardar():
    estructuravalida, hayduplicados, mensajevalidacion = validarantesdeguardar(listauniversidades, listadeportistas, listadisciplinas, listainscripciones, listaresultados)

    if estructuravalida == False:
        messagebox.showerror("Error", mensajevalidacion)
        actualizarareainformacion(mensajevalidacion)
    else:
        if hayduplicados == True:
            messagebox.showwarning("Datos repetidos", mensajevalidacion + "\n\nLos datos se guardarán de todos modos.")

        exito, mensaje = guardardatosjson(listauniversidades, listadeportistas, listadisciplinas, listainscripciones, listaresultados)

        if exito == True:
            exitocsv, mensajecsv = generar_medallero_csv(listauniversidades, listaresultados)
            if hayduplicados == True:
                textoinfo = "Datos guardados, con advertencia de datos repetidos."
            else:
                textoinfo = "Datos guardados correctamente."

            if exitocsv == True:
                messagebox.showinfo("Éxito", mensaje + "\n" + mensajecsv)
                actualizarareainformacion(textoinfo)
            else:
                messagebox.showerror("Error", mensaje + "\nPero no se pudo generar el medallero CSV: " + mensajecsv)
                actualizarareainformacion(textoinfo + " Error en medallero CSV: " + mensajecsv)
        else:
            messagebox.showerror("Error", mensaje)
            actualizarareainformacion(mensaje)


def accioncargar():
    exito, mensaje = cargardatosjson(listauniversidades, listadeportistas, listadisciplinas, listainscripciones, listaresultados)

    if exito == True:
        messagebox.showinfo("Éxito", mensaje)
        actualizarareainformacion("Datos cargados correctamente.")
        accionlistar()
        accionlistardep()
        accionlistardis()
    else:
        messagebox.showerror("Error", mensaje)
        actualizarareainformacion(mensaje)


def accionmedallerocsv():
    exito, mensaje = generar_medallero_csv(listauniversidades, listaresultados)

    if exito == True:
        messagebox.showinfo("Éxito", mensaje)
        actualizarareainformacion("Medallero CSV generado correctamente.")
    else:
        messagebox.showerror("Error", mensaje)
        actualizarareainformacion(mensaje)

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


#Ventana Inscripciones-----------------------------------------------------

pestañainscripciones = ttk.Frame(notebook)
notebook.add(pestañainscripciones, text=" Inscripciones ")
framecontenidoinsc = tk.Frame(pestañainscripciones)
framecontenidoinsc.pack(fill="both", expand=True, padx=15, pady=15)
frameizquierdainsc = tk.Frame(framecontenidoinsc)
frameizquierdainsc.pack(side="left", anchor="n", padx=10)
tk.Label(frameizquierdainsc, text="Inscripciones", font=("Segoe UI", 16, "bold"), fg=AZUL).pack(anchor="w", pady=(0, 10))
tk.Label(frameizquierdainsc, text="Documento del deportista", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_insc_doc = tk.Entry(frameizquierdainsc, **estiloentry)
entry_insc_doc.pack(pady=(2, 8), ipady=4, fill="x")
tk.Label(frameizquierdainsc, text="Disciplina", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_insc_disc = tk.Entry(frameizquierdainsc, **estiloentry)
entry_insc_disc.pack(pady=(2, 8), ipady=4, fill="x")
framebotonesinsc = tk.Frame(frameizquierdainsc)
framebotonesinsc.pack(pady=15)
tk.Button(framebotonesinsc, text="Inscribir", bg=AZUL, fg="white", relief="flat", width=9, command=accioninscribir).grid(row=0, column=0, padx=3)
tk.Button(framebotonesinsc, text="Listar", width=9, bg="white", relief="solid", bd=1, command=accionlistarinscripciones).grid(row=0, column=1, padx=3)
tk.Button(framebotonesinsc, text="Eliminar", width=9, bg="white", relief="solid", bd=1, command=accioneliminarinscripcion).grid(row=0, column=2, padx=3)
framederechainsc = tk.Frame(framecontenidoinsc)
framederechainsc.pack(side="left", anchor="n", padx=25)
tk.Label(framederechainsc, text="Inscripciones por disciplina", font=("Segoe UI", 11, "bold"), bg="#E3ECF5", fg=AZUL, anchor="w", padx=12, pady=10).pack(fill="x")
listboxresultadosinsc = tk.Listbox(framederechainsc, width=48, height=14, bd=0, highlightthickness=1, highlightbackground="#C9D3DE", activestyle="none", font=("Segoe UI", 10), selectbackground="#CFE0F1", selectforeground=AZUL)
listboxresultadosinsc.pack(pady=5)

#Ventana Resultados---------------------------------------------------------
pestañresultados = ttk.Frame(notebook)
notebook.add(pestañresultados, text=" Resultados ")
framecontenidores = tk.Frame(pestañresultados)
framecontenidores.pack(fill="both", expand=True, padx=15, pady=15)
frameizquierdares = tk.Frame(framecontenidores)
frameizquierdares.pack(side="left", anchor="n", padx=10)
tk.Label(frameizquierdares, text="Resultados", font=("Segoe UI", 16, "bold"), fg=AZUL).pack(anchor="w", pady=(0, 10))
tk.Label(frameizquierdares, text="Disciplina", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_res_disc = tk.Entry(frameizquierdares, **estiloentry)
entry_res_disc.pack(pady=(2, 8), ipady=4, fill="x")
tk.Label(frameizquierdares, text="Universidad", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_res_univ = tk.Entry(frameizquierdares, **estiloentry)
entry_res_univ.pack(pady=(2, 8), ipady=4, fill="x")
tk.Label(frameizquierdares, text="Posición (Oro, Plata o Bronce)", font=("Segoe UI", 9)).pack(anchor="w", pady=2)
entry_res_pos = tk.Entry(frameizquierdares, **estiloentry)
entry_res_pos.pack(pady=(2, 8), ipady=4, fill="x")
framebotonesres = tk.Frame(frameizquierdares)
framebotonesres.pack(pady=15)
tk.Button(framebotonesres, text="Registrar", bg=AZUL, fg="white", relief="flat", width=9, command=accionregistrarresultado).grid(row=0, column=0, padx=3)
tk.Button(framebotonesres, text="Listar", width=9, bg="white", relief="solid", bd=1, command=accionlistarresultados).grid(row=0, column=1, padx=3)
tk.Button(framebotonesres, text="Eliminar", width=9, bg="white", relief="solid", bd=1, command=accioneliminarresultado).grid(row=0, column=2, padx=3)
framederechares = tk.Frame(framecontenidores)
framederechares.pack(side="left", anchor="n", padx=25)
tk.Label(framederechares, text="Resultados por disciplina", font=("Segoe UI", 11, "bold"), bg="#E3ECF5", fg=AZUL, anchor="w", padx=12, pady=10).pack(fill="x")
listboxresultadosres = tk.Listbox(framederechares, width=48, height=14, bd=0, highlightthickness=1, highlightbackground="#C9D3DE", activestyle="none", font=("Segoe UI", 10), selectbackground="#CFE0F1", selectforeground=AZUL)
listboxresultadosres.pack(pady=5)

#Ventana Consultas---------------------------------------------------------
pestañaconsultas = ttk.Frame(notebook)
notebook.add(pestañaconsultas, text=" Consultas ")
framecontenidoconsultas = tk.Frame(pestañaconsultas)
framecontenidoconsultas.pack(fill="both", expand=True, padx=15, pady=15)
frameizquierdaconsultas = tk.Frame(framecontenidoconsultas)
frameizquierdaconsultas.pack(side="left", anchor="n", padx=10)
tk.Label(frameizquierdaconsultas, text="Consultas", font=("Segoe UI", 16, "bold"), fg=AZUL).pack(anchor="w", pady=(0, 10))
tk.Button(frameizquierdaconsultas, text="Medallero", bg=AZUL, fg="white", relief="flat", width=25, command=accionconsultarmedallero).pack(anchor="w", pady=5)
tk.Button(frameizquierdaconsultas, text="Universidad Ganadora", width=25, bg="white", relief="solid", bd=1, command=accionconsultarganadora).pack(anchor="w", pady=5)
tk.Button(frameizquierdaconsultas, text="Deportistas Participantes", width=25, bg="white", relief="solid", bd=1, command=accionconsultardeportistas).pack(anchor="w", pady=5)
tk.Button(frameizquierdaconsultas, text="Estadísticas Generales", width=25, bg="white", relief="solid", bd=1, command=accionconsultarestadisticas).pack(anchor="w", pady=5)
#Zona Reporte Pandas
tk.Button(frameizquierdaconsultas, text="Generar Reporte con Pandas", bg=AZUL, fg="white", relief="flat", width=25, command=accionreportepandas).pack(anchor="w", pady=5)

#-------------------- Archivos (Karol)
tk.Frame(frameizquierdaconsultas, height=1, bg="#C9D3DE").pack(fill="x", pady=(12, 8))
tk.Label(frameizquierdaconsultas, text="Acción de almacenamiento", font=("Segoe UI", 11, "bold"), fg=AZUL).pack(anchor="w")
tk.Label(frameizquierdaconsultas, text="Archivo: copa_loyola_datos.json", font=("Segoe UI", 9), fg="#555555").pack(anchor="w", pady=(2, 6))
tk.Button(frameizquierdaconsultas, text="Guardar datos (JSON)", bg=AZUL, fg="white", relief="flat", width=25, command=accionguardar).pack(anchor="w", pady=3)
tk.Button(frameizquierdaconsultas, text="Cargar datos (JSON)", width=25, bg="white", relief="solid", bd=1, command=accioncargar).pack(anchor="w", pady=3)
tk.Button(frameizquierdaconsultas, text="Medallero (CSV)", width=25, bg="white", relief="solid", bd=1, command=accionmedallerocsv).pack(anchor="w", pady=3)

tk.Label(frameizquierdaconsultas, text="Información / resultados", font=("Segoe UI", 10, "bold"), fg=AZUL).pack(anchor="w", pady=(12, 4))
lblinfomensaje = tk.Label(frameizquierdaconsultas, text="", font=("Segoe UI", 9, "bold"), bg="#EEF3F8", fg=AZUL, anchor="w", justify="left", wraplength=260, padx=10, pady=6)
lblinfomensaje.pack(fill="x")
lblinfoconteo = tk.Label(frameizquierdaconsultas, text="", font=("Segoe UI", 9), bg="#EEF3F8", anchor="w", justify="left", padx=10, pady=6)
lblinfoconteo.pack(fill="x")
actualizarareainformacion("Sin operaciones todavía.")

# Nombre de la pestaña ventana más grande para que quepa la sección nueva
notebook.tab(pestañaconsultas, text=" Consultas / Archivos / Reportes ")
ventana.geometry("900x640")
#---------------------------------------
framederechaconsultas = tk.Frame(framecontenidoconsultas)
framederechaconsultas.pack(side="left", anchor="n", padx=25)
tk.Label(framederechaconsultas, text="Resultados de la consulta", font=("Segoe UI", 11, "bold"), bg="#E3ECF5", fg=AZUL, anchor="w", padx=12, pady=10).pack(fill="x")
listboxconsultas = tk.Listbox(framederechaconsultas, width=60, height=19, bd=0, highlightthickness=1, highlightbackground="#C9D3DE", activestyle="none", font=("Segoe UI", 10), selectbackground="#CFE0F1", selectforeground=AZUL)
listboxconsultas.pack(pady=5)
ventana.mainloop()