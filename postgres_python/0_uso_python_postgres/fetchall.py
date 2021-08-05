#conexion de python a base de datos:
import psycopg2




conexion = psycopg2.connect(
    user='sergio',
    password='admin',
    host='localhost',
    port='5432',
    database ='new_db'
)
#print(conexion)

try:
    with conexion:
        #Se llama metodo cursor
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM users;'
            cursor.execute(sentencia)
            registro = cursor.fetchall()
            print(registro)

except Exception as e:
    print(f'Ocurrio un error {e}')

finally:
    conexion.close()


#psycopg2.errors.InsufficientPrivilege: permission denied for table users == GRANT postgres TO sergio;

    