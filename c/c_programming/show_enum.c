#include <stdio.h>

int p(int a){
    printf("%d\n", a);
}

int main(int argc, char const *argv[])
{
    enum boolean { NO, YES } a;
    enum boolean b = YES;
    enum escapes { BELL = '\a', BACKSPACE = '\b', TAB = '\t', NEWLINE = '\n', VTAB = '\v', RETURN = '\r' };
    enum months { JAN = 1, FEB, MAR, APR, MAY, JUN,
                 JUL, AUG, SEP, OCT, NOV, DEC };
                       /* FEB = 2, MAR = 3, etc. */
    // p(boolean);
    p(a);
    a = YES;
    p(a);
    p(b);

    months first = FEB;
    p(first);

    escapes tab = TAB;
    p(tab);

    printf("%s\n", "ok");
    return 0;
}
