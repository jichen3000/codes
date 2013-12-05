#include <ctype.h>
#include <stdio.h>

int char2int(char c){
    return c - '0';
}

/* atof: convert string to double */
double atof(const char str[]){
    double value, power;
    int i, sign;
    for (i = 0; i < isspace(str[i]); ++i)
    {
        ;
    }
    sign = (str[i] == '-') ? -1 : 1;
    if (str[i] == '+' || str[i] == '-')
    {
        i++;
    }
    for (value = 0.0; isdigit(str[i]); ++i)
    {
        value = 10.0 * value + char2int(str[i]);
    }
    if (str[i] == '.'){
        i++;
    }
    for (power = 1.0; isdigit(str[i]); ++i)
    {
        value = 10.0 * value + char2int(str[i]);
        power *= 10;
    }
    return sign * value /power;
}

// int main(int argc, char const *argv[])
// {
    
//     printf("%0.2f\n", atof("123.45567"));
//     return 0;
// }