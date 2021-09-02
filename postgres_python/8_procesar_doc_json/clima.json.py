import urllib.request
import json

res = urllib.request.urlopen('http://globalmentoring.com.mx/api/clima.json')

res_red = res.read()
#print(res_red)

json_res = json.loads(res_red.decode('utf-8'))
#print(json_res)

descripcion_clima = json_res.get('clima')
print (f'Description clima {descripcion_clima}')