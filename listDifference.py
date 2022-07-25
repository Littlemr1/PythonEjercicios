lenguajes_1 = ['Python', 'C++', 'Java', 'C#']
lenguajes_2 = ['C#', 'PHP', 'JavaScript', 'C']

resultado = set(lenguajes_1).difference(set(lenguajes_2))
print(resultado)

print()

resultado = set(lenguajes_2).difference(set(lenguajes_1))
print(resultado)
