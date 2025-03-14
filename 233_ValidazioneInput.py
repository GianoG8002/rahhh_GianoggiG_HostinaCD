def ottieni_numeri(n):
    if type(n) == int:
        return n
    else:
        return 'Errore'

print(ottieni_numeri(2))
print(ottieni_numeri(6))
print(ottieni_numeri(False))
print(ottieni_numeri('wjai'))