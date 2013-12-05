#include <stdio.h>
#include <string.h>

char *str_copy(char *dest, const char *src)
{
    char *tmp = dest;

    while ((*dest++ = *src++) != '\0')
        /* nothing */;
    return tmp;
}

char *str_append(char *dest, const char *src)
{
    char *tmp = dest;

    while (*dest)
        dest++;
    while ((*dest++ = *src++) != '\0')
        ;
    return tmp;
}


size_t return_str_by_argument(char in_str[], char out_str[])
{
    printf("str_copy: %s\n",str_copy(out_str, in_str));
    str_append(out_str, "mm");
    return strlen(out_str);
}

char *return_str_local_variable(char in_str[])
{
    char out_str[100];
    str_copy(out_str, in_str);
    str_append(out_str, "mm");
    return out_str;
}

// the best practice
char *return_str(char *out_str, char const *in_str)
{
    char *result = out_str;
    str_copy(out_str, in_str);
    str_append(out_str, "mm");
    return result;
}

int get_char(char const *str, int index)
{
    return str[index];
}

int main(int argc, char const *argv[])
{
    char in_str[] = "123";
    char out_str[100];
    size_t length;
    char *result;

    length = return_str_by_argument(in_str, out_str);
    printf("in_str: %s\n", in_str);
    printf("out_str: %s\n", out_str);
    printf("result: %ld\n", length);

    // return_str_local_variable(in_str);
    printf("in_str: %s\n", in_str);
    printf("out_str: %s\n", return_str_local_variable(in_str));

    result = return_str(out_str, in_str);
    printf("in_str: %s\n", in_str);
    printf("out_str: %s\n", out_str);
    printf("result: %s\n", result);

    printf("get_char: %d\n", get_char(in_str, 2));    
    return 0;
}