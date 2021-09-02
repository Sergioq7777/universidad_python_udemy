class Mi_Lista:
    
    def __init__(self, elementos):
        self._elementos = list(elementos)
    

    def agregar_elementos(self, elemento):
        self._elementos.append(elemento)
    
    def obtener_elemntos(self, indice):
        return self._elementos[indice]
    
    def ordenar_elemntros(self):
        return self._elementos.sort()
    
    def len_elementos(self):
        return len(self._elementos)
    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'


class Lista_Hija(Mi_Lista):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        self.ordenar_elemntros()
    
    def agregar_elementos(self, elemento):
        super().agregar_elementos(elemento)
        self.ordenar_elemntros()



class Lista_enteros(Mi_Lista):
    def __init__(self,elementos=[]):
        for i in elementos:
            self._validar(i)
        
        super().__init__(elementos)
    
    def _validar(self, elemento):
        if not isinstance(elemento,int):
            raise ValueError(f'No es un valor entero {elemento}')
    
    def agregar_elementos(self,elemento):
        self._validar(elemento)
        super().agregar_elementos(elemento)


#Herencia multiple
class ListaEnteros_Ordenada(Lista_Hija,Lista_enteros):
    pass
    



#Lista de herencia multiple
list_multiple = ListaEnteros_Ordenada([4,-10,1,15,8,96,-6])
print(list_multiple)
list_multiple.agregar_elementos(-27)
print(list_multiple)


lista_simple = Mi_Lista([5,3,6,8])
print(lista_simple)

lista_hija = Lista_Hija([3,7,9,34,5,-1,70])
print(lista_hija)


lista_enteros = Lista_enteros([3,5,6])
print(lista_enteros)


print('Es entero?', isinstance(3,int))
print('Es str? :', isinstance("Hola",str))