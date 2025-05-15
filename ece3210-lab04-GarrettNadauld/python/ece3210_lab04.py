import matplotlib.pyplot as plt
import numpy as np
import _ece3210_lab04
import time
import pandas as pd
from tabulate import tabulate

def py_fourier_series(a_0, a_n, b_n, t, T):

    #check length of a_n and b_n
    if len(a_n) != len(b_n):
        raise ValueError("Length of a_n does not match the length of b_n")

    f_m = np.full(len(t), a_0)
    w_0 = (2 * np.pi) / T

    for n in range(1, len(a_n)+1):
        f_m +=  a_n[n-1] * np.cos(n*w_0*t) + b_n[n-1] * np.sin(n*w_0*t)

    return f_m

def c_fourier_series(a_0, a_n, b_n, t, T):

    #check array length
    if len(a_n) != len(b_n):
        raise ValueError("Length of a_n does not match the length of b_n")

    f_m = np.zeros(len(t), dtype=float)
    
    f_m = _ece3210_lab04.fourier_series(a_0, a_n, b_n, t, T)

    return f_m

def main():
    
    #initializing variables
    m = [2, 4, 7, 11, 25, 50, 100, 175, 250]
    t = np.linspace(-2, 2, 5000)
    f_ec = np.zeros_like(t)
    e_t = np.zeros((len(m), len(t)))
    p_ec = np.zeros(len(m))
    c_time = np.zeros(len(m))
    py_time = np.zeros(len(m))
    f_t = 2 * (t + 2) * (np.heaviside(t + 2, 1) - np.heaviside(t + 1.5, 1)) \
          + ((-2) * (t + 1)) * (np.heaviside(t + 1.5, 1) - np.heaviside(t + 0.5, 1)) \
          + 2 * t * (np.heaviside(t + 0.5, 1) - np.heaviside(t - 0.5, 1)) \
          + ((-2) * (t - 1)) * (np.heaviside(t - 0.5, 1) - np.heaviside(t - 1.5, 1)) \
          + 2 * (t - 2) * (np.heaviside(t - 1.5, 1) - np.heaviside(t - 2, 1))
    a_0 = 0.0
    T = 2.0

    plt.plot(t, f_t, label='f(t)')
    
    #calculate b_n and graph the fourier series
    for n in range(len(m)):
        a_n = np.zeros(m[n])
        b_n = np.zeros(m[n])
        for i in range(1, m[n]):
            b_n[i-1] = ((np.cos(1.5 * np.pi * i) - np.cos(0.5 * np.pi * i)) / (np.pi * i)) + ((6 * np.sin(0.5 * i * np.pi) - 2 * np.sin(1.5 * np.pi * i)) / ((i**2)*(np.pi**2)))
        
        #python function and graphing
        #f_mp = py_fourier_series(a_0, a_n, b_n, t, T)
        #plt.plot(t, f_mp, label='Py_Fourier')
        

        #c function and graphing
        f_mc = c_fourier_series(a_0, a_n, b_n, t, T)
        e_t[n] = f_mc - f_t
        p_ec[n] = (0.5) * np.sum((e_t[n]**2)*(t[1]-t[0]))
        print(p_ec[n])
        plt.plot(t, f_mc, label='C_Fourier, m=%d'%m[n])


        #Timing
        py_start = time.time()
        py_fourier_series(a_0, a_n, b_n, t, T)
        py_end = time.time()
        py_time[n] = py_end-py_start
        c_start = time.time()
        c_fourier_series(a_0, a_n, b_n, t, T)
        c_end = time.time()
        c_time[n] = c_end-c_start

    #plot harmonics
    plt.grid()
    plt.legend()
    plt.title('Fourier Series for Various Harmonics')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.show()

    #plt error
    for n in range(len(m)):
        plt.plot(t, e_t[n], label='Error, m=%d'%m[n])
    plt.grid(True)
    plt.legend()
    plt.title('Error Values by Harmonics')
    plt.xlabel('m')
    plt.ylabel('e(t)')
    plt.show()

    #print error power
    print(m)
    print(p_ec)

    #timing graph
    plt.loglog(m, py_time, label='Python Timing')
    plt.loglog(m, c_time, label='C Timing')
    plt.legend()
    plt.title('Python and C Timing')
    plt.xlabel('m')
    plt.ylabel('time (s)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
