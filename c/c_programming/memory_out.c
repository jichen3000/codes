#include <stdio.h>
#include <stdlib.h>

// it shows how difficult to encounter the failure of locating memory.
int main(int argc, char const *argv[])
{

    long i = 0;
    while(1){
        if (i % 1024 == 0){
            printf("i %ld\n", i);
        }
        malloc(1048576);
        i++;
    }
    return 0;
}