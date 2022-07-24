"""
Question A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡ The numbers after the direction are steps.
Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer. Example:
If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2
"""

"""
Pregunta Un robot se mueve en un plano partiendo del punto original (0,0). El robot puede moverse hacia ARRIBA, ABAJO, IZQUIERDA y DERECHA con unos pasos dados.
La traza del movimiento del robot es la siguiente: ARRIBA 5 ABAJO 3 IZQUIERDA 3 DERECHA 2 ¡ Los números después de la dirección son pasos.
Por favor, escriba un programa para calcular la distancia desde la posición actual después de una secuencia de movimiento y el punto original.
Si la distancia es un flotador, entonces sólo imprime el entero más cercano. Ejemplo:
Si las siguientes tuplas se dan como entrada al programa: ARRIBA 5 ABAJO 3 IZQUIERDA 3 DERECHA 2 Entonces, la salida del programa debería ser 2
"""

import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
