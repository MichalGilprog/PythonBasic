def rzeczy(pierwsza_rzecz, *args):
    print(pierwsza_rzecz)
    print(args[0])
    for arg in args:
        print(arg)


rzeczy('lampa', 'koc', 'lozko')


def dziennik(klasa, **kwargs):
    print('Klasa' + klasa)
    for nazwisko in kwargs.keys():
        print(nazwisko)
    print(kwargs.get('Kowalski'))


dziennik(Kowalski=1, Nowak=2, Maly=3)
