#Atributos publicos, protegidos , privados


class Miclase:
    def __init__(self,publico,protegido,privado):
        self.publico = publico
        #acceder de esta misma clase o subclase
        self._protegido = protegido
        #Solo para esta clase
        self.__privado = privado


objeto = Miclase('Valor publico','Valor protegido','Valor publico')

print(objeto.publico)
print(objeto._protegido)
print(objeto._Miclase__privado)
