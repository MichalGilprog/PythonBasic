file = open("wiadomosc.txt")
zawartosc = file.read()
print(zawartosc)
file.close()

file = open("wiadomosc.txt")
zawartosc = file.readlines()
print(zawartosc)
file.close()


file = open("wiadomosc.txt")
zawartosc = file.readline()
print(zawartosc)
file.close()
print(type(file))
file = open("wiadomosc.txt")
for line in file:
    print(line)


