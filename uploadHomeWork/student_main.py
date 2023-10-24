import tkinter as tk
import tkinter.font as tkFont
import kardex_viewer 
import ui_main_window, ui_add_meets
import teacher_main,proffesor_profile,iu_apuntes,ui_room_reservation,homeworkNotification

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
    teacher_main.vistaCrearExamen()

def show_docente():
    proffesor_profile.vista_docnete()

def show_notas():
    iu_apuntes.show_notas()

def show_reservar():
    ui_room_reservation.show_reservar()

def enviar_noti():
    homeworkNotification.show_confirmation()

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

    btn_inscripciones = tk.Button(btn_frame, text="Entregar Tarea", command=show_inscripciones_content)
    btn_inscripciones.grid(row=0, column=1, padx=10)

    btn_horarios = tk.Button(btn_frame, text="crear Meets", command=show_horarios_content)
    btn_horarios.grid(row=0, column=2, padx=10)

    btn_tareas_asignadas = tk.Button(btn_frame, text="crear examen", command=show_tareas_asignadas_content)
    btn_tareas_asignadas.grid(row=0, column=3, padx=10)

    btn_tareas_asignadas2 = tk.Button(btn_frame, text="perfil de docentes", command=show_docente)
    btn_tareas_asignadas2.grid(row=0, column=4, padx=10)

    btn_tareas_asignadas3 = tk.Button(btn_frame, text="Notas personales", command=show_notas)
    btn_tareas_asignadas3.grid(row=0, column=5, padx=10)

    btn_tareas_asignadas4 = tk.Button(btn_frame, text="Reservar Aula", command=show_reservar)
    btn_tareas_asignadas4.grid(row=0, column=6, padx=10)

    btn_tareas_asignadas5 = tk.Button(btn_frame, text="Enviar Recordatorio", command=enviar_noti)
    btn_tareas_asignadas5.grid(row=0, column=7, padx=10)


    frame_kardex = tk.Frame(root)
    frame_kardex.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)  # Llena todo el espacio sobrante

    root.mainloop()

