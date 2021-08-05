from conexion import  Conexion
from persona import Persona
from logger_base import  log

class PersonaDAO:
    """
    DAO = Data Access Object
    """

    _SELECCIONAR = 'SELECT * FROM login_user ORDER BY id_persona;'
    _INSERTAR = 'INSERT INTO login_user(nombre,apellido,age) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE login_user SET nombre=%s,apellido=%s,age=%s WHERE id_persona=%s'
    _BORRAR = 'DELETE FROM login_user WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                
                for registro in registros:
                    persona = Persona(registro[0],registro[1],registro[2],registro[3])
                    personas.append(persona)
                return personas
        
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.age)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f'Personas a insertada: {persona}')
                return cursor.rowcount
    

    @classmethod
    def actualizar(cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.age, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug(f'Personas actualizada: {persona}')
                return cursor.rowcount
    
    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._BORRAR,valores)
                log.debug(f'Personas actualizada: {persona}')
                return cursor.rowcount
    

                


if __name__ == '__main__':


    persona_cuatro = Persona(id_persona = 4)
    persona_eliminada = PersonaDAO.eliminar(persona_cuatro)
    log.debug(f'Personas eliminadas: {persona_eliminada}')


    persona_tres = Persona(13,"Juliana","Torres",13)
    persona_actualizadas = PersonaDAO.actualizar(persona_tres)
    log.debug(f'Personas insertadas : {persona_actualizadas}')


    # Insertar un registro
    #persona_one = Persona(nombre='Andres',apellido='MonR',age=45)
    #personas_inertadas = PersonaDAO.insertar(persona_one)
    #log.debug(f'Personas insertadas : {personas_inertadas}')


    #personas = PersonaDAO.seleccionar()
    #for persona in personas:
    #    log.debug(persona)
