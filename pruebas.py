import json
import subprocess
from ttkbootstrap import Window, Frame, Label, Entry, Combobox, Button
from ttkbootstrap.constants import *

# Función para cargar las pruebas desde el archivo JSON
def cargar_pruebas():
    with open("pruebas.json", "r") as file:
        data = json.load(file)
    return data["pruebas"]

# Cargar las pruebas
pruebas = cargar_pruebas()

# Función para actualizar el módulo cuando se selecciona una prueba
def actualizar_modulo(event):
    selected_prueba = nombre_prueba_combobox.get()
    for prueba in pruebas:
        if prueba["nombre"] == selected_prueba:
            modulo_prueba.configure(text=prueba["modulo"])
            break

# Función para ejecutar la prueba seleccionada
def ejecutar_prueba():
    # Obtener valores de usuario y contraseña
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()
    if not usuario or not contrasena:
        print("Error: Usuario y Contraseña son requeridos.")
        return

    # Obtener la prueba seleccionada
    selected_prueba = nombre_prueba_combobox.get()
    for prueba in pruebas:
        if prueba["nombre"] == selected_prueba:
            script = prueba["script"]
            # Ejecutar el script de Selenium pasando usuario y contraseña como argumentos
            subprocess.run(["python", script, usuario, contrasena])
            break

# Crear la ventana principal
root = Window(themename="cosmo")
root.title("Interfaz Mejorada")
root.geometry("500x400")

# Configurar estilos
label_font = ("Helvetica", 11, "bold")

# Frame principal
frame = Frame(root, padding=20)
frame.pack(fill=BOTH, expand=True)

# Campo "Usuario"
Label(frame, text="Usuario", font=label_font).grid(row=0, column=0, pady=10, sticky="w")
usuario_entry = Entry(frame, bootstyle="info", width=30)
usuario_entry.grid(row=0, column=1, pady=10)

# Campo "Contraseña"
Label(frame, text="Contraseña", font=label_font).grid(row=1, column=0, pady=10, sticky="w")
contrasena_entry = Entry(frame, bootstyle="info", show="*", width=30)
contrasena_entry.grid(row=1, column=1, pady=10)

# Etiqueta y Combobox para "Nombre de Prueba"
Label(frame, text="Nombre Prueba", font=label_font).grid(row=2, column=0, pady=10, sticky="w")
nombre_prueba_combobox = Combobox(frame, bootstyle="info", values=[prueba["nombre"] for prueba in pruebas], state="readonly")
nombre_prueba_combobox.grid(row=2, column=1, pady=10)
nombre_prueba_combobox.bind("<<ComboboxSelected>>", actualizar_modulo)

# Etiqueta de "Módulo Prueba"
Label(frame, text="Módulo Prueba", font=label_font).grid(row=3, column=0, pady=10, sticky="w")
modulo_prueba = Label(frame, text="Seleccione una prueba", font=label_font)
modulo_prueba.grid(row=3, column=1, pady=10, sticky="w")

# Botón "Probar"
Button(frame, text="Probar", bootstyle="success", width=10, command=ejecutar_prueba).grid(row=4, column=1, pady=20)

# Iniciar la ventana principal
root.mainloop()
