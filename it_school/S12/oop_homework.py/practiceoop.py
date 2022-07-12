class Robot:
    garantie = 10 
    def __init__(self, nume, serial_number, hardware, software, sleep):
        self.nume = nume
        self.serial_number = serial_number
        self.harware = hardware
        self.software = software
        self.sleep = sleep

    def turn_on(self):
        if self.sleep == False:
           return f'{self.nume} is already runing'
        else:
            self.sleep = False
            return f'{self.nume} truned on'

r1 = Robot("John", "12345", "i5", "Python", True)
print(r1.software)
print(r1.sleep)
print(Robot.garantie)
print(r1.garantie)