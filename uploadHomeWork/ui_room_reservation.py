import tkinter as tk
import tkinter.messagebox as mbox
from db_uploadHomeWork import get_all_classrooms, get_available_time_slots, reserve_classroom, get_all_time_slots, get_student_reservations

def open_time_slot_selection_window(classroom_id):
    win_timeslots = tk.Toplevel(root)
    win_timeslots.title("Horarios disponibles")
    win_timeslots.geometry("600x400")

    lbl_header = tk.Label(win_timeslots, text="Selecciona un horario:", font=("Arial", 20))
    lbl_header.pack(pady=20)

    # Supongamos que la fecha de reserva es el día de hoy. Si necesitas otra lógica, ajusta esto.
    from datetime import date
    current_date = date.today()

    # Usamos nuestra nueva función para obtener todos los horarios
    all_slots = get_all_time_slots()
    available_slots_ids = [slot[0] for slot in get_available_time_slots(classroom_id, current_date)]

    for slot in all_slots:
        is_available = slot[0] in available_slots_ids
        btn_slot = tk.Button(win_timeslots, text=f"{slot[1]} - {slot[2]}", 
                             bg="green" if is_available else "red",
                             command=lambda sid=slot[0]: reserve_slot(classroom_id, sid, current_date) if is_available else None)
        btn_slot.pack(pady=10)



def reserve_slot(classroom_id, time_slot_id, date):
    # Aquí, verificamos si el horario seleccionado está disponible antes de intentar la reserva.
    available_slots = get_available_time_slots(classroom_id, date)
    if time_slot_id not in [slot[0] for slot in available_slots]:
        mbox.showerror("Error", "El horario seleccionado no está disponible.")
        return

    # Supongo que el estudiante tiene un ID, aquí pongo un ejemplo con el ID 1.
    student_id = 1
    reserve_classroom(classroom_id, time_slot_id, student_id, date)
    mbox.showinfo("Éxito", "Aula reservada exitosamente!")

def show_student_reservations():
    student_id = 1  # Asume que este es el ID del estudiante actual. Ajusta según tu implementación.

    reservations = get_student_reservations(student_id)

    win_reservations = tk.Toplevel(root)
    win_reservations.title("Mis Reservas")
    win_reservations.geometry("700x400")

    lbl_header = tk.Label(win_reservations, text="Mis Reservas:", font=("Arial", 20))
    lbl_header.pack(pady=20)

    # Creando un marco para la tabla y organizando widgets con grid dentro de este marco.
    frame_table = tk.Frame(win_reservations)
    frame_table.pack(pady=20)

    # Creando la tabla dentro del marco
    for idx, reservation in enumerate(reservations):
        lbl_classroom = tk.Label(frame_table, text=reservation[0], font=("Arial", 14))
        lbl_classroom.grid(row=idx+1, column=0, padx=10, pady=5)

        lbl_capacity = tk.Label(frame_table, text=str(reservation[1]), font=("Arial", 14))
        lbl_capacity.grid(row=idx+1, column=1, padx=10, pady=5)

        lbl_time = tk.Label(frame_table, text=f"{reservation[2]} - {reservation[3]}", font=("Arial", 14))
        lbl_time.grid(row=idx+1, column=2, padx=10, pady=5)

    # Agregando encabezados
    lbl_classroom_header = tk.Label(frame_table, text="Aula", font=("Arial", 16, "bold"))
    lbl_classroom_header.grid(row=0, column=0, padx=10, pady=10)

    lbl_capacity_header = tk.Label(frame_table, text="Capacidad", font=("Arial", 16, "bold"))
    lbl_capacity_header.grid(row=0, column=1, padx=10, pady=10)

    lbl_time_header = tk.Label(frame_table, text="Tiempo", font=("Arial", 16, "bold"))
    lbl_time_header.grid(row=0, column=2, padx=10, pady=10)

def show_reservar():
    global root
    root = tk.Tk()
    root.title("Sistema de Reservas")
    root.geometry("800x500")

    lbl_title = tk.Label(root, text="Sistema de Reservas de Aulas", font=("Arial", 24, "bold"))
    lbl_title.pack(pady=20)
    btn_my_reservations = tk.Button(root, text="Mis Reservas", command=show_student_reservations, font=("Arial", 20))
    btn_my_reservations.pack(pady=20)


    # Mostramos directamente las aulas disponibles en la ventana principal
    for classroom in get_all_classrooms():
        btn_classroom = tk.Button(root, text=f"{classroom[1]} - Capacidad: {classroom[2]}", 
                                command=lambda cid=classroom[0]: open_time_slot_selection_window(cid))
        btn_classroom.pack(pady=10)

    root.mainloop()
