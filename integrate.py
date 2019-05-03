# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:46:07 2019

@author: SATISH
"""

def integrate(f,a,b,n=1000):
    steps=(b-a)/n# robust it with more general and bad arguments
    I=0
    for i in range(n):
        I+=(f(a+i*steps)+f(a+(i+1)*steps))*steps/2
    return I

def approximate_pi(n):
    c=lambda x: (4-x**2)**0.5
    pi=integrate_mc(c,0,2,(0,2),n)
    return pi
    
def maxmin_value(f,a,b):
    L=[f(a+i*(b-a)/999) for i in range(1000)]
    return [min(L),max(L)]

def integrate_mc(f,a,b,L,N=1000):
    if N<=0:
        raise ValueError('incorrect no of steps mentioned in argument')
        exit
    if L[0]>L[1]:
        raise ValueError('Incorrect order of minimum and maximum value')
        exit
    if L[0]>maxmin_value(f,a,b)[0] or L[1]<maxmin_value(f,a,b)[1]:
        raise ValueError('Minimum and maximum values are not correct in domain')
        exit
    import random
    count=0
    for i in range(N):
        x=random.uniform(a,b)
        y=random.uniform(L[0],L[1])
        if f(x)*y>=0:
            if abs(y)<abs(f(x)):
                count+=1
    if L[0]*L[1]<=0:
        return (count*(b-a)*(L[1]-L[0])/N)
    else:
        if L[0]>0:
            return (count*(b-a)*(L[1]-L[0])/N)+((b-a)*L[0])
        else:
            return (count*(b-a)*(L[1]-L[0])/N)+((b-a)*L[1])
        
import matplotlib.pyplot as plt
f=lambda x: x**2+x+1
# integration from 0 to 10 
# hand written calculations gives 
n=list(range(1000))
a=393.3333333333
I=integrate(f,0,10,1000)
I1=[abs(I-a) for i in range(1000)]
I2=[]
for i in range(1000):
    I2.append(abs(integrate_mc(f,0,10,(1,111),i+1)-a))

fig1,ax=plt.subplots(figsize=(7,7))
plt.plot(n,I1,'r',linewidth=3,label='Reimann sum Method')
plt.plot(n,I2,'b',linewidth=3,label='Monte Carlo integration')
plt.axis([0, 1000, -10, 450])
plt.title('Convergence Plot (f(x)=x**2+x+1)')
plt.xlabel('No of Sample(0 to 1000)')
plt.ylabel('Absolute Error(from Hand Integration Value 393.33333')
plt.legend(fancybox=True,shadow=True)
plt.grid(True)
plt.show()

        

