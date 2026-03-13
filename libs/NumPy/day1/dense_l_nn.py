#  perceptron or dense layer 
#out=XW+b  ---> x - inputs,W- weights, b - bias, @ - matrix multiplication

import numpy as np
x=np.array([1,2,3])
w=np.array([
    [0.1,0.2],
    [0.3,0.4],
    [0.5,0.6]
])
b=np.array([0.1,0.2])
out=x@w+b
print(out)
