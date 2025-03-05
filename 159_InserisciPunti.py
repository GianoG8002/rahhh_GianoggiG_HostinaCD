s = input('inserire la stringa: ')
o = ''
for c in range(len(s)):
    o = o+('.'*c)
    o = o+s[c]
print(o)