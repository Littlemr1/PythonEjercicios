"""
Question: Write a program that accepts a comma separated sequence of words as input and prints the words
in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program: without,hello,bag,world Then,
the output should be: bag,hello,without,world
"""

"""
Pregunta: Escriba un programa que acepte como entrada una secuencia de palabras separadas por comas
e imprima las palabras en una secuencia separada por comas después de ordenarlas alfabéticamente.
Suponga que se suministra la siguiente entrada al programa: sin,hola,bolsa,mundo Entonces,
la salida debería ser: bolsa,hola,mundo,sin(Ordenadas en español)
"""

items=[x for x in input().split(',')]
items.sort()
print(','.join(items))