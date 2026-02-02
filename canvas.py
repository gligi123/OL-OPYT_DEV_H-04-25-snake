import tkinter as tk
import customtkinter as ctk


STEP = 150

# root = tk.Tk()
root = ctk.CTk()
root.title('Tkinter canvas demo')

lbl_title = ctk.CTkLabel(root, text='Canvas demo', font=('Verdana', 18))
lbl_title.pack(pady=25)

canvas = ctk.CTkCanvas(root, width=800, height=600, bg='black')
canvas.pack()

canvas.create_text(10, 10, anchor='nw', fill='white', text='Tekst unutar Canvas widget-a')
canvas.create_oval(25, 25, 75, 75, fill='red', outline='')
canvas.create_rectangle(25 + STEP, 25 + STEP, 75 + STEP, 75 + STEP, fill='red', outline='')


root.mainloop()
