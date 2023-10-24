import tkinter as tk
from tkinter import ttk
import teacher_main, ui_add_meets,homeworkNotification

def get_materias(docente_id):
    # Aquí va tu función para recuperar las materias del docente. Esto es solo un ejemplo.
    return ["Matemáticas", "Historia"]

def mostrar_materia(materia):
    # Esta función se ejecutará al hacer clic en una materia
    print(f"Seleccionaste la materia: {materia}")

def crear_examen():
    print("Crear examen")
    teacher_main.vistaCrearExamen()

def crear_reuniones():
    print("Crear reuniones")
    ui_add_meets.view_meeting_creation()

def enviar_recordatorios():
    homeworkNotification.select_subject_and_get_id()



# Crear la ventana principal
def ventana_docente():
    root = tk.Tk()
    root.title("Materias Docente")
    root.geometry("800x500")

    docente_id = 1  # Suponiendo que trabajaremos con el docente con ID 1
    materias = get_materias(docente_id)

    # Título grande
    welcome_label = ttk.Label(root, text=f"Bienvenido docente ID: {docente_id}", font=("Arial", 18, "bold"))
    welcome_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    # Título mediano
    materias_label = ttk.Label(root, text="Materias a cargo", font=("Arial", 14, "bold"))
    materias_label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

    # Contenedor para las tarjetas
    cards_container = ttk.Frame(root)
    cards_container.grid(row=2, column=0, sticky="w", padx=20)

    # Creación de las tarjetas como botones
    for i, materia in enumerate(materias):
        button = tk.Button(cards_container, text=materia, font=("Arial", 14), command=lambda m=materia: mostrar_materia(m), width=20, height=5)
        button.grid(row=0, column=i, padx=5, pady=10)

    # Botones adicionales
    btn_examen = tk.Button(root, text="Crear Examen", command=crear_examen)
    btn_examen.grid(row=0, column=1, sticky="e", padx=20, pady=10)

    btn_reuniones = tk.Button(root, text="Crear Reuniones", command=crear_reuniones)
    btn_reuniones.grid(row=1, column=1, sticky="e", padx=20, pady=10)

    btn_recordatorios = tk.Button(root, text="Enviar Recordatorios", command=enviar_recordatorios)
    btn_recordatorios.grid(row=2, column=1, sticky="e", padx=20, pady=10)

    root.mainloop()
