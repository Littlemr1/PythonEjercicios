import json

objeto = {'nombre': 'Edward', 'apellido': 'Ortiz', 'edad': 29}

print(type(objeto))

datos_json = json.dumps(objeto)

print(datos_json)
print(type(datos_json))
