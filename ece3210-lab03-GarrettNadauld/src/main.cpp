//
// Created by Garrett Nadauld on 9/21/23.
//
#include <cstdio>

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>

extern "C" {
#include "convolve.h"
}

namespace py = pybind11;

std::tuple<py::array_t<double>, py::array_t<double>> convolve(py::array_t<double> &f_np, py::array_t<double> &f_time_np, py::array_t<double> &h_np, py::array_t<double> &h_time_np){

    array f_time;
    f_time.len = (size_t)f_time_np.request().size;
    f_time.data = (double *)f_time_np.request().ptr;

    array f;
    f.len = (size_t)f_np.request().size;
    f.data = (double *)f_np.request().ptr;

    array h_time;
    h_time.len = (size_t)h_time_np.request().size;
    h_time.data = (double *)h_time_np.request().ptr;

    array h;
    h.len = (size_t)h_np.request().size;
    h.data = (double *)h_np.request().ptr;

    py::array_t<double> y_np = py::array_t<double>((pybind11::ssize_t)(f.len + h.len - 1));

    array y;
    y.len = (size_t)y_np.request().size;
    y.data = (double *)y_np.request().ptr;

    py::array_t<double> y_time_np = py::array_t<double>((pybind11::ssize_t)(f_time.len + h_time.len - 1));

    array y_time;
    y_time.len = (size_t)y_time_np.request().size;
    y_time.data = (double *)y_time_np.request().ptr;

    cont_convolve(&y, &y_time, &f, &f_time, &h, &h_time);

    return std::make_tuple(y_np, y_time_np);
}


PYBIND11_MODULE(_ece3210_lab03, m)
{
m.doc() = "a collection of functions for ECE 3210 lab 3";
m.def("convolve", &convolve,
"computes the convolution of two given functions");
}
