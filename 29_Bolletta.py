quota = 20
volume = float(input('inserire il volume del gas consumato: '))
if volume <= 500:
    costo = volume * .575 + quota
else:
    volume = volume - 500
    costo = volume * .783 + 500 * .575 + quota
print('la bolletta è di', costo)