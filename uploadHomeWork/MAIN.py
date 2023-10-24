import tkinter as tk
from tkinter import ttk
import MAIN_DOCENTE, MAIN_ESTUDIANTE

def on_docente_click():
    MAIN_DOCENTE.ventana_docente()

def on_estudiante_click():
    MAIN_ESTUDIANTE.ventanta_estudiante()

def main_ui():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("")
    root.geometry("400x300")  # Ancho x Alto

    # Centrar la ventana en la pantalla
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth()/2 - window_width/2)
    position_down = int(root.winfo_screenheight()/2 - window_height/2)
    root.geometry("+{}+{}".format(position_right, position_down))

    # Establecer un color de fondo agradable
    root.configure(bg='#f2f2f2')

    # Crear un marco para contener los botones
    frame = ttk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Crear los botones
    docente_btn = ttk.Button(frame, text="Docente", command=on_docente_click)
    docente_btn.grid(row=0, column=0, padx=10, pady=10)

    estudiante_btn = ttk.Button(frame, text="Estudiante", command=on_estudiante_click)
    estudiante_btn.grid(row=0, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_ui()
