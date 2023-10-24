import smtplib
import tkinter as tk
from tkinter import simpledialog, Listbox
import psycopg2  
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import Listbox, Tk, messagebox



data = None

def get_homeworks(subject_id):
    global data
    database="sisII_FINAL"
    user="postgres"
    password="123456"
    host="localhost"

    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    cursor = conn.cursor()
    cursor.callproc('GetNextHomeworks', (subject_id,))
    data = cursor.fetchall()
    cursor.close()
    conn.close()  

def get_subjects():
    subjects = []
    connection = None
    try:
        connection = psycopg2.connect(
            database="sisII_FINAL",
            user="postgres",
            password="123456",
            host="localhost"
        )
        cursor = connection.cursor()
        query = """SELECT idassinament, name FROM subject"""  # Añadido idassinament
        cursor.execute(query,)
        subjects = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al conectar", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
    return subjects  # Devolvemos la lista de materias con sus IDs


         

def send_notification():

    global data

    smtp_server = 'smtp.gmail.com'  
    smtp_port = 587  
    username = 'fantasticos705@gmail.com'
    password = 'wdoy xmzx zcwt recw'


    print(data)
    sender = 'fantasticos705@gmail.com'

    for item in data:
        name = str(item[0])
        title = str(item[1])
        email = str(item[2])
        due_date = str(item[2])
        name_subject = str(item[2])
        

        addressee = email


        
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = addressee
        message['Subject'] = title
        body = "Hola " + name + ", la tarea " + title + " de la materia "+name_subject+" se entrega pronto. Vence el" + due_date + "."
        message.attach(MIMEText(body, 'plain'))

        
            # Crear una nueva ventana emergente para mostrar el mensaje de espera
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
            
            waiting_window.destroy()  # Destruir la ventana de espera
            messagebox.showinfo("Confirmación", "Las notificaciones han sido enviadas con éxito")
        except Exception as e:
            waiting_window.destroy()  # Destruir la ventana de espera en caso de error también
            print("Error al enviar el correo:", str(e))
            messagebox.showerror("Error", "Ocurrió un error al enviar el correo.")


def show_confirmation(subject_id):
    get_homeworks(subject_id)
    send_notification()

def select_subject_and_get_id():
    # Obtener la lista de materias
    subjects = get_subjects()
    
    # Función que se ejecutará al hacer click en una materia
    def on_select(evt):
        # Dado que el widget es una instancia de Listbox, usamos curselection() para obtener el índice seleccionado
        index = listbox.curselection()[0]
        selected_subject = subjects[index]
        print(f"Has seleccionado {selected_subject[1]} con ID {selected_subject[0]}")
        show_confirmation(selected_subject[0])
        root.destroy()  # Cerrar la ventana tras seleccionar una materia
    
    # Crear una ventana
    root = tk.Tk()
    root.title("Selecciona una materia")

    listbox = Listbox(root)
    listbox.pack(pady=20)

    # Añadir materias al listbox
    for _, subject_name in subjects:
        listbox.insert(tk.END, subject_name)

    # Asignar función al evento de selección
    listbox.bind('<<ListboxSelect>>', on_select)

    root.mainloop()

# Llamar a la función para probar



 
