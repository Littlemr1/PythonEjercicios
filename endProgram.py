try:
    cadena = input('Digite un número: ')
    numero = int(cadena)
    exit(0)
except ValueError as e:
    print('Error:', e)
    exit(1)
