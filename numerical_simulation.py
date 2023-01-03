import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from square_well_hamiltonian import matrix_elements
from square_well_utilities import energy
from constants import *
hamiltonian=None
def odes(t, a):
    return -1j*np.matmul(hamiltonian,a)
dim=9
hamiltonian = matrix_elements(dim)
tmax = 6
a_init = np.zeros(dim, dtype=complex)
a_init[0]=1

t=np.linspace(0,tmax,501)
sol=solve_ivp(odes,[0,tmax],a_init, t_eval=t)
print(sol['message'])
times = sol['t']
vals = sol['y']
plt.plot(times,np.abs(vals[0,:]))
plt.show()
assert True

