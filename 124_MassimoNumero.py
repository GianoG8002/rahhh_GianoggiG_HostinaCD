n = input('inserire una lista di numeri separati da degli spazi: ')
o = []
for i in n.split():
    o.append(int(i))
print('il numero più grande tra quelli inseriti è:', max(o))