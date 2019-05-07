#%matplotlib inline
from numpy import random
import numpy as nump
import matplotlib.pyplot as plt

a=0
b=nump.pi
N=10000000

xrand=random.uniform(a,b,N)

def fun(x):
    return(nump.sin(x))
sum=0.0

for i in xrand:
    sum+=fun(i)

answer= (b-a)*sum/float(N)
print(answer)