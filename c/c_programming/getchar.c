#include <stdio.h>

int main(int argc, char const *argv[])
{
    /* code */
    int c;
    // first version
    // c = getchar();
    // while(c != EOF){
    //     putchar(c);
    //     c = getchar();
    // }

    // second version
    printf("EOF: %d\n", EOF);
    while((c = getchar()) != EOF){
        putchar(c);
    }
}