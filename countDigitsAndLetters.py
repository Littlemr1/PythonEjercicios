"""
Question: Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program:
hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3
"""

"""
Pregunta: Escribe un programa que acepte una frase y calcule el número de letras y dígitos. Suponga que se suministra la siguiente entrada al programa:
¡Hola mundo! 123 Entonces, la salida debería ser LETRAS 10 DÍGITOS 3
"""

s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])
