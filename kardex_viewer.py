import tkinter as tk
from tkinter import ttk  # Importa el módulo ttk para el widget Treeview
from uploadHomeWork import db_uploadHomeWork as database

def show_kardex_content(frame_kardex, student_id):
    # Función para mostrar el contenido del kardex en el frame_kardex proporcionado.

    # Lógica para obtener los datos del kardex desde la base de datos
    kardex_data = database.get_student_grades(student_id)

    # Crea un widget Treeview para mostrar los datos en una tabla
    kardex_table = ttk.Treeview(frame_kardex, columns=("Subject", "Level", "Enrollment Year", "First Partial", "Second Partial", "Final Exam", "Final Grade", "RFIN"), show="headings")
    
    # Configura las columnas de la tabla
    kardex_table.heading("Subject", text="Subject")
    kardex_table.heading("Level", text="Level")
    kardex_table.heading("Enrollment Year", text="Enrollment Year")
    kardex_table.heading("First Partial", text="First Partial")
    kardex_table.heading("Second Partial", text="Second Partial")
    kardex_table.heading("Final Exam", text="Final Exam")
    kardex_table.heading("Final Grade", text="Final Grade")
    kardex_table.heading("RFIN", text="RFIN")
    
    # Ajusta el ancho de las columnas para que ocupen todo el ancho del widget
    for column in ("Subject", "Level", "Enrollment Year", "First Partial", "Second Partial", "Final Exam", "Final Grade", "RFIN"):
        kardex_table.column(column, width=100)  # Puedes ajustar el ancho según tus necesidades

    # Agrega los datos del kardex a la tabla
    for row in kardex_data:
        kardex_table.insert("", "end", values=row)
    
    # Empaqueta la tabla en el frame_kardex
    kardex_table.pack(fill="both", expand=True)
    # Después de obtener los datos del kardex desde la base de datos
    kardex_data = database.get_student_grades(student_id)

    # Inicializa variables para rastrear la información
    total_materias_cursadas = len(kardex_data)
    total_materias_aprobadas = 0
    total_materias_reprobadas = 0
    total_materias_abandonadas = 0
    suma_calificaciones = 0

    # Calcula los totales y promedios
    for row in kardex_data:
        final_grade = row[6]  # Supongo que la calificación final está en la columna 6
        if final_grade >= 51:
            total_materias_aprobadas += 1
        elif final_grade == -1:  # Supongo que -1 indica que una materia fue abandonada
            total_materias_abandonadas += 1
        else:
            total_materias_reprobadas += 1
        suma_calificaciones += final_grade

    # Calcula el promedio general y el promedio de las materias aprobadas
    promedio_general = suma_calificaciones / total_materias_cursadas if total_materias_cursadas > 0 else 0
    promedio_aprobadas = suma_calificaciones / total_materias_aprobadas if total_materias_aprobadas > 0 else 0

    # Crea etiquetas para mostrar los totales y promedios
    label_total_cursadas = tk.Label(frame_kardex, text=f"Total de materias cursadas: {total_materias_cursadas}")
    label_total_aprobadas = tk.Label(frame_kardex, text=f"Total de materias aprobadas: {total_materias_aprobadas}")
    label_total_reprobadas = tk.Label(frame_kardex, text=f"Total de materias reprobadas: {total_materias_reprobadas}")
    label_total_abandonadas = tk.Label(frame_kardex, text=f"Total de materias abandonadas: {total_materias_abandonadas}")
    label_promedio_general = tk.Label(frame_kardex, text=f"Promedio general: {promedio_general:.2f}")
    label_promedio_aprobadas = tk.Label(frame_kardex, text=f"Promedio de materias aprobadas: {promedio_aprobadas:.2f}")

    # Empaqueta las etiquetas en el frame
    label_total_cursadas.pack()
    label_total_aprobadas.pack()
    label_total_reprobadas.pack()
    label_total_abandonadas.pack()
    label_promedio_general.pack()
    label_promedio_aprobadas.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Kardex Viewer")

    # Crea un frame para mostrar el contenido del kardex.
    frame_kardex = tk.Frame(root)
    frame_kardex.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Define el ID del estudiante (debes ajustarlo según tu base de datos)
    student_id = 1  # Por ejemplo, asumamos que el ID del estudiante es 1.

    # Muestra el contenido del kardex en el frame.
    show_kardex_content(frame_kardex, student_id)

    root.mainloop()
