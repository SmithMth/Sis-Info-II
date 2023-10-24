import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
from tkinter import ttk
import psycopg2
import send_links

# Declaramos las variables globales
global cal_start, cal_end, time_entry, subject_combobox

def generate_meet_link():
    # Usamos las variables globales
    global cal_start, cal_end, time_entry, subject_combobox

    start_date = cal_start.get_date()
    end_date = cal_end.get_date()
    time = time_entry.get()
    subject = subject_combobox.get()
    # Genera el enlace de Google Meet
    meet_link = "https://meet.google.com/gxh-qqgc-vin"
    
    # Conexión a la base de datos
    try:
        connection = psycopg2.connect(
            database="sisII_FINAL",
            user="postgres",
            password="123456",
            host="localhost"
        )
        cursor = connection.cursor()
        query = """
            SELECT idassinament 
            FROM subject 
            WHERE name = %s
        """
        cursor.execute(query, (subject,))
        result = cursor.fetchone()
        
        # Falta corregir el id de maestro 
        cursor.callproc('insert_meet', (result[0], start_date, end_date, time, meet_link))
        connection.commit()
        send_links.get_meet_link()
        

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al insertar datos:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

def get_subjects():
    answer = []
    connection = None
    try:
        connection = psycopg2.connect(
            database="sisII_FINAL",
            user="postgres",
            password="123456",
            host="localhost"
        )
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

def view_meeting_creation():
    global cal_start, cal_end, time_entry, subject_combobox

    window = tk.Tk()
    window.title("Programar Videollamada")

    cal_start = Calendar(window, date_pattern='yyyy-mm-dd')
    cal_start.pack()

    cal_end = Calendar(window, date_pattern='yyyy-mm-dd')
    cal_end.pack()

    time_label = tk.Label(window, text="Hora (HH:MM):")
    time_label.pack()
    time_entry = tk.Entry(window)
    time_entry.pack()

    subjects = get_subjects()
    subject_label = tk.Label(window, text="Selecciona una materia:")
    subject_label.pack()
    subject_combobox = ttk.Combobox(window, values=subjects)
    subject_combobox.pack()
    subject_combobox.set(subjects[0])

    generate_button = tk.Button(window, text="Programar y Generar Enlace", command=generate_meet_link)
    generate_button.pack()

    window.mainloop()


