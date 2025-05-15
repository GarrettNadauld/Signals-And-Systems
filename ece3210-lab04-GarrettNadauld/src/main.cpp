#include <cstdio>

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>

extern "C" {
#include "fourier_series.h"
}

namespace py = pybind11;

py::array fourier_series(double a_0, py::array_t<double> &a_n_np, py::array_t<double> &b_n_np, py::array_t<double> &t_np, double T){


    array a_n;
    a_n.len = (size_t)a_n_np.request().size;
    a_n.data = (double *)a_n_np.request().ptr;

    array b_n;
    b_n.len = (size_t)b_n_np.request().size;
    b_n.data = (double *)b_n_np.request().ptr;

    array t;
    t.len = (size_t)t_np.request().size;
    t.data = (double *)t_np.request().ptr;

    py::array_t<double> f_m_np = py::array_t<double>((pybind11::ssize_t)(t.len));

    array f_m;
    f_m.len = (size_t)f_m_np.request().size;
    f_m.data = (double *)f_m_np.request().ptr;

    fourier_t(&f_m, a_0, &a_n, &b_n, &t, T);

    return f_m_np;
}


PYBIND11_MODULE(_ece3210_lab04, m)
{
m.doc() = "a collection of functions for ECE 3210 lab 4";
m.def("fourier_series", &fourier_series,
"computes the fourier series of given a0, an, bn and T");
}
