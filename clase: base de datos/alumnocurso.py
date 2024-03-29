#################################
#Bases de datos
#################################

import sqlite3
import os
conn=sqlite3.connect('cursosProteco.db')  #Hacemos la conexión a la base de datos
#Y la crea

#La mayoría de las operaciones sobre las bases de datos se hacen utilizando
#un objeto que apunta a la base de datos y a través del cual podemos 
#ejecutar instrucciones similares al SQL estandar para obtener, insertar, actualizar o
#borrar algun dato.

cursor=conn.cursor()

print("\n\t\tBase de datos de los cursos de PROTECO")


#Creación de tablas
#Las operaciones se ejecutan a través del método execute del curso que
#declaramos

try:
	cursor.execute('''
		CREATE TABLE alumno(
		folio INTEGER PRIMARY KEY,
		nombreAlu TEXT,
		apPat TEXT, 
		apMat TEXT)''')
	cursor.execute('''
		CREATE TABLE curso(
		idCurso INTEGER PRIMARY KEY,
		nombreCurso TEXT,
		cupo INTEGER)''')
	cursor.execute('''
		CREATE TABLE alumno_curso(
		folio INTEGER,
		idCurso INTEGER,
		calificacion FLOAT,
		FOREIGN KEY(folio) REFERENCES alumno(folio)
		FOREIGN KEY(idCurso) REFERENCES curso(idCurso)
		PRIMARY KEY(folio,idCurso)
		)''')
	
except:
	print("Saltándose la creación de la tabla porque ya existe! :D")

#Insertar cosas.
"""La forma recomendada es utilizar placeholders(marcadores de posición)
puesto que si armamos la cadena usando variables de python podemos correr
el riesgo de que nos hagan SQL injection"""



while True:
	opcion = input(""" 
					  \n1.-Registrar alumno
					  \n2.-Registrar curso
					  \n3.-Ver cursos
					  \n4.-Ver alumnos
					  \n5.-Eliminar curso
					  \n6.-Eliminar alumno
					  \n7.-Actualizar datos curso
					  \n8.-Actualizar datos alumno
					  \n9.-Salir 
					  \nIngresa la opción que deseas realizar:""")
	if opcion=='1':
		#Solicitamos los datos a guardar
		folio = int(input("Ingresa el folio del asistente: "))
		nombreAlu = input("Ingresa el nombre: ")
		apPat = input("Ingresa el apellido paterno: ")
		apMat = input("Ingresa el apellido materno: ")
		
		#Query a ejecutar
		cursor.execute('INSERT INTO alumno(folio,nombreAlu,apPat,apMat) VALUES("%d", "%s","%s","%s")'%(folio,nombreAlu,apPat,apMat))	
		#Recordar que hay que guardar los cambios
		conn.commit()
		print("Alumno agregado exitosamente!")
	if opcion=='2':
		#Solicitamos los datos
		idCurso = int(input("Ingresa el id del curso: "))
		nombreCurso = input("Ingresa el nombre del curso: ")
		cupo = int(input("Ingresa el cupo del curso: "))
		#Query a ejecutar
		cursor.execute('INSERT INTO curso(idCurso,nombreCurso,cupo) VALUES("%d", "%s","%d")'%(idCurso,nombreCurso,cupo))	
		print("Curso agregado exitosamente!")
		#Salvar cambios	
		conn.commit()	
		
	if opcion=='3':
		for row in conn.execute('SELECT * FROM curso ORDER BY idCurso ASC'):
			print("idCurso: ", row[0], " Nombre del curso: ", row[1], "Cupo: ", row[2])


	if opcion=='4':
		for row in conn.execute('SELECT * FROM alumno ORDER BY folio DESC'):
			print("Folio: ", row[0], " Nombre: ", row[1], row[2], row[3])
	
	if opcion=='5': #Eliminar curso
		os.system('clear')
		print('Cursos disponibles: \n')
		for row in conn.execute('SELECT * FROM curso ORDER BY idCurso ASC'):
			print("idCurso: ", row[0], " Nombre del curso: ", row[1], "Cupo: ", row[2])
		idCurso = int(input('Ingresa el id del curso que deseas borrar'))
		cursor.execute("DELETE FROM curso WHERE idCurso=%d"%idCurso)
		print('Curso eliminado correctamente!')
		conn.commit()



	if opcion=='6': #Eliminar alumno
		os.system('clear')
		print('Alumnos disponibles: \n')
		for row in conn.execute('SELECT * FROM alumno ORDER BY folio DESC'):
			print("Folio: ", row[0], " Nombre: ", row[1], row[2], row[3])
		folio = int(input('Ingresa el folio del alumno: '))
		cursor.execute("DELETE FROM alumno WHERE folio=%d"%folio)
		conn.commit() #NO OLVIDAR

	if opcion=='7': #Actualizar datos de curso
		pass

	if opcion=='8': #Actualizar datos de alumno
		print('---- Modificando alumno ----')
		Folio = int(input("Ingresa el folio del alumno que deseas modificar: "))
		nuevoNombre = input('Ingresa el nombre: ')
		nuevoApPat = input('Ingresa el apellido paterno: ')
		nuevoApMat = input('Ingresa el apellido materno: ')

		#Query a ejecutar
		cursor.execute('''UPDATE alumno SET nombreAlu = ?, apPat = ?, apMat = ? WHERE folio = ?''',(nuevoNombre, nuevoApPat, nuevoApMat, Folio))
		conn.commit()
		print('Alumno modificado exitosamente!')

	if opcion=='9':
		print('Gracias por usar la Database de Proteco, hasta pronto!')
	#else:
	#	print("Opción incorrecta, intenta de nuevo!")



#Ver todos los datos de la tabla

#for row in conn.execute('SELECT * FROM alumnos ORDER BY promedio DESC'):
#	print("Nombre: ",row[1],"Promedio: ",row[2])

#Cerrar la conexión
conn.close()