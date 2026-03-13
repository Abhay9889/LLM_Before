import numpy as np
A = np.array([
[1,2,3],
[4,5,6],
[7,8,9]
])

b=np.array([10,20,30])
print(A+b)

embedding=np.random.randn(4,6)
print("Embedding-->")
print(embedding)
print("---------------------------------------") 
pos=np.random.randn(4,6)
result=embedding+pos
print(result)