"""
Write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2 c,2 b,2 e,1 d,1 g,1 f,1
"""

"""
Escribe un programa que cuente e imprima los números de cada carácter en una cadena introducida por consola.
Ejemplo: Si la siguiente cadena se da como entrada al programa:
abcdefgabc
Entonces, la salida del programa debería ser
a,2 c,2 b,2 e,1 d,1 g,1 f,1
"""

dic = {}
s=raw_input()
for s in s:
    dic[s] = dic.get(s,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
