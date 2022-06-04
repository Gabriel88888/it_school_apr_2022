# import random


# # # n = random.randint(0, 100)

# def say_welcome_message(name, lucky_number):
   
#     print("Welcome back", name, "!")
#     print("Lucky number is", lucky_number)

# #apel
# say_welcome_message ("gabi", 8)
# say_welcome_message ("hugo", 10)



# def is_even(n):
#     """Check if number is even"""
#     if n % 2 == 0:
#         return  True
#     else:
#         return False


# for i in range(10):
#     if is_even(i):
#         print("numar par")
#     else:
#         print("numar impar")
# for i in range(101):
#     if is_even(i):
#         print("**")
#     else:
#         print("--")



# 2. Utilizati functia de la pct 1 pentru a afisa toate numerele impare in intervalul
# [0, 50] si in intervalul [2000, 2100].

# for i in range (51):
#     if i % 2 != 0:
#         print(i, end = ' ')

# for i in range(1999, 2101):
#     if i % 2 != 0:
#         print(i, end = ' ')



# 3. Scrieti o functie care returneaza daca unu nr. (reprezentan un an) este
# considerat an bisect.


# year  =  int(input("Introdu un an: "))
# def is_bisect(n):
#      if n % 400 == 0:
#          return True
#      elif n % 100 == 0:
#                return False
#      else:
#           if n % 4 == 0:
#                return True

# if is_bisect(year):
#     print("este bisect")
# else:
#     print("nu este bisect")
# =========================================================================================

# 4. Scrieti o functie care returneaza volumul unui cub in litri. Aceasta va primi
# un singur argument reprezentand muchia cubului in metri.


# def cub_volume(edge):
#     """Calculate cube volume in liters"""
#     #1 m3 = 1000
#     return edge ** 3 * 1000
# def convert_to_m3(mc):
#     """Convert liters in m3"""
#     return mc / 1000

# print("volumul cubului: ", convert_to_m3(cub_volume(18)) ,"m3")

# #Ierarhie de apelare:
# 1 cube cub_volume
# 2 convert volume
# 3 print



#==========================================================================================
# 5. Scrieti o functie care returneaza volumul unui cilintru in litri,
# Aceasta va primi doua argumente reprezentand inaltimea si raza bazei in metri.




# import math
# def cylinder_volume(h, r):
#     return (math.pi * r * r * h)

# def raza(h, r):
#     return((2 * math.pi * r * h) + (2 * math.pi * math.pow(r, 2)))


# h = float(input('Introduceti inaltimea cilindrului: '))
# r = float(input('Introduceti raza cilindrului: '))

# vol = cylinder_volume(h, r)
# raza = raza(h , r)

# print('Volumul unui cilindru in litrii: {0:.2f}'.format(vol))




#===========================================================================================
# 6. Scrie o functie care converteste litrii in metri cubi.


# def cub_volume(edge):
# #     """Calculate cube volume in liters"""
# #     #1 m3 = 1000
#     return edge ** 3 * 1000
# def convert_to_m3(mc):
#     """Convert liters in m3"""
#     return mc / 1000

# print("volumul cubului: ", convert_to_m3(cub_volume(18)) ,"m3")



#===========================================================================================
# 7. Foloseste functiile de la pct. 4-6 pentru a calcula cate cuburi cu muchia de 18 metri
# sunt necesare pentru a umple un cilindru cu raza bazei de 20 m si inaltimea de 55 m.
# - Printeaza volumul cubului in metri cubi #### Volumul cubului: 20 m^3
# - Printeaza volumul cilindrului in metri cubi.
# - Printeaza rezultatul de la pct. 7
# - Toate valorile printate vor fi insotite de mesaje descriptive.



# def cub_volume(edge):
#   return edge ** 3 * 1000
# def convert_to_m3(mc):
    
#     return mc / 1000

# print("Volumul cubului: ", convert_to_m3(cub_volume(18)) ,"m3")


# r = float(input("Introduceti raza: "))
# h = float(input("Introduceti inaltimea: "))

# volume = 3.14 * r * r * h
# print("Volumul cilindrului in litrii este: ", volume)



# print("Sunt necesare -", volume / 5832.0,  "- cuburi ")








#===========================================================================================


# 8. Scrie un logger.