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
            #sentencia recive this parameter
            sentencia = 'SELECT * FROM users WHERE id IN %s;'
            entrada = input("type the options: ")
            llave_primaria = (tuple(entrada.split(',')),)
            cursor.execute(sentencia,llave_primaria)
            registro = cursor.fetchall()
            for regis in registro:
                print(regis)

except Exception as e:
    print(f'Ocurrio un error {e}')

finally:
    conexion.close()


#psycopg2.errors.InsufficientPrivilege: permission denied for table users == GRANT postgres TO sergio;

    