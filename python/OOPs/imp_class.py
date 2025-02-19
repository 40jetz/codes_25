#NOTE - when you do print(instance.method) notice no '()' you get addres as the output
import csv

class Item:
    instances = []
    pay_rate: float = 0.6

    def __init__(self , name : str, price : float , quantity=0) -> None:
        Item.instances.append(self)

        number_of_instances = len(self.instances)

        #validate received args
        assert price >= 0 , f" Price {price} is not greaterthan 0 "
        assert quantity >= 0 , f"Quantity {quantity} is not greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        
        return f'[ {self.name} , {self.price} , {self.quantity} ]'

    

    def calculate_total_price(self):
        return int(self.price) * int(self.quantity)
    
    def num_of_instances():
        return f'Instances: {len(Item.instances)}'
    
    def discount(self):
        return self.price * Item.pay_rate
   
    @classmethod    
    def instanciate_from_csv (cls):

        with open("D:\\coding_stuff\\2025_progress\\python_code\\1_oops\\items.csv" , 'r') as f:
        # with open('items.csv' , 'r') as f:    
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                # print(item)
                Item ( 
                    name=item.get('name'),
                    price = int(item.get('price')),
                    quantity = int(item.get('quantity'))
                    )
                
    def __repr__(self):
        return 'Item ( {self.name} , {self.price} , {self.quantity} ) \n '

# item1 = Item( "Phone" , 1000,250 )
# item2 = Item( "Laptop" , 15_000, 55 )
# item3 = Item( "Camere" , 500 ,20 )
# item2.has_numpad = False

# print(Item.num_of_instances()) 
# print(item1.__dict__) #gives all the atributes that are only in this instance
# print(item1.discount())

# item2.pay_rate = 0.5
# item3.pay_rate = 0.7

# print(f"special discount for Laptops is {item2.discount()}")

# print(item1)



Item.instanciate_from_csv()
print(Item.instances)


