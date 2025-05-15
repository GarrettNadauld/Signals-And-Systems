#ifndef INTEGRATE_H
#define INTEGRATE_H
#include <stddef.h>

/* *
Computes cumulative integration by trapezoidal
approximation .
* @param * y array struct of values to populate / return .
the values should be initialized as zero (0)
* @param * y_time array struct of time values to populate /
return . the values should be initialized as
zero (0)
* @param * f array struct of values of f ( t ) to integrate over
* @param * f_time array struct of time values corresponding to
f ( t )
* @return void all returns are handled by reference
*/
typedef struct array {
    size_t len ;
    double * data ;
} array;

void cumulative_integrate ( array *y , array * y_time ,
const array *f , const array * f_time ) ;

#endif
