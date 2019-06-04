import sqlite3
import os

conn = sqlite3.connect('alumnos.db') #hacemos la conexion a la
									# base de datos
cursor = conn.cursor()

print("\n\t Base de datos de los asistentes de Python AM\t")

nombre = input('Ingresa el nombre del asistente: ')
promedio = float(input('¿Qué promedio tiene? '))

#Crear tablas
#Las operaciones se ejecutan a través del método 
#del curso que declaramos

try:
	cursor.execute('''CREATE TABLE alumnos(id integer primary key,nombre text,promedio float)''')
except:
	print('Saltando la creación de la tabla porque ya existe :)')

#Insertar datos

cursor.execute('INSERT INTO alumnos(nombre,promedio) VALUES ("%s","%f")'%(nombre,promedio))

#Guardar los cambios
conn.commit()

#Ver todos los datos de la tabla
for row in conn.execute('SELECT * FROM alumnos ORDER BY promedio DESC'):
	print('Nombre: ', row[1], "Promedio: ", row[2])

#Cerrar la conexión
conn.close()

