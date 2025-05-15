//
// Created by Garrett Nadauld on 9/21/23.
//
#ifndef CONVOLVE_H
#define CONVOLVE_H
#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>


typedef struct array {
    size_t len ;
    double *data ;
} array;

void cont_convolve(array *y, array * y_time, const array *f, const array *f_time, const array *h, const array *h_time);

#endif
