import numpy as np
import torch

a = np.arange(0,24).reshape(4,-1)
print(a)

t = torch.Tensor(a)
print("Tensor is::\n", t)
"""
Matrix Multiplication - torch.mm(a,b) = a @ b # both are same
a * b = a.Mul(b) - is elementwise multiplication
a.dot(b) - 
"""
x = torch.arange(1,9).reshape(2,4)
a = torch.tensor(x)
y = torch.arange(9,17).reshape(4,2)
b = torch.tensor(y)
# print(a*b) - this fails because the dimensions are same for both matrices
print(a.mm(b))
"""
Utilities:
a.numel() - prints no of elements in a tensor
a.norm() - normal distribution value
 
"""