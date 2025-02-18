n1 = int(input("Inserisci il dividendo: "))
n2 = int(input("Inserisci il divisore: "))
for i in range(n1, 0, -1):
    if i % n2 == 0:
        print(i, end=" ")
