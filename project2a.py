import array
import numpy as np
import matplotlib as plt
# project 2(a)

n5 = np.array([1,2,3,4,5])
n10 = np.linspace(1,10,10)
n20 = np.linspace(1,20,20)


print(n5)
print(n10)
print(n20)

n10 = []


for x in range(1,11,1):
	t = (2/3)^(x+2)
	n10.append(t) 
	print(x)


plt.plot(x,y)

# sumof5 = (2/3)^(n5+2)

# print(sumof5)

"""
n10 = list(range(1,11,1))
n20 = list(range(1,21,1))

print(n10)
print(n20)
print(n5)
"""

#s5 =  (2/3).^(n5+2)

#print(s5)


