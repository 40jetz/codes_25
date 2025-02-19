# keys =  [1,2,3,4,5,6]
# values = [1,4,9,16,25,36]
# dict = {}
# for i in range(len(keys)):
    
#     dict[keys[i]] = values[i]

# print(dict)

# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}



class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None        

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420