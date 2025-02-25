s = input('inserire la stringa da verificare: ')
print('inserire il carattere da verificare: ')
c = ''
while len(c)>1 or len(c) == 0:
    c = input()
    if len(c)>1:
        print('inserire un solo carattere ')
n = 0
for i in range(len(s)):
    if s[i] == c:
        n+=1
print('ci sono', n, c, 'nella stringa', s)