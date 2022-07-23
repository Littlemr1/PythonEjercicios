"""
Question: Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example Let us assume the following comma separated input sequence is given to the program: 100,150,180
The output of the program should be: 18,22,24
"""

"""
Pregunta: Escribe un programa que calcule e imprima el valor según la fórmula dada:
Q = Raíz cuadrada de [(2 * C * D)/H] A continuación se indican los valores fijos de C y H: C es 50. H es 30.
D es la variable cuyos valores deben introducirse en el programa en una secuencia separada por comas.
Ejemplo Supongamos que se da al programa la siguiente secuencia de entrada separada por comas: 100,150,180
La salida del programa debe ser: 18,22,24
"""

import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))