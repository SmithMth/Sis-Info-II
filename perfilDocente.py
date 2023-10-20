import tkinter as tk
from tkinter import ttk

# Datos de ejemplo de los docentes
docentes = [
    {
        "nombre": "Profesor 1",
        "carrera": "Matemáticas",
        "foto_url": "url_de_la_foto_1.jpg"
    },
    {
        "nombre": "Profesor 2",
        "carrera": "Física",
        "foto_url": "url_de_la_foto_2.jpg"
    },
    # Agrega más docentes aquí
]

def mostrar_perfil(docente):
    # Función para mostrar el perfil de un docente en la ventana de perfil
    perfil_nombre.set(docente["nombre"])
    perfil_carrera.set(docente["carrera"])
    # Puedes cargar la foto del docente aquí (reemplaza la URL)

# Función para cambiar el docente seleccionado
def cambiar_docente(event):
    selected_docente = lista_docentes.selection()[0]
    docente = docentes[selected_docente]
    mostrar_perfil(docente)

# Crear ventana principal
root = tk.Tk()
root.title("Perfiles de Docentes")

# Crear una lista de docentes
lista_docentes = ttk.Treeview(root, columns=("Nombre", "Carrera"))
lista_docentes.heading("#1", text="Nombre")
lista_docentes.heading("#2", text="Carrera")
lista_docentes.pack()

# Agregar docentes a la lista
for i, docente in enumerate(docentes):
    lista_docentes.insert("", "end", iid=i, values=(docente["nombre"], docente["carrera"]))

# Variables para el perfil del docente
perfil_nombre = tk.StringVar()
perfil_carrera = tk.StringVar()

# Crear un marco para el perfil
marco_perfil = tk.Frame(root)
marco_perfil.pack(side="right")

# Etiqueta para el nombre del docente
etiqueta_nombre = tk.Label(marco_perfil, textvariable=perfil_nombre, font=("Helvetica", 16))
etiqueta_nombre.pack()

# Etiqueta para la carrera del docente
etiqueta_carrera = tk.Label(marco_perfil, textvariable=perfil_carrera)
etiqueta_carrera.pack()

# Botón para enviar un mensaje al docente (puedes agregar funcionalidad aquí)
boton_mensaje = tk.Button(marco_perfil, text="Enviar Mensaje")
boton_mensaje.pack()

# Asociar la selección de la lista a la función cambiar_docente
lista_docentes.bind("<<TreeviewSelect>>", cambiar_docente)

# Mostrar el primer docente en la lista
mostrar_perfil(docentes[0])

root.mainloop()
