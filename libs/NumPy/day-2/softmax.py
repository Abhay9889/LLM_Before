import numpy as np
def softmax(x):
    exp_x=np.exp(x)
    return exp_x/np.sum(exp_x)

scores=np.array([2,1,0])
print(softmax(scores))