/*
gcc -g rand.c matrix.c matrix_test.c -o matrix_test
time ./matrix_test 1000 10000 1000
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "rand.h"
#include "matrix.h"

int main(int argc, char **argv) {
    setbuf(stdout, NULL);
    
    if (argc < 4) {
        printf("Usage: %s <M> <K> <N>\n", argv[0]);
        return 1;
    }

    int M = atoi(argv[1]);
    int K = atoi(argv[2]);
    int N = atoi(argv[3]);

    float *C = malloc(M*N*sizeof(float));

    float *A = malloc(M*K*sizeof(float));
    init_rand(A, M*K);

    float *B = malloc(K*N*sizeof(float));
    init_rand(B, K*N);

    time_t current_time;
    time(&current_time);
    srand((unsigned int)current_time);

    clock_t begin_time;
    clock_t end_time;
    begin_time = clock();
    mul(C, A, B, M, K, N);
    end_time = clock();
    printf("total time is: %f", (double)(end_time - begin_time)/CLOCKS_PER_SEC);
    
    free(A);
    free(B);
    free(C);
    return 0;
}