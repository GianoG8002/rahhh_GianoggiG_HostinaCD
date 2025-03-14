def quadrato(n):
    return n * n
def somma_quadrati(a, b):
    return [quadrato(a) + quadrato(b), (quadrato(a) +quadrato(b)) / 2]

print(somma_quadrati(3, 4))
print(somma_quadrati(3, 8))
print(somma_quadrati(6, 9))