#closure

def primera_fun(a,b):
    return lambda: a+b

mi_fun_dev = primera_fun(4,2)

print(f'devolviendo fun closure: { mi_fun_dev() }')