#Stacks are LIFO data structures. The last element added is the first one to be removed.
#Operations on stack:
#1. push: Add an element to the top of the stack.
#2. pop: Remove an element from the top of the stack.
#3. peek: Get the top element of the stack.
#4. is_empty: Check if the stack is empty.
#5. size: Get the number of elements in the stack.

#common implementation of stack is using list in python
#Other implementations are using linked list or deque from collections module.

#using lists

stack = [] # Created an empty stack
stack.append(1) #push 1 to stack
stack.append(2) #push 2 to stack
stack.append(3) #push 3 to stack
print(stack) #[1, 2, 3]
print(stack.pop()) #pop 3
# print(len(stack)) #2 - size of stack
print(stack.__len__()) #2 - size of stack #Justa fancy way of calling len(stack)
print(stack) #[1, 2]
print(stack[-1]) #2 - peek

#using deque
from collections import deque
