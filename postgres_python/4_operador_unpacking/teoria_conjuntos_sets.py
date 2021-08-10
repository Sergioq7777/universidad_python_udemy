#SET

#operacin de conjuntos en set
#Personas con diferentes caracteristics

pelo_negro = {"sergio", "juan" , "pedro", "maria"}
pelo_rubio = {"laura", "lorenzo", "marco"}
ojos_cafes = {"juan","laura"}
ojos_verdes = {"sergio","maria"}
menos_30 = {'juan','karla',"maria"}

#Union
print(f"Union: de pelo negro con ojos verdes :{pelo_negro.union(ojos_verdes)}")

#Intersection

print(f"intersection: de ojos cafes con pelo rubio : {ojos_cafes.intersection(pelo_rubio)}")

#Difference

print(f"Difference: pelo negro sin ojos color verde : {pelo_negro.difference(ojos_cafes)}")

#Diferencia simetrica

print(f'Diferencia simetrica: pelo negro u ojos cafes {pelo_negro.symmetric_difference(ojos_cafes)}')