#include <stdio.h>

int count_char(void);

// using ctl+d to end the input
int main(int argc, char const *argv[])
{
    printf("count: %d\n", count_char());
    return 0;
}

int count_char(void){
    int nc;
    for(nc=0; getchar() != EOF; ++nc){

    }
    return nc;
}