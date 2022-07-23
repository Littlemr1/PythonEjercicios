"""
Question: Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then,
the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
"""

"""
Pregunta: Escribe un programa que acepte una secuencia de números separados por comas
desde la consola y genere una lista y una tupla que contenga cada número.
Supongamos que se suministra al programa la siguiente entrada 34,67,55,33,12,98 Entonces,
la salida debería ser: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
"""

values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)
