while True:
    try:
        print('Podaj pierwszą liczbe')
        pierwsza_liczba = int(input())
        print('Podaj drugą liczbe')
        druga_liczba = int(input())
        print(pierwsza_liczba + druga_liczba)
        break
    except ValueError:
        print("Podałeś błędna wartość")
        print("podaj jeszcze raz")
        continue
