# ordered, immutable, duplicate = False

my_tup = (1,2,3,4,5)

my_tup.count(2)
my_tup.index(2)

for i in my_tup:
    print (i)

#unpacking tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits #tropic variable

print(green)
print(yellow)
print(red)

ruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(*green, yellow, red) = fruits #tropic variable

print(green)
print(yellow)
print(red)

# Joing tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Multiplying tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)