"""
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
Example: If the following n is given as input to the program:
7
Then, the output of the program should be:
13
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

"""
La Secuencia de Fibonacci se calcula a partir de la siguiente fórmula
f(n)=0 si n=0 f(n)=1 si n=1 f(n)=f(n-1)+f(n-2) si n>1
Escribe un programa que calcule el valor de f(n) con una entrada n dada por consola.
Ejemplo: Si se da el siguiente n como entrada al programa:
7
Entonces, la salida del programa debe ser
13
En caso de que se suministren datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola.
"""

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print(f(n))
as
