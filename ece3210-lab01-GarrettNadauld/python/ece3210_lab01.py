import numpy as np
import scipy as sp
from scipy import integrate
import _ece3210_lab01
import matplotlib.pyplot as plt

def py_cumtrapz(f, f_time):
    if f.shape != f_time.shape:
        raise ValueError("Inputs f and f_time do not have the same dimension                        ality")
    #calc time intervals
    dt = f_time[1:] - f_time[:-1]

    #trap areas
    trap_area = 0.5 * (f[:-1] + f[1:]) * dt
    cum_area = np.cumsum(trap_area)

    #calc y_time
    y_time = f_time[:-1] + 0.5 * dt

    return cum_area, y_time

def c_cumtrapz(f, f_time):
    if f.shape != f_time.shape:
         raise ValueError("Inputs f and f_time do not have the same dimensionality")
    y = np.zeros_like(f)
    y_time = np.zeros_like(f_time)

    y, y_t = _ece3210_lab01.cumtrapz(f, f_time)

    return y, y_t

def main():
    #getting function and time values
    t = np.linspace(0, 4, 10000)
    f = t * np.exp(-2*t) * np.heaviside(t-1, 1)
    c_y, c_t = c_cumtrapz(f, t)
    p_y, p_t = py_cumtrapz(f, t)
    #plotting
    plt.plot(t, f, label='function')
    plt.plot(c_t, c_y, label='c_cumtrapz')
    plt.plot(p_t, p_y, label='py_cumtrapz')
    plt.plot(t, (0.25 * (-2 * t * np.exp(-2*t) - np.exp(-2*t) + 3 * np.exp(-2))) * np.heaviside(t-1, 1), label='analytical')
    plt.legend()
    plt.title('Lab 1')
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.show()

if __name__ == "__main__":
    main()
