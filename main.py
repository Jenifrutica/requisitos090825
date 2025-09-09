import tkinter as tk
from tkinter import messagebox

# ===== Colores =====
COLOR_DARK = "#2E2F44"    
COLOR_MID = "#7B8BA4"     
COLOR_LIGHT = "#BFD7D5"   
COLOR_WHITE = "#F2F7F7"   

# ===== Idiomas =====
languages = {
    "es": {
        "title": "EduConnect - Plataforma Educativa",
        "welcome": "Bienvenido a EduConnect",
        "pay": "Pagar curso de extensión",
        "success_payment": "Pago realizado con éxito (simulado).",
        "language": "Idioma",
        "exit": "Salir",
        "courses": "Inscripción a Cursos",
        "resources": "Descarga de Recursos",
        "subscribe": "Inscribirse",
        "download": "Descargar"
    },
    "en": {
        "title": "EduConnect - Educational Platform",
        "welcome": "Welcome to EduConnect",
        "pay": "Pay for extension course",
        "success_payment": "Payment completed successfully (simulated).",
        "language": "Language",
        "exit": "Exit",
        "courses": "Course Enrollment",
        "resources": "Download Resources",
        "subscribe": "Enroll",
        "download": "Download"
    }
}
current_lang = "es"

# ===== Funciones Idiomas y Pagos =====
def change_language(lang):
    global current_lang
    current_lang = lang
    update_texts()

def update_texts():
    root.title(languages[current_lang]["title"])
    lbl_welcome.config(text=languages[current_lang]["welcome"])
    btn_pay.config(text=languages[current_lang]["pay"])
    lbl_courses.config(text=languages[current_lang]["courses"])
    lbl_resources.config(text=languages[current_lang]["resources"])
    btn_subscribe.config(text=languages[current_lang]["subscribe"])
    btn_download.config(text=languages[current_lang]["download"])
    menu_bar.entryconfig(1, label=languages[current_lang]["language"])
    menu_bar.entryconfig(2, label=languages[current_lang]["exit"])

def pay_course():
    messagebox.showinfo("Pago", languages[current_lang]["success_payment"])

# ===== Requerimiento 1: Inscripción a Cursos =====
def obtener_cursos():
    return {
        1: "Programación en Python",
        2: "Matemáticas Discretas", 
        3: "Bases de Datos",
        4: "Algoritmos y Estructuras",
        5: "Desarrollo Web"
    }

def inscribir():
    try:
        idx = listbox_cursos.curselection()[0]  # índice seleccionado
        curso_id = idx + 1
        if curso_id in inscripciones:
            messagebox.showwarning("Aviso", "Ya estás inscrito en este curso")
        else:
            inscripciones.append(curso_id)
            messagebox.showinfo("Inscripción", f"Inscrito en: {cursos[curso_id]}")
    except IndexError:
        messagebox.showwarning("Error", "Selecciona un curso")

# ===== Requerimiento 2: Descarga de Recursos =====
def obtener_recursos():
    return {
        1: {"nombre": "Manual de Python", "tipo": "PDF"},
        2: {"nombre": "Ejercicios Matemáticas", "tipo": "DOCX"},
        3: {"nombre": "Guía de SQL", "tipo": "PDF"},
        4: {"nombre": "Algoritmos Básicos", "tipo": "PDF"},
        5: {"nombre": "Plantilla HTML", "tipo": "DOCX"}
    }

def descargar():
    try:
        idx = listbox_recursos.curselection()[0]
        recurso_id = idx + 1
        recurso = recursos[recurso_id]
        messagebox.showinfo(
            "Descarga", 
            f"Descargando {recurso['nombre']} ({recurso['tipo']})...\nCompleto."
        )
    except IndexError:
        messagebox.showwarning("Error", "Selecciona un recurso")

# ===== Ventana principal =====
root = tk.Tk()
root.geometry("650x500")
root.title(languages[current_lang]["title"])
root.configure(bg=COLOR_WHITE)

# Menú superior
menu_bar = tk.Menu(root, bg=COLOR_DARK, fg=COLOR_WHITE, tearoff=0)
root.config(menu=menu_bar)

language_menu = tk.Menu(menu_bar, tearoff=0, bg=COLOR_MID, fg=COLOR_WHITE)
language_menu.add_command(label="Español", command=lambda: change_language("es"))
language_menu.add_command(label="English", command=lambda: change_language("en"))

menu_bar.add_cascade(label=languages[current_lang]["language"], menu=language_menu)
menu_bar.add_command(label=languages[current_lang]["exit"], command=root.quit)

# ===== Sección Bienvenida =====
lbl_welcome = tk.Label(
    root, 
    text=languages[current_lang]["welcome"], 
    font=("Impact", 22),  
    fg=COLOR_DARK,
    bg=COLOR_WHITE
)
lbl_welcome.pack(pady=10)

btn_pay = tk.Button(
    root, 
    text=languages[current_lang]["pay"], 
    command=pay_course, 
    font=("Arial", 12), 
    bg=COLOR_MID,
    fg=COLOR_WHITE
)
btn_pay.pack(pady=5)

# ===== Sección Inscripción a Cursos =====
lbl_courses = tk.Label(root, text=languages[current_lang]["courses"], font=("Arial", 14, "bold"), bg=COLOR_WHITE, fg=COLOR_DARK)
lbl_courses.pack(pady=10)

cursos = obtener_cursos()
inscripciones = []
listbox_cursos = tk.Listbox(root, height=5, font=("Arial", 11), bg=COLOR_LIGHT)
for curso in cursos.values():
    listbox_cursos.insert(tk.END, curso)
listbox_cursos.pack(pady=5)

btn_subscribe = tk.Button(root, text=languages[current_lang]["subscribe"], command=inscribir, bg=COLOR_MID, fg=COLOR_WHITE)
btn_subscribe.pack(pady=5)

# ===== Sección Descarga de Recursos =====
lbl_resources = tk.Label(root, text=languages[current_lang]["resources"], font=("Arial", 14, "bold"), bg=COLOR_WHITE, fg=COLOR_DARK)
lbl_resources.pack(pady=10)

recursos = obtener_recursos()
listbox_recursos = tk.Listbox(root, height=5, font=("Arial", 11), bg=COLOR_LIGHT)
for recurso in recursos.values():
    listbox_recursos.insert(tk.END, f"{recurso['nombre']} ({recurso['tipo']})")
listbox_recursos.pack(pady=5)

btn_download = tk.Button(root, text=languages[current_lang]["download"], command=descargar, bg=COLOR_MID, fg=COLOR_WHITE)
btn_download.pack(pady=5)

# Actualizar textos
update_texts()

root.mainloop()
