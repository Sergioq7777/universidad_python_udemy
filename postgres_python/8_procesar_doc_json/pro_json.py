import urllib.request
import  json

respuesta = urllib.request.urlopen('http://globalmentoring.com.mx/api/personas.json')
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(f'\nformato json: {cuerpo_respuesta}\n')


# procesar respuesta
json_response = json.loads(cuerpo_respuesta.decode('utf-8'))
print(f'\nformato json.loads: {json_response}')

# Imprimir solo los nombres de las personas
#JSON se convierte a listas y diccionarios en python

for persona in json_response['personas']:
    print(f'\nformato solo seccion personas: {persona["nombre"]} de edad {persona["edad"]}')
