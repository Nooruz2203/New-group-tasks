# class Airplane:
#     def __init__(self,make,model,year,max_speed,odometer,is_flying):
#             self.make = make
#             self.model = model
#             self.year = year
#             self.max_speed = max_speed
#             self.odometer = odometer
#             self.is_flying = False
#     def take_off(self):
#         self.is_flying = True
#         print('Самолет взлетел')
#     def fly(self):
#         self.odometer /= 100
#         print(self.odometer)

#     def land(self):
#         self.is_flying = False
#         print('Самолет приземлился')

# Airplane=Airplane("Boeing", "an214", "2016",'1000 km/h',100000,False)
# Airplane.take_off()
# Airplane.fly()
# Airplane.land()

class Car:
    def __init__(self, make, model, year, odometer,fuel,drive):
            self.make = make
            self.model = model
            self.year = year
            self.odometer = odometer
            self.fuel = fuel
            self.drive = drive

    def distance(self):
        self.drive /= 10
        print(self.drive)
    def add_distance(self):
        self.odometer += self.drive
        print(self.odometer)

    def subtract_fuel(self):
        if self.fuel - self.drive > 0:
            print('lets drive')
        else:
            print('Need more fuel, please, fill more!')

Car=Car("Mazda", "rx", "2016",0,70,100)
Car.distance()
Car.add_distance()
Car.subtract_fuel()