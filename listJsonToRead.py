import json

arreglo_json = '["Python", "Java", "PHP", "C#", "PHP"]'

lista = json.loads(arreglo_json)

print(type(lista))
print(lista)
