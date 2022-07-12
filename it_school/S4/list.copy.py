


colours1 = ["red", "blue"]
colours2 = colours1.copy()


print(colours1, colours2)

colours2[0] = "modified"

print(colours1, colours2)




def fct(list_in):
    print(list_in)

fct(colours1)
#s