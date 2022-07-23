"""
Question: Write a program which will find all such numbers which are divisible by 7
but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should
be printed in a comma-separated sequence on a single line.
"""

"""
Pregunta: Escriba un programa que encuentre todos los números divisibles por 7
pero que no sean múltiplos de 5, entre 2000 y 3200 (ambos incluidos). Los números obtenidos deben
imprimirse en una secuencia separada por comas en una sola línea.
"""

def getDivisor() :
    l=[]
    for i in range(2000, 3201):
        if (i%7==0) and (i%5!=0):
            l.append(str(i))

    print(','.join(l))

if __name__=="__main__":
    getDivisor()
