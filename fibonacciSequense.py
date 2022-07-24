"""
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example: If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
"""


"""
La Secuencia de Fibonacci se calcula a partir de la siguiente fórmula
f(n)=0 si n=0 f(n)=1 si n=1 f(n)=f(n-1)+f(n-2) si n>1
Por favor, escriba un programa utilizando la comprensión de listas para imprimir la Secuencia de Fibonacci en forma separada por comas con una entrada n dada por consola.
Ejemplo: Si se da el siguiente n como entrada al programa:
7
Entonces, la salida del programa debería ser
0,1,1,2,3,5,8,13
"""

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))
