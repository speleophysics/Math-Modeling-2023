import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded

secs_per_day = 24.0 * 60.0 * 60.0


# Simulation of river sewage pulse
def adv_disp_sewage(
    V=1.0,
    D=100.0,
    L=200.0 * 1000.0,
    duration_days=7.0,
    ntimes=2000,
    endtime=4.0,
    nx=500,
    xmax=1.0,
):
    duration_sec = duration_days * secs_per_day  # 7 days
    duration = duration_sec * V / L
    dt = endtime / (ntimes - 1)
    Pe = V * L / D
    dx = xmax / (nx - 1.0)
    print("Peclet Number=", Pe)
    print("Flowthrough time (days)=", L / V / secs_per_day)
    times = np.linspace(0, endtime, ntimes)
    x = np.linspace(0, xmax, nx)
    A_upper = dt * (1.0 / (4.0 * dx) - 1.0 / (2.0 * Pe * dx**2.0)) * np.ones(nx - 1)
    A_lower = dt * (-1.0 / (4.0 * dx) - 1.0 / (2.0 * Pe * dx**2.0)) * np.ones(nx - 1)
    A_mid = (1.0 + dt / (Pe * dx**2.0)) * np.ones(nx - 1)
    A_upper[0] = 0.0
    A_lower[-1] = 0.0
    A_lower[-2] = -dt / (2.0 * dx)
    A_mid[-1] = 1.0 + dt / (2 * dx)
    C = np.zeros([ntimes, nx])
    C[0, :] = 0.0
    C_upstream = 1.0
    C_downstream = 0.0
    A = np.vstack((A_upper, A_mid, A_lower))
    C[:, 0] = C_upstream
    C[times > duration, 0] = 0.0
    C[:, -1] = C_downstream
    b = np.zeros(nx - 1)
    for n in np.arange(ntimes - 1):
        b[0:-1] = (
            C[n, 1:-1] * (1.0 - dt / (Pe * dx**2.0))
            + C[n, 0:-2] * (dt / (4.0 * dx) + dt / (2.0 * Pe * dx**2.0))
            + C[n, 2:] * (-dt / (4.0 * dx) + dt / (2.0 * Pe * dx**2.0))
        )
        b[0] += dt * (1.0 / (4.0 * dx) + 1.0 / (2.0 * Pe * dx**2.0)) * C[n, 0]
        b[-1] = (1.0 - dt / (2.0 * dx)) * C[n, -1] + (dt / (2 * dx)) * C[n, -2]
        C[n + 1, 1:] = solve_banded((1, 1), A, b)
    return x, times, C


def plot_concentrations_at_timesteps(x, C, timesteps=None):
    if timesteps is None:
        ntimes = C.shape[0]  # Timesteps are first dimension of array
        timesteps = np.array(
            [
                1,
                int(np.round(ntimes / 4)),
                int(np.round(ntimes / 2)),
                int(np.round(3 * ntimes / 4)),
                ntimes - 1,
            ]
        )
    time_labels = []
    for time in timesteps:
        plt.plot(x, C[time, :])
        time_labels.append(str(time))
    plt.xlabel("Distance Downstream (dimensionless)")
    plt.ylabel("Concentration (dimensionless)")
    plt.legend(time_labels)


def plot_concentration_over_time(t, C, location_idx=-1):
    plt.plot(t, C[:, location_idx])
    plt.xlabel("Time (dimensionless)")
    plt.ylabel("Concentration (dimensionless)")
