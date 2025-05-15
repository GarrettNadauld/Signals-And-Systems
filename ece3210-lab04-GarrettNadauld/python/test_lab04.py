import random
import unittest

import numpy as np

import ece3210_lab04
import ece3210_lab04_sol

class TestFourierSeries(unittest.TestCase):

    def test_py(self):

        T = random.uniform(0.1,1)
        start = random.uniform(-2,2)
        end = start + T
        t = np.linspace(start, end, 2000)
                
        m = random.randint(10,30)

        a_0 = random.uniform(-5,5)
        a_n = np.random.uniform(-10,10,size=(m))
        b_n = np.random.uniform(-10,10,size=(m))

        
        f_sol = ece3210_lab04_sol.py_fourier_series(a_0, a_n, b_n,
                                                    t, T)

        f_m = ece3210_lab04.py_fourier_series(a_0, a_n, b_n,
                                              t, T)

        np.testing.assert_array_almost_equal(f_sol,
                                             f_m)

    def test_value_error_py(self):
        T = random.uniform(0.1,1)
        start = random.uniform(-2,2)
        end = start + T
        t = np.linspace(start, end, 2000)
        
        m = 10
        n = 9
        
        a_0 = random.uniform(-5,5)
        a_n = np.random.uniform(-10,10,size=(m))
        b_n = np.random.uniform(-10,10,size=(n))
        
        with self.assertRaises(ValueError):
            ece3210_lab04.py_fourier_series(a_0, a_n, b_n,
                                            t, T)
            
    def test_c(self):

        T = random.uniform(0.1,1)
        start = random.uniform(-2,2)
        end = start + T
        t = np.linspace(start, end, 2000)
                
        m = random.randint(10,30)

        a_0 = random.uniform(-5,5)
        a_n = np.random.uniform(-10,10,size=(m))
        b_n = np.random.uniform(-10,10,size=(m))

        
        f_sol = ece3210_lab04_sol.py_fourier_series(a_0, a_n, b_n,
                                                    t, T)

        f_m = ece3210_lab04.c_fourier_series(a_0, a_n, b_n,
                                              t, T)

        np.testing.assert_array_almost_equal(f_sol,
                                             f_m)

    def test_value_error_c(self):
        T = random.uniform(0.1,1)
        start = random.uniform(-2,2)
        end = start + T
        t = np.linspace(start, end, 2000)
        
        m = 10
        n = 9
        
        a_0 = random.uniform(-5,5)
        a_n = np.random.uniform(-10,10,size=(m))
        b_n = np.random.uniform(-10,10,size=(n))
        
        with self.assertRaises(ValueError):
            ece3210_lab04.c_fourier_series(a_0, a_n, b_n,
                                           t, T)

    #     f_start = random.uniform(-5, 5)
    #     f_end = random.uniform(f_start+1, 10)
    #     t_f = np.arange(f_start, f_end, T)

    #     f = np.random.uniform(-100,100,size=len(t_f))

    #     h_start = random.uniform(-5, 5)
    #     h_end = random.uniform(h_start+1, 10)
    #     t_h = np.arange(h_start, h_end, T)

    #     h = np.random.uniform(-100,100,size=len(t_h))

    #     y_sol, t_sol = ece3210_lab03_sol.convolve(f, t_f,
    #                                        h, t_h)
    #     y_py, t_py_y = ece3210_lab03.py_convolve(f, t_f,
    #                                              h, t_h)

    #     np.testing.assert_array_almost_equal(y_py,
    #                                          y_sol)

    #     np.testing.assert_array_almost_equal(t_py_y,
    #                                          t_sol)

    # def test_c(self):

    #     T = random.uniform(0.001,0.010)

    #     f_start = random.uniform(-5, 5)
    #     f_end = random.uniform(f_start+1, 10)
    #     t_f = np.arange(f_start, f_end, T)

    #     f = np.random.uniform(-100,100,size=len(t_f))

    #     h_start = random.uniform(-5, 5)
    #     h_end = random.uniform(h_start+1, 10)
    #     t_h = np.arange(h_start, h_end, T)

    #     h = np.random.uniform(-100,100,size=len(t_h))

    #     y_sol, t_sol = ece3210_lab03_sol.convolve(f, t_f,
    #                                               h, t_h)
    #     y_c, t_c_y = ece3210_lab03.c_convolve(f, t_f,
    #                                           h, t_h)

    #     np.testing.assert_array_almost_equal(y_c,
    #                                          y_sol)

    #     np.testing.assert_array_almost_equal(t_c_y,
    #                                          t_sol)

    # def test_value_error_c(self):
    #     t_f = np.linspace(0, 10, 99)
    #     f = np.linspace(0, 10, 100)
    #     t_h = np.linspace(0, 10, 50)
    #     h = np.linspace(0, 10, 50)

    #     with self.assertRaises(ValueError):
    #         ece3210_lab03.c_convolve(f,t_f,h,t_h)

    #     t_f = np.linspace(0, 10, 100)
    #     f = np.linspace(0, 10, 100)
    #     t_h = np.linspace(0, 10, 49)
    #     h = np.linspace(0, 10, 50)

    #     with self.assertRaises(ValueError):
    #         ece3210_lab03.c_convolve(f,t_f,h,t_h)

            
if __name__ == '__main__':
    unittest.main()




