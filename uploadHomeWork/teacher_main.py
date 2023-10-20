import tkinter as tk
import from_creat

def show_create_exam(frame_content):
    for widget in frame_content.winfo_children():
        widget.destroy()
    tk.Label(frame_content, text="Aquí podrás crear un examen").pack()
    from_creat.vista_creacionExamen()

def show_view_scores(frame_content):
    for widget in frame_content.winfo_children():
        widget.destroy()
    tk.Label(frame_content, text="Aquí podrás ver las notas de los exámenes enviados por tus estudiantes").pack()

def show_view_students(frame_content):
    for widget in frame_content.winfo_children():
        widget.destroy()
    tk.Label(frame_content, text="Aquí podrás ver la lista de tus estudiantes").pack()
    
def show_view_add_meet(frame_content):
    for widget in frame_content.winfo_children():
        widget.destroy()
    tk.Label(frame_content, text="Aquí podrás ver la lista de tus estudiantes").pack()

def vistaCrearExamen():
    root = tk.Tk()
    root.title("Página de Inicio del Profesor")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}")

    frame_content = tk.Frame(root)
    frame_content.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    btn_frame = tk.Frame(root)
    btn_frame.pack(side="top")

    btn_create_exam = tk.Button(btn_frame, text="Crear Examen", command=show_create_exam)
    btn_create_exam.grid(row=0, column=0, padx=10)

    btn_view_scores = tk.Button(btn_frame, text="Ver Notas", command=show_view_scores)
    btn_view_scores.grid(row=0, column=1, padx=10)

    btn_view_students = tk.Button(btn_frame, text="Ver Estudiantes", command=show_view_students)
    btn_view_students.grid(row=0, column=2, padx=10)
    
    btn_view_students = tk.Button(btn_frame, text="Crear Meet", command=show_view_add_meet)
    btn_view_students.grid(row=0, column=3, padx=10)

    

    root.mainloop()
