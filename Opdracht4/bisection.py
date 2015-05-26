from math import floor
import math

def findRoot(f,a,b,epsilon):
    a, b = [min(a,b),max(a,b)]
    m = (a + b)/2
     
    if b - a <= epsilon:
        return(m)
    
    elif (f(a)*f(m)) < 0: 
        return findRoot(f,a,m,epsilon)
            
    elif (f(m)*f(b)) < 0:
        return findRoot(f,m,b,epsilon)
        
    elif f(m) == 0:
        return m
            

def findAllRoots(f,a,b,epsilon):
    ls = []
    n = (b-a) / epsilon
    for i in range(floor(n)):
        x, y = [a+(i-1) * epsilon, a + (i+epsilon) *epsilon]
        if (f(x)*f(y) < 0):
            root = findRoot(f,x,y,epsilon)
            if root != None:
                ls.append(root)
    return ls
