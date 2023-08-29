/*
Inference for resnet model in pure c
Example compile: (see README for more details)
$ gcc -O3 -o resnet resnet.c -lm
gcc -E resnet.c -o resnet.i
gcc -S resnet.i -o resnet.S
gcc -c resnet.i -o resnet.o
objdump -d ./resnet.o
*/

#include <stdio.h>


int main(int argc, char *argv[]) {
    
    char *checkpoint = NULL;
    char *a = "abc";

}