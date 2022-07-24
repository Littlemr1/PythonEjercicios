"""
Question: Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following: D 100 W 200

D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500
"""

"""
Pregunta: Escriba un programa que calcule el importe neto de una cuenta bancaria basándose en un registro de transacciones a partir de la entrada de la consola.
El formato del registro de transacciones es el siguiente D 100 W 200

D significa depósito mientras que W significa retirada. Supongamos que se suministra la siguiente entrada al programa: D 300 D 300 W 200 D 100 Entonces,
la salida debería ser 500
"""

netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(netAmount)
