#include "transforms.h"

void dft(array *F_r, const array *x) {
    size_t len = x->len;

    for(int i=0; i<len; i++) {
        F_r->data[2*i] = 0.0;
        F_r->data[2*i+1] = 0.0;
        for(int j=0; j<len; j++) {
            double th = (-2*M_PI/(double)len)*j*i;
            F_r->data[2*i] += x->data[2*j]*cos(th) - x->data[(2*j)+1]*sin(th);
            F_r->data[(2*i)+1] += x->data[2*j]*sin(th) + x->data[(2*j)+1]*cos(th);

        }
    }
}

//uint32_t revbit(uint32_t num, int log2n) {
//    uint32_t revnum = 0;
//    for(int i=0; i<log2n; i++) {
//        revnum = (revnum << 1) | (num & 1);
//        num >>= 1;
//    }
//    return revnum;
//}

//void bitReverse(_Complex double *b, int log2n) {
//    int n = 1 << log2n;
//    for(int i=0; i<n; i++) {
//        uint32_t j = revbit(i, log2n);
//        if(i<j) {
//            float temp = b[i];
//            b[i] = b[j];
//            b[j] = temp;
//        }
//    }
//}

//void fft(array *F_r, const array *x) {
//    int len = x->len;
//    int log2n = (int)log2(len);
//    int n = 1<<log2n;
//    double complex *b = (double complex *)x;
//    double complex *z = (double complex *)F_r;
//    bitReverse(b, log2n);

//    for(int stage=1; stage<=log2n; stage++) {
//        int step = 1<<stage;
//        int hstep = step/2;
//        float _Complex twiddle = cexp(-I * M_PI/hstep);

//        for(int i=0; i<n; i+=step) {
//            double _Complex w = 1.0;
//            for(int j=0; j<hstep; j++) {
//                double _Complex t = w*b[i+j+hstep];
//                double _Complex u = b[i+j];
//                b[i+j] = u+t;
//                b[i+j+hstep] = u-t;
//                w *= twiddle;
//            }
//        }
//    }
//    double *d = (double *)b;
//    F_r = x;
//}

//int bitReverse(int num, int numBits) {
//    int reversed = 0;
//    for (int i = 0; i < numBits; i++) {
//        reversed = (reversed << 1) | (num & 1);
//        num >>= 1;
//    }
//    return reversed;
//}
//
//// Function to perform FFT
//void fft(array *F_r, array *x, int n) {
//    if (n <= 1) {
//        return;
//    }
//
//    // Perform bit-reversal of the input data
//    for (int i = 0; i < n; i++) {
//        int j = bitReverse(i, log2(n));
//        if (j > i) {
//            // Swap data[i] and data[j]
//            double temp = x->data[2 * i];
//            x->data[2 * i] = x->data[2 * j];
//            x->data[2 * j] = temp;
//
//            temp = x->data[2 * i + 1];
//            x->data[2 * i + 1] = x->data[2 * j + 1];
//            x->data[2 * j + 1] = temp;
//        }
//    }
//
//    // Split the array into even and odd parts
//    complex double* even = malloc(n / 2 * sizeof(complex double));
//    complex double* odd = malloc(n / 2 * sizeof(complex double));
//
//    for (int i = 0; i < n / 2; i++) {
//        even[i] = x->data[2 * i];
//        odd[i] = x->data[2 * i + 1];
//    }
//
//    // Recursively compute the FFT for even and odd parts
//    fft(F_r, even, n / 2);
//    fft(F_r, odd, n / 2);
//
//    // Combine the results
//    for (int k = 0; k < n / 2; k++) {
//        complex double t = cexp(-I * 2.0 * M_PI * k / n) * odd[k];
//        x->data[k] = even[k] + t;
//        x->data[k + n / 2] = even[k] - t;
//    }
//
//    free(even);
//    free(odd);
//
//    for (int i = 0; i < 2 * n; i++) {
//        F_r->data[i] = x->data[i];
//    }
//}

void cont_convolve(array *y, const array *f, const array *h) { 
    for(size_t i=0; i<f->len+h->len-1; i++) {
        y->data[i]= 0.0;
        for(size_t j=0; j<f->len; j++) {
            size_t k=i-j;
            if(i>=j && (i-j)<h->len) {
                y->data[i] += f->data[j] * h->data[k]; 
            }
        }
    }
}
