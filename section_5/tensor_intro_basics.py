import numpy as np
import torch
arr = np.arange(0,10)
print(np)

#above lines covered converting np array to torch tensor
# focus is on torch tensors
print("retains the dtype from np array as int always")
x = torch.tensor(arr)  
print(x)

#considers the input as float by default
print(" dtype is float by default")
y = torch.Tensor(arr)
print(y)

print("creating tensors directly")
print(torch.empty(2,2)) # creates 2,3 array with very close values to zeros.

print(torch.zeros(2,3, dtype=torch.int64))

print(torch.ones(4,3))
print(torch.arange(0,18,2).reshape(3,3))
print("changing the dtype of a tensor")
my_tensor = torch.tensor([1,2,3,4,5,6,7,8,9]).reshape(3,3)
print(my_tensor, "torch dtype is ", my_tensor.dtype)
new_tensor = torch.tensor(my_tensor)
#new_tensor = new_tensor.type(torch.float16)
#print("dtype of new_tensor is::", new_tensor.dtype)
#torch.rand()

#x = torch.tensor(0,10, shape=(3,3))
#torch.rand_like(x)  # retains the shape of x, produces with new values.
#torch.randn_like(x)
#torch.rand_like(x, low=0, high=10)
#torch.manual_seed(100)

#in place tensor functions like np arrays

a = torch.tensor([1,2,3])
b = torch.tensor([4,5,6])
a.add(b)  # not inplace, torch.add(a,b)
print('a tensor after addition is::\n',a)
a.add_(b)
print("a tensor after inplace addition is::\n",a)
