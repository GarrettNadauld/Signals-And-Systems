import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def cheby(rp, rs, wp, ws):
    n, wn = signal.cheb1ord(wp, ws, rp, rs, analog=True)
    b, a = signal.cheby1(n, rp, wn, btype='low', analog=True)
    split = signal.cheby1(n, rp, wn, btype='low', analog=True, output='sos')

    print(b)
    print(a)
    print(split)

    poles = np.roots(a)

    plt.scatter(poles.real, poles.imag, marker='x', color='r', label='Poles')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axhline(0, color='black', linewidth=2)
    plt.axvline(0, color='black', linewidth=2)
    plt.xlim([-10E4, 10E4])
    plt.ylim([-10E4, 10E4])
    plt.title('Poles')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.legend()
    plt.grid('True')
    plt.show()

    w, h = signal.freqs(b, a)
    return w, h, split

def circuit(split):
    Rs = 1000
    split[0,2] = split[0,2]/split[1,5]
    split[1,2] = split[1,5]
    # print(split[1,4])
    C1 = 2/(split[1,4] * Rs)
    C2 = 1/((Rs**2)*C1*split[1,5])

    # print(C1)
    # print(C2)

    R = 1000
    C3 = 1/(R*split[0,2])
    # print(C3)

def main():
    #getting Cheb values
    rip = 1.5
    rs = 24
    wp = 10E3
    ws = 20E3
    wp = 2*np.pi*wp
    ws = 2*np.pi*ws

    w, h, split = cheby(rip, rs, wp, ws)
    hz = w/(2*np.pi)

    circuit(split)

    #CSV Data
    #Oscilloscope data
    data = pd.read_csv('scope_3.csv', encoding='ISO-8859-1')
    f = data[' Frequency (Hz)'].to_numpy()
    g = data[' Gain (dB)'].to_numpy()
    p = data[' Phase (°)'].to_numpy()

    #Multisim Magnitude
    data = pd.read_csv('Magnitude.xlsx - Sheet1.csv')
    mf = data['X--Trace 1::[V(9) | V(PR1)]'].to_numpy()
    my = data['Y--Trace 1::[V(9) | V(PR1)]'].to_numpy()

    #Multisim Angle
    data = pd.read_csv('Phase.xlsx - Sheet1.csv')
    mangle = data['Y--Trace 1::[V(9) | V(PR1)]']
    mang = data['X--Trace 1::[V(9) | V(PR1)]']
    mangle = mangle * (np.pi/180)
    phase = np.mod(mangle + np.pi, 2 * np.pi) - np.pi
    phase = phase * (180/np.pi)

    plt.plot(hz, 20*np.log10(np.abs(h)), label='Analytical', color='red')
    plt.plot(mf, 20*np.log10(np.abs(my)), label='Multisim', linestyle='--', color='green')
    plt.plot(f, g, label='Implementation', linestyle='--', color='blue')
    plt.xscale('log')
    plt.grid('True')
    plt.title('Magnitude vs Frequency')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.legend()
    plt.show()

    plt.plot(hz, np.angle(h, deg=True), label='Analytical', color='red')
    plt.plot(mang, phase, label='Multisim', linestyle='--', color='green')
    plt.plot(f, p, label='Implementation', linestyle='--', color='blue')
    plt.xscale('log')
    plt.grid('True')
    plt.title('Phase vs Frequency')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (°)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()