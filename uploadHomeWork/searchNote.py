import tkinter as tk
from tkinter import messagebox
import psycopg2

def search_note():
    note_name = name_entry.get()
    conn = psycopg2.connect(
        database="sisII_FINAL",
        user="postgres",
        password="123456",
        host="localhost"
    )
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM notes WHERE nameN = %s", (note_name,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result is not None:
        id_notes, id_student, idassignment, nameN, subjectN, themeN, noteN = result
        result_text.config(text=f"Nombre: {nameN}\nMateria: {subjectN}\nTema: {themeN}\nNota: {noteN}")
    else:
        result_text.config(text="La nota no existe.")

# Crear la ventana principal
window = tk.Tk()
window.title("Buscar Nota")

# Crear etiqueta y campo de entrada
name_label = tk.Label(window, text="Nombre de la Nota:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Botón de búsqueda
search_button = tk.Button(window, text="Buscar Nota", command=search_note)
search_button.pack()

# Etiqueta de resultado
result_text = tk.Label(window, text="", justify=tk.LEFT)  # Alineación a la izquierda
result_text.pack()

# Iniciar la aplicación
window.mainloop()