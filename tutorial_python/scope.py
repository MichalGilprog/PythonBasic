imie = "Bartek"
nazwisko = "Nowak"
def przedstaw_sie():
    global nazwisko
    nazwisko = "Kowalski"
    print(nazwisko)
    print(imie)

print(imie)
print(nazwisko)
przedstaw_sie()
print(nazwisko)