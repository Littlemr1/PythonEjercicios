"""
Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

"""
Pregunta: Escriba un programa que encuentre todos los números comprendidos entre 1000 y 3000 (ambos incluidos) de forma que cada dígito del número
sea un número par. Los números obtenidos deben imprimirse en una secuencia separada por comas en una sola línea.
"""

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))
