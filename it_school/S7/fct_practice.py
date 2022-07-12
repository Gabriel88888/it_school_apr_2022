valoare = input("Introdu un numar: ")

def calcul_suma(valoare):
    suma = 0
    for i in range(int(valoare) + 1):
        suma = suma + i
    return suma

rezultat = str(calcul_suma(valoare))

print("Suma pentru " + valoare + " este " + rezultat)