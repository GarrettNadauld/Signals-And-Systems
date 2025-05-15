#include "../include/integrate.h"
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void cumulative_integrate(array *y, array *y_time, const array *f,                                  const array *f_time){
    //y_time->data[0] = 0.0;
    //y->data[0] = 0.0;

    if (f->len != f_time->len){
        return;
    }

    for (int i = 1; i < f->len; ++i) {
        double dt = f_time->data[i] - f_time->data[i-1];
        y->data[i-1] = (f->data[i] + f->data[i-1]) * dt * 0.5;
        y_time->data[i-1] = (f_time->data[i-1] + f_time->data[i]) * 0.5;
        //printf("y data: %f\n",y->data[i]);
        //printf("y time: %f\n",y_time->data[i]);
    }

    
    for (int j = 1; j < y->len; ++j) {
        y->data[j] = y->data[j] + y->data[j-1];
    }
}
