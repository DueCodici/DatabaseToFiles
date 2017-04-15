#!/usr/bin/python3

import csv
import pymysql

db = pymysql.connect("localhost","root","Password123!!","universidad" )
cursor = db.cursor()
sql = """SELECT c.id_clase as 'Id de clase', 
	c.nombre_clase as 'Nombre de clase', 
	t.nombre_tipo_clase as 'Tipo de clase' 
	FROM clase c 
	inner join tipo_clase t 
	on c.id_tipo_clase = t.id_tipo_clase
	ORDER BY c.id_clase;"""

try:
	cursor.execute(sql)
	results = cursor.fetchall()
	with open('clases.csv','w') as csvfile:
		csv_writer = csv.writer(csvfile)
		
		num_fields = len(cursor.description)
		print("Number of fields: %d" % num_fields)
		field_names = [header[0] for header in cursor.description]
		csv_writer.writerow(field_names)

		for row in results:
			id_clase = row[0]
			nombre_clase = row[1]
			tipo_clase_id = row[2]
			print("Id: %d Clase: %s Tipo clase: %s" % (id_clase, nombre_clase, tipo_clase_id))
			csv_writer.writerow(row)
except:
	print ("Error: unable to fetch data")

db.close()