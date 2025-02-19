class StaticArray :
    def __init__ (self, size):
        self.size = size

    def create (self, data = [] ) :
        if len(data) > self.size :
            raise Exception("Data size is greater than array size")
        self.array = []
        for i in data:
            self.array.append(i)

        def throw():
            for i in self.array:
                print(i)

        return throw
    
arr1 = StaticArray (5)
arr1_ = arr1.create([1,2,3,4,5])
arr1_() # 1 2 3 4 5
    