class Plane:
    def __init__(self):
        
        self.engines = 4
        self.doors = 8       
        self.length = 50
        self.wing_span = 33
        self.tank_volume = 22
        self.__engine_on = False

    def start_engine(self):
        print("Start engine...")
        self.__engine_on = True
    


class CargoPlane(Plane):
    def start_engine(self):
        print("Start big engine...")
        # super() - ne da acces la metodele clasei parinte
        return super().start_engine()

        
class Airliner(Plane):
    def __init__(self):
        super().__init__(2, 8)
        self.seat_number = 100

class PrivatePlane(Plane):
    pass

class Glider:
    pass


cargo_p = CargoPlane()
airliner = Airliner()
private_p = PrivatePlane()
glider = Glider()

# cargo_p.start_engine()
# print(cargo_p.is_engine_running())

# airliner.start_engine()
# print(airliner.is_engine_running())



# private_p.start_engine()
# print(private_p.is_engine_running())

def prepare_for_takeoff(plane):
    """Configureaza avionul pentru decolare"""

    print("Configure plane for takeoff...")
    if isinstance(plane,Plane):
        plane.start_engine()
    print("Taking off...")