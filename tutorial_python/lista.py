zbior_zwierzat = ["kot", "pies", "owad"]
print(type(zbior_zwierzat))

imiona = ['Bartek', 'Tomek', "Andrzej", 1, 2, 3]

print(imiona[1])
print(imiona[2:4])
print(imiona.index("Tomek"))
imiona.append("Bartek")
imiona.insert(0, "Michal")
print(imiona)
print(len(imiona))

print(imiona[-1])
imiona.remove("Bartek")
print(imiona)
del imiona[0]
print(imiona)


pierwsza_lista = ['lampa','koc', 'cos']
print(pierwsza_lista*3)
druga_lista = [1,2,3,3]
print(pierwsza_lista+druga_lista)
pierwsza_lista.sort()
print(pierwsza_lista)
koc,krzeslo,lampa = pierwsza_lista
print(koc)
print(krzeslo)

