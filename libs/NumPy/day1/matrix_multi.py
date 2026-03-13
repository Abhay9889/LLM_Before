import numpy as np
arr=np.array([
    [1,2,3],
    [4,5,6]
])
arr1 = np.array([[7,8],
                 [9,10],
                 [11,12]])

ans=np.dot(arr,arr1)  ## (2,3) dot (3,2) → (2,2)
print(ans)

#(m×n) × (n×p) = (m×p)


A = np.array([[1,2,3],
              [4,5,6]])

B = np.array([[7,8],
              [9,10],
              [11,12]])
print("---------------------------------------------------")
C = A @ B
print(C)

#For higher dimensions, @ is more predictable and recommended, while np.dot can behave differently.