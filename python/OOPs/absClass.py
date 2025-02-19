from abc import  ABC, abstractmethod

#NOTE - abstract classes don't have objects  therefore use abc module

class Computer (ABC): #NOTE - can't make object for this class

    @abstractmethod
    def process ():
        pass

class Laptop (Computer):
    def process(self):
        return "Running"
    
#com = Computer() will give error

com1 = Laptop()
print(com1.process())