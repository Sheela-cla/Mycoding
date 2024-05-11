class Food:
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
    def __str__(self):
        return f'Height : {self.height} ft, Weight : {self.weight} Kgs'
class Flesh_eating(Food):
    def species(self):
        print(f'---FLESH EATING ANIMAL---')
        if self.weight >100:
            print(f" It's Height: {self.height} ft and Weight: {self.weight} Kgs eats 6 Kg Meat every day")
        else:
            print(f"It's Height: {self.height} ft and Weight: {self.weight} Kgs eats 3 Kg Meat every day")
class Grass_eating(Food):
    def species(self):
        print("---GRASS EATING ANIMAL---")
        if self.weight >100:
            print(f"It's Height: {self.height} ft and Weight: {self.weight} Kgs Eats 6 Kg Grass Food every day")
        else:
            print(f" It's Height: {self.height} ft and Weight: {self.weight} Kgs Eats 3 Kg Grass Food every day")



