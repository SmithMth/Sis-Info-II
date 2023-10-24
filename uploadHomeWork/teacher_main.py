import tkinter as tk
from from_creat import ExamGeneratorApp

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
    app = ExamGeneratorApp(root)
    root.title("Página de Inicio del Profesor")
    root.mainloop()
