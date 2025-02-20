import stackClass as sc

stack2 = sc.Stack(5)
stack2.push(1)
stack2.push(2)
stack2.push(3)
stack2.push(4)
stack2.push(5)

print(len(stack2))
print("Peek of the stack is : " , stack2.peek())