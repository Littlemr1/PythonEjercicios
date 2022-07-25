import re

def validar_password(password):
    if 8 <= len(password) <= 16:
        if re.search('[a-z]', password) and re.search('[A-Z]', password):
            if re.search('[0-9]', password):
                if re.search('[$@#]', password):
                    return True
    
    return False

clave = input('Escriba la contraseña: ')

print(validar_password(clave))
