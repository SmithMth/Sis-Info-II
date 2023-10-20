import tkinter as tk
from tkinter import messagebox
import psycopg2

id_student = int(1)
idassinament = int(1)

nameN = None
subjectN = None
themeN = None 
noteN = None


def saveNote():
    global nameN, subjectN, themeN, noteN
    nameN = nameEntry.get()
    subjectN = subjectEntry.get()
    themeN = themeEntry.get()
    noteN = noteText.get(1.0, "end-1c")  # Obtenemos el texto de la nota


    save = saveNotainDB()
    if save:
        messagebox.showinfo("Guardado", "La nota ha sido guardada exitosamente.")
    else:
        messagebox.showinfo("Error", "No esta inscrito en la materia")
    

def saveNotainDB():
    
    global nameN, subjectN, themeN, noteN
    hostname = "localhost"
    database = "sisII_FINAL"
    username = "postgres"
    password = "123456"



    conn = psycopg2.connect(
        host=hostname,
        database=database,
        user=username,
        password=password
    )

    cursor = conn.cursor()
    subjectName = subjectN
    student_id = id_student 
    cursor.execute("SELECT is_student_enrolled(%s, %s);", (student_id, subjectName))
    ##cursor.callproc("get_idassinament", [nameSearch])
    result = cursor.fetchone()[0]
    

    if idassinament == result:
        cursor.callproc("insert_note", (id_student,idassinament ,str(nameN), str(subjectN), str(themeN), str(noteN)))
        conn.commit()
        save = True
    else:
        save = False
    cursor.close()
    conn.close()
    return save

# Creamos la ventana
window = tk.Tk()
window.title("Crear nueva nota")

# Creacion de los label e inputs
nameLabel = tk.Label(window, text="Nombre:")
nameLabel.pack()
nameEntry = tk.Entry(window)
nameEntry.pack()

subjectLabel = tk.Label(window, text="Materia:")
subjectLabel.pack()
subjectEntry = tk.Entry(window)
subjectEntry.pack()

themeLabel = tk.Label(window, text="Tema:")
themeLabel.pack()
themeEntry = tk.Entry(window)
themeEntry.pack()

noteLabel = tk.Label(window, text="Nota:")
noteLabel.pack()
noteText = tk.Text(window, height=10, width=40)
noteText.pack()

# Boton de guardar
saveButton = tk.Button(window, text="Guardar", command=saveNote)
saveButton.pack()

# Inicia la aplicacion
window.mainloop()