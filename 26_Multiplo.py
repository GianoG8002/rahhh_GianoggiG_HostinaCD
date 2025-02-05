n1 = int(input('inserisci un numero: '))
n2 = int(input('inserisci un altro numero: '))
if max(n1,n2)%min(n1,n2) == 0:
  print(str(max(n1,n2)),'è divisibile per',str(min(n1,n2)))
