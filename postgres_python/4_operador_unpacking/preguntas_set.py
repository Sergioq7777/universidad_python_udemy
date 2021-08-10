
pelo_negro = {"sergio", "juan" , "pedro", "maria"}
pelo_rubio = {"laura", "lorenzo", "marco"}
ojos_cafes = {"juan","laura"}
ojos_verdes = {"sergio","maria"}
menos_30 = {'juan','pedro',"maria"}

#SubSet
#Si un set esta contenido en otro subset

print(f'Si menores de 30 es sub set de pelo negro :{menos_30.issubset(pelo_negro)}')


#superSet
#Si un set contiene a otro set...
print(f'Si pelo negro es set de menores de 30 {menos_30.issuperset(pelo_negro)}')


#disjoint

print(f'si pelo egro esta en pelo rubio: {pelo_negro.isdisjoint(pelo_rubio)}')
