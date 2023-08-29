
#include <stdlib.h>

void init_rand(float* w, int size) {
    for (int i = 0; i < size; i++) {
        w[i] = (float)rand()/(float)(1);
    }
}
