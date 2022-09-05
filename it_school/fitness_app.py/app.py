import webbrowser
from time import sleep

print("Aceasta  este o aplicatie care te va ajuta sa scazi sau sa cresti in greutate")
nume = input("Pentru inceput te rog sa imi spui cum te numesti: ")
ani = input("Cati ani ai?: ")
kg = input("Imi poti spune ce greutate ai?: ")
inaltime= input("Inaltimea in centimetri(cm): ")
Sex = input("Si in final imi poti spune sexul tau? (masculin, feminin) \n"
            "Daca nu ai dori sa raspunzi la aceasta intrebare scrie '.' ")
sleep(0.3)

print("Acum iti vom calcula rata metabolica: ")
print("calculam................................................................")
sleep(1)

if Sex.lower() == "masculin":
    Bmr = (66.47 +( 13.75 * int(kg) + (5.003 * int(inaltime) - (6.755 * int(ani)))))
    print(f"Daca vei consuma acest numar de calorii zilnic nici nu vei slabii dar nici nu te vei "
          f"ingrasa {Bmr}")
elif Sex.lower() == "feminin":
    bmr = 655.1 + (9.563 * int(kg)) + (1.85 * int(inaltime)) - (4.676 * int(ani))
    print(f"Daca vei consuma acest numar de calorii zilnic nici nu vei slabii dar nici nu te vei "
          f"ingrasa {bmr}")
else:
    Bmr = (66.47 + (13.75 * int(kg) + (5.003 * int(inaltime) - (6.755 * int(ani)))))
    print(Bmr)
    print(f"Daca vei consuma acest numar de calorii zilnic nici nu vei slabii dar nici nu te vei "
          f"ingrasa {Bmr}")

scop = input("Doresti sa scazi in greutate?: ")

if scop.lower() == "da":
   alegere = input("Ati dori sa va recomand site-uri si aplicatii pentru a va ajuta?")
   if alegere.lower() == "da":
        print("Iti voi deschide in broswer 3 site-uri; Aplicatie pentru monitorizarea greutatii, dieta pentru scadere in greutate si exercitii ")
        sleep(1)
        webbrowser.open("https://www.myfitnesspal.com/")
        sleep(1)
        webbrowser.open("https://cureslabit.ro/slabire/plan-de-slabit-in-7-zile/")
        sleep(1)
        webbrowser.open("https://www.youtube.com/watch?v=8mOrDuV1EBU")
   else:
       print(f"Foarte bine {nume} iti urez mult succes")
else:
    alegere = input("Ati dori sa va recomand site-uri si aplicatii pentru a va ajuta? ")
    if alegere.lower() == "da":
        print(print("Iti voi deschide in broswer 3 site-uri; Aplicatie pentru monitorizarea greutatii, dieta pentru crestere in masa musculara si exercitii "))
        sleep(1)
        webbrowser.open("https://www.myfitnesspal.com/")
        sleep(1)
        webbrowser.open("https://doc.ro/controlul-greutatii/dieta-pentru-crestere-in-greutate-si-marirea-masei-musculare")
        sleep(1)
        webbrowser.open("https://www.youtube.com/watch?v=j6UyNq_TwGA")
    else:
        print(f"Foarte bine {nume} iti urez mult succes")


