class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "nazywam sie " + self.imie + " " + self.nazwisko


class Student(Osoba):

    def __init__(self, imie, nazwisko, numer_indeksu):
        Osoba.__init__(self, imie, nazwisko)
        self.index = numer_indeksu

    def podaj_numer_indeksu(self):
        return "Moj nr indeksu: "+ str(self.index)

    def przedstaw_sie(self):
        return "jestem studentem i mam na imie " +self.imie


osoba = Osoba("Tomek","Kot")
print(osoba.przedstaw_sie())
#print(student.podaj_numer_indeksu())