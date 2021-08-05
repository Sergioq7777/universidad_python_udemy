#conexion de python a base de datos:
import psycopg2 as bd




conexion = bd.connect(
    user='sergio',
    password='admin',
    host='localhost',
    port='5432',
    database ='new_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO login_user(nombre,apellido,age) VALUES(%s,%s,%s);'
            valores = ('nataly', 'castillo','27')
            cursor.execute(sentencia,valores)
            
            sentencia = 'UPDATE login_user SET nombre=%s, apellido=%s, age=%s WHERE id=%s'
            valores = ('Daniela','Santamaria','27',6)
            cursor.execute(sentencia,valores)

except Exception as e:
    print(f'Ocurrio un error {e}')

finally:
    conexion.close()

