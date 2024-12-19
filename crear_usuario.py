import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
from tkinter import simpledialog

def login_facebook(usuario, contrasena):
    # Configuración del navegador
    cantidad = simpledialog.askinteger("Cantidad de Usuarios", "¿Cuántos usuarios deseas crear?", minvalue=1, maxvalue=100)
    driver = webdriver.Chrome()  # Asegúrate de tener el driver configurado
    driver.get("https://www.facebook.com")  # Página de Facebook

    # Encontrar los campos de usuario y contraseña
    usuario_input = driver.find_element(By.ID, "email")  # Campo de usuario
    contrasena_input = driver.find_element(By.ID, "pass")  # Campo de contraseña

    # Ingresar el usuario y la contraseña
    usuario_input.send_keys(usuario)
    contrasena_input.send_keys(contrasena)

    # Encontrar el botón de inicio de sesión y hacer clic
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    # Esperar unos segundos para ver si se inicia sesión correctamente
    driver.implicitly_wait(5)  # Espera hasta que la página cargue (ajusta si es necesario)

    print("Intento de inicio de sesión completado.")
    # Si deseas cerrar el navegador después de la prueba
    driver.quit()

if __name__ == "__main__":
    # Leer argumentos de línea de comandos
    if len(sys.argv) < 3:
        print("Error: Usuario y Contraseña son requeridos.")
        sys.exit(1)

    usuario = sys.argv[1]
    contrasena = sys.argv[2]
    login_facebook(usuario, contrasena)
