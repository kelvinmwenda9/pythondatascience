# create a fish
# states: species, color, weight,speed
# behaviours: swimming, jumping, eating, playing

class Fish:
    def __init__(self, species,color,weight,speed):
        self.species = species
        self.color = color
        self.weight = weight
        self.speed = speed

    def swim(self):
        print('The fish swims at a speed of ', self.speed, 'KPH')
        print('The fish is ', self.species)
        print('The fish is ', self.color)
    def jump(self):
        print('The fish has a weight of', self.weight, 'Pounds')



object = Fish('Tilapia','Gold','20','30')
object.swim()