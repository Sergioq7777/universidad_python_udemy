#Generadores. 
#funcion especial permite regresar secuencia de valores.
#Yield=producir entregar valores en secuencia en vez de return.


def generadores():
    yield 1
    yield 2
    yield 3

#Consumir generador a demanda
gen = generadores()
#Con cada llamada se consume un valor
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) no generara mas delo que se ha programado



for valor in generadores():
    print(f'valor = {valor}')