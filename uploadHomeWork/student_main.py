import tkinter as tk
import tkinter.font as tkFont
import kardex_viewer 
import ui_main_window, ui_add_meets

def show_kardex_content():
    # Elimina todos los widgets existentes en frame_kardex
    for widget in frame_kardex.winfo_children():
        widget.destroy()

    # Llama a la función para mostrar el nuevo contenido
    kardex_viewer.show_kardex_content(frame_kardex, 1)


def show_inscripciones_content():
    ui_main_window.run_entregar_tarea()

def show_horarios_content():
    ui_add_meets.view_meeting_creation()

def show_tareas_asignadas_content():
    pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Página de Inicio de Estudiante")

    # Obtener las dimensiones de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Configurar la geometría de la ventana para que ocupe toda la pantalla
    root.geometry(f"{screen_width}x{screen_height}")

    # Barra superior con botones
    btn_frame = tk.Frame(root)
    btn_frame.pack(side="top")

    btn_kardex = tk.Button(btn_frame, text="Ver Kardex", command=show_kardex_content)
    btn_kardex.grid(row=0, column=0, padx=10)

    btn_inscripciones = tk.Button(btn_frame, text="Inscribirse", command=show_inscripciones_content)
    btn_inscripciones.grid(row=0, column=1, padx=10)

    btn_horarios = tk.Button(btn_frame, text="Ver Horarios", command=show_horarios_content)
    btn_horarios.grid(row=0, column=2, padx=10)

    btn_tareas_asignadas = tk.Button(btn_frame, text="Tareas Asignadas", command=show_tareas_asignadas_content)
    btn_tareas_asignadas.grid(row=0, column=3, padx=10)

    frame_kardex = tk.Frame(root)
    frame_kardex.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)  # Llena todo el espacio sobrante

    root.mainloop()

