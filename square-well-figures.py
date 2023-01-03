import matplotlib.pyplot as plt
import numpy as np
from square_well_utilities import *
plt.rcParams['text.usetex'] = True

x=np.linspace(0,1,101)
fig,[ax0,ax2] = plt.subplots(2)
plt.title("Square Well Qubit")
plt.legend([r'|0\rangle',r'|1\rangle'])
ax0.set_title('Wave function')
ax0.plot(x,psi(1,x))
ax0.plot(x,psi(2,x))
ax0.set_ylabel(r'$\Psi$')
integrand, h12 = matrix_element(1,2,x)
ax2.plot(x,integrand)
h = np.array([[h12,0],[0,h12]])
T=np.pi/(2*h12)
ax2.set_title("Matrix Element")
ax2.annotate(r'$H_{12}=$'+f'{h12:.3f}',[0.2,0.1])
plt.tight_layout()
plt.savefig('square-well.jpg')
plt.show()
plt.close()

plt.ylim(0,100)
notes=[r'$|1\rangle$',r'$|2\rangle$',r'$|3\rangle$',r'$|4\rangle$',r'$|5\rangle$']
for n in range(1,5):
    x=[0,L]
    y=[energy(n),energy(n)]
    nn=str(n)
    plt.annotate(notes[n-1], [L/4,energy(n)+2])
    plt.plot(x,y)
plt.savefig('energy-levels.jpg')
plt.show()
assert True
