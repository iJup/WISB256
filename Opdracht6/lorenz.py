from scipy import integrate
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange

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
