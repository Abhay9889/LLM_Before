import numpy as np

# batch=1, tokens=3, embedding_dim=4
Q = np.random.rand(1,3,4)
K = np.random.rand(1,3,4)
V = np.random.rand(1,3,4)

d_k = Q.shape[-1]

#  QK^T using einsum
scores = np.einsum("bqd,bkd->bqk", Q, K)

#  scale
scores = scores / np.sqrt(d_k)

#  softmax
exp_scores = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)

#  multiply with V
output = np.einsum("bqk,bkd->bqd", weights, V)

print("Attention Output:\n", output)