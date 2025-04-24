import datetime as dt
import os
import pandas as pd
import sqlite3
from variables import *

def consulta_elemento(tabla, nombre):
    query = f"""
        SELECT *
        FROM {tabla}
        WHERE Nombre LIKE '%{nombre}%'
        """
    ID = pd.read_sql(query, conexion).ID

    if len(ID) == 0:
        return 'No se encontró ID.'
    return ID
def consulta_id(tabla, ID:list):
    query = f"""
        SELECT *
        FROM {tabla}
        WHERE ID = '{ID}'
        """
    return pd.read_sql(query, conexion)['Nombre'][0]
def consulta(suministro):
    tabla, algo = suministro[0], suministro[1]

    elemento = input(f'Inserte {algo}:').capitalize()
    resultados = consulta_elemento(tabla, elemento)

    if type(resultados) == str:
        print(resultados)
        return 'salida'
    else:
        if len(resultados) > 1:
            for index, resultado in enumerate(resultados):
                print(index, consulta_id(tabla, resultado))

            index = input(f'Seleccione {algo}:')
            while index.isnumeric() != True or int(index) > len(resultados)-1 or int(len(resultados)-1) <0:
                index = input(f'Inserte un número entre 0-{len(resultados)-1}:')
            ID = resultados[int(index)]
        else:
            ID = resultados[0]
            index = 0
    
    print(consulta_id(tabla, ID))
    
    return str(ID)

def consulta_tabla(tabla):
    return pd.read_sql(f"SELECT * FROM {tabla}", conexion)

def insertar_suministros(fecha, ID_proveedor, ID_pieza, cantidad):
    query = f"INSERT INTO Registro (FECHA, ID_PROVEEDOR, ID_PIEZA, CANTIDAD) VALUES (?,?,?,?)"
    cursor.execute(query,(fecha,ID_proveedor,ID_pieza,cantidad))
    conexion.commit()

    query = """SELECT * FROM Registro"""
    df= pd.read_sql(query, conexion).set_index('FECHA')

    return df

def insertar_campo(algo):
    if algo == "proveedor":

        nombre = input("Introduzca el nombre del nuevo proveedor:")
        direccion = input("Introduzca la dirección, solo el tipo de vía y número:")
        ciudad = input("Introduzca la ciudad:")
        provincia = input("Introduzca la provincia:")
        ID_prov = len(consulta_tabla("Proveedores")) + 1 #input("Introduzca un nuevo ID:") # podemos hacer que detecte el indice + 1 del df?? si introducimos un num repetido, esto se rompe al ser el primary key

        query = f"INSERT INTO Proveedores (ID, NOMBRE, DIRECCION, CIUDAD, PROVINCIA) VALUES (?,?,?,?,?)"
        cursor.execute(query,(ID_prov, nombre, direccion, ciudad, provincia))
        conexion.commit()

        query = """SELECT * FROM Proveedores"""
        df= pd.read_sql(query, conexion).set_index('ID')
    else:
        nombre = input("Introduzca el nombre de la nueva pieza:")
        color = input("Introduzca el color:")
        precio = float(input("Introduzca el precio:"))
        ID_cat = "unknown"   # unkown ya que no tenemos funcion que consulte categorias
        ID_pieza = len(consulta_tabla("Pieza")) + 1 #input("Introduzca un nuevo ID:") # lo mismo que con el ID proveedor
        
        query = f"INSERT INTO Pieza (ID, NOMBRE, COLOR, PRECIO, ID_CATEGORIA) VALUES (?,?,?,?,?)"
        cursor.execute(query,(ID_pieza, nombre, color, precio, ID_cat))
        conexion.commit()

        query = """SELECT * FROM Pieza"""
        df= pd.read_sql(query, conexion).set_index('ID')
        
    return df

def elige(algo, index):
    texto = [f'No se encontró {algo}, ¿desea agregar {algo} (S/N)', f'¿Desea añadir {algo}? (S/N)']
    eleccion = input(texto[index]).upper()
    while eleccion != 'S' and eleccion != 'N':
        eleccion = input(texto[index]).upper()
    return eleccion        

def consulta_base_datos():
        
    hoy = dt.datetime.now().strftime("%Y-%m-%d")

    tablas = [('Proveedores','proveedor'),('Pieza','pieza')]

    while True:
        ID_proveedor = consulta(tablas[0])
        if ID_proveedor == 'salida':
            if elige(tablas[0][1], 0) == 'S':
                print(insertar_campo(tablas[0][1]))
            else:
                break

        while True:
            ID_pieza = consulta(tablas[1])
            if ID_pieza == 'salida':
                if elige(tablas[1][1], 0) == 'S':
                    print(insertar_campo(tablas[1][1]))
                else:
                    break      
            cantidad = input(f'Indique cantidad de piezas:')
            while cantidad.isnumeric() != True or int(cantidad) <= 0:
                cantidad = input(f'Inserte una cantidad:')
            print(cantidad)
            
            insertar_suministros(hoy, ID_proveedor, ID_pieza, cantidad)
            print(consulta_tabla('Registro'))

            if elige(tablas[1][1], 1) == 'S':
                continue
            else:
                break
        if elige(tablas[0][1], 1) == 'S':
            continue
        break

def elige_tabla():
    query = """
    SELECT name
    FROM sqlite_master
    where type = 'table'
    """

    resultados = pd.read_sql(query, conexion)
    for index, resultado in enumerate(resultados.name):
        print(index, resultado)

    index = input(f'Seleccione tabla:')
    while index.isnumeric() != True or int(index) > len(resultados)-1 or int(len(resultados)-1) <0:
        index = input(f'Inserte un número entre 0-{len(resultados)-1}:')
    tabla = resultados.iloc[int(index),0]

    return tabla

def clear(): # Limpiar pantalla
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")