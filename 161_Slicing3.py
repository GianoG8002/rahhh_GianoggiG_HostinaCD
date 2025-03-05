s = input('inserire una stringa: ')
l = s.split(' ')
o = ''
for i in range(len(l)):
    if i!=0 and i!=(len(l)-1):
        o = o+l[i]+' '
print(o)