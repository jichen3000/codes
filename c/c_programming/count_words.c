#include <stdio.h>

#define INSIDE_WORD 1 // inside a word
#define OUTSIDE_WORD 0 // outside a word

int main(int argc, char const *argv[])
{
    int c, line_count, word_count, char_count, state;

    state = OUTSIDE_WORD;
    line_count, word_count, char_count = 0;
    while((c = getchar() ) != EOF){
        ++char_count;
        if(c == '\n'){
            ++line_count;
        }
        if(c == ' ' || c == '\n' || c == '\t'){
            state = OUTSIDE_WORD;
        }else if(state == OUTSIDE_WORD){
            state = INSIDE_WORD;
            ++word_count;
        }
    }
    printf("count of words: %d, count of lines: %d, count of chars: %d \n", 
        word_count, line_count, char_count);
    return 0;
}