import numpy as np
from constants import *
# Energy levels
def energy(n):
    return n**2*np.pi**2*hbar**2/(2*m*L**2)
# Wave function
def psi(n,x):
    return np.sqrt(2/L)*np.sin((n+1)*np.pi*x/L)
# Drive
def dv(x):
    v0=.01*(energy(2)-energy(1))
    return -v0*(9*np.pi**2/(16*L))*(x/L-1/2)