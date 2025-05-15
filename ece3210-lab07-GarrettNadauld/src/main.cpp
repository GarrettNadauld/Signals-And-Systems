#include <cstdio>

#include <stdio.h>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <cmath>

extern "C" {
#include "transforms.h"
}

namespace py = pybind11;

py::array calc_dft(py::array_t<std::complex<double>> &x_np)
{

    array x;
    x.len = (size_t)x_np.request().size;
    x.data = (double *)x_np.request().ptr;


    py::array_t<std::complex<double>> F_r_np =
	py::array_t<std::complex<double>>((pybind11::ssize_t)(x.len));
    
    array F_r;
    F_r.len = (size_t)F_r_np.request().size;
    F_r.data = (double *)F_r_np.request().ptr;

    dft(&F_r, &x);
    
    return F_r_np;
}

//py::array calc_fft(py::array_t<std::complex<double>> &x_np)
//{
// 
/*     array x;
     x.len = (size_t)x_np.request().size;
     x.data = (double *)x_np.request().ptr;
    
     int ogsize = x.len;
     int size = pow(2, ceil(log2(ogsize)));

     array px;
     px.len = (size_t)size; 
     px.data = (double *)x_np.request().ptr;
//     for(int i=0; i<ogsize; i++) {
//        px->data[i] = x->data[i];
//     }


     py::array_t<std::complex<double>> F_r_np =
     py::array_t<std::complex<double>>((pybind11::ssize_t)(x.len));
 
     array F_r;
     F_r.len = (size_t)F_r_np.request().size;
     F_r.data = (double *)F_r_np.request().ptr;


     fft(&F_r, &px);
 
     return F_r_np;
}*/

py::array convolve(py::array_t<double> &f_np, py::array_t<double> &h_np) {
    array f;
    f.len = (size_t)f_np.request().size;
    f.data = (double *)f_np.request().ptr;

    array h;
    h.len = (size_t)h_np.request().size;
    h.data = (double *)h_np.request().ptr;

    py::array_t<double> y_np = py::array_t<double>((pybind11::ssize_t)(f.len + h.len - 1));

    array y;
    y.len = (size_t)y_np.request().size;
    y.data = (double *)y_np.request().ptr;

    cont_convolve(&y, &f, &h);

    return (y_np);
}

PYBIND11_MODULE(_ece3210_lab07, m)
{
    m.doc() = "a collection of functions for ECE 3210 lab 7";
    m.def("calc_dft", &calc_dft,
          "computes the cumulative integral of an arbitrary waveform");
//    m.def("calc_fft", &calc_fft,
//           "computes the cumulative integral of an arbitrary waveform");
    m.def("convolve", &convolve,
           "computes the convolution of two given functions");
}
