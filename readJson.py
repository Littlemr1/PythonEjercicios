import json

with open('Parte001/paises_capitales.json') as f:
    paises = json.load(f)

print(type(paises))
print(len(paises))

print(paises)

print()

print(paises[0])
print(type(paises[0]))
