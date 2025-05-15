#include "fourier_series.h"

void fourier_t(array *f_m, const double a_0, const array *a_n, const array *b_n, const array *t, const double T) {

    double w_0 = (2*PI)/ (T);    

    for (size_t i = 0; i < t->len; i++) {
        f_m->data[i] = a_0;
        for (size_t j = 1; j <= a_n->len; j++) {
            f_m->data[i] += a_n->data[j-1] * cos(j*w_0*t->data[i]) +                                      b_n->data[j-1] * sin(j*w_0*t->data[i]);        
        }
    }
}
