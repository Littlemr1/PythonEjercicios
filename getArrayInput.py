"""
Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 Then,
the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""

"""
Pregunta: Escriba un programa que tome 2 dígitos, X,Y como entrada y genere un array de 2 dimensiones.
El valor del elemento en la fila i y la columna j del array debe ser i*j.
Nota: i=0,1.., X-1; j=0,1,Y-1. Ejemplo Supongamos que se dan las siguientes entradas al programa: 3,5 Entonces,
la salida del programa debería ser: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""

input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)