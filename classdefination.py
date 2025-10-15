
class car: 
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.is_started= False

    def start (self):
        if not self.is_started:
           print(f"The {self.year} {self.make}{self.model} is starting")
           self.is_started =True
        else :
            print(f"The {self.year} {self.make} {self.model} is already running")

    def stop (self):
        if  self.is_started:
            print(f"The {self.year} {self.make} {self.model} is stoping")
        else :
            print(f"The {self.year} {self.make} {self.model} is already stopped")

print("--- car class Demonstration---")
my_car=car("range rover","tesla model s",2022)

print(f"My Car is {my_car.make,my_car.model,my_car.year}")

my_car.start()
my_car.start()
my_car.stop()
my_car.stop()
