# suma multiplilor de 3 si 5 in intervalul 0 - 1000


# multipli_3 = list(range(3, 1001, 3))
# multipli_5 = list(range(5, 1001, 5))

# print(sum(set(multipli_3 + multipli_5)))


#nu se face niciodata
# print(sum(set(list(range(3, 1001, 3)) + list(range(5, 1001, 5)))))


a = int (input("Introduceti capatul intervalului: "))
b= int(input("Introduceti primul numar: "))
c = int (input("Introduceti al doilea numar: "))

multiplii_b = list (range(1*b, a+1, b))
multimplii_c = list (range(1*c,a+1,c ))


set1 = set(multiplii_b)
set2 = set(multimplii_c)


intersec = set1.intersection (set2)
for i in intersec:
    print (i)