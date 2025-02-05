print('identifichiamo la tua generazione')
input()
y = int(input('inserisci il tuo anno di nascita: '))
if y < 1946:
    print('sei più anziano dei boomer!')
elif y <= 1964:
    print('sei un boomer')
elif y <= 1980:
    print('fai parte della generazione X')
elif y <= 2000:
    print('sei un millenial')
else:
    print('fai parte della generazione Z')