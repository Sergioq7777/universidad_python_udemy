diccionario = {'Sergio':27 , 'Valeria':7, 'Pau':4, 'Marlen':54}
print(diccionario)

#Agregando valor
diccionario['tatiana']=16
print(diccionario)


# """.get""" Metodo recupera llave sin lanzar excepcion
print(diccionario.get('Sergio','no se encontro'))
print(diccionario.get('Serg','no se encontro'))


#""".setdefault""" Si modifica el dicc,agemas agraga un valor

nombre = diccionario.setdefault('Andres','Valor por default')
print(nombre)
print(diccionario)

#"""Imprimir con pprint""" sort_dicts = poner en orden de ingreso
from pprint import pprint as pp
pp(diccionario, sort_dicts = False)
