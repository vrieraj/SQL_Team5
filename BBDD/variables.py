import sqlite3
conexion = sqlite3.connect("./piezas.db")
cursor = conexion.cursor()
tablas = [('Proveedores','proveedor'),('Pieza','pieza')]