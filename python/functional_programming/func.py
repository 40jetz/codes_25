print("output")

def ret_output(a,b):
    return a+b 
    
ret0 = ret_output(2,3) # should give 5
def ret_loop(a):
    for i in range (1,6):
        return a+i #should terminate the func at single call 
        
ret1 = ret_loop(1)

def yeild_table(a):
    
    for i in range(1,4):
        yield i #should not terminate the func at single call
        
    
ret2 = yeild_table(2)
    
print(ret0)
print(ret1)
#print(ret2) return a lazy iterator/generator object 
for value in ret2:
    print(value)