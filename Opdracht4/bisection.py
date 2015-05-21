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
            
