class Pies:
    gatunek = "Pies domowy"

    def __init__(self, rasa, imie, wiek):
        print('Wewnatrz metoda init')
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):
        return ('hau hau')

    def zaprezentuj_psa(self):
        print('Rasa to: ' + self.rasa)
        print('Imie psa: ' + self.imie)
        print('Wiek psa: ' + str(self.wiek))



reksio = Pies('kundelek', 'Reksio', 2)
print(reksio.imie)
reksio.wiek=3

print(reksio.wiek)
print(reksio.rasa)
print(reksio.gatunek)
reksio.gatunek = 'ptak'

print(reksio.gatunek)


print(reksio.szczekaj())
print(reksio.zaprezentuj_psa())





