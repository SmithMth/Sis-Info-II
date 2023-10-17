import tkinter as tk
from tkinter import Text, Scrollbar, messagebox

def save_note():
    note = text_note.get("1.0", "end-1c")  
    with open("note.txt", "w") as file:
        file.write(note)
    messagebox.showinfo("Note Saved", "The note has been saved successfully.")

window = tk.Tk()
window.title("Note-taking Application")

text_note = Text(window, wrap="word", width=40, height=10)
text_note.pack()

scrollbar = Scrollbar(window, command=text_note.yview)
scrollbar.pack(side="right", fill="y")
text_note.config(yscrollcommand=scrollbar.set)

button_save = tk.Button(window, text="Save Note", command=save_note)
button_save.pack()

window.mainloop()