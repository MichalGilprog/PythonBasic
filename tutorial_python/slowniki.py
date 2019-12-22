dziennik = {1: 'Kowalski', 2: 'Nowak', 3: 'Piechniczek'}

print(dziennik)
print(dziennik.get(1))
dziennik[4] = 'Jankowski'

for key in dziennik.keys():
    print(key)

for values in dziennik.values():
    print(values)

del dziennik[1]

print(dziennik)

dziennik[0] = 'Nowy uczen'
print(dziennik)
print('nowy uczen' + dziennik[0])