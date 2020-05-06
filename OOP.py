 class Airplane:
     def __init__(self,make,model,year,max_speed,odometer,is_flying):
             self.make = make
             self.model = model
             self.year = year
             self.max_speed = max_speed
             self.odometer = odometer
             self.is_flying = False
     def take_off(self):
         self.is_flying = True
         print('Самолет взлетел')
     def fly(self):
         self.odometer /= 100
         print(self.odometer)

     def land(self):
         self.is_flying = False
         print('Самолет приземлился')

 Airplane=Airplane("Boeing", "an214", "2016",'1000 km/h',100000,False)
 Airplane.take_off()
 Airplane.fly()
 Airplane.land()


