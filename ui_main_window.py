
import tkinter as tk
import db_uploadHomeWork as database
import ui_submission_window as ui_submission_window

root = tk.Tk()
root.title("Información de la Tarea")
root.geometry("900x500")  # Ventana más rectangular
root.configure(bg='white')  # Fondo blanco

# Asumo que ya tienes el idAssinament e idHomeWork de algún modo. Aquí uso 1 como ejemplo.
idAssinament = 1
idHomeWork = 1

subject_name = database.get_subject_name(idAssinament)
assignment_details = database.get_assignment_details(idHomeWork)

# Encabezado con el nombre de la materia
lbl_subject = tk.Label(root, text=subject_name, font=("Arial", 24, "bold"), anchor="w", bg='white')  # Fondo blanco
lbl_subject.place(x=20, y=10)

# Etiqueta "Tarea"
lbl_task_label = tk.Label(root, text="Tarea", font=("Arial", 18), anchor="w", bg='white')
lbl_task_label.place(x=20, y=60)

# Nombre de la tarea
lbl_task_name = tk.Label(root, text=assignment_details["title"], font=("Arial", 20), anchor="w", bg='white')
lbl_task_name.place(x=20, y=100)

# Descripción de la tarea
lbl_task_description = tk.Label(root, text=assignment_details["description"], font=("Arial", 16), wraplength=550, justify="left", anchor="w", bg='white')
lbl_task_description.place(x=20, y=150)

# Fecha de vencimiento a la derecha
lbl_due_date = tk.Label(root, text=f"Fecha de vencimiento: {assignment_details['due_date']}", font=("Arial", 18), bg='white')
lbl_due_date.place(relx=0.7, rely=0.1, anchor="center")

# Botón para realizar entrega
def open_submission_window():
    ui_submission_window.show_submission_window(idStudent=1, idHomeWork=1)
    root.destroy()

btn_submit = tk.Button(root, text="Realizar entrega", command=open_submission_window, font=("Arial", 16))
btn_submit.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()
