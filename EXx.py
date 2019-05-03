# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:56:02 2019

@author: SATISH
"""
class function:
    def __init__(self,*coeff):
        self.order=len(coeff)-1
        self.coeff=coeff
        
    def __repr__(self):
        return ''.join(['{:+g}x^{:d}'.format(a,n) for n, a in enumerate(self.coeff)][::-1])
    
    def __str__(self):
        return ''.join(['{:+g}x^{:d}'.format(a,n) for n, a in enumerate(self.coeff)][::-1])
        
    def value(self,a):
        v=0
        for i in range(len(self.coeff)):
            v+=(a**i)*self.coeff[i]
        return v
    
    def is_value_in(self,a,b):
        f_a=self.value(a)
        if b*f_a<0:
            return False
        else:
            if abs(f_a)>abs(b):
                return True
            
    def maxmin_value(self,a,b):
        L=[self.value(a+i*(b-a)/999) for i in range(1000)]
        return [max(L),min(L)]

class Circle_function():
    def __init__(self,r,c):
        self.radius=r
        self.center=c
        self.center_x=c[0]
        self.center_y=c[1]
    def __repr__(self):
        return '(x-%g)^2+(y-%g)^2 = %g'%(self.center_x,self.center_y,self.radius**2)
    
    def __str__(self):
        return '(x-%g)^2+(y-%g)^2 = %g'%(self.center_x,self.center_y,self.radius**2)
        
    def value(self,a):
        if a>(self.center-self.radius) and a<(self.center+self.radius):
            y1=self.center_y+(self.radius**2-(a-self.center_x)**2)**0.5
            y2=self.center_y-(self.radius**2-(a-self.center_x)**2)**0.5
            return y1,y2
        else:
            raise ValueError('Out of Domain')
            exit
            
    def is_value_in(self,a,b):
        if ((a-self.center_x)**2+(b-self.center_y)**2)>self.radius**2:
            return False
        else:
            return True
    
    def maxmin_value(self,a,b):
        L=[self.value(a+i*(b-a)/999) for i in range(1000)]
        return [max(L),min(L)]
    
def integrate(f,a,b,n=1000):
    steps=(b-a)/n# robust it with more general and bad arguments
    I=0
    for i in range(n):
        I+=(f.value(a+i*steps)+f.value(a+(i+1)*steps))*steps/2
    return I

def approximate_pi(n):
    c=Circle_function(1,(0,0))
    p=[]
    for i in range(100):
        p.append(integrate_mc(c,-1,1,(-1,1),n))
    pi=sum(p)/100
    return pi
    
def integrate_mc(f,a,b,L,N=100):
    if L[0]>L[1]:
        raise ValueError('Incorrect order of minimum and maximum value')
        exit
#    if L[0]>f.maxmin_value(a,b)[1] or L[1]<f.maxmin_value(a,b)[0]:
#        raise ValueError('Minimum and maximum values are not correct in domain')
#        exit
    import random
    count=0
    for i in range(N):
        if f.is_value_in(random.uniform(a,b),random.uniform(L[0],L[1])):
            count+=1
    if L[0]*L[1]<0:
        return (count*(b-a)*(L[1]-L[0])/N)
    else:
        if L[0]>0:
            return (count*(b-a)*(L[1]-L[0])/N)+((b-a)*L[0])
        else:
            return (count*(b-a)*(L[1]-L[0])/N)+((b-a)*L[1])

if __main__ == '__name__':
