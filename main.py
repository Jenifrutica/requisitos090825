import tkinter as tk
from tkinter import messagebox

# Colorsitos
COLOR_DARK = "#2E2F44"    
COLOR_MID = "#7B8BA4"     
COLOR_LIGHT = "#BFD7D5"   
COLOR_WHITE = "#F2F7F7"   

# Req. idiomas
languages = {
    "es": {
        "title": "EduConnect - Plataforma Educativa",
        "welcome": "Bienvenido a EduConnect",
        "pay": "Pagar curso de extensión",
        "success_payment": "Pago realizado con éxito (simulado).",
        "language": "Idioma",
        "exit": "Salir"
    },
    "en": {
        "title": "EduConnect - Educational Platform",
        "welcome": "Welcome to EduConnect",
        "pay": "Pay for extension course",
        "success_payment": "Payment completed successfully (simulated).",
        "language": "Language",
        "exit": "Exit"
    }
}

current_lang = "es"

def change_language(lang):
    global current_lang
    current_lang = lang
    update_texts()

def update_texts():
    root.title(languages[current_lang]["title"])
    lbl_welcome.config(text=languages[current_lang]["welcome"])
    btn_pay.config(text=languages[current_lang]["pay"])
    menu_bar.entryconfig(1, label=languages[current_lang]["language"])
    menu_bar.entryconfig(2, label=languages[current_lang]["exit"])

def pay_course():
    messagebox.showinfo("Pago", languages[current_lang]["success_payment"])

# Ventana principal
root = tk.Tk()
root.geometry("500x300")
root.title(languages[current_lang]["title"])
root.configure(bg=COLOR_WHITE)

# Menú superior
menu_bar = tk.Menu(root, bg=COLOR_DARK, fg=COLOR_WHITE, tearoff=0)
root.config(menu=menu_bar)

# Submenú de idiomas
language_menu = tk.Menu(menu_bar, tearoff=0, bg=COLOR_MID, fg=COLOR_WHITE)
language_menu.add_command(label="Español", command=lambda: change_language("es"))
language_menu.add_command(label="English", command=lambda: change_language("en"))

menu_bar.add_cascade(label=languages[current_lang]["language"], menu=language_menu)
menu_bar.add_command(label=languages[current_lang]["exit"], command=root.quit)

# Welcome mensaje
lbl_welcome = tk.Label(
    root, 
    text=languages[current_lang]["welcome"], 
    font=("Impact", 22),  
    fg=COLOR_DARK,
    bg=COLOR_WHITE
)
lbl_welcome.pack(pady=30)

# Botón de pago 
btn_pay = tk.Button(
    root, 
    text=languages[current_lang]["pay"], 
    command=pay_course, 
    font=("Arial", 12), 
    bg=COLOR_MID,
    fg=COLOR_WHITE,
    activebackground=COLOR_LIGHT,
    activeforeground=COLOR_DARK
)
btn_pay.pack(pady=15)

update_texts()

root.mainloop()
