#funciones anonimas
#funciones pequeñas sin nombre asgnado en una linea de code
# permite asignar una funcin a una variable

#1 ejemplo
mi_fun_lamda = lambda a,b: a+b

res = mi_fun_lamda(3,4)
print(f"printing with lamda : {res}")


#2 ejemplo
# funcion lambda que no recibe argumentos

mi_fun_lamda_dos = lambda: "Fun sin argumentos"

print(f'imprimiendo Lambda sin args{mi_fun_lamda_dos()}')

#3 emeplo
#asignando paramentros por default

mi_fun_lambda_tres = lambda a=4, b=5:a+4
print(f'printing with parameters: {mi_fun_lambda_tres()}')


#4 ejemplo
#with args para tuplas y kwargs para dicts

mi_fun_lambda_cuatro = lambda *args, **kwargs: len(args) + len(kwargs)

print(f"printing with args and kwargs: {mi_fun_lambda_cuatro(1,2,3, s=1,t=4)}")






