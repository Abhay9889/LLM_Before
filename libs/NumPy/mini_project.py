'''

Tokens
 ↓
Embedding
 ↓
Positional Encoding
 ↓
Self Attention
 ↓
Output

'''

import numpy as np
def softmax(x):
    x=x-np.max(x,axis=-1,keepdims=True)
    exp_x=np.exp(x)
    return exp_x/np.sum(exp_x,axis=-1,keepdims=True)

def attenstion(Q,K,V):
    dk=Q.shape[-1]
    scores=Q@K.T/np.sqrt(dk)
    weigths=softmax(scores)
    return weigths@V

class TransformerLayer:
    def __init__(self,d_model):
        self.Wq = np.random.randn(d_model,d_model)
        self.Wk = np.random.randn(d_model,d_model)
        self.Wv = np.random.randn(d_model,d_model)
    def forward(self,x):
        Q=x@self.Wq
        K=x@self.Wk
        V=x@self.Wv
        return attenstion(Q,K,V)
    
seq_len = 5
d_model = 16
X = np.random.randn(seq_len,d_model)
layer = TransformerLayer(d_model)

out = layer.forward(X)

print(out.shape)