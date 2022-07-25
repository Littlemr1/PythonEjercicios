from random import randint

aleatorio = randint(1, 9)
numero = 0

while aleatorio != numero:
    numero = int(input('Adivine un número entre 1 y 9: '))

print('¡Bien hecho!')
