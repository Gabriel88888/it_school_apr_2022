# 1. Scrieti o functie care returneaza reversul unei liste. Lista primita ca parametru nu 
# trebuie modificata.

#============================================================================================
# 2. Scrieti o functie care returneaza True daca lista primita ca param. este sortata,
# altfel returneaza False.

#REZOLVARE:


# lst = [1, 4, 7, 14, 10, 55, 33]

# lst1 = sorted(lst)

# if lst1 == sorted(lst):
#     print(True)
# else:
#     print(False)




#============================================================================================
# 3. Scrieti o functie care primeste doua liste ca parametri. Listele contin numere intregi.
# Fct. returneaza o singura lista formata din inmultirea dupa cum urmeaza: primul elem. din prima 
# lista X primul elem. din a 2-a lista .... etc.
# [1, 2, 3]
# [3, 4, 6]
# => [3, 8, 18]

#REZOLVARE:


# list1 = [2, 4, 8]
# list2 = [3, 5, 2]

# list3 = []

# print("Lista 1 valoare", list1)
# print("Lista 2 valoare", list2)

# for n in range(0, len(list1)):
#     list3.append(list1[n] * list2[n])

# print("Rezultatul inmultirii celor 2 liste: ", list3)


# ==========================================================================================
# 4) Create a mixed (sting and int) list with 10 elements

# a = ['dog', 'cat', 'rabbit', 'horse']
# b = [1, 2, 3, 4]











#==========================================================================================

# 5) Print first and last element


# lst = [10, 12, 14, 16, 18, 20]

# print(lst[0])
# print(lst[-1])



#===========================================================================================
# 6) Replace second element with 144

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# numbers[1] = 144
# print(numbers)


# 7) Print the index of element with value 144

# numbers = [1, 2, 3, 4, 5, 144, 6, 7, 8]

# print(list(enumerate(numbers)))

# 8) Make a function to remove all the element with a maximal value from a list; return a new list (original list does not modify)











# 9) Make a function for printing the first 5 longest strings in a list ; (len("test"))

















# 10) Make a function to check if the elements of a lists are equals (without using for) -> return bool


#=============================================================================================================


# 11) Count each word in list. Print how may times each word appears in list.

# Output ex:
# a 30
# the 20
# home 1
# # test 4
# words = ['Python', 'is', 'an', 'easy', 'to', 'learn', 'powerful', 'programming', 'language', 'It', 'has', 'efficient', 'high-level', 'data', 'structures', 'and', 'a', 'simple', 'but', 'effective', 'approach', 'to', 'object-oriented', 'programming', 'Pythons', 'elegant', 'syntax', 'and', 'dynamic', 'typing', 'together', 'with', 'its', 'interpreted', 'nature', 'make', 'it', 'an', 'ideal', 'language', 'for', 'scripting', 'and', 'rapid', 'application', 'development', 'in', 'many', 'areas', 'on', 'most', 'platforms', 'The', 'Python', 'interpreter', 'and', 'the', 'extensive', 'standard', 'library', 'are', 'freely', 'available', 'in', 'source', 'or', 'binary', 'form', 'for', 'all', 'major', 'platforms', 'from', 'the', 'Python', 'web', 'site', 'and', 'may', 'be', 'freely', 'distributed', 'The', 'same', 'site', 'also', 'contains', 'distributions', 'of', 'and', 'pointers', 'to', 'many', 'free', 'third', 'party', 'Python', 'modules', 'programs', 'and', 'tools', 'and', 'additional', 'documentation', 'The', 'Python', 'interpreter', 'is', 'easily', 'extended', 'with', 'new', 'functions', 'and', 'data', 'types', 'implemented', 'in', 'C', 'or', 'C++', '(or', 'other', 'languages', 'callable', 'from', 'C)', 'Python', 'is', 'also', 'suitable', 'as', 'an', 'extension', 'language', 'for', 'customizable', 'applications', 'This', 'tutorial', 'introduces', 'the', 'reader', 'informally', 'to', 'the', 'basic', 'concepts', 'and', 'features', 'of', 'the', 'Python', 'language', 'and', 'system', 'It', 'helps', 'to', 'have', 'a', 'Python', 'interpreter', 'handy', 'for', 'hands-on', 'experience', 'but', 'all', 'examples', 'are', 'self-contained', 'so', 'the', 'tutorial', 'can', 'be', 'read', 'off-line', 'as', 'well', 'For', 'a', 'description', 'of', 'standard', 'objects', 'and', 'modules', 'see', 'The', 'Python', 'Standard', 'Library', 'The', 'Python', 'Language', 'Reference', 'gives', 'a', 'more', 'formal', 'definition', 'of', 'the', 'language', 'To', 'write', 'extensions', 'in', 'C', 'or', 'C++', 'read', 'Extending', 'and', 'Embedding', 'the', 'Python', 'Interpreter', 'and', 'Python/C', 'API', 'Reference', 'Manual', 'There', 'are', 'also', 'several', 'books', 'covering', 'Python', 'in', 'depth', 'This', 'tutorial', 'does', 'not', 'attempt', 'to', 'be', 'comprehensive', 'and', 'cover', 'every', 'single', 'feature', 'or', 'even', 'every', 'commonly', 'used', 'feature', 'Instead', 'it', 'introduces', 'many', 'of', 'Python’s', 'most', 'noteworthy', 'features', 'and', 'will', 'give', 'you', 'a', 'good', 'idea', 'of', 'the', 'language’s', 'flavor', 'and', 'style', 'After', 'reading', 'it', 'you', 'will', 'be', 'able', 'to', 'read', 'and', 'write', 'Python', 'modules', 'and', 'programs', 'and', 'you', 'will', 'be', 'ready', 'to', 'learn', 'more', 'about', 'the', 'various', 'Python', 'library', 'modules', 'described', 'in', 'The', 'Python', 'Standard', 'Library']

# print("Elementul a , apare de : ", words.count('a'), "ori")
# print("Elementul the , apare de : ", words.count('the'), "ori")
# print("Elementul it , apare de : ", words.count('it'), "ori")
# print("Elementul to , apare de : ", words.count('to'), "ori")