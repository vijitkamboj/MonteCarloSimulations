
from numpy import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

Toatal_pts= 10000 #random pts

circlex=[]
circley=[]

squarex=[]
squarey=[]

for i in range(Toatal_pts):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)

    if x**2+y**2 <= 1:
        circlex.append(x)
        circley.append(y)
    else:
        squarex.append(x)
        squarey.append(y)
pi=4*len(circlex)/float(Toatal_pts)
print(pi)


plt.plot(circlex,circley,"r.")
plt.plot(squarex,squarey,"g.")
plt.show()
