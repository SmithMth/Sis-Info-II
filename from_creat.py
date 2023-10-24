import tkinter as tk
from tkinter import Canvas, Scrollbar
import database
import json

class ExamGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Examen")
        self.root.geometry("800x600")

        self.all_options = []
        self.all_questions = []

        self.initialize_ui()

    def initialize_ui(self):
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(side="top", fill="x")

        tk.Label(self.btn_frame, text="Nombre del examen: ").pack(side="left")
        self.exam_name_entry = tk.Entry(self.btn_frame, width=30)
        self.exam_name_entry.pack(side="left")

        add_question_button = tk.Button(self.btn_frame, text="Añadir pregunta", command=self.add_multiple_choice)
        add_question_button.pack(side="left")

        save_button = tk.Button(self.btn_frame, text="Guardar", command=self.save_to_db)
        save_button.pack(side="right")

        self.canvas = Canvas(self.root)
        self.scrollbar = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.frame_on_canvas = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_on_canvas, anchor="nw")

        self.frame_on_canvas.bind("<Configure>", self.on_configure)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def add_multiple_choice(self):
        inner_frame = tk.Frame(self.frame_on_canvas)
        inner_frame.pack(fill='x', padx=10, pady=10)

        tk.Label(inner_frame, text="Pregunta de selección múltiple:").grid(row=0, column=0)
        question_entry = tk.Entry(inner_frame, width=50)
        question_entry.grid(row=0, column=1, columnspan=3)

        tk.Label(inner_frame, text="Número de opciones:").grid(row=1, column=0)
        num_options = tk.Spinbox(inner_frame, from_=2, to=10, width=5)
        num_options.grid(row=1, column=1)

        set_button = tk.Button(inner_frame, text="Establecer", command=lambda: self.update_options(inner_frame, num_options, set_button))
        set_button.grid(row=1, column=2)
        self.all_questions.append((inner_frame, question_entry))
        
    def update_options(self, frame, num_options, set_button):
        options_frame = tk.Frame(frame)
        options_frame.grid(row=2, columnspan=4)

        n = int(num_options.get())
        current_options = []
        for i in range(n):
            var = tk.IntVar()
            tk.Checkbutton(options_frame, text=f"Opción {i + 1}", variable=var).grid(row=i, column=0)
            entry = tk.Entry(options_frame, width=40)
            entry.grid(row=i, column=1)
            current_options.append((var, entry))

        self.all_options.append(current_options)
        
        delete_button = tk.Button(frame, text="Eliminar Pregunta", command=lambda: self.delete_question(frame, current_options))
        delete_button.grid(row=3, columnspan=4)
        
        set_button.destroy()

    def delete_question(self, inner_frame, current_options):
        inner_frame.destroy()
        self.all_questions = [(frame, entry) for frame, entry in self.all_questions if frame != inner_frame]
        self.all_options.remove(current_options)

    def save_to_db(self):
        conn = database.get_connection()
        cur = conn.cursor()
        exam_name = self.exam_name_entry.get()
        questions_and_options = {
            "questions": []
        }

        for idx, (_, question_entry) in enumerate(self.all_questions):
            question = {
                "text": question_entry.get(),
                "options": []
            }
            for var, entry in self.all_options[idx]:
                option = {
                    "text": entry.get(),
                    "is_checked": bool(var.get())
                }
                question["options"].append(option)
            
            questions_and_options["questions"].append(question)

        cur.callproc('save_exam', [exam_name, json.dumps(questions_and_options)])

        conn.commit()
        cur.close()
        conn.close()


    def on_configure(self, event):
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1*(event.delta//120), "units")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExamGeneratorApp(root)
    root.mainloop()
