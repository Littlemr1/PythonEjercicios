"""
Question: Define a class which has at least two methods: getString: to get a string from console input printString:
to print the string in upper case. Also please include simple test function to test the class methods.
"""

"""
Pregunta: Defina una clase que tenga al menos dos métodos: getString: para obtener una cadena de la entrada de la consola printString:
para imprimir la cadena en mayúsculas. También incluya una función de prueba simple para probar los métodos de la clase.
"""


class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()
