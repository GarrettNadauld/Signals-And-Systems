#ifndef TRANSFORMS_H
#define TRANSFORMS_H
#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <complex.h>
#include <stdint.h>

typedef struct{
    size_t len;
    double *data;
} array;

void dft(array *F_r, const array *x);

//uint32_t revbit(uint32_t num, int log2n);

//void bitReverse(_Complex double *b, int log2n);

//void fft(array *F_r, const array *x);

//int bitReverse(int num, int numBits);

//void fft(array *F_r, array *x, int n);

void cont_convolve(array *y, const array *f, const array *h);

#endif
