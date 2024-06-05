import numpy as np
from panel import Row
from tables import Col

#list
mlist = [1,2,3]
print(type(mlist))

#converting list to numpy array now
marr = np.array(mlist)
print(type(marr))
print(marr)
#np arrange - range of elements [0,10) - with a gap of 2 for each element
print(np.arange(0,10,2))

#np ones, zeros, eye, linspace
print(np.zeros((4,5)))

print(np.ones((3,4)))
# does not take tuple for array declaration
print(np.eye(4,5))

# we can easily perform arithmatic operations on numpy arrays
# arr = np.ones((2,3)) * 100

print(np.linspace(0,10,30))

#part - 2
print(np.random.rand( 1))
#prints 4 random floating numbers between 0,1
print(np.random.rand( 4))
#prints 4 arrays with a size of 2 - 4X2 array
a1 = np.random.rand( 4, 2)
print(a1)

print(type(a1))

#standard/normal distribution 
print(np.random.randn(1,2))
print(np.random.normal(2,2,(2,3)))
print('-'*80)
#print random integers
print(np.random.randint(1,50,3))
print(np.random.randint(1,50,(3,2)))
#prints 10 random int numbers between 100-200 inclusive
a2 = np.random.randint(100,200,10)
print(a2)
print(len(a2))
print(a2.max())
print(a2.argmax(), a2.argmin(), a2.argsort())
print(a2.shape)
#print(a2.reshape(2,5))

#numpy index selection
#slicing of array points to the original so keep in mind about that.
#use np.array.copy() - to get the real copy of that array.
print(a2)
arry_copy = a2.copy()
print(arry_copy * 100)