import numpy as np
import math
import _ece3210_lab07

def dft(x):
    
    F_r = _ece3210_lab07.calc_dft(x)
    
    return F_r

#def fft(x):
#    F_r = _ece3210_lab07.calc_fft(x)
    
#    return F_r

def convolve(f,g):
    y = _ece3210_lab07.convolve(f,g)
    return y

def main():
    x = np.arange(1, 17)
    nd = np.fft.fft(x)
    cd = dft(x)
#    cf = fft(x)
    print(nd)
    print("np.fft")
    print(cd)
    print("python implementation")
    print(cf)
    print("c fft")

if __name__ == "__main__":
    main()
