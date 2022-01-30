# py9.szotar.3.1
3.1 Feladat

szotar = {
    'szam': 10,
    'szoveg': 'valami',
    'igazhamis': True,    
}

print(szotar)
print()

beker = input('Szeretnél változtatni az adatszerkezeten? (igen/nem): ')
if beker == "igen" or beker == "Igen":
    beker1 = input('Első új érték: ')
    beker2 = input('Második új érték: ')
     
    szotar[beker1] = beker2

if beker == "nem" or beker == "Nem":
    exit

print(szotar)
