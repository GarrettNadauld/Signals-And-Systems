import random
import time 
import unittest

import numpy as np
from scipy import signal

import ece3210_lab07

class TestFFT(unittest.TestCase):
     def test_dft(self):
          print("\nTesting DFT fidelity")
          N = random.randint(500,1000)
          x_re = np.random.uniform(-1000,1000,size=N)
          x_im = np.random.uniform(-1000,1000,size=N)
          
          x = x_re + 1j*x_im
          
          X_my = ece3210_lab07.dft(x)
          X_sol = np.fft.fft(x)

          np.testing.assert_array_almost_equal(X_my, X_sol)
                   

     def test_fft(self):
          print("\nTesting FFT fidelity")
          N = random.randint(500,1000)
          x = np.random.uniform(-1000,1000,size=N)
          
          X_my = ece3210_lab07.fft(x)
          N_adjust = int(2**np.ceil(np.log2(N)))
          X_sol = np.fft.fft(x,N_adjust)
          
          np.testing.assert_array_almost_equal(X_my, X_sol)
          
     def test_ifft(self):
          print("\nTesting IFFT fidelity")
          N = random.randint(500,1000)
          
          X_re = np.random.uniform(-1000,1000,size=N)
          X_im = np.random.uniform(-1000,1000,size=N)

          X = X_re + 1j*X_im

          x_my = ece3210_lab07.ifft(X)
          N_adjust = int(2**np.ceil(np.log2(N)))
          x_sol = np.fft.ifft(X,N_adjust)

          np.testing.assert_array_almost_equal(x_my, x_sol)

     def test_fft_speed(self):
          print("\nTesting FFT speed")
          N = 2**22
          k = np.arange(N)
          x = np.cos(np.pi*0.1*k)
          
          start = time.time()
          ece3210_lab07.fft(x)
          end = time.time()

          runtime = end - start

          print("time: %f" % runtime)

          self.assertLess(runtime, 5,
                          "code is too slow at %f seconds" % runtime)

     def test_convolve(self):
          print("\nTesting linear convolution")
          n_f = random.randint(500,1000)
          n_h = random.randint(500,1000)
          
          f = np.random.uniform(-1000,1000,size=n_f)
          h = np.random.uniform(-1000,1000,size=n_h)
          
          y_my = ece3210_lab07.convolve(f,h)
          y_sol = np.convolve(f,h)

          np.testing.assert_array_almost_equal(y_my, y_sol)
          
     def test_fft_convolve(self):
          print("\nTesting FFT convolution")
          N_f = random.randint(500,1000)
          N_h = random.randint(500,1000)

          f_re = np.random.uniform(-1000,1000,size=N_f)
          f_im = np.random.uniform(-1000,1000,size=N_f)
          
          f = f_re + 1j*f_im

          h_re = np.random.uniform(-1000,1000,size=N_h)
          h_im = np.random.uniform(-1000,1000,size=N_h)

          h = h_re + 1j*h_im
          
          y_my = ece3210_lab07.fft_convolve(f,h)
          y_sol = np.convolve(f, h)
          
          np.testing.assert_array_almost_equal(y_my, y_sol)

       
         
if __name__ == "__main__":
     unittest.main()
