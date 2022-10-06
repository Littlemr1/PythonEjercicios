import ast

lenguajes = "['Python', 'JavaScript', 'C#', 'C++', 'PHP']"

print(type(lenguajes))
print(isinstance(lenguajes, list))
print(isinstance(lenguajes, str))

print()
asd
resultado = ast.literal_eval(lenguajes)

print(type(resultado))
print(isinstance(resultado, list))
print(isinstance(resultado, str))

print()

print(lenguajes)
print(resultado)
