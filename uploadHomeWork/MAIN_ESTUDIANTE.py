import tkinter as tk
from tkinter import ttk
import db_uploadHomeWork as database
import kardex_viewer,iu_apuntes,ui_room_reservation,proffesor_profile,ui_main_window,db_uploadHomeWork

def get_materias(student_name):
    # Aquí va tu función para recuperar las materias. Esto es solo un ejemplo.
    return db_uploadHomeWork.get_materias(1)

def mostrar_materia(materia):
    # Esta función se ejecutará al hacer clic en una materia
    ui_main_window.run_entregar_tarea(materia)
    print(f"Seleccionaste la materia: {materia}")

def ver_kardex():
    print("Ver kardex")
    
    # Llama a la función para mostrar el nuevo contenido
    for widget in frame_kardex.winfo_children():
        widget.destroy()

    # Llama a la función para mostrar el nuevo contenido
    kardex_viewer.show_kardex_content(frame_kardex, 1)

def notas_personales():
    print("Notas personales")
    iu_apuntes.show_notas()

def reservar_aula():
    ui_room_reservation.show_reservar()
    

def perfil_docente():
    print("Perfil docente")
    proffesor_profile.vista_docnete()

def resolution_exam(id):
    root = tk.Tk()
    app = ExamSolverApp(root, id)  # Supongamos que el ID del examen que quieres resolver es 1
    root.mainloop()
    
# Crear la ventana principal


def ventanta_estudiante():
    global frame_kardex
    root = tk.Tk()
    root.title("Materias Inscritas")
    root.geometry("800x500")

    main_container = ttk.Frame(root)
    main_container.pack(fill=tk.BOTH, expand=True)

    student_name = "Saul"  # Suponiendo que queremos ver las materias para el estudiante "Saul"
    materias = get_materias(student_name)

    # Título grande
    welcome_label = ttk.Label(main_container, text=f"Bienvenido estudiante {student_name}", font=("Arial", 18, "bold"))
    welcome_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    # Título mediano
    materias_label = ttk.Label(main_container, text="Materias", font=("Arial", 14, "bold"))
    materias_label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

    # Contenedor para las tarjetas
    cards_container = ttk.Frame(main_container)
    cards_container.grid(row=2, column=0, sticky="w", padx=20)

    # Creación de las tarjetas como botones
    for i, materia in enumerate(materias):
        button = tk.Button(cards_container, text=materia, font=("Arial", 14), command=lambda m=materia: mostrar_materia(m), width=20, height=5)
        button.grid(row=0, column=i, padx=5, pady=10)

    # Botones adicionales
    btn_kardex = tk.Button(main_container, text="Ver Kardex", command=ver_kardex)
    btn_kardex.grid(row=0, column=1, sticky="e", padx=20, pady=10)

    btn_notas = tk.Button(main_container, text="Notas Personales", command=notas_personales)
    btn_notas.grid(row=1, column=1, sticky="e", padx=20, pady=10)

    btn_reservar = tk.Button(main_container, text="Reservar Aula", command=reservar_aula)
    btn_reservar.grid(row=2, column=1, sticky="e", padx=20, pady=10)

    btn_perfil = tk.Button(main_container, text="Perfil Docente", command=perfil_docente)
    btn_perfil.grid(row=3, column=1, sticky="e", padx=20, pady=10)

    frame_kardex = tk.Frame(main_container)
    frame_kardex.grid(row=4, column=0, columnspan=2, sticky='nsew')
    
    
    
    # Adding combobox drop down list
    exams = get_exams_list()
    exam_names = [exam[1] for exam in exams]  # Extract exam names from the list of tuples
    combo['values'] = exam_names

    combo.pack()
    combo.current(0)  # set the selected item

    # Add button
    btn = tk.Button(root, text="Ingresar al Examen")
    btn.pack()
    btn.bind('<Button-1>', enter_exam)

    root.mainloop()
    
def get_exams_list():
    connection = database.get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM Exams")
    exams = cursor.fetchall()
    connection.close()
    return exams

def enter_exam(event):
    selected_exam_name = combo.get()
    selected_exam_id = exams_dict[selected_exam_name]  # Get the ID from the dictionary
    if selected_exam_id:
        resolution_exam(selected_exam_id)
        print(f"Entering exam: {selected_exam_name} with ID: {selected_exam_id}")
    else:
        print("Please select an exam first.")