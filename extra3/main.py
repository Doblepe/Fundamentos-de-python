import sqlite3
from alumno import alumno
from alumnoDAO import alumnoDao

con = None
try:
    #creamos la conexión
    con = sqlite3.connect('./mydatabase.db')
    #creando la tabla
    alumnoDao.crear_tabla(con)
    
    #pedir_datos()

    #creando los alumnos
    alum1 = alumno("xxx","xxx","xxx",22)
    alum2 = alumno("yyy","yyy",'yyy',24)
    
    #insertar los alumnos en la BBDD
    alumnoDao.insertar_registro(con,alum1)
    alumnoDao.insertar_registro(con,alum2)
    alumnoDao.actualizar_registro(con, 'yyy', 4)
    alumnoDao.mostrarDB()

except Exception as e:
    print("Error en el main: ",e)


