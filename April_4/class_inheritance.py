class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        return f'Manufacture: {self.make} Model : {self.model} Year: {self.year}'
    def start(self):
        print("The car is starting, it's in good condition")
    def stop (self):
        print("The car is not starting, it's condition is bad")
    def fuel_up(self):
        print("The car needs to be fueled")
class Car(Vehicle):
    def __init__(self,make,model,year,num_door):
        super().__init__(make,model,year)
        self.num_door = num_door
    def __str__(self):
        return f'{super().__str__()} Number of doors: {self.num_door}'
    def honk_horn(self):
            print("My horn reach upto 200 meters")

class Bicycle(Vehicle):
    def __init__(self,make,model,year,num_gears):
        super().__init__(make,model,year)
        self.num_gears = num_gears
    def __str__(self):
        return f'{super().__str__()} Number of gears: {self.num_gears}'
    def honk_bell(self):
        print("I'm Bicycle my horn reach upto 50 meters")
class Motorcycle(Vehicle):
    def __init__(self,make,model,year,num_wheels):
        super().__init__(make,model,year)
        self.num_wheels =num_wheels
    def __str__(self):
        return f'{super().__str__()} Number of wheels: {self.num_wheels}'
    def wheels(self):
        print("I'm Motorcycle my horn reach upto 100 meters")

t = Vehicle('Ford','Sports',2023)
print(t)
c = Car('Volvo','1.4m',2023,4)
b= Bicycle('Nike','Race','2024',2)
m = Motorcycle('Honda','2.4',2024,2)
print(m)
print(c)
print(b)
b.honk_bell()
c.honk_horn()
t.start()
t.stop()









