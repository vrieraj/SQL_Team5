import datetime as dt
import pandas as pd
import sqlite3
from funciones import *
from variables import *


def menu_principal():
    print("""
  ____  ____   _      ____   _____                          _______                    _     
 / ___||  _ \\ | |    / ___| | ____|__ _ ___ _ __ ___   ___ |__   __|__  _ __ ___  ___ | |__  
 \\___ \\| |_) || |   | |     |  _| / _` / __| '_ ` _ \\ / _ \\   | | / _ \\| '__/ _ \\/ _ \\| '_ \\ 
  ___) |  __/ | |___| |___  | |__| (_| \\__ \\ | | | | |  __/   | || (_) | | |  __/ (_) | |_) |
 |____/|_|    |_____\\____| |_____\\__,_|___/_| |_| |_|\\___|   |_| \\___/|_|  \\___|\\___/|_.__/""")
          
    menu = '\n\t 1. Recepción de suminitros\n\t 2. Consulta de registro\n\t 3. Agregar registro\n\t 4. Salir\n'
    eleccion = input(menu)

    while eleccion.isnumeric() != True or int(eleccion) > 4 or int(eleccion) <0:
        eleccion = input(menu)
    opcion = int(eleccion)

    if opcion == 1:
        consulta_base_datos()

    elif opcion == 2:
        tabla = elige_tabla()
        consulta_tabla(tabla)

    elif opcion == 3:
        menu = '\n\t 1. Proveedores\n\t 2. Pieza'
        eleccion = input(menu)
        while eleccion.isnumeric() != True or int(eleccion) > 2 or int(eleccion) <0:
            eleccion = input(menu)
        insertar_campo(tablas[int(eleccion)-1][0])

    elif opcion == 4:
        quit()

    menu_principal()


menu_principal()