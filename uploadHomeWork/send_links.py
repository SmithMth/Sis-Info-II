from tkinter import messagebox
import psycopg2
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk

def get_meet_link():
    try:
        # Connect to the database
        connection = psycopg2.connect(
            database="sisII_FINAL",
            user="postgres",
            password="123456",
            host="localhost"
        )
        cursor = connection.cursor()

        # SQL query to fetch "name" and "link" based on the specified conditions
        query = """
            SELECT m.idassinament, m.link, s.name, m.hour, m.datestart, m.dateend
            FROM meet AS m
            INNER JOIN subject AS s ON m.idassinament = s.idassinament
            ORDER BY m.id DESC
            LIMIT 1
        """
        cursor.execute(query)
        fetched_records = cursor.fetchall()

        print(fetched_records)

        for record in fetched_records:
            id_subject, link, name_subject, hora, star_fecha, end_fecha = record  
            query_student = """
                SELECT e.name, e.email
                FROM student AS e 
                INNER JOIN student_assignament sa ON e.idstudent = sa.idstudent
                WHERE idassignament = %s
            """
            cursor.execute(query_student, (id_subject,))
            for name_student, email_to_send in cursor.fetchall():
                send_meet(name_student, name_subject, link, email_to_send, hora, star_fecha, end_fecha)


    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while fetching and sending meet links:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

def send_meet(name, name_subject, link, email,hora,star_fecha, end_fecha):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = 'fantasticos705@gmail.com' 
    password = 'wdoy xmzx zcwt recw'
    sender = 'fantasticos705@gmail.com'  # Replace with your Gmail address

    addressee = email

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = addressee
    message['Subject'] = name_subject
    body = f"""
    Hola estimado {name},
    
    Tienes una reunión programada para la materia {name_subject}:
    Enlace de la reunión: {link}
    Fecha de inicio: {star_fecha}
    Fecha de finalización: {end_fecha}
    Hora: {hora}
    """
    message.attach(MIMEText(body, 'plain'))

    waiting_window = tk.Toplevel()
    waiting_window.geometry("200x100")
    waiting_label = tk.Label(waiting_window, text="Espere por favor...")
    waiting_label.pack(pady=20)
    waiting_window.update()  # Esto es importante para asegurarse de que la ventana se muestre antes de continuar
    try:
        server_smtp = smtplib.SMTP(smtp_server, smtp_port)
        server_smtp.starttls()
        server_smtp.login(username, password)
        server_smtp.sendmail(sender, addressee, message.as_string())
        server_smtp.quit()
        print("Correo enviado con éxito")
        waiting_window.destroy()
        messagebox.showinfo("Éxito", "Reunion programada con exito")
    except Exception as e:
        waiting_window.destroy()
        print("Error al enviar el correo:", str(e))


    