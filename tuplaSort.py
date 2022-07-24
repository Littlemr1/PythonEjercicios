"""
Question: You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers.
The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Then,
the output of the program should be: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""

"""
Pregunta: Se requiere escribir un programa que ordene las tuplas (nombre, edad, altura) por orden ascendente donde el nombre es una cadena,
la edad y la altura son números. Las tuplas se introducen por consola. El criterio de ordenación es:
1: Ordenar en base al nombre;
2: Luego ordenar en base a la edad;
3: Luego ordenar por la altura.
La prioridad es que nombre > edad > puntuación. Si se dan las siguientes tuplas como entrada al programa:
Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Entonces, la salida del programa debería ser:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))
