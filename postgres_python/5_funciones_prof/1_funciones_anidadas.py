#Calculadora funciones anidadas

def calculadora(a,b,operador):
    def sumar(a,b):
        return f'Resultado de suma :{a+b}'
    def resta(a,b):
        return f'Resultado de resta :{a-b}'
    def mult(a,b):
        return f'Resultado de mult :{a*b}'
    def div(a,b):
        return f'Resultado de div :{a/b}'
    
    if operador == '+':
        print(sumar(a,b))
    elif operador=='-':
        print(resta(a,b))
    elif operador=='*':
        print(mult(a,b))
    elif operador=='/':
        print(div(a,b))
    else:
        print('Write valid option...')


if __name__ == '__main__':
    operator = str(input("Choose operation + , - , * , /  :  "))
    if operator:
        a = int(input("Type first number: "))
        b = int(input("Type second number: "))
        calculadora(a,b,operator)
    else:
        print('Choose an option...')