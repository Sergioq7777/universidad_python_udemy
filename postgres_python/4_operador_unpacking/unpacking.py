#*args
# desempaquetar

numero = [ 1,2,3]

print(numero)
print(*numero, sep='-')

# **kwargs

def suma(a,b,c):
    return f'Suma: {a+b+c}'

#desempaqueta la lista
print(suma(*numero))

