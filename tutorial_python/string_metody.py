imie = "Michal"
nazwisko = "Kowalski 'Nowak'"
adres = '''Kwiatowa 26/1
            Warszawa 02-001'''

print(nazwisko)
print('Czytam \tksiazke \n \'WŁADCA pierścieni\'')


print ("małe litery".upper())
print ("DUŻE LITERY".lower())

print(imie.islower())
print(nazwisko.isupper())


for char in "Michał":
    print(char)

print(imie[0])
print(imie[2:5])
print(imie.index("a"))
print ("Kasia" not in "Ala ma kota")

print(" OK ".join(['Ala','ma','kota']))
print ("Ala ma kota i psa".split(" "))
print(imie.startswith("Mi"))
print(imie.endswith("al"))