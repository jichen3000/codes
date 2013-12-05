#include <stdio.h>

/* bitcount:  count 1 bits in x */
int bitcount(unsigned x)
{
    int b;
    for (b = 0; x != 0; x >>= 1)
        if (x & 01)
            b++;
    return b;
}

int main(int argc, char const *argv[])
{
    int n;

    n = 4;

    printf("%d\n", n);
    // printf("%d\n", ~n);
    printf("%d\n", n ^ 1);
    printf("%d\n", n & 1);
    printf("%d\n", n | 1);
    printf("%d\n", n << 2);
    printf("%d\n", n >> 1);

    printf("%d\n", ~0);
    printf("%d\n", ~0 << 2);
    printf("%d\n", ~(~0 << 2));

    printf("%d\n", bitcount(4));
    printf("%d\n", bitcount(9));
    printf("%d\n", bitcount(0));
    printf("%d\n", bitcount(~0));
    return 0;
}