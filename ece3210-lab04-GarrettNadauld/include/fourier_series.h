#ifndef FOURIER_SERIES_H
#define FOURIER_SERIES_H
#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define PI 3.14159265358979323846
typedef struct {
    size_t len ;
    double *data ;
} array;

void fourier_t(array *f_m, const double a_0, const array *a_n, const array *b_n, const array *t, const double T);

#endif
