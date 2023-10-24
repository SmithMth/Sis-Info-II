import tkinter as tk
from tkinter import messagebox

import database
import json

class ExamSolverApp:
    def __init__(self, root, exam_id):
        self.root = root
        self.root.title("Resolver Examen")
        self.root.geometry("800x600")

        self.exam_id = 6
        self.answer_vars = []  # Lista para almacenar las variables IntVar de Tkinter para cada opción

        self.initialize_ui()

    def get_exam_from_db(self):
        conn = database.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT get_exam(%s);", [self.exam_id])
        exam_data = cur.fetchone()[0]
        cur.close()
        conn.close()

        return exam_data

    def initialize_ui(self):
        exam_data = self.get_exam_from_db()

        tk.Label(self.root, text=f"Examen: {exam_data['name']}").pack()

        for question_data in exam_data['questions']:
            question_frame = tk.Frame(self.root)
            question_frame.pack(pady=10)

            tk.Label(question_frame, text=question_data['question_text']).pack()
            current_question_vars = []

            for option in question_data['options']:
                var = tk.IntVar()
                tk.Checkbutton(question_frame, text=option['option_text'], variable=var).pack()
                current_question_vars.append((var, option['is_checked']))

            self.answer_vars.append(current_question_vars)

        tk.Button(self.root, text="Enviar respuestas", command=self.submit_answers).pack(pady=10)
        
    def submit_answers(self):
        score = 0
        total_questions = len(self.answer_vars)

        for question_vars in self.answer_vars:
            if all((var.get() == 1) == is_checked for var, is_checked in question_vars):
                score += 1

        percentage = (score / total_questions) * 100
        messagebox.showinfo("Resultado", f"Respuestas correctas: {score}/{total_questions} ({percentage:.2f}%)")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExamSolverApp(root, 1)  # Supongamos que el ID del examen que quieres resolver es 1
    root.mainloop()