# unordered, no duplicated 
# supports mathematical operations

N = {1,2,3,6,6,9,4}
print(N)

for i in N:
    print(i)

N.add(12)
N.remove(12)
N.discard(88) # doesn't raise an error if item des not exist
print(N.pop())
# N.clear #clears the set

zero = {0}
W = N.union(zero)
zero.intersection(W)
W.difference(zero)
zero.issubset(W)
W.issuperset(zero)

#kindly check w3schools too