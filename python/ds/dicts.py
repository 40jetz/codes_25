things = {
    
  "name" : "John" ,
  "age" : 24,
  "certification" : "B.tech EE",
  "fav_gun" : ".357"

}

things['Work'] = None

things.update({'Birth':"14-sep-1999"})

key_ls = things.keys()
value_ls = things.values()
print(value_ls)
print(value_ls)

def pop_that():
    that = things.popitem()
    print(that)

pop_that()

things.pop("certification")
del things["fav_gun"]


def del_dict(): #raises exception
  useless = dict()

  del useless

  try:
      print(useless)

  except:
      raise Exception(' Are you dumb ')
  
clear_me = dict()
clear_me["some"] = "thing"

print(clear_me)

clear_me.clear()
print(clear_me)

for x,y in things.items():
    print(x, ':' , y)

