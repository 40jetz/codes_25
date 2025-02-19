# for row in range(1,6):

#     for column in range(1,row+1):
        
#         print(row ,end='')

#     print("")


# def full_pyramid(n):
#     for i in range(1, n + 1):
#         # Print leading spaces
#         for j in range(n-i):
#             print(" ", end="")
        
#         # Print asterisks for the current row
#         for k in range(1, 2*i):
#             print("*", end="")
#         print()
   
# full_pyramid(5)

# for row in range(1,6):

#     for j in range(1,6-row):
#         print(" ",end='')
        

#     for column in range(1,row+1):
        
#         print(row ,end='')

#     print("")

# def inverted_pyramid(n):
#     for i in range(n,0,-1):
#         for j in range(1,i+1):
#             print((n+1)-i,end='') #change (n+1)-i to i to get from 5 to 1
#         print()

# inverted_pyramid(5)

# def inverted_centered_pyramid(n):
#     for i in range(n,0,-1):
#         for j in range(0,n-i):
#             print(' ',end='')
#         for k in range(n,n-i,-1):
#             print((n+1)-i,end='') #n-(i-1) for ascending order of 1 to n
#         print('')


# inverted_centered_pyramid(5)

