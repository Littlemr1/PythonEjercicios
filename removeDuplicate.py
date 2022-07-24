"""
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
"""

"""
Con una lista dada [12,24,35,24,88,120,155,88,120,155], escriba un programa para imprimir esta lista después de eliminar todos los valores duplicados con el orden original reservado.
"""

def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))
