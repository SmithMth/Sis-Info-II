import tkinter as tk
from tkinter import filedialog, messagebox
import db_uploadHomeWork as database
from os.path import basename


files_to_upload = []

def show_submission_window(idStudent, idHomeWork):
    window = tk.Tk()
    window.title("Entregar tarea")
    window.geometry("400x400")

    lbl_files = tk.Label(window, text="Archivos seleccionados:")
    lbl_files.pack(pady=10)

    listbox_files = tk.Listbox(window, height=10, width=50)
    listbox_files.pack(pady=10)

    def add_file():
        file = filedialog.askopenfile(title="Selecciona un archivo para la tarea")
        if file:
            files_to_upload.append(file.name)
            file_name_only = basename(file.name)  
            listbox_files.insert(tk.END, file_name_only)


    btn_add_file = tk.Button(window, text="Añadir archivo", command=add_file)
    btn_add_file.pack(pady=10)

    lbl_comment = tk.Label(window, text="Comentario:")
    lbl_comment.pack(pady=10)

    comment = tk.Text(window, height=5, width=40)
    comment.pack(pady=10)

    def save_submission():
        submission_date = "2023-10-15" 
        submission_id = database.add_submission(idStudent, idHomeWork, comment.get("1.0", "end-1c"), submission_date)

        for file_path in files_to_upload:
            with open(file_path, "rb") as f:
                fileContent = f.read()
                fileType = file_path.split('.')[-1]
                database.add_file(submission_id, fileContent, fileType)
        
        messagebox.showinfo("Éxito", "Tarea enviada con éxito!")
        window.destroy()

    btn_submit = tk.Button(window, text="Entregar", command=save_submission)
    btn_submit.pack(pady=20)

    window.mainloop()
