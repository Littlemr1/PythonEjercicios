"""
Question: Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
"""

"""
Pregunta: Escriba un programa que pueda calcular el factorial de un número dado.
Los resultados deben imprimirse en una secuencia separada por comas en una sola línea. 
Supongamos que se suministra la siguiente entrada al programa: 8 Entonces, la salida debe ser 40320
"""

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))

if __name__ == '__main__':
    fact(x)