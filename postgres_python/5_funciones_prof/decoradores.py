#decoradores
# recibir funcion como parametro y entregar otra
# agregar mas funcionalidad a una funcion existente

#1) funcion decorador: (a)

#2) Funcion a decorar: (b)

#3) Funcion decorada: (c)

#Creando decorador...
def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args,**kwargs):
        print("antes de ejecutar la funcion")
        res = funcion_a_decorar_b(*args,**kwargs)
        print("Despues de ejecutar la funcion")
        return res
    return funcion_decorada_c

@funcion_decorador_a
def mostrar_mensaje():
    print('Hola desde la fun mostrar_mensaje')

@funcion_decorador_a
def suma(a,b):
    return a+b

print(f'Respuesta suma con decorador: {suma(5,9)}')