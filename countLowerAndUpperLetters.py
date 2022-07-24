"""
Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
"""

"""
Pregunta: Escriba un programa que acepte una frase y calcule el número de letras mayúsculas y minúsculas.
Suponga que se suministra la siguiente entrada al programa: ¡Hola mundo! Entonces, la salida debería ser MAYÚSCULAS 1 MINÚSCULAS 9
"""

s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("MÁYUSCULAS", d["UPPER CASE"])
print("MÍNUSCULAS", d["LOWER CASE"])
