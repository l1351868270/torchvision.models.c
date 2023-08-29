

void mul(float *C, float *A, float *B, int M, int K, int N) {
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            float tmp = 0;
            for (int k = 0; k < K; k++) {
                tmp += A[i*K + k] * B[k*N + j];
            }
            C[i*N + j] = tmp;
        }
    }
}