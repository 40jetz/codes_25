myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

file = {
    "Python" : {
        "files" : 10
    },

    "xml" : {
        "files" : None
    }
}

print(myfamily["child2"]["name"])

# for i in myfamily :
#     print(myfamily[i])

# for x, obj in myfamily.items():
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])

a = {
  
  "b" : {

    "c" :{
      
      "name" : "three"

    }

  }

}

for x,y in a.items() :
  print(x, ":" , y)

  for  p,q in y.items():
    print(p, ":" , q)

    for i,j in q.items():
      print(i, ':' , q[i])


#NOTE - NEsted List 

matrix = [[j for j in range(2)] for i in range(2)]

for i in matrix:
  print(i)