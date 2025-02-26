s = input('inserire una stringa: ')
print(s,end='')
for i in range(len(s)):
    print(s[-i-1],end='')