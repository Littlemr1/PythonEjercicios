"""
Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
"""

"""
Escribe un programa que resuelva un antiguo acertijo chino: Contamos 35 cabezas y 94 patas entre las gallinas y los conejos de una granja.
¿Cuántos conejos y cuántas gallinas tenemos?
"""

def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)
