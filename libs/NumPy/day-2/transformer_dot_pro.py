import numpy as np
x=np.random.randn(3,4)
wq=np.random.randn(4,4)
wk=np.random.randn(4,4)
wv=np.random.randn(4,4)

Q=x@wq
K=x@wk
V=x@wv
print(Q)
print("------------------------------------------------------")
print(K)
print("------------------------------------------------------")

print(V)
print("------------------------------------------------------")

import numpy as np
# Linear Projections
Q = np.array([[1,0,1]])
K = np.array([[1,0,1],[0,1,1]])
V = np.array([[1,2],[3,4]])

scores = Q @ K.T  #Similarity Score
scaled = scores / np.sqrt(K.shape[1])  # Scaling

weights = np.exp(scaled) / np.sum(np.exp(scaled))  # Softmax applied 

output = weights @ V  #Weighted Value Sum

print(output)