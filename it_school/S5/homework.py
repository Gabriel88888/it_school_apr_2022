# # # # # # # raza = int(input("Raza este: "))
# # # # # # # perimetru = 2 * 3.14 * raza
# # # # # # # aria = 3.14 * (raza ** 2)

# # # # # # # if raza <= 100:
# # # # # # #     print("Perimetrul cercului= ", perimetru)
# # # # # # # elif raza < 100:
# # # # # # #     print("Aria cercului= ", aria)
# # # # # # # else:
# # # # # # #     print("End")


# # # # # # h = 9
# # # # # # m = 17
# # # # # # if m < 15:
# # # # # #     print("Sfertul academic")
# # # # # # elif h > 9 and h <=17:
# # # # # #     print("Buna ziua!")
# # # # # # else:
# # # # # #     print("Buna seara")




# # # # # a = input("a =")
# # # # # b = input("b= ")

# # # # # a = int(a)
# # # # # b = int(b)

# # # # # if a > b:
# # # # #     print("a mai mare decat b")
# # # # #     if b < b - a:
# # # # #         print("b este mai mic decat jumatatea lui a")
# # # # # elif a == b:
# # # # #     print("a si b sunt egale")
# # # # # else:
# # # # #     print ("b mai mare decat a")
    

# # # # # print("DONE")




# # # # numar = input("n= ")
# # # # numar = int(numar)

# # # # if numar < 10  or numar > 50:
# # # #     print("numar acceptat")
# # # # else:
# # # #     print("numar neacceptat")





# age = input("Varsta ")
# age = int(age)

# if age >= 18:
#     print("Major")
# elif age < 18:
#     print("Minor")

#======================================================================






# # 4. Scrieti un program care citeste de la tastatura un nr natural "n", 
# # si afiseaza n! (factorial). 6! = 1 * 2 * 3 * 4 * 5 * 6


# n = int(input("Introdu un numar: "))

# fact = 1

# for i in range(1, n + 1):
#     fact = fact * i
# print("Factorial: " ,fact)

#==========================================================================

   
    


# 5. Scrieti un program care afiseaza toate litere (capitale) ale 
# alfabetului englez, pe aceiasi linie despartite prin spatiu. 
# **A se vedea tablelul ASCII. chr(65) -> A


# for i in range(65, 91):
#     print(chr(i), end = '  ')

#==============================================================================



# 6. Intr-o cutie se află 300 de bile, numerotate cu numere începând de la unu, 
# din trei în trei. Toate bilele cărora le corespund numere pare sunt verzi. 
# Să se afle câte bile verzi sunt.


# even_count = 0
# for i in range(1, 900, 3):
#     if i % 2 == 0:
#         print(i, end = '  ')
#         even_count = even_count + 1
# print(" === Total Bile Verzi ===", even_count)

#=====================================================================================
    



# 7. Scrieti un program care citeste doua nr de la tastatura si calculeaza produsul
# lor. A nu se utiliza operatorul de inmultire.















# 8. Scrieti un program de tip joc "ghiceste numarul".
#     Cerinte: 
#     1. Programul genereaza un numar aleator in intervalul [1, 99].
#     2. Intr-o bucla conditionata de gasirea numarului cautat:
#         - se citeste de la tastatura un numar
#         - se compara cu numarul cautat
#         - daca numarul introdus este mai mic decat numarul cautat se afiseaza +
#         - daca este mai mic se afiseaza -
#     3. Dupa ce numarul este ghicit se afiseaza un mesaj de felicitare si numarul cautat.

#     EX: 
#     Incepe jocul!
#     Introduceti un numar intre 1 si 99.
#     3
#     +
#     6
#     +
#     20
#     +
#     60
#     -
#     50
#     +
#     56
#     -
#     Felicitari!
#     Ai ghicit numarul: 56



# import random
# n = 100
# to_be_guessed = int(n * random.random() + 1)
# guess = 0

# while guess !=  56:
#     guess = int(input("Incepe jocul: "))
#     if guess > 0:
#         if guess > 56:
#             print(" - ")
#         elif guess < 56:
#                 print(" + ")
# else:print("Felicitari , ai ghicit numarul")

#===========================================================================

 


# 9. Sa se modifice programul de la pct. 8 astfel:
#     - modificam intervalul de generare la [1, 300]
#     - in loc de + - o sa afisam dupa cum urmeaza;
#     - cand numarul introdus este:
#         +/- 50 fata de numarul cautat: "Gheata"
#         +/- 40 fata de numarul cautat: "Frig"
#         +/- 30 fata de numarul cautat: "Rece"
#         +/- 20 fata de numarul cautat: "Caldut"
#         +/- 10 fata de numarul cautat: "Cald"
#         +/- 5 fata de numarul cautat: "Frige"
#         +/- 2 fata de numarul cautat: "Arde"

#     EX:
#     Incepe jocul!
#     Introduceti un numar intre 1 si 99.
#     50
#     Caldut
#     44
#     Caldut
#     60
#     Rece
#     34
#     Frige
#     33
#     Frige
#     31
#     Arde
#     Felicitari!
#     Ai ghicit numarul: 31



# import random
# n = 300
# b = 240
# c = 190
# d = 130
# e = 90
# to_be_guessed = int(n * random.random() + 1)
# guess = 31

# while guess == 31 :
#     guess = int(input("Incepe jocul: "))
# if n >= 250:
#     print("Gheata")
# elif b >= 190:
#     print("Frig")
# elif c >= 140:
#     print("rece")
# elif d >= 100:
#     print("caldut")
# elif e >= 40:
#     print("frige")
# else:
#     if guess == 30:
#         print("Felicitari")

    # if guess > 0:
    #     if guess > 56:
    #         print(" - ")
    #     elif guess < 56:
    #             print(" + ")
# else:print("Felicitari , ai ghicit numarul")













# 10. Scrieti un program care citeste un numar natural (n) de la tastatura si 
# genereaza un grafic de forma:

# *
# *
# **
# ***
# *****
# ********

# Graficul va fi format din n linii iar pe fiecare linie se afiseaza x stelute.
# x reprezinta al n nr a lui Fibonacci.




# n = 3
# k = 1
# n = int(input(" Grafic de forma: "))

# while k <= n:
#     print("*" * k, "+" * (n - k), sep='')
#     k = k + 1



# def fibonacci

# n = int(input(" Grafic de forma: "))
# a = 0
# b = 1
# c = a + b

# while c <= n:
#     print(c)
#     a = b
#     b = c
#     c = a + b

# for i in range(1, n + 1):
#     print("* " * i)

# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("numar negativ")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range (2, n):
#             c = a + b
#             a = b
#             b = c
#         return b
# print(fibonacci(10))



