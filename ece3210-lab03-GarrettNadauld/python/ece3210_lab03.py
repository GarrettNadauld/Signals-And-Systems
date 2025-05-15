import numpy as np
import matplotlib.pyplot as plt
import _ece3210_lab03
import time

def py_convolve(f, t_f, h, t_h):
    y = np.zeros(len(f) + len(h) - 1, dtype=float)

    dt_f = t_f[2] - t_f[1]

    #flip h
    h_flipped = h[::-1]

    #check lengths of arrays
    if len(f) != len(t_f):
        raise ValueError("Length of f does not match length of f_t")
    if len(h) != len(t_h):
        raise ValueError("Length of f does not match length of f_t")

    #add zeros to beginning and ending of functions
    zeroesf = np.zeros(len(f)-1, dtype=float)
    zeroesh = np.zeros(len(h)-1, dtype=float)

    f = np.concatenate((zeroesh, f))
    h_flipped = np.concatenate((h_flipped, zeroesf))

    #calculate the result
    for shift in range(len(h_flipped)):
        h_shift = np.roll(h_flipped, shift)
        result = dt_f * np.sum(np.multiply(f, h_shift))
        y[shift] = result

    #calculate t_y
    t_y = np.zeros(len(y))
    # t_y[0] = t_f[0] + t_h[0]
    t_y = np.linspace(t_f[0] + t_h[0], t_f[-1] + t_h[-1], len(y))

    return y, t_y

def c_convolve (f , t_f , h , t_h ) :
        if len(f) != len(t_f):
            raise ValueError("Inputs f and f_time do not have the same dimensionality")
        if len(h) != len(t_h):
            raise ValueError("Inputs f and f_time do not have the same dimensionality")
        
        y = np.zeros((len(f) + len(h) - 1))
        y_t = np.zeros(len(y))

        y, y_t = _ece3210_lab03.convolve(f, t_f, h, t_h)

        return y, y_t

def main():
    
    #testing functions
    #f = np.array([0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0])
    #tf = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3])
    #g = np.array([0, 0.5, 1, 1.5, 2])
    #tg = np.array([-1, -0.5, 0, 0.5, 1])
    #y, y_t = py_convolve(f, tf, g, tg) 
    #print(y)
    #print(y_t)
    #y, y_t = c_convolve(f, tf, g, tg)
    #print(y)
    #print(y_t)

    t = np.linspace(0, 15, 10000)
    f = np.exp(-t/2) * (np.heaviside(t-1, 1) - np.heaviside(t-10, 1)) 
    h = np.exp(-t) * (np.heaviside(t-2, 1) - np.heaviside(t-5, 1))
    py, pt_y = py_convolve(f, t, h, t)
    cy, ct_y = c_convolve(f, t, h, t)

    #analytical convolution
    y_t = (2*(np.exp((-t/2)-1)-np.exp(.5-t)))*(np.heaviside(t-3, 1)-np.heaviside(t-6, 1)) + 2*np.exp(-t/2)*(np.exp(-1)-np.exp(-2.5))*(np.heaviside(t-6, 1)-np.heaviside(t-12, 1)) + 2*(np.exp(5-t)-np.exp(-0.5*t-2.5))*(np.heaviside(t-12, 1)-np.heaviside(t-15, 1))
    
    #Timing
    T = [0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00005]
    py_time = np.zeros(len(T))
    c_time = np.zeros(len(T))
    for i in range(len(T)):    
        t_w = np.arange(1, 5, T[i])
        t_q = np.arange(-2, 3, T[i])
        w = np.random.uniform(-10, 10, size=len(t_w))
        q = np.random.uniform(-10, 10, size=len(t_q))
        py_start = time.time()
        py_convolve(w, t_w, q, t_q)
        py_end = time.time()
        py_time[i] = py_end-py_start
        c_start = time.time()
        c_convolve(w, t_w, q, t_q)
        c_end = time.time()
        c_time[i] = c_end-c_start

    plt.loglog(T, py_time, label='Python Timing')
    plt.loglog(T, c_time, label='C Timing')
    plt.legend()
    plt.title('Python and C Timing')
    plt.xlabel('T')
    plt.ylabel('Time (s)')
    plt.grid(True)
    plt.show()

    #graphing
    plt.plot(pt_y, py, label='Python Solution')
    plt.plot(t, y_t, label='Analytical Solution', linestyle='--')
    plt.plot(ct_y, cy, label='C Solution', linestyle='--')
    plt.legend()
    plt.title('h(t) vs. time')
    plt.xlabel('time (s)')
    plt.ylabel('h(t) (v)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
