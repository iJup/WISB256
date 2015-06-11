from scipy import integrate
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import arange, array, linalg
import cmath

class Lorenz:

    def __init__(self, x, sigma=10, rho=28, beta=8/3):
        self.sigma = float(sigma)
        self.rho = float(rho)
        self.beta = float(beta)

        self.x = x

    def func(self, x, t):
        
        x_punt = self.sigma * (x[1] - x[0])
        y_punt = x[0] * (self.rho - x[2]) - x[1]
        z_punt = x[0] * x[1] - self.beta * x[2]
        
        return [x_punt, y_punt, z_punt]

    def solve(self, T, dt):
        N = (T / dt)

        t = arange(0, T, dt)
        o = odeint(self.func, self.x, t)

        return o               

    def df(self, x):
        u = [[0,0,0], [0,0,0], [0,0,0]]
        u[0][0] = -self.sigma
        u[0][1] = self.sigma
        u[0][2] = 0
        u[1][0] = self.rho - x[2]
        u[1][1] = -1
        u[1][2] = -x[0]
        u[2][0] = x[1]
        u[2][1] = x[0]
        u[2][2] = -self.beta

        a = np.matrix(u)
        
        return a

    def isStable(self, punt):
        matrix = self.df(punt)
        w = linalg.eigvals(matrix) #array van 3 eigenwaarden
        print(w)


        if( w[0].real < 0 and w[1].real < 0 and w[2].real < 0):
            print ('True')
            return True
        else:
            print('False')
            return False
        
        
