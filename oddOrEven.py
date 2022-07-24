"""
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
"""

"""
Definir una función que pueda aceptar un número entero como entrada e imprimir "Es un número par" si el número es par, en caso contrario imprimir "Es un número impar".
"""

def checkValue(n):
    if n%2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
        
checkValue(7)
