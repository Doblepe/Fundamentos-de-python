import sqlite3
from alumno import alumno

class alumnoDao:
    
    #función para crear tabla
    def crear_tabla(con):
        try:
            sql = '''
                create table if not exists alumnos(
                    nombre varchar (100),
                    apellido varchar(100),
                    dni varchar (10) primary key,
                    edad tinyint
                )
            '''
            cursor = con.cursor()
            cursor.execute(sql)
            print("La tabla se ha creado correctamente")
        except Exception as e:
            print("Error: ",e)
    
    #función para insertar registro
    def insertar_registro(con,alumno):
        try:
            sql = '''
                insert into alumnos(nombre,apellido,dni,edad)
                values (?,?,?,?)
            '''
            parametro = (alumno.nombre,alumno.apellido,alumno.dni,alumno.edad)
            cursor = con.cursor()
            cursor.execute(sql,parametro)
            con.commit()
            print("El registro se ha insertado")
        except Exception as e:
            print("Error: ",e)
         #función para actualizar registro   
    def actualizar_registro (con, alumno):
        try:
            sql = '''
            UPDATE alumnos
            SET nombre = ?,
                apellido= ?,
                edad = ?,
            WHERE id = ?;
            '''
            parametro = (con,alumno.nombre,alumno.apellido,alumno.dni,alumno.edad)
            cursor = con.cursor()
            cursor.execute(sql, parametro)
            con.commit()
            print('LA TABLAA SE HA ACTUALIZADO')
        except Exception as e:
            print('Error' + e)
    def mostrarDB(con):
        try:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM alumnos")
            rows = cursor.fetchall()   
            for row in rows:
               print(row)
        except Exception as e:
            print('Error ' + e)
    #función actualizar -> se le pasara un objeto persona y mediante su DNI le cambiamos la edad
    
    #función recuperar registros -> recuperamos todos los registros y mostramos por pantalla
    
    #función recuperar 1 registro -> mostramos los datos de un alumno mediante el dni pasado por argumento
    
    #función aliminar registro -> eliminamos un alumno mediante el DNI pasado por argumento
    
    #función vaciar tabla
    
    