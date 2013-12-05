#include <stdio.h>

void printd(int num){
    printf("num: %d\n", num);
    if (num < 0){
        putchar('-');
        num = -num;
    }
    if (num / 10){
        printd(num / 10);
    }
    putchar(num % 10 + '0');
}

int main(int argc, char const *argv[]){
    printd(1234);
    return 0;
}