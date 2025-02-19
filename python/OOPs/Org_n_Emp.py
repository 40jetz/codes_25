class House:

    def __init__(self , name , rooms : int , people : int):

        self.name = name
        self._rooms = rooms
        self. _people = people

    def __str__ (self):

        return f" The house named \"{self.name}\" has {self._rooms} rooms and {self._people} "
    
class Person():

    def __init__(self , name : str , role : str , age : int ):
        self.name = name
        self.role = role
        self.age = age
        self.works_in_Org = None # setting default value
        self._address = None

    def __str__ (self):
        return f"Employee : ({self.name} , {self.age} , {self.role}) " 

    def _Address (self):
        return self._address

class Organisation(Person) :
    
    def __init__(self, name : str, service : str):
        self.name = name 
        self.service = service

    def __str__ (self):
        return f" The {self.name} provides {self.services} "
    
    @staticmethod
    def ShowEmployees ():
        for person,works in Pzz.items():
            if works == True:
                return f"{person}"
    


House1 = House("Apoorv" , 6 , 4)


House2 = House ("BHB" , 5 , 2)


p1 = Person("Apoorv" , "SWE" , 25)
p1.works_in_Org = True
p1._address = "80zz"


p2 = Person("Lehman" , "Tester" , 28)
p2.works_in_Org = True 
p2._address = "3rdside"


p3 = Person("Neel" , "UE" , 20) 
p3.works_in_Org = False
p3._address = "RPT"

Pzz = {
    p1 : p1.works_in_Org ,
    p2 : p2.works_in_Org , 
    p3 : p3.works_in_Org 
}

print(Organisation.ShowEmployees())