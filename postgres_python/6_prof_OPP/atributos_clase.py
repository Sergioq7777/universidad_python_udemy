class Persona:

    contador_personas = 0

    @classmethod
    def id_contador(cls):
        cls.contador_personas +=1
        return cls.contador_personas

    def __init__(self,name,age):
        self.id_personas = Persona.id_contador()
        self._name= name
        self._age = age
    
    @property
    def id(self):
        return self.id_personas
    @id.setter
    def id(self,id_personas):
        self.id_personas = id_personas
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age

    def __str__(self):
        return f'id: {self.id_personas} Nombre: {self.name} Age: {self.age}'
    

if __name__=='__main__':
    persona_uno = Persona("Sergio",29)
    print(persona_uno)
    persona_uno.name = "Andres"
    print(persona_uno)
    print(persona_uno.__dict__)
    person_dos = Persona("Anastasia",33)
    print(person_dos)
    person_dos.id = 3
    print(person_dos)
