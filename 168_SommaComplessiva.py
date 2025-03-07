lista_numeri = []
n = 10
while n != 0:
  n = int(input("Inserisci numero o inserisci 0 se vuoi fermarti: "))
  lista_numeri.append(n)
print('somma totale:', sum(lista_numeri))