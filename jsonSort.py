import json

objeto = {'7': 5, '9': 12, '1': 3, '2': 5}

print(objeto)

resultado = json.dumps(objeto, sort_keys=True, indent=4)

print(resultado)
