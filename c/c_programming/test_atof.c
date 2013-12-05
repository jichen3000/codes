#include <stdio.h>
#include "colin_commons.h"


int main(int argc, char const *argv[]){
    char line[1000];
    double sum;

    sum = 0;
    while(get_line(line)){
        printf("\t%g\n", sum += atof(line));
    }

    return 0;
}