import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
from tkinter import ttk
import psycopg2

def generate_meet_link():
    start_date = cal_start.get_date()
    end_date = cal_end.get_date()
    time = time_entry.get()
    subject = subject_combobox.get()
    # Genera el enlace de Google Meet
    meet_link = "https://meet.google.com/gxh-qqgc-vin"
    #coneccion a la base de datos
    try:
        # Conectarse a la base de datos
        connection = psycopg2.connect(
            host="b0zyrecsgde9whh1dmka-postgresql.services.clever-cloud.com",
            database="b0zyrecsgde9whh1dmka",
            user="uehhymdo1hkrhqcxc3qz",
            password="WCWL5On4oVwb5AOnWjDYGi5KCvyiAY"
        )
        cursor = connection.cursor()
        query = """
            SELECT idassinament 
            FROM subject 
            WHERE name = %s
        """
        cursor.execute(query,subject)
        result = int(cursor.fetchone()) 
        #falta corregir el id de maestro 
        cursor.callproc('insertar_meet', (2, result, start_date, end_date, time, meet_link))
        connection.commit()
        messagebox.showinfo("Éxito", "Datos insertados correctamente")
        

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al insertar datos:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()  

def get_subjects():
    answer = []
    connection = None  # Inicializa la variable connection como None
    try:
        # Conectarse a la base de datos
        connection = psycopg2.connect(
            host="b0zyrecsgde9whh1dmka-postgresql.services.clever-cloud.com",
            database="b0zyrecsgde9whh1dmka",
            user="uehhymdo1hkrhqcxc3qz",
            password="WCWL5On4oVwb5AOnWjDYGi5KCvyiAY")
        cursor = connection.cursor()
        query = """SELECT name FROM subject"""
        cursor.execute(query,)
        answer = cursor.fetchall()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al conectar", error)

    finally:
        if connection:
            cursor.close()
            connection.close() 

    return answer


#--------------------------------------------------------------------------------------------------
    

window = tk.Tk()
window.title("Programar Videollamada")

# Agregar el calendario de fecha de inicio
cal_start = Calendar(window, date_pattern='yyyy-mm-dd')
cal_start.pack()

# Agregar el calendario de fecha de finalización
cal_end = Calendar(window, date_pattern='yyyy-mm-dd')
cal_end.pack()

time_label = tk.Label(window, text="Hora (HH:MM):")
time_label.pack()
time_entry = tk.Entry(window)
time_entry.pack()

# Agregar el Combobox para las materias
# Lista de nombres de materias
subjects = get_subjects()
subject_label = tk.Label(window, text="Selecciona una materia:")
subject_label.pack()
subject_combobox = ttk.Combobox(window, values=subjects)
subject_combobox.pack()
subject_combobox.set(subjects[0])  # Establece el valor predeterminado



generate_button = tk.Button(window, text="Programar y Generar Enlace", command=generate_meet_link)
generate_button.pack()


window.mainloop()
