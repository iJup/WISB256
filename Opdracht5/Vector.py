import math

class Vector():

    def __init__(self,n,k=0):
        self.n = n
        if type(k) == int or type(k) == float:
            self.pijl = [float(k) for i in range(n)]
        elif type(k) != int:
            self.pijl = [k[i] for i in range(n)]

    def __str__(self):
        self.string =  ""
        for i in range(self.n):
            self.string += "{0:.6f}".format(self.pijl[i]) + "\n"
        return self.string

    def lincomb(self, other, alpha, beta):
        lijst = [0] * self.n
        for i in range(self.n):
            lijst[i] = alpha * self.pijl[i] + beta * other.pijl[i]
        return Vector(self.n, lijst)

    def scalar(self, alpha):
        return self.lincomb(self, alpha, 0)
        
    def inner(self, other):
        inner = 0
        for i in range(self.n):
            inner += self.pijl[i] * other.pijl[i]
        return inner

    def norm(self):
        return math.sqrt( self.inner(self))

def GrammSchmidt(V):
    u = []
    e = [0] * len(V)
    u.append(V[0])
    
    for i in range(1,len(V)):
        z = V[i]
        for j in range(i):
            proj_V = u[j-1].scalar( V[i].inner(u[j-1]) / u[j-1].inner(u[j-1]) )
            z = z.lincomb(proj_V, 1, -1)
        u.append(z)
        
    for k in range(len(V)):
        e[k] = u[k].scalar(1/u[k].norm())
        
    return e
                
            
