#include <stdio.h>

int main(int argc, char const *argv[])
{
    int c, nl;
    nl = 0;
    while((c = getchar()) != EOF){
        printf("%d\n", c); // this code will impact the result of puchar()
        putchar(c);
        if( c == '\n' ){
            ++nl;
        }
    }
    printf("count of lines: %d\n", nl);
    return 0;
}