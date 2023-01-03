import numpy as np
from square_well_utilities import psi, dv
def matrix_element(i,j,x):
    integrand = psi(i,x)*dv(x)*psi(j,x)
    return integrand, np.trapz(integrand,x)
def matrix_elements(dim):
    x=np.linspace(0,1,1001)
    matrix = np.empty((dim,dim), dtype=complex)
    for i in range(dim):
        for j in range(i,dim):
            _, matrix[i,j] = matrix_element(i,j,x)
            matrix[j,i]=matrix[i,j]
    return matrix
def pickle_all_matrix_elements(dim):
    name = f'hamiltonian{dim}'
    np.save(name, matrix_elements(dim))
