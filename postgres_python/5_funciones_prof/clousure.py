#closure

def primera_fun(a,b):
    def sumar():
        return a+b
    
    return sumar

mi_fun_dev = primera_fun(4,2)

print(f'devolviendo fun closure: { mi_fun_dev() }')