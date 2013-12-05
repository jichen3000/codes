#include <stdio.h>

int get_line(char str[]){
    int c, i;

    i = 0;
    while( (c=getchar()) != EOF && c != '\n'){
        str[i++] = c;
    }
    if (c == '\n'){
        str[i++] = c;
    }
    str[i] = '\0';
    return i;
}

// int main(int argc, char const *argv[]){
//     char line[1000];
//     while(get_line(line) > 0){
//         printf("%s\n", line);
//     }
//     return 0;
// }