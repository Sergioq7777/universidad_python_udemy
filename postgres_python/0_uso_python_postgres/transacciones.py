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
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO login_user(nombre,apellido,age) VALUES(%s,%s,%s);'
    valores = ('Maria', 'Rodriguez','5465')
    cursor.execute(sentencia,valores)
    conexion.commit()
    print('Termina transaccion')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error se hizo rollback{e}')

finally:
    conexion.close()

