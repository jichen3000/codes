#include <stdio.h>
#include <stdlib.h>
#define len(x)  (sizeof(x) / sizeof(x[0]))

int p_string(char str[]){
    printf("string: %s\n", str);
    return 0;
}

int p_int(int aint){
    printf("int: %d\n", aint);
    return 0;
}

int map(void *pointers[],int length, int (*func)(void *)){
    // long length = 4;
    printf("%ld\n", sizeof(pointers));
    printf("%ld\n", sizeof(pointers[0]));
    // printf("%s\n", typeof(length));
    for (int i = 0; i < length; ++i){
        (*func)(pointers[i]);
    }
    return 0;
}

int main(int argc, char const *argv[]){
    // int will have an issue, since convert to void**, will change the size of an item of pointers.
    int lineptr[] = { 3, 2, 5, 100};
    printf("%ld\n", sizeof(lineptr));
    printf("%ld\n", sizeof(lineptr[0]));
    map((void**) lineptr, len(lineptr), (int (*)(void *))p_int );


    // const char *lineptr[] = { "3", "2", "5", "100dddd" };
    // map((void**) lineptr, (int (*)(void *))p_string );
    return 0;
}