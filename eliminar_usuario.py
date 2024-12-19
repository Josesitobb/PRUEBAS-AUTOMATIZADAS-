import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Función para obtener la cantidad de usuarios
def obtener_cantidad_usuarios():
    # Ventana emergente para ingresar la cantidad de usuarios
    cantidad = simpledialog.askinteger("Cantidad de Usuarios", "¿Cuántos usuarios deseas crear?", minvalue=1, maxvalue=100)
    
    # Si el usuario no ingresa nada, devolver 0
    if cantidad is None:
        cantidad = 0
    
    # Mostrar la cantidad de usuarios seleccionados
    print(f"Cantidad de usuarios a crear: {cantidad}")
    
    # Llamar a la función para realizar la prueba de creación de usuarios
    prueba_creacion_usuarios(cantidad)

# Función para realizar la prueba de creación de usuarios (simulada)
def prueba_creacion_usuarios(cantidad):
    # Si no se ha ingresado una cantidad válida, mostramos un mensaje y salimos
    if cantidad <= 0:
        print("No se seleccionó una cantidad válida de usuarios.")
        return
    
    # Aquí se simula la creación de los usuarios (esto se puede hacer con Selenium)
    for i in range(cantidad):
        # Simulación de creación de usuario (puedes cambiar esto por tu prueba con Selenium)
        print(f"Creando usuario {i+1}...")  
        time.sleep(1)  # Simular el tiempo de creación de usuario
    
    # Aquí es donde ejecutarías la prueba de Selenium, por ejemplo:
    login_facebook()

# Función para la prueba de inicio de sesión con Selenium
def login_facebook():
    # Configurar el controlador de Selenium (puedes usar Chrome o Firefox)
    driver = webdriver.Chrome()  # Cambia esto si usas Firefox o algún otro navegador
    
    # Abrir la página de inicio de sesión de Facebook
    driver.get("https://www.facebook.com")
    time.sleep(2)  # Esperar a que cargue la página
    
    # Encontrar los campos de usuario y contraseña (puedes adaptarlo a tu prueba de creación)
    campo_usuario = driver.find_element("id", "email")
    campo_contrasena = driver.find_element("id", "pass")
    
    # Ingresar los datos del usuario y la contraseña
    campo_usuario.send_keys("usuario_test")
    campo_contrasena.send_keys("contrasena_test")
    
    # Hacer clic en el botón de iniciar sesión
    campo_contrasena.send_keys(Keys.RETURN)
    
    # Esperar un momento para ver lo que sucede
    time.sleep(5)
    
    # Cerrar el navegador
    driver.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Prueba de Creación de Usuarios")
ventana.geometry("300x200")

# Etiqueta explicativa
etiqueta = tk.Label(ventana, text="Haz clic en 'Iniciar Prueba' para comenzar la creación de usuarios.")
etiqueta.pack(pady=20)

# Botón para iniciar la prueba de creación de usuarios
boton_iniciar = tk.Button(ventana, text="Iniciar Prueba", command=obtener_cantidad_usuarios)
boton_iniciar.pack(pady=10)

# Iniciar la ventana principal
ventana.mainloop()
