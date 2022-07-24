"""
Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010
Notes: Assume the data is input by console.
"""

"""
Pregunta: Escriba un programa que acepte como entrada una secuencia de números binarios de 4 dígitos separados por comas y que compruebe si son divisibles por 5
o no. Los números que son divisibles por 5 deben imprimirse en una secuencia separada por comas. Ejemplo: 0100,0011,1010,1001 Entonces la salida debe ser: 1010
Notas: Supongamos que los datos se introducen por consola.
"""

value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))
