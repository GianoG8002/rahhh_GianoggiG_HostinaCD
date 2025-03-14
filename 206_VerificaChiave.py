libro = {'titolo':'Mein Kampf','autore':'Adolf Hitler','pubblicazione':'luglio 1925'}
print('dizionario originale:',libro)
if libro.pop('editore',None) == None:
    libro.update(editore='editore sconosciuto')
print('dizionario aggiornato',libro)