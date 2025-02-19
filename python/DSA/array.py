import numpy as np

a_mul = np.array([[1, 2, 3, 4, 5] , [6, 7,'8', 9, 10]] , dtype = np.int32)  #2D array
# print(a_mul[0])
# print(a_mul[:,:])
print(a_mul.shape)

b_mul = np.array([[[[1,1,1],[1,1,1]],
                  [[2,2,2],[2,2,2]],
                  [[3,3,3],[3,3,3]],
                  [[4,4,4],[4,4,4]]],     #A little bit comples array
                  [[[1,1,1],[1,1,1]],     #4D array
                  [[2,2,2],[2,2,2]],      #2x4x2x3
                  [[3,3,3],[3,3,3]],
                  [[4,4,4],[4,4,4]]]]

                  )

c_mul = np.array(['h','e','l','l','o'])              

# print(b_mul.shape)
print(b_mul.ndim)
print(b_mul.size)
print(b_mul.dtype)
print(c_mul.itemsize) #size of each element in bytes
