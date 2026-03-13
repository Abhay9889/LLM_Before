import numpy as np
class Dense:
    def __init__(self,input_size,output_size):
        self.w=np.random.randn(input_size,output_size)
        self.b=np.zeros(output_size)

    def forward(self,x):
        return x@self.w+self.b
        
layer=Dense(3,2)
x=np.array([[1,2,3]])
print(layer.forward(x))

"""

Image → NumPy Array
       ↓
Flatten
       ↓
Dense Layer
       ↓
Prediction

"""