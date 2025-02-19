class Animal():
    def eat():
        return "yes"

class Prey(Animal) : #NOTE - inherit from Animal 
    def flee(self):
        print("Fleeing")

#NOTE - inherits from Prey and Preditor at second level (multiple inheritance)

class Preditor:
    def hunt(self):
        print("Hunting")

class Rabbit(Prey):
    pass

class Hawk(Preditor) :
    pass

class Fish(Preditor , Prey) :
    pass

fish = Fish()
hawk = Hawk()
rabbit = Rabbit()

fish.flee()
fish.hunt()