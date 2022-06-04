user_info = {
    "name" : "Alex",
    "age" : 28,
    "email" : "alex.radu@emil.com",
    "gender" : "m",

}

china_years = {
    2010: "Dragonului",
    2011: "Cocosului",
    2012: "Iepurelui",  
}

#sortare dupa chei
sorted_user_info = sorted(user_info.items())

print("Sortat dupa chei")

def comparator(t):
    return[1]


for k, v in sorted(user_info.items()):
    print(k, "||",  v)

#sortare dupa valori
print("Sortat dupa valori")

for k, v in sorted(china_years.items(), key=comparator):
     print("Anul", k, "a fost anul", v)
