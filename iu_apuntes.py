import tkinter as tk
from tkinter import messagebox

def saveNote():
    name = nameEntry.get()
    subject = subjectEntry.get()
    theme = themeEntry.get()
    note = noteText.get(1.0, "end-1c")  # Obtenemos el texto de la nota

    messagebox.showinfo("Saved", "Note saved successfully.")

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