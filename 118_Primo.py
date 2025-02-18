n = int(input("Inserisci un numero: "))
l = []
for i in range(1,n+1):
    if (n%i == 0):
        l.append(i)
if l == [1,n]:
    print('il numero che hai inserito è primo')
else:    
    print('il numero che hai inserito non è primo')