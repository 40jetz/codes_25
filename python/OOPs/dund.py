class Counter:
    def __init__(self):
        self.value = 1

    def obj_up(self):
        self.value += 1

    def obj_down(self):
        self.value -= 1

    def __str__ (self) -> str :
        return f"count = {self.value}"

    def __repr__(self):
        return f" Its a developer friendly input, used for debugging "

    def __add__ (self , other) :
        if isinstance(other , Counter):
            return self.value + other.value

        raise Exception("Invalid Type : Can't add objects of different class")

count1 = Counter()
count2 = Counter()
print(count1+count2)

#NOTE -  Kindly search more on these methods