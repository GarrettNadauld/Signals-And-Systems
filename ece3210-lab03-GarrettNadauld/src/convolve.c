//
// Created by Garrett Nadauld on 9/21/23.
//
#include "convolve.h"

void cont_convolve(array *y, array *y_time, const array *f, const array *f_time, const array *h, const array *h_time){
    double dt = f_time->data[1] - f_time->data[0];
    
    for (size_t i = 0; i < f->len + h->len - 1; i++) {
        y->data[i] = 0.0;
        for (size_t j = 0; j < f->len; j++) {
            size_t k = i - j;
            if (i >= j && (i-j) < h->len) {
                y->data[i] += f->data[j] * h->data[k] * dt;
            }
        }
    }
    y_time->data[0] = f_time->data[0] + h_time->data[0];
    for (size_t p = 1; p < f->len + h->len - 1; p++) {
    y_time->data[p] = y_time->data[p-1] + dt;
    }
}
