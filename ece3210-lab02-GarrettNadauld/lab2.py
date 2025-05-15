import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def f_t(R, C, L, t):
    b = 1/(R*C)
    c = 1/(L*C)
    coeff = [1, b, c]
    lam1, lam2 = np.roots(coeff)
    c2 = 1/(lam2-lam1)
    c1 = -c2
    y_t = (1e-4) * (1/(R*C)) * ((c1 * lam1 * np.exp(lam1 * t) + (lam2 * c2 * np.exp(lam2 * t)))) * np.heaviside(t, 1)


    return y_t


def csv(data):


    desired_start_time = 0 # 0 seconds
    desired_end_time = 0.0003 # 300 microseconds
    tolerance = 0.000001 # 1 microsecond tolerance


    # Filter the data for the desired time range with tolerance
    filtered_data = data[
                (data['second'] >= desired_start_time - tolerance) &
                (data['second'] <= desired_end_time + tolerance)
                ]


    # Extract the 'time' and 'value' columns into separate arrays
    time_array = filtered_data['second'].to_numpy()
    value_array = filtered_data['Volt'].to_numpy()
    
    value_array = value_array * 10
    
    return(time_array, value_array)


def main():
    R = 1000
    L = 1E-3
    C = 0.033e-6
    t = np.linspace(0, 300e-6, 10000)
    y_t = f_t(R, C, L, t)
    data = pd.read_csv('scope_0.csv', skiprows=1)
    lab_t, lab_y = csv(data)
    plt.plot(t, y_t, label='Analytical', linestyle='--')
    plt.plot(lab_t, lab_y, label='Lab Values', linestyle='--')
    plt.legend()
    plt.title('h(t) vs. time')
    plt.xlabel('time (s)')
    plt.ylabel('h(t) (v)')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()

