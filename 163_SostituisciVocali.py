s = input('inserire una stringa: ')
l = ['A','a','E','e','I','i','O','o','U','u']
for i in range(len(l)):
    s = s.replace(l[i],'*')
print(s)