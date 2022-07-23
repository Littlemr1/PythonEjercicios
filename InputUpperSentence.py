"""
Question: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
"""

"""
Pregunta: Escriba un programa que acepte una secuencia de líneas como entrada e imprima las líneas después de poner todos los caracteres
de la frase en mayúsculas. Suponga que se suministra la siguiente entrada al programa: Hola mundo La práctica hace la perfección Entonces,
la salida debería ser HOLA MUNDO LA PRÁCTICA HACE LA PERFECCIÓN
"""

lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)
