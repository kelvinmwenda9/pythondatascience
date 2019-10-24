# object oriented programming
# real world object car, pen
# object have states and behaviours
# car states: color, weight, height, cost, age, how an object is at the moment
# car behavior: move, carry, hoot...what object does

class Car:
    '''This a car class'''
    # __init__ is special function, that creates object states
    # self represents this object the state
    def __init__(self, color, height, cost, wheels, speed):
        self.wheels = wheels # save wheels to self
        self.color = color
        self.height = height
        self.cost = cost
        self.speed = speed

    # behaviours
    def move(self):
        print('The car is moving slowly')
        print('The car has ', self.wheels, ' wheels')
        print('The color is ', self.color)
        print('the car will cost ', self.cost, 'KES')

    def carry(self):
        print('The car is suitable for small families')

    def hoot(self):
        print('The car is hooting at', self.height)

    def racing(self):
        print('The car is racing at a speed of', self.speed)


object = Car(color='Black',height=2.5,wheels=4,cost=1550000,speed=150)
object.move()
object.carry()
object.hoot()
object.racing()

