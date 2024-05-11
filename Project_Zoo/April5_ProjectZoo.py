from Project_Zoo.April5_food_projectzoo import *
class Animal:
    def __init__(self,name,age,energy_level):
        self.name = name
        self.age =age
        self.energy_level = energy_level
    def __str__(self):
        return f'{self.name} Age: {self.age} Energy_Level: {self.energy_level}'
    def eat(self):
        if self.energy_level >=120:
            print("High energy level- feed 1 Kg less")
        else:
            print("Low energy level - feed 1 Kg more")

    def sleep(self):
        if self.energy_level >=110 and self.energy_level <120:
            print(f"Time to rest for {self.name}!")
    def make_sounds(self):
        if self.energy_level <100:
            print(f'{self.name} make sounds in Hungry')
        elif self.energy_level >=120:
            print(f'{self.name} wants to spend energy')

class Herbivores(Animal):
    species = 'Herbivores'
    def eat(self):
        print(f'{h.name} is grazing \nEnergy Level before grazing {self.energy_level}')
        self.energy_level += 20
        print(f'Energy Level after grazing {self.energy_level}')

class Carnivores(Animal):
    species = 'Carnivores'
    def eat(self):
        print(f'{c.name}--------hunt between 1 to 2 p.m----------')
        print(f'Energy Level of {c.name} before hunting {self.energy_level}')
        print(f'{c.name} hunted {h2.name}')
        self.energy_level += 50
        print(f'Energy Level of {c.name} after hunting {h2.name} is {self.energy_level}')


class Visitors():
     def __init__(self,name,age):
         self.name = name
         self.age = age
         self.food_by_visitors = 10
     def feed(self):
         h.energy_level += self.food_by_visitors
         print("Visitors are allowed to feed only herbivores------between 2 to 3 p.m-----")
         print(f"{self.name} is feeding the {h.name} and it's energy increased to : {h.energy_level} \n")
     def animal_show(self):
         print("---------------Animal-show starts at 3 p.m-----------------")
         print(f'{self.name} is watching {h.name} playing football \n')
         print("The Zoo closes at 6 p.m. Visit us again to have more fun !")

h =Herbivores('Elephant',15,120)
h1 = Herbivores('Zebra',10,70)
h2 = Herbivores('Giraffe',5,50)
c = Carnivores('Tiger', 7,140)
f = Flesh_eating(3,110)
g = Grass_eating(5, 70)

class Day_In_Zoo():
    def zoo_routine(self):
        herbivores_animal = [h,c]
        for animal in herbivores_animal:
            print(animal)
            print("It's a", animal.species)
            animal.eat()
            animal.sleep()
            animal.make_sounds()
            print("\n")

print("\nThe Zoo welcomes you to enjoy watching animal_show, animal_hunt and feed animal ! please check the time for each program\n The Zoo opens at 10 a.m")
print(f'\nDaily routine of animal in Zoo based on their energy level e.g:\n')
a = Animal('Lion',10,130)
print("1)",a)
# d = Flesh_eating(3,110)
f.species()
a.eat()
a.make_sounds()
a.sleep()
a2 = Animal('Deer',5,60)
print("2)",a2)
g.species()
a2.eat()
a2.make_sounds()
a2.sleep()

print("-------------------------------------------------------------------------------")
zoo = Day_In_Zoo()
zoo.zoo_routine()

print("-----------------------------------------------------------------------------------")
v = Visitors('John',25)
v1 = Visitors('Naruto',20)
v.feed()
v1.animal_show()










