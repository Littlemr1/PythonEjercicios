"""
Question: Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""

"""
Pregunta: Definir una clase con un generador que pueda iterar los números, que son divisibles por 7, entre un rango dado 0 y n.
"""

def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reverse(100):
    print(i)
