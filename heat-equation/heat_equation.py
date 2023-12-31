# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.linalg import solve_banded

m_per_km = 1000
mm_per_m = 1000
kappa = 1.0 / mm_per_m / mm_per_m  # thermal diffusivity 1 mm^2/s converted to m^2/s
secs_per_year = 60 * 60 * 24 * 365


def solve_T(
    nx=100,
    nt=100, 
    L=100 * m_per_km, 
    T_hot=1600, 
    T_ocean=0, 
    insulated_lower_bnd=False,
    implicit = False,
    Fo = 0.5,
):
    # Define domain and create Temperature array, and set timesteps
    dx = L / nx  # nx/L
    dt = Fo * dx**2 / kappa
    x = np.arange(nx) * dx / m_per_km
    t = np.arange(nt) * dt / secs_per_year
    T = np.zeros([nt, nx])

    # Set initial condition
    T[0, :] = T_hot
    # Set boundary conditions
    T[:, 0] = T_ocean
    if not insulated_lower_bnd:
        T[:, -1] = T_hot


    if not implicit:        
        # Solve for temperature in loop
        for n in np.arange(nt - 1):
            T[n + 1, 1:-1] = Fo * T[n, 2:] + (1 - 2 * Fo) * T[n, 1:-1] + Fo * T[n, 0:-2]
            if insulated_lower_bnd:
                T[n + 1, -1] = (1 - 2 * Fo) * T[n, -1] + 2 * Fo * T[n, -2]
    else:
        # Create A matrix
        A_upper = -Fo*np.ones(nx-2)
        A_upper[0] = 0
        A_mid = (1+2*Fo)*np.ones(nx-2)
        A_lower = -Fo*np.ones(nx-2)
        A_lower[-1] = 0
        A = np.vstack((A_upper, A_mid, A_lower))
        for n in np.arange(nt-1):
            b = T[n,1:-1]
            b[0] += Fo*T[n+1,0]
            b[-1] += Fo*T[n+1,-1]
            T[n+1, 1:-1] = solve_banded((1,1), A, b)

    # Calculate analytical solution
    def T_ana(n):
        j = np.arange(nx)
        return T_ocean + (T_hot - T_ocean) * erf(0.5 * np.sqrt(j**2 / (Fo * n)))

    sol = {"T": T, "T_ana": T_ana, "x": x, "t": t}

    return sol
