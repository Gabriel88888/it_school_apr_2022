class Ticket:
    def __init__(self,price):
        #Atribute de instanta
        self.price = price
    
    def get_price_w_taxes(self):
        return self.price + self.price * 0.19

    #definire metoda statica
    @staticmethod
    def get_tva_ratio(): # metodele statice nu au nevoie de self
        return 0.19



#instantiere
# tk = Ticket()

#tk = obiect = instanta
# tk.get_tva_ratio
print(Ticket.get_tva_ratio())