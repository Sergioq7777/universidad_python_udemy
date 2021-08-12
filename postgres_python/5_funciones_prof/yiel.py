# Generadores

def generador(a,b):
    for num in range(a,b):
        yield num

mi_generador = generador(1,6)

for gen in mi_generador:
    print(gen)

generator = generador(1,5)

try:
    print(f"consumo a demanda: {next(generator)}")
    print(f"consumo a demanda: {next(generator)}")
    print(f"consumo a demanda: {next(generator)}")
    print(f"consumo a demanda: {next(generator)}")
    print(f"consumo a demanda: {next(generator)}")
    print(f"consumo a demanda: {next(generator)}")
except StopIteration as e:
    print(f'error {e}')


generathor = generador(1,4)
while True:
    try:
        valor = next(generathor)
        print(f'impresion valor generador {valor}')
    except StopIteration as e:
        print("Se termino el generador")
        break