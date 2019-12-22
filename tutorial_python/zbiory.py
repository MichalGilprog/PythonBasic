pierwszy_zbior = {"Warszawa", "Kraków" , "Wrocław", 'Łódz'}
drugi_zbiór = {"Warszawa"}

pierwszy_zbior.add("Kielce")
print(pierwszy_zbior)
pierwszy_zbior.add("Łódz")
print(pierwszy_zbior)
print(type(pierwszy_zbior))

print(pierwszy_zbior -drugi_zbiór)
print(pierwszy_zbior | drugi_zbiór)
print(pierwszy_zbior & drugi_zbiór)
print(pierwszy_zbior ^ drugi_zbiór)