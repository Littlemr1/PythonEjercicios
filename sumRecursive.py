def secuencia(n):
    if n == 1 or n == 2 or n == 3 or n == 4:
        return 1
    else:
        return secuencia(n - 1) + secuencia(n - 2) + secuencia(n - 3) + secuencia(n - 4)

print(secuencia(5))
print(secuencia(6))
