'''
        Following is an example of Encapsulation
'''


class Person:
    def __init__(self,name):
        self.__name = name

    @property
    def name (self):
        return f'name = {self.__name}'
    
    @name.setter
    def name (self,value):
        if len(value) > 5:
            raise Exception('LOL no')
        else:
            self.__name = value

    
P1 = Person("Mdot EBK")
print(P1.name)


P1.name = "Sha Gzzzzzzzzzz"
print(P1.name)