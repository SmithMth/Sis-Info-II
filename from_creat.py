import tkinter as tk

def add_multiple_choice(frame):
    inner_frame = tk.Frame(frame)
    inner_frame.pack()
    
    tk.Label(inner_frame, text="Pregunta de selección múltiple:").grid(row=0, column=0)
    tk.Entry(inner_frame, width=50).grid(row=0, column=1)

    tk.Label(inner_frame, text="Número de opciones:").grid(row=1, column=0)
    num_options = tk.Spinbox(inner_frame, from_=2, to=10, width=5)
    num_options.grid(row=1, column=1)

    tk.Button(inner_frame, text="Actualizar", command=lambda: update_options(options_frame, num_options)).grid(row=1, column=2)

    options_frame = tk.Frame(inner_frame)
    options_frame.grid(row=2, columnspan=3)

    tk.Label(inner_frame, text="Respuesta correcta:").grid(row=3, column=0)
    tk.Entry(inner_frame, width=20).grid(row=3, column=1)
    tk.Label(inner_frame, text="---").grid(row=4, columnspan=3)

def update_options(frame, num_options):
    for widget in frame.winfo_children():
        widget.destroy()
    n = int(num_options.get())
    for i in range(n):
        tk.Entry(frame, width=40).pack()
        
def add_true_false(frame):
    inner_frame = tk.Frame(frame)
    inner_frame.pack()
    
    tk.Label(inner_frame, text="Pregunta de Verdadero o Falso:").grid(row=0, column=0)
    tk.Entry(inner_frame, width=50).grid(row=0, column=1)

    tk.Label(inner_frame, text="Respuesta correcta:").grid(row=1, column=0)
    tk.Entry(inner_frame, width=20).grid(row=1, column=1)
    tk.Label(inner_frame, text="---").grid(row=2, columnspan=2)

def add_matching(frame):
    inner_frame = tk.Frame(frame)
    inner_frame.pack()

    tk.Label(inner_frame, text="Pregunta de Asociar con flechas:").grid(row=0, column=0)
    tk.Entry(inner_frame, width=50).grid(row=0, column=1)

    tk.Label(inner_frame, text="Número de emparejamientos:").grid(row=1, column=0)
    num_pairs = tk.Spinbox(inner_frame, from_=2, to=10, width=5)
    num_pairs.grid(row=1, column=1)

    tk.Button(inner_frame, text="Actualizar", command=lambda: update_pairs(pairs_frame, num_pairs)).grid(row=1, column=2)

    pairs_frame = tk.Frame(inner_frame)
    pairs_frame.grid(row=2, columnspan=3)

    tk.Label(inner_frame, text="---").grid(row=3, columnspan=3)

def update_pairs(frame, num_pairs):
    for widget in frame.winfo_children():
        widget.destroy()
    n = int(num_pairs.get())
    for i in range(n):
        tk.Entry(frame, width=20).pack(side="left")
        tk.Label(frame, text="<->").pack(side="left")
        tk.Entry(frame, width=20).pack(side="left")
        tk.Button(frame, text="Eliminar").pack(side="left")
        
def add_q_and_a(frame):
    tk.Label(frame, text="Pregunta y Respuesta:").pack()
    tk.Entry(frame, width=50).pack()
    tk.Label(frame, text="---").pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Generador de Examen")

    frame_content = tk.Frame(root)
    frame_content.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    btn_frame = tk.Frame(root)
    btn_frame.pack(side="top")

    tk.Button(btn_frame, text="Selección múltiple", command=lambda: add_multiple_choice(frame_content)).grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="Verdadero o Falso", command=lambda: add_true_false(frame_content)).grid(row=0, column=1, padx=10)
    tk.Button(btn_frame, text="Asociar con flechas", command=lambda: add_matching(frame_content)).grid(row=0, column=2, padx=10)
    tk.Button(btn_frame, text="Pregunta y Respuesta", command=lambda: add_q_and_a(frame_content)).grid(row=0, column=3, padx=10)

    root.mainloop()
