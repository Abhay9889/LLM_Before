import numpy as np

arr=np.array([
    [12,30,37,35],   
    [1,2,3,4]
])
#  ---->  2 rows , 4 columns
print(f"{arr}")
print(arr.shape)
print(arr.ndim)
arr1=np.array([
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,21]
    ]
])

print(arr1)
print(arr1.shape)
print(arr1.ndim)