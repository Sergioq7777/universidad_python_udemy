#Set definition
conjunto = set([1,2,34,2,23,4,5])
print(type(conjunto))
print(f"conjunto tipo: {type(conjunto)}")

#Dictionary
distiona = {'a':200}
print(f"conjunto2 tipo: {type(distiona)}")


#Agregar un set a otro set
conjunto2 = {100,200,300,300}
print(f"conjunto2 tipo: {type(conjunto2)}")
conjunto.update(conjunto2)
print(f"conjunto tipo: {type(conjunto)}")
print(conjunto)
#or
conjunto.update([66,77,88])
print(conjunto)


#Copia poco profunda

conjunto_copy = conjunto.copy()
print(f"Conjunto copy: {conjunto_copy}")
print(f"Es igual en contenido: {conjunto_copy == conjunto}")
print(f"Es igual direccion de memoria: {conjunto_copy is conjunto}")