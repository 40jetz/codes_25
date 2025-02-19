# ordered, mutale(chngeable), duplicate = True

my_list = [1,2,3,4,5]

for i in my_list:
    print(i)

if 2 in my_list:
    print (True)
else:
    print(False)

my_list.append(6)
print(my_list)

my_list.insert(7,6)
print(my_list)

my_list.remove(7)
print(my_list)

my_list.pop([5])
print(my_list)

my_list.extent([6,7,8,9,10])
print(my_list)

inverted = my_list.reverse()
sorted_list = my_list.sort() #sort( key= a func for specified sorting , reverse=Bool)

my_list.index(4)

my_list.count(1)

reversed.clear()
print(reversed)

