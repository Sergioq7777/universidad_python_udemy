from  logger_base import log


class Persona:
    def __init__(self, id_persona=None ,nombre=None, apellido=None, age=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._age= age

    def __str__(self):
        return f"""
                id: {self._id_persona}
                nombre: {self._nombre}
                apellido: {self._apellido}
                age: {self._age} 
                """
    
    @property
    def id_persona(self):
        return self._id_persona
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona
    
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age

if __name__ == '__main__':
    new_persona = Persona(1,"Sergio","Quiroga",24)
    log.debug(new_persona)
    print(new_persona)

    new_persona = Persona(nombre="Sergio",apellido="Quiroga",age=55)
    log.debug(new_persona)