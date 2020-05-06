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
