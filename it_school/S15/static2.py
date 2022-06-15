class Pen:

# atribut de clasa
    brand = 'NOKI'

    def __init__(self,color):
        self.color = color
        self.is_empty = False


pen = Pen('red')
pen2 = Pen('black')

print(pen.brand)
print(pen2.brand)

pen2.owner = "Mihai"


# pen2.brand = "pen2-brand"







# print(Pen.brand)
# print(pen.brand)


