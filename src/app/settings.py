#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

import os
from src.app.info import APP_NAME
from src.etc.imports import ctk, system
from src.etc.variables import logo_file

# Controls the dimensions of the application.
APP_WIDTH = 450
APP_HEIGHT = 300

# Create main window
APP = ctk.CTk()
APP.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
APP.title(APP_NAME)
APP.wm_attributes("-topmost", True)

# Set minimum and maximum APP dimensions
APP.minsize(width=APP_WIDTH, height=APP_HEIGHT)  # Altura mínima em pixels
APP.maxsize(width=APP_WIDTH, height=APP_HEIGHT)  # Altura máxima em pixels

# Get screen dimensions
SCREEN_WIDTH = APP.winfo_screenwidth()
SCREEN_HEIGHT = APP.winfo_screenheight()

# Calculate central window position
posicao_x = (SCREEN_WIDTH - APP_WIDTH) // 2
posicao_y = (SCREEN_HEIGHT - APP_HEIGHT) // 2

# Set window geometry (centered on screen)
APP.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{posicao_x}+{posicao_y}")

# Initial configuration of customtkinter
ctk.set_appearance_mode("dark")  # Modo "dark"
ctk.set_default_color_theme("blue")  # Tema azul

# Check if the operating system is Windows
if system() == 'Windows':
    try:
        if os.path.exists(logo_file):
            APP.iconbitmap(logo_file)
        else:
            # Caminho alternativo se o ícone não for encontrado
            APP.iconbitmap(rf"_internal\resources\image\logo.ico")
    except FileNotFoundError as e:
        print(f"Erro: {e}")
