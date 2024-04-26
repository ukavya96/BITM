from AbstractVehicle import AbstractVehicle
class Bike(AbstractVehicle):
    def display_details(self):
        print("Bike Details")
        print("color",self.color)
        print("number of tyres",self.num_tyres)
        print("Gears",self.gears)
        
class Car(AbstractVehicle):
    def display_details(self):
        print("Car Details")
        print("color",self.color)
        print("number of tyres",self.num_tyres)
        print("Gears",self.gears)
                
class Scooty(AbstractVehicle):
    def display_details(self):
        print("Scooty Details")
        print("color",self.color)
        print("number of tyres",self.num_tyres)
        print("Gears",self.gears)
                 
