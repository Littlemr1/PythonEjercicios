"""
Question: A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1
"""

"""
Pregunta: Un sitio web requiere que los usuarios introduzcan un nombre de usuario y una contraseña para registrarse.
Escriba un programa para comprobar la validez de la contraseña introducida por los usuarios. Los siguientes son los criterios para comprobar la contraseña:

Al menos 1 letra entre [a-z]
Al menos 1 número entre [0-9]
Al menos 1 letra entre [A-Z]
Al menos 1 carácter de [$#@]
Longitud mínima de la contraseña de la transacción: 6
Longitud máxima de la contraseña de la transacción: 12
Su programa debe aceptar una secuencia de contraseñas separadas por comas y las comprobará de acuerdo con los criterios anteriores.
Las contraseñas que coincidan con los criterios se imprimirán, cada una separada por una coma.
Ejemplo Si se dan las siguientes contraseñas como entrada al programa: ABd1234@1,a F1#,2w3E*,2We3345 Entonces, la salida del programa debería ser:ABd1234@1
"""

import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))
