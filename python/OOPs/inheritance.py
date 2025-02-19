class Animal:
    def __init__ (self, name : str , is_pet : bool):
        self.name = name
        self.is_alive = True
        self.is_pet = is_pet 

    def eat (self):
        return f' {self.name} is eating '
    
    def sleep (self):
        return f' {self.name} is sleeping '
    
class Dog(Animal):
    def bark (self):
        return ' Woof Woof ! '
    
class Cat(Animal):
    def meow (self):
        return "Meow"
    
dog1 = Dog("Ruffy" , True )
cat1 = Cat("Gen" , False )

print(dog1.bark())
print(dog1.eat())