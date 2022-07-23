"""
Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words
and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then,
the output should be: again and hello makes perfect practice world
"""

"""
Pregunta: Escriba un programa que acepte una secuencia de palabras separadas por espacios en blanco como entrada e imprima las palabras
después de eliminar todas las palabras duplicadas y ordenarlas alfanuméricamente. Supongamos que el programa recibe la siguiente entrada:
hola mundo y la práctica hace al mundo perfecto y hola mundo otra vez Entonces, la salida debería ser: otra vez y hola hace al mundo perfecto la práctica
"""

s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
