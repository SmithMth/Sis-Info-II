import tkinter as tk
from tkinter import ttk
import psycopg2

def get_docentes_from_database():
    docentes = []
    try:
        # Conéctate a la base de datos
        connection = psycopg2.connect(
            host="b0zyrecsgde9whh1dmka-postgresql.services.clever-cloud.com",
            database="b0zyrecsgde9whh1dmka",
            user="uehhymdo1hkrhqcxc3qz",
            password="WCWL5On4oVwb5AOnWjDYGi5KCvyiAY"
        )
        cursor = connection.cursor()

        # Realiza una consulta para obtener la lista de docentes
        cursor.execute("SELECT name, bachelordegree FROM proffesor")  
        rows = cursor.fetchall()
        for row in rows:
            nombre, titulo = row
            docentes.append({"nombre": nombre, "titulo": titulo})

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al obtener la lista de docentes:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

    return docentes

def mostrar_perfil(docente):
    perfil_nombre.set(docente["nombre"])
    perfil_carrera.set(docente["titulo"])

def cambiar_docente(event):
    selected_docente = lista_docentes.selection()[0]
    index = int(lista_docentes.index(selected_docente))
    docente = docentes[index]
    mostrar_perfil(docente)

def cargar_docentes(docentes):
    lista_docentes.delete(*lista_docentes.get_children())
    for i, docente in enumerate(docentes):
        lista_docentes.insert("", "end", iid=i, values=(docente["nombre"], docente["titulo"]))

root = tk.Tk()
root.title("Perfiles de Docentes")

lista_docentes = ttk.Treeview(root, columns=("Nombre", "Título"))
lista_docentes.heading("#1", text="Nombre")
lista_docentes.heading("#2", text="Título")
lista_docentes.pack()
docentes = get_docentes_from_database()

for i, docente in enumerate(docentes):
    lista_docentes.insert("", "end", iid=i, values=(docente["nombre"], docente["titulo"]))

perfil_nombre = tk.StringVar()
perfil_carrera = tk.StringVar()

marco_perfil = tk.Frame(root)
marco_perfil.pack(side="right")

etiqueta_nombre = tk.Label(marco_perfil, textvariable=perfil_nombre, font=("Helvetica", 16))
etiqueta_nombre.pack()

etiqueta_carrera = tk.Label(marco_perfil, textvariable=perfil_carrera)
etiqueta_carrera.pack()

boton_mensaje = tk.Button(marco_perfil, text="Enviar Mensaje")
boton_mensaje.pack()

lista_docentes.bind("<<TreeviewSelect>>", cambiar_docente)

mostrar_perfil(docentes[0])

cargar_docentes(docentes)

root.mainloop()
