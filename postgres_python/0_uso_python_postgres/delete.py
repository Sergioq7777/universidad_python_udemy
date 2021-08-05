#conexion de python a base de datos:
import psycopg2




conexion = psycopg2.connect(
    user='sergio',
    password='admin',
    host='localhost',
    port='5432',
    database ='new_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE from users WHERE id=%s'
            entrada = input("type the id: ")
            valores = (entrada,)
            cursor.execute(sentencia,valores)
            registro_insertados = cursor.rowcount
            print(f'Registros Insertados: {registro_insertados}')
except Exception as e:
    print(f'Ocurrio un error {e}')

finally:
    conexion.close()

