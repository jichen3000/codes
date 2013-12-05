#include <stdio.h>

/* strlen:  return length of s */
int my_strlen(const char s[])
{
    int i = 0;
    while (s[i] != '\0'){        
       ++i;
    }
    return i; 
}

int main(int argc, char const *argv[])
{
    const char msg[] = "warning: ";
    int result = my_strlen(msg);
    printf("str length: %d\n", result);
    return 0;
}