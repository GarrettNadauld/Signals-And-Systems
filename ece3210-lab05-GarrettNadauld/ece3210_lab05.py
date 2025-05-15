import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#create the transfer function
def y(R, C, L, w_0, m, t):
    b = 1/(R*C)
    c = 1/(L*C)
    j = (-1)**(1/2)
    y_t = np.zeros(len(t), dtype=complex)
    for n in range(-m, (m+1)):
        y_t += ((b*j*w_0)/(((j*n*w_0)**2)+(b*j*n*w_0)+c))*(8*np.sin(n*np.pi/2)/(np.pi))*np.exp(j*n*w_0*t)

    return y_t

#create f(t)
def f(w_0, m, t):
    j = (-1)**(1/2)
    f_t = np.zeros(len(t), dtype=complex)
    for n in range(-m, (m+1)):
        if n != 0:
            f_t += ((8*np.sin(n*np.pi*0.5))/(n*np.pi)) * np.exp(j*n*w_0*t)
    
    return f_t

#read csv file
def csv(data, T):
    #sort data to desired times
    start_time = -T+2.2E-5
    end_time = T+2.2E-5
    tol = 0.000001
    filtered_data = data[
        (data['second'] >= start_time - tol) &
        (data['second'] <= end_time + tol)
    ]

    time = filtered_data['second'].to_numpy()
    value = filtered_data['Volt'].to_numpy()

    return(time, value)

def main():
    #constants
    R = 1000
    C = .033E-6
    L = 1E-3
    T = 1/1.6E4
    t = np.arange(-T, T, 0.0000005)
    m = 35
    w_0 = 4E4 * np.pi
    
    #y_t
    y_t = y(R, C, L, w_0, m, t)
    
    #f_t
    f_t = f(w_0, m, t)

    #lab data
    data = pd.read_csv('scope_0.csv', skiprows=1)
    lab_t, lab_y = csv(data, T)
    lab_t = lab_t -2.2E-5
    #plotting
    plt.plot(lab_t, lab_y, label='Lab Values')
    plt.plot(t, f_t, label='f(t)')
    plt.plot(t, y_t, label='Analytical Response')
    plt.grid(True)
    plt.title('System Response to a Periodic Signal')
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
