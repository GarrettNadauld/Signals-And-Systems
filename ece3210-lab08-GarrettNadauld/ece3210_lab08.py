import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def hs(t, R, C1, C2):
    H_s = (1/(R*C1*C2)) / (t**2 + 2/(R*C1)*t + 1/((R**2)*C1*C2))
    return H_s

# def csv(data):
#     f = data['Frequency (Hz)'].to_numpy()


def main():
    #Analytical Variables
    R = 10E3
    C1 = 3.183E-9
    C2 = 0.79577E-9
    t = np.linspace(50, 50000, 100000)
    s = 2* np.pi * t * (-1)**.5
    H_s = hs(s, R, C1, C2)
    mag = np.abs(H_s)
    mag = 20 * np.log10(mag) - 80
    phase = np.angle(H_s) * 180/np.pi

    #CSV Data
    data = pd.read_csv('scope_6.csv', encoding='ISO-8859-1')
    # print(data.head())
    f = data[' Frequency (Hz)'].to_numpy()
    a = data[' Amplitude (Vpp)'].to_numpy()
    g = data[' Gain (dB)'].to_numpy()
    p = data[' Phase (°)'].to_numpy()

    data = pd.read_csv('Sheet1MULTISIM.xlsx - Sheet1.csv')
    mf = data['X--Trace 1::[V(4) | V(PR1)]'].to_numpy()
    my = data['Y--Trace 1::[V(4) | V(PR1)]'].to_numpy()
    data = pd.read_csv('Sheet1.csv')
    mangle = data['Y--Trace 1::[V(4) | V(PR1)]']
    mang = data['X--Trace 1::[V(4) | V(PR1)]']
    mmag = np.abs(my)
    mmag = 20 * np.log10(mmag)
    mphase = np.tan(my/mf) * 180/np.pi

    #plotting
    plt.plot(t, mag, label='Analytical', color='red', alpha=0.7)
    plt.plot(f, g, label='Oscilloscope', color='green', alpha=0.7)
    plt.plot(mf, mmag, label='MultiSim', color='blue', alpha=0.7, linestyle='--')
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.title("Magnitude vs Frequency")
    plt.legend()
    plt.show()
    plt.plot(t, phase, label='Analytical', color='red', alpha=0.7)
    plt.plot(f, p, label='Oscilloscope', color='green', alpha=0.7)
    plt.plot(mang, mangle, label='MultiSim', color='blue', alpha=0.7, linestyle='--')
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (°)")
    plt.title("Phase vs Frequency")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()