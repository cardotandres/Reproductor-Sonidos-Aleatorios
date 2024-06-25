import pystray
from pystray import MenuItem as item
from PIL import Image
import pygame
import random
import time
import threading
import os
import ctypes
import sys

# Inicializar mixer, definición de rutas y funciones
pygame.mixer.init()

if hasattr(sys, '_MEIPASS'):
    DIR_BASE = sys._MEIPASS
else:
    DIR_BASE = os.path.abspath(".")

RUTA_ICONO = os.path.join(DIR_BASE, 'data/icon.png')
DIR_SONIDO = os.path.join(DIR_BASE, 'data')
ARCHS_SONIDO = [s for s in os.listdir(DIR_SONIDO) if s.endswith('.mp3')]

def play_sonido_aleatorio():
    arch_sonido = random.choice(ARCHS_SONIDO)
    pygame.mixer.music.load(os.path.join(DIR_SONIDO, arch_sonido))
    pygame.mixer.music.play()

def loop_sonido_aleatorio():
    while True:
        sleep_time = random.randint(60, 300)
        time.sleep(sleep_time)
        play_sonido_aleatorio()

def setup_icono(icono):
    icono.visible = True

def on_quit(icono, item):
    icono.stop()
    pygame.mixer.music.stop()
    os._exit(0)

def main():
    # Ocultar la ventana, crear icono
    if sys.platform == 'win32':
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    imagen = Image.open(RUTA_ICONO)
    menu = (item('Salir', on_quit),)
    icono = pystray.Icon('sound_player', imagen, 'Sound Player', menu)

    # Inicializar, minimizar al área de notificaciones, mantener en segundo plano
    threading.Thread(target=icono.run, daemon=True).start()
    threading.Thread(target=loop_sonido_aleatorio, daemon=True).start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()