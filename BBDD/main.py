import datetime as dt
import pandas as pd
import sqlite3
from funciones import *
from variables import *


def menu_principal():
    print("""
        _______.  ______       __         .___________. _______      ___      .___  ___.          _____  
        /       | /  __  \     |  |        |           ||   ____|    /   \     |   \/   |         | ____| 
       |   (----`|  |  |  |    |  |        `---|  |----`|  |__      /  ^  \    |  \  /  |  ______ | |__   
        \   \    |  |  |  |    |  |            |  |     |   __|    /  /_\  \   |  |\/|  | |______||___ \  
    .----)   |   |  `--'  '--. |  `----.       |  |     |  |____  /  _____  \  |  |  |  |          ___) | 
    |_______/     \_____\_____\|_______|       |__|     |_______|/__/     \__\ |__|  |__|         |____/  
    """)

    menu = '\n\t 1. Recepción de suminitros\n\t 2. Consulta de registro\n\t 3. Agregar registro\n\t 4. Salir\n'
    eleccion = input(menu)

    while eleccion.isnumeric() != True or int(eleccion) > 4 or int(eleccion) <0:
        eleccion = input(menu)
    opcion = int(eleccion)

    if opcion == 1:
        consulta_base_datos()

    elif opcion == 2:
        tabla = elige_tabla()
        print(consulta_tabla(tabla))

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