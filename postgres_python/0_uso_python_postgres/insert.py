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
            sentencia = 'INSERT INTO users(full_name,cc,date) VALUES (%s, %s, now())'
            valores = (
                ('juan','123'),
                ('jaqui','321'),
                ('lauren','888'),
            )
            cursor.executemany(sentencia,valores)
            registro_insertados = cursor.rowcount
            print(f'Registros Insertados: {registro_insertados}')
except Exception as e:
    print(f'Ocurrio un error {e}')

finally:
    conexion.close()

