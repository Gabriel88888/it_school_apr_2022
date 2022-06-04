china_years = {
    2010: "Dragonului",
    2011: "Cocosului",
    2012: "Iepurelui",  
}



#lista chei-valori

k_v_china_years = china_years.items()

for kv in china_years.items():
    print("Anul", kv[0], "a fost anul", kv[1])

for k, v in china_years.items():
    print("Anul", k, "a fost anul", v)