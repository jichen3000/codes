#include <stdio.h>
#include <stdlib.h>


int main(int argc, char const *argv[])
{
    struct {
           unsigned int is_keyword : 1;
           unsigned int is_extern  : 1;
           unsigned int is_static  : 1;
    } flags;

    printf("unsigned size: %ld\n", sizeof(unsigned));
    printf("flags size: %ld\n", sizeof(flags));
    flags.is_static = 1;
    flags.is_extern = 0;
    if (flags.is_extern == 0){
        printf("%u\n", flags.is_extern);
    }
    return 0;
}